#!/usr/bin/env python3
"""Generate demo SOC logs for the audioprothesistes SOC MVP.

The generated files are safe fake logs for documentation, SIEM parsing tests,
dashboard screenshots and demo scenarios.
"""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path


USERS = ["y.focsa", "y.guerniou", "k.felix", "m.diacoumba", "a.martin", "c.bernard"]
SCENARIOS = [
    "normal",
    "brute_force",
    "suspicious_process",
    "usb_suspect",
    "patient_access_anomaly",
    "phishing",
    "port_scan",
]

ENDPOINT_HOSTS_BY_SITE = {
    "SITE-01": ["PC-S01-AUDIO-01", "SRV-S01-FICHIERS"],
    "SITE-02": ["PC-S02-AUDIO-01"],
    "SITE-03": ["PC-S03-AUDIO-01"],
}

APP_HOSTS_BY_SITE = {
    "SITE-01": ["APP-S01-CRM"],
    "SITE-03": ["APP-S03-LOGS"],
}

MAIL_HOSTS_BY_SITE = {
    "SITE-02": ["MAIL-S02"],
}

FIREWALL_HOSTS_BY_SITE = {
    "SITE-01": ["FW-S01"],
    "SITE-02": ["FW-S02"],
}


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def event_base(now: datetime, index: int, scenario: str, hosts_by_site: dict[str, list[str]]) -> dict:
    site = random.choice(list(hosts_by_site.keys()))
    return {
        "timestamp": iso(now + timedelta(seconds=index * random.randint(3, 20))),
        "site": site,
        "hostname": random.choice(hosts_by_site[site]),
        "user": random.choice(USERS),
        "scenario": scenario,
        "project": "soc-audiopro",
        "environment": "mvp",
    }


def endpoint_event(now: datetime, index: int, scenario: str) -> dict:
    evt = event_base(now, index, scenario, ENDPOINT_HOSTS_BY_SITE)
    evt["source"] = "endpoint"
    if scenario == "brute_force":
        evt.update(
            action="login_failed",
            result="failure",
            src_ip=f"10.10.{random.randint(1,3)}.{random.randint(20,240)}",
            auth_failures=random.randint(5, 12),
            message="Multiple failed login attempts detected",
        )
    elif scenario == "suspicious_process":
        evt.update(
            action="process_start",
            process=random.choice(["powershell.exe", "cmd.exe", "wscript.exe", "unknown_tool.exe"]),
            command_line="powershell -enc <demo_payload>",
            severity="high",
            message="Suspicious command execution",
        )
    elif scenario == "usb_suspect":
        evt.update(
            action="usb_connected",
            device_id=f"USB-DEMO-{random.randint(1000,9999)}",
            severity="medium",
            message="Unauthorized USB device connected",
        )
    else:
        evt.update(action="login_success", result="success", message="Normal endpoint activity")
    return evt


def app_event(now: datetime, index: int, scenario: str) -> dict:
    evt = event_base(now, index, scenario, APP_HOSTS_BY_SITE)
    evt["source"] = "application"
    evt["application"] = random.choice(["crm", "rdv", "patient-records"])
    if scenario == "patient_access_anomaly":
        evt.update(
            action="patient_record_read",
            patient_record=f"PATIENT-DEMO-{random.randint(10000,99999)}",
            access_count=random.randint(20, 60),
            severity="high",
            message="Abnormal patient record access volume",
        )
    else:
        evt.update(action="appointment_view", severity="info", message="Normal business application access")
    return evt


def mail_event(now: datetime, index: int, scenario: str) -> dict:
    evt = event_base(now, index, scenario, MAIL_HOSTS_BY_SITE)
    evt["source"] = "mail"
    if scenario == "phishing":
        evt.update(
            sender=random.choice(["billing-security.example", "support-update.example", "fake-bank.example"]),
            recipient=f"{random.choice(USERS)}@audio-demo.local",
            subject=random.choice(["Facture urgente", "Mise a jour compte", "Document a signer"]),
            url="https://phishing-demo.invalid/login",
            attachment=random.choice(["invoice.html", "scan.zip", "none"]),
            severity="high",
            message="Suspicious phishing email detected",
        )
    else:
        evt.update(sender="newsletter@example.invalid", severity="info", message="Normal email event")
    return evt


def firewall_line(now: datetime, index: int, scenario: str) -> str:
    dt = now + timedelta(seconds=index * random.randint(2, 18))
    site = random.choice(list(FIREWALL_HOSTS_BY_SITE.keys()))
    host = random.choice(FIREWALL_HOSTS_BY_SITE[site])
    site_net = int(site[-2:])
    if scenario == "port_scan":
        src = f"198.51.100.{random.randint(10,240)}"
        dst = f"10.10.{site_net}.{random.randint(10,60)}"
        ports = ",".join(str(p) for p in random.sample([22, 80, 443, 445, 3389, 8080], 4))
        return f"{dt:%b %d %H:%M:%S} {host} firewall action=deny scenario=port_scan src={src} dst={dst} ports={ports} message=\"Port scan suspected\""
    src = f"10.10.{site_net}.{random.randint(10,240)}"
    dst = f"203.0.113.{random.randint(10,240)}"
    return f"{dt:%b %d %H:%M:%S} {host} firewall action=allow scenario=normal src={src} dst={dst} port=443 message=\"Normal outbound traffic\""


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="logs/generated", help="Output directory")
    parser.add_argument("--count", type=int, default=200, help="Number of events per JSONL family")
    args = parser.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc) - timedelta(hours=2)
    endpoint_scenarios = ["normal"] * 8 + ["brute_force", "suspicious_process", "usb_suspect"]

    endpoint_rows = [endpoint_event(now, i, random.choice(endpoint_scenarios)) for i in range(args.count)]
    app_rows = [app_event(now, i, random.choice(["normal"] * 10 + ["patient_access_anomaly"])) for i in range(args.count)]
    mail_rows = [mail_event(now, i, random.choice(["normal"] * 10 + ["phishing"])) for i in range(args.count)]
    firewall_rows = [firewall_line(now, i, random.choice(["normal"] * 8 + ["port_scan"])) for i in range(args.count)]

    write_jsonl(out / "endpoint_events.jsonl", endpoint_rows)
    write_jsonl(out / "application_events.jsonl", app_rows)
    write_jsonl(out / "mail_events.jsonl", mail_rows)
    (out / "firewall_syslog.log").write_text("\n".join(firewall_rows) + "\n", encoding="utf-8")

    print(f"Generated demo logs in {out.resolve()}")


if __name__ == "__main__":
    main()
