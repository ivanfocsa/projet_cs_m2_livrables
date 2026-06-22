#!/usr/bin/env python3
"""Verify that the concrete SOC implementation artifacts are present."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "étape 1/implementation/README.md",
    "étape 1/implementation/wazuh/ossec-manager-daylight.conf",
    "étape 1/implementation/wazuh/local_decoders_daylight.xml",
    "étape 1/implementation/pfsense/syslog-settings.md",
    "étape 1/implementation/sysmon/daylight-sysmon-config.xml",
    "étape 1/implementation/suricata/daylight.rules",
    "étape 1/implementation/suricata/suricata-wazuh-localfile.conf",
    "étape 1/implementation/opensearch/wazuh-retention-policy.json",
    "étape 1/implementation/dashboards/dashboard-filters.md",
    "étape 1/implementation/runbook/IMPLEMENTATION_CHECKLIST.md",
    "étape 1/detection/wazuh/local_rules.xml",
    "étape 1/logs/generated/endpoint_events.jsonl",
    "étape 1/logs/generated/application_events.jsonl",
    "étape 1/logs/generated/ad_events.jsonl",
    "étape 1/logs/generated/mail_events.jsonl",
    "étape 1/logs/generated/firewall_syslog.log",
]

EXPECTED_RULES = {
    "100100": "suspicious_process",
    "100110": "brute_force",
    "100120": "patient_access_anomaly",
    "100130": "privileged_group_change",
    "100140": "usb_suspect",
    "100150": "phishing",
    "100160": "port_scan",
}


def fail(message: str) -> None:
    raise SystemExit(f"[FAIL] {message}")


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def main() -> None:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    if missing:
        fail("Fichiers manquants:\n" + "\n".join(f"- {item}" for item in missing))

    rules = (ROOT / "étape 1/detection/wazuh/local_rules.xml").read_text(encoding="utf-8")
    for rule_id, scenario in EXPECTED_RULES.items():
        if f'id="{rule_id}"' not in rules:
            fail(f"Regle Wazuh manquante: {rule_id}")
        if f"<field name=\"scenario\">{scenario}</field>" not in rules:
            fail(f"Scenario Wazuh manquant pour {rule_id}: {scenario}")

    scenario_seen: set[str] = set()
    for rel in [
        "étape 1/logs/generated/endpoint_events.jsonl",
        "étape 1/logs/generated/application_events.jsonl",
        "étape 1/logs/generated/ad_events.jsonl",
        "étape 1/logs/generated/mail_events.jsonl",
    ]:
        rows = read_jsonl(ROOT / rel)
        if not rows:
            fail(f"Log vide: {rel}")
        scenario_seen.update(str(row.get("scenario", "")) for row in rows)

    firewall_log = (ROOT / "étape 1/logs/generated/firewall_syslog.log").read_text(encoding="utf-8")
    for hostname in ["FW-S01", "FW-S02"]:
        if hostname not in firewall_log:
            fail(f"Hostname firewall absent du syslog: {hostname}")
    for scenario in ["brute_force", "port_scan"]:
        if f"scenario={scenario}" not in firewall_log:
            fail(f"Scenario firewall absent: {scenario}")
        scenario_seen.add(scenario)

    missing_scenarios = sorted(set(EXPECTED_RULES.values()) - scenario_seen)
    if missing_scenarios:
        fail("Scenarios sans log de demonstration: " + ", ".join(missing_scenarios))

    retention = json.loads((ROOT / "étape 1/implementation/opensearch/wazuh-retention-policy.json").read_text(encoding="utf-8"))
    if retention["policy"]["states"][0]["transitions"][0]["conditions"]["min_index_age"] != "90d":
        fail("Retention OpenSearch attendue: 90d")

    decoders = (ROOT / "étape 1/implementation/wazuh/local_decoders_daylight.xml").read_text(encoding="utf-8")
    if not re.search(r"<decoder name=\"daylight-firewall", decoders):
        fail("Decoder firewall Daylight absent")

    print("[OK] Implementation concrete verifiee")
    print("[OK] Regles:", ", ".join(EXPECTED_RULES.keys()))
    print("[OK] Scenarios:", ", ".join(sorted(EXPECTED_RULES.values())))
    print("[OK] Firewall: FW-S01/FW-S02 + brute_force/port_scan")


if __name__ == "__main__":
    main()
