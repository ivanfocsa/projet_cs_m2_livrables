#!/usr/bin/env python3
"""Prepare final proof artifacts for the SOC M2 deliverables.

The script generates reviewer-friendly evidence files from the demo logs:
- alert mapping table
- log inventory
- rule copy
- dashboard-style PNG captures from the Daylight demo events

The PNG files are demo evidence generated from the same fields that are meant
to be visible in Wazuh. If a live Wazuh platform is available, replace the PNGs
with real Wazuh Dashboard screenshots while keeping the same filenames.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "étape 1" / "logs" / "generated"
RULES_FILE = ROOT / "étape 1" / "detection" / "wazuh" / "local_rules.xml"
PROOF_DIR = ROOT / "livrables" / "preuves" / "sprint-01"
CAPTURE_DIR = PROOF_DIR / "captures-dashboard"


ALERT_RULES = [
    {
        "id": "100100",
        "level": 10,
        "scenario": "suspicious_process",
        "title": "Execution PowerShell suspecte",
        "source": "Endpoint",
        "mitre": "T1059.001",
        "capture": "03-alerte-powershell-100100.png",
    },
    {
        "id": "100110",
        "level": 12,
        "scenario": "brute_force",
        "title": "Brute force acces distant",
        "source": "Firewall/syslog",
        "preferred_source": "firewall",
        "mitre": "T1110",
        "capture": "04-alerte-bruteforce-100110.png",
    },
    {
        "id": "100120",
        "level": 10,
        "scenario": "patient_access_anomaly",
        "title": "Acces anormal aux dossiers patients",
        "source": "Application metier",
        "mitre": "T1530",
        "capture": "05-alerte-dossier-patient-100120.png",
    },
    {
        "id": "100130",
        "level": 14,
        "scenario": "privileged_group_change",
        "title": "Modification d'un groupe privilegie",
        "source": "Active Directory",
        "mitre": "T1098",
        "capture": "06-alerte-groupe-privilegie-100130.png",
    },
    {
        "id": "100140",
        "level": 7,
        "scenario": "usb_suspect",
        "title": "Usage USB detecte",
        "source": "Endpoint",
        "mitre": "T1091",
        "capture": "07-alerte-usb-100140.png",
    },
    {
        "id": "100150",
        "level": 10,
        "scenario": "phishing",
        "title": "Suspicion phishing messagerie",
        "source": "Messagerie",
        "mitre": "T1566",
        "capture": "08-alerte-phishing-100150.png",
    },
    {
        "id": "100160",
        "level": 8,
        "scenario": "port_scan",
        "title": "Suspicion scan reseau",
        "source": "Firewall/syslog",
        "mitre": "T1046",
        "capture": "09-alerte-scan-100160.png",
    },
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


F = {
    "xs": font(15),
    "sm": font(18),
    "md": font(23),
    "lg": font(31, True),
    "xl": font(42, True),
    "bold": font(20, True),
    "mono": font(16),
}


COLORS = {
    "bg": "#f3f6fb",
    "panel": "#ffffff",
    "ink": "#172033",
    "muted": "#667085",
    "line": "#d9e1ec",
    "blue": "#1f5eff",
    "nav": "#0f172a",
    "green": "#12b76a",
    "orange": "#f79009",
    "red": "#d92d20",
    "purple": "#7a5af8",
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


SYSLOG_PAIR = re.compile(r"(\w+)=([^ ]+)")


def read_firewall(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            values = dict(SYSLOG_PAIR.findall(line))
            rows.append(
                {
                    "timestamp": "2026-demo-syslog",
                    "site": "SITE-01" if "FW-S01" in line else "SITE-02",
                    "hostname": "FW-S01" if "FW-S01" in line else "FW-S02",
                    "source": "firewall",
                    "scenario": values.get("scenario", "normal"),
                    "action": values.get("action", "unknown"),
                    "src_ip": values.get("src", "-"),
                    "dst_ip": values.get("dst", "-"),
                    "port": values.get("port", values.get("ports", "-")),
                    "user": values.get("user", "-"),
                    "message": line.split('message="')[-1].rstrip('"') if 'message="' in line else line,
                    "raw": line,
                }
            )
    return rows


def all_events() -> list[dict[str, Any]]:
    events = []
    for name in ["endpoint_events.jsonl", "application_events.jsonl", "mail_events.jsonl", "ad_events.jsonl"]:
        path = LOG_DIR / name
        if path.exists():
            events.extend(read_jsonl(path))
    events.extend(read_firewall(LOG_DIR / "firewall_syslog.log"))
    return events


def first_by_scenario(events: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    selected: dict[str, dict[str, Any]] = {}
    for rule in ALERT_RULES:
        preferred_source = rule.get("preferred_source")
        match = None
        if preferred_source:
            match = next(
                (
                    event
                    for event in events
                    if event.get("scenario") == rule["scenario"] and event.get("source") == preferred_source
                ),
                None,
            )
        if not match:
            match = next((event for event in events if event.get("scenario") == rule["scenario"]), None)
        if match:
            selected[rule["scenario"]] = match
    return selected


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str | None = None, radius: int = 14) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline)


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, fill: str = COLORS["ink"], ft: ImageFont.ImageFont = F["sm"]) -> None:
    draw.text(xy, value, fill=fill, font=ft)


def wrap(value: str, max_chars: int) -> list[str]:
    words = value.split()
    lines: list[str] = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        if len(test) <= max_chars:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def base_canvas(title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (1280, 720), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 1280, 82), fill=COLORS["nav"])
    text(draw, (34, 22), "Wazuh Dashboard - Daylight SOC MVP", "#ffffff", F["lg"])
    text(draw, (930, 28), "Demo logs | SOC externalise", "#cbd5e1", F["sm"])
    text(draw, (40, 110), title, COLORS["ink"], F["xl"])
    text(draw, (42, 160), subtitle, COLORS["muted"], F["md"])
    return img, draw


def severity_color(level: int) -> str:
    if level >= 13:
        return COLORS["red"]
    if level >= 10:
        return COLORS["orange"]
    if level >= 7:
        return COLORS["purple"]
    return COLORS["green"]


def draw_card(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, title: str, value: str, accent: str) -> None:
    rounded(draw, (x, y, x + w, y + h), COLORS["panel"], COLORS["line"])
    draw.rectangle((x, y, x + 7, y + h), fill=accent)
    text(draw, (x + 24, y + 18), title, COLORS["muted"], F["sm"])
    text(draw, (x + 24, y + 48), value, COLORS["ink"], F["lg"])


def save_home(events: list[dict[str, Any]], selected: dict[str, dict[str, Any]]) -> None:
    img, draw = base_canvas("Supervision globale", "Vue synthetique des alertes generees a partir des logs de demonstration Daylight.")
    counts = Counter(event.get("scenario", "unknown") for event in events)
    total_alerts = sum(counts[rule["scenario"]] for rule in ALERT_RULES)
    high_alerts = sum(counts[rule["scenario"]] for rule in ALERT_RULES if rule["level"] >= 10)
    sites = Counter(event.get("site", "-") for event in events)
    draw_card(draw, 42, 215, 270, 102, "Alertes SOC", str(total_alerts), COLORS["blue"])
    draw_card(draw, 340, 215, 270, 102, "Alertes hautes+", str(high_alerts), COLORS["orange"])
    draw_card(draw, 638, 215, 270, 102, "Sources", "5 familles", COLORS["green"])
    draw_card(draw, 936, 215, 270, 102, "Sites MVP", str(len([s for s in sites if s != "-"])), COLORS["purple"])

    rounded(draw, (42, 350, 596, 650), COLORS["panel"], COLORS["line"])
    text(draw, (70, 376), "Alertes par scenario", COLORS["ink"], F["lg"])
    y = 430
    max_count = max([counts[rule["scenario"]] for rule in ALERT_RULES] + [1])
    for rule in ALERT_RULES[:6]:
        count = counts[rule["scenario"]]
        bar_w = int(210 * count / max_count)
        text(draw, (72, y), rule["title"][:34], COLORS["ink"], F["sm"])
        draw.rounded_rectangle((320, y + 2, 320 + bar_w, y + 22), radius=8, fill=severity_color(rule["level"]))
        text(draw, (552, y), str(count), COLORS["muted"], F["sm"])
        y += 34

    rounded(draw, (628, 350, 1206, 650), COLORS["panel"], COLORS["line"])
    text(draw, (656, 376), "Dernieres alertes a montrer en video", COLORS["ink"], F["lg"])
    y = 430
    for rule in ALERT_RULES[:5]:
        event = selected.get(rule["scenario"], {})
        line = f"{rule['id']} | L{rule['level']} | {event.get('site', '-')} | {event.get('hostname', '-')}"
        text(draw, (658, y), line, COLORS["ink"], F["bold"])
        text(draw, (658, y + 24), rule["title"], COLORS["muted"], F["sm"])
        y += 48

    img.save(CAPTURE_DIR / "01-dashboard-home.png")


def save_alert_list(events: list[dict[str, Any]], selected: dict[str, dict[str, Any]]) -> None:
    img, draw = base_canvas("Alertes Daylight", "Liste des alertes exploitables pour le rapport et la demonstration MVP.")
    rounded(draw, (42, 210, 1238, 650), COLORS["panel"], COLORS["line"])
    headers = ["Rule ID", "Lvl", "Scenario", "Site", "Host", "User", "Source"]
    xs = [72, 178, 240, 570, 720, 900, 1040]
    for x, h in zip(xs, headers):
        text(draw, (x, 236), h, COLORS["muted"], F["bold"])
    draw.line((68, 270, 1208, 270), fill=COLORS["line"], width=2)
    y = 294
    for rule in ALERT_RULES:
        event = selected.get(rule["scenario"], {})
        values = [
            rule["id"],
            str(rule["level"]),
            rule["title"][:29],
            str(event.get("site", "-")),
            str(event.get("hostname", "-"))[:17],
            str(event.get("user", event.get("actor", "-")))[:16],
            rule["source"],
        ]
        draw.rounded_rectangle((70, y - 7, 138, y + 24), radius=8, fill=severity_color(rule["level"]))
        text(draw, (80, y), rule["id"], "#ffffff", F["xs"])
        for x, value in zip(xs[1:], values[1:]):
            text(draw, (x, y), value, COLORS["ink"], F["sm"])
        y += 46
    img.save(CAPTURE_DIR / "02-alertes-daylight-liste.png")


def event_field(event: dict[str, Any], key: str) -> str:
    value = event.get(key, "-")
    if isinstance(value, list):
        return ", ".join(map(str, value))
    return str(value)


def save_detail(rule: dict[str, Any], event: dict[str, Any]) -> None:
    img, draw = base_canvas(f"Detail alerte {rule['id']}", f"{rule['title']} - niveau {rule['level']} - {rule['source']}")
    rounded(draw, (42, 215, 500, 625), COLORS["panel"], COLORS["line"])
    draw.rounded_rectangle((72, 245, 182, 287), radius=10, fill=severity_color(rule["level"]))
    text(draw, (92, 254), f"L{rule['level']}", "#ffffff", F["lg"])
    fields = [
        ("Scenario", rule["scenario"]),
        ("MITRE", rule["mitre"]),
        ("Site", event_field(event, "site")),
        ("Machine", event_field(event, "hostname")),
        ("Utilisateur", event_field(event, "user") if event.get("user") else event_field(event, "actor")),
        ("Source", event_field(event, "source")),
    ]
    y = 316
    for label, value in fields:
        text(draw, (72, y), label, COLORS["muted"], F["sm"])
        text(draw, (215, y), value[:27], COLORS["ink"], F["bold"])
        y += 42

    rounded(draw, (532, 215, 1238, 625), COLORS["panel"], COLORS["line"])
    text(draw, (562, 244), "Contexte technique", COLORS["ink"], F["lg"])
    context_keys = [
        "timestamp",
        "action",
        "process",
        "command_line",
        "src_ip",
        "dst_ip",
        "port",
        "target_group",
        "added_user",
        "patient_record",
        "access_count",
        "device_id",
        "sender",
        "subject",
        "message",
    ]
    y = 300
    for key in context_keys:
        if key not in event:
            continue
        value = event_field(event, key)
        text(draw, (562, y), key, COLORS["muted"], F["xs"])
        for i, line in enumerate(wrap(value, 58)[:2]):
            text(draw, (742, y + i * 19), line, COLORS["ink"], F["xs"])
        y += 44
        if y > 586:
            break
    img.save(CAPTURE_DIR / str(rule["capture"]))


def write_evidence(events: list[dict[str, Any]], selected: dict[str, dict[str, Any]]) -> None:
    PROOF_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)

    shutil.copyfile(RULES_FILE, PROOF_DIR / "daylight-local-rules.txt")

    log_files = [
        LOG_DIR / "endpoint_events.jsonl",
        LOG_DIR / "application_events.jsonl",
        LOG_DIR / "mail_events.jsonl",
        LOG_DIR / "ad_events.jsonl",
        LOG_DIR / "firewall_syslog.log",
    ]
    lines = ["# Inventaire des logs Daylight", ""]
    for path in log_files:
        if not path.exists():
            continue
        line_count = len(path.read_text(encoding="utf-8").splitlines())
        lines.append(f"- `{path.relative_to(ROOT)}` : {line_count} lignes, sha256 `{sha256(path)}`")
    (PROOF_DIR / "daylight-log-files.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    table = [
        "# Alertes Daylight detectees",
        "",
        "| ID | Niveau | Scenario | Source | Site | Machine | Utilisateur | Capture |",
        "|---|---:|---|---|---|---|---|---|",
    ]
    tail_lines = []
    for rule in ALERT_RULES:
        event = selected.get(rule["scenario"], {})
        user = event.get("user", event.get("actor", "-"))
        table.append(
            f"| {rule['id']} | {rule['level']} | {rule['title']} | {rule['source']} | "
            f"{event.get('site', '-')} | {event.get('hostname', '-')} | {user} | "
            f"`captures-dashboard/{rule['capture']}` |"
        )
        tail_lines.append(json.dumps({"rule_id": rule["id"], "level": rule["level"], "title": rule["title"], "event": event}, ensure_ascii=True))
    (PROOF_DIR / "daylight-alerts-table.md").write_text("\n".join(table) + "\n", encoding="utf-8")
    (PROOF_DIR / "alerts-tail.txt").write_text("\n".join(tail_lines) + "\n", encoding="utf-8")

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (PROOF_DIR / "wazuh-manager-status.txt").write_text(
        "Etat Wazuh - preuve a valider sur l'environnement de demonstration live\n"
        f"Generation dossier preuves : {now}\n"
        "Note : Docker n'est pas disponible dans l'environnement local Codex utilise pour preparer ce rendu.\n"
        "Action soutenance : remplacer ce fichier par la sortie `docker compose ps` et `docker exec wazuh-manager /var/ossec/bin/wazuh-control status` si la plateforme live est accessible.\n",
        encoding="utf-8",
    )
    (PROOF_DIR / "docker-compose-ps.txt").write_text(
        "Docker non disponible sur l'environnement local de preparation.\n"
        "Commande attendue sur le poste de demonstration : docker compose ps\n"
        "Services attendus : wazuh.manager, wazuh.indexer, wazuh.dashboard.\n",
        encoding="utf-8",
    )
    (PROOF_DIR / "README.md").write_text(
        "# Preuves sprint 01\n\n"
        "Ce dossier centralise les preuves du MVP SOC Daylight.\n\n"
        "- Les fichiers `daylight-*.txt/md` inventorient les logs, les regles et les alertes.\n"
        "- Le dossier `captures-dashboard/` contient des captures dashboard de demonstrateur generees depuis les logs Daylight.\n"
        "- Si un Wazuh live est disponible, remplacer les PNG par des captures reelles Wazuh en gardant les memes noms.\n"
        "- Les fichiers `docker-compose-ps.txt` et `wazuh-manager-status.txt` sont a remplacer par les sorties live si la plateforme tourne au moment de la soutenance.\n",
        encoding="utf-8",
    )


def main() -> None:
    PROOF_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    events = all_events()
    selected = first_by_scenario(events)
    missing = [rule["scenario"] for rule in ALERT_RULES if rule["scenario"] not in selected]
    if missing:
        raise SystemExit(f"Missing demo events for scenarios: {', '.join(missing)}")
    write_evidence(events, selected)
    save_home(events, selected)
    save_alert_list(events, selected)
    for rule in ALERT_RULES:
        save_detail(rule, selected[rule["scenario"]])
    print(f"Prepared evidence in {PROOF_DIR.relative_to(ROOT)}")
    print(f"Prepared captures in {CAPTURE_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
