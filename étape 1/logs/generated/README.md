# Logs de demonstration generes

Ces fichiers sont des faux logs sans donnees reelles. Ils servent a tester l'ingestion dans Wazuh, a creer des captures de dashboard et a rejouer les scenarios SOC.

| Fichier | Contenu |
|---|---|
| `endpoint_events.jsonl` | Evenements postes et serveurs : brute force, execution suspecte, USB, activite normale. |
| `application_events.jsonl` | Evenements applicatifs : acces dossiers patients, activite CRM/RDV normale. |
| `mail_events.jsonl` | Evenements messagerie : phishing et activite normale. |
| `firewall_syslog.log` | Logs firewall au format syslog simplifie : trafic normal et scan reseau. |

Regeneration :

```bash
python scripts/generate_demo_logs.py --out logs/generated --count 200
```

