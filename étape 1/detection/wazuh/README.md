# Regles Wazuh - SOC audioprothesistes

Ce dossier contient des regles de depart pour le demonstrateur.

## Important

Les regles sont des templates pedagogiques. Elles doivent etre adaptees aux champs reels apres ingestion dans Wazuh.

Approche recommandee :

1. Generer des logs avec `scripts/generate_demo_logs.py`.
2. Verifier les champs visibles dans Wazuh.
3. Adapter les noms de champs dans `local_rules.xml`.
4. Tester scenario par scenario.
5. Capturer les alertes.

## Scenarios couverts

| Regle | Scenario |
|---|---|
| `100100` | Brute force |
| `100110` | Execution suspecte |
| `100120` | Usage USB suspect |
| `100130` | Acces anormal dossier patient |
| `100140` | Phishing |
| `100150` | Scan reseau |

