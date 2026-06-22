# Implementation concrete du SOC Daylight

Ce dossier transforme les choix d'architecture en elements directement exploitables.

## Ordre d'implementation

1. Demarrer le socle Wazuh avec `scripts/setup-siem-lab.ps1`.
2. Copier les regles Wazuh depuis `../detection/wazuh/local_rules.xml`.
3. Ajouter les decoders et sources de logs du dossier `wazuh/`.
4. Configurer pfSense selon `pfsense/syslog-settings.md` ou rejouer `../logs/generated/firewall_syslog.log`.
5. Pour Windows, installer l'agent Wazuh et, en production, Sysmon avec `sysmon/daylight-sysmon-config.xml`.
6. En evolution, ajouter Suricata avec `suricata/daylight.rules`.
7. Verifier la couverture avec :

```bash
npm run verify:concrete-stack
```

## Ce qui est implemente ici

| Brique | Fichier | Usage |
|---|---|---|
| Wazuh Manager | `wazuh/ossec-manager-daylight.conf` | Snippets collecte syslog et fichiers JSONL. |
| Wazuh decoders | `wazuh/local_decoders_daylight.xml` | Parsing des logs firewall `FW-S01/FW-S02`. |
| pfSense | `pfsense/syslog-settings.md` | Configuration syslog concrete. |
| Sysmon | `sysmon/daylight-sysmon-config.xml` | Collecte Windows avancee en production. |
| Suricata | `suricata/daylight.rules` | IDS reseau en evolution. |
| Retention | `opensearch/wazuh-retention-policy.json` | Base de politique de conservation. |
| Dashboards | `dashboards/dashboard-filters.md` | Filtres a creer dans Wazuh Dashboard. |
| Verification | `../../scripts/verify-concrete-stack.py` | Controle rapide des fichiers et scenarios. |

## Message a defendre

Le MVP n'est pas une production complete, mais chaque brique conceptuelle a une implementation concrete : Wazuh pour le SIEM, agents pour postes/serveurs, pfSense/syslog pour firewall, JSONL pour applications et messagerie, RBAC pour les roles, playbooks pour la reponse, retention et dashboards pour l'exploitation.

