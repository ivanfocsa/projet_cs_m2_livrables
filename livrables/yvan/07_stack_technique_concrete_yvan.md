# Stack technique concrete - Yvan FOCSA

## Reponse courte si le jury demande "quel firewall ?"

Le firewall cible retenu pour l'architecture est **pfSense CE**.

Dans le MVP, nous n'avons pas de VM pfSense complete a montrer : le firewall est represente par les equipements `FW-S01` et `FW-S02`, avec des logs reseau realistes dans `etape 1/logs/generated/firewall_syslog.log`. Ces logs simulent ce que pfSense enverrait vers Wazuh via syslog.

En production, chaque centre aurait un firewall `FW-SXX-PFSENSE` qui envoie ses logs au Wazuh Manager par syslog, idealement via VPN site-a-site et avec filtrage par adresse IP source.

Phrase a dire :

> Pour la partie firewall, le choix concret est pfSense CE. Dans le MVP, on simule ses logs avec `FW-S01` et `FW-S02`, mais l'architecture cible prevoit un export syslog pfSense vers Wazuh. Le modele reste compatible avec Fortigate, Stormshield ou Sophos si le client possede deja ces equipements, car le point important est l'export syslog vers le SOC.

## Stack concrete par brique SI

| Brique | Choix concret MVP | Choix cible production | Preuve / fichier |
|---|---|---|---|
| SOC central | Wazuh Manager, Wazuh Indexer/OpenSearch, Wazuh Dashboard | Wazuh sur VM ou serveurs dedies, stockage dimensionne, sauvegardes | Dashboard Wazuh, script `setup-siem-lab.ps1` |
| Postes de travail | `PC-S01-AUDIO-01`, `PC-S02-AUDIO-01`, agent Wazuh | Windows 10/11 Pro avec agent Wazuh et Sysmon si possible | Alertes `100100` PowerShell et `100140` USB |
| Serveurs internes | `SRV-S01-FICHIERS`, `serveur-01`, agent Wazuh, `/var/log/auth.log` | Windows Server/AD, serveur fichiers, journaux Security/EventLog | Alerte `100130` modification groupe privilegie |
| Firewall / routeur | `FW-S01`, `FW-S02`, logs syslog simules | pfSense CE par site, export syslog vers Wazuh via VPN | `firewall_syslog.log`, alertes `100110` et `100160` |
| Applications metier | `APP-S01-CRM`, `APP-S03-LOGS`, logs JSONL | Application CRM/RDV/dossiers patients avec logs applicatifs normalises | `application_events.jsonl`, alerte `100120` |
| Messagerie | `MAIL-S02`, logs JSONL simules | Zimbra, Exchange ou Microsoft 365 audit logs selon client | `mail_events.jsonl`, alerte `100150` |
| Reporting / preuves | Markdown, PDF, captures dashboard | Reporting mensuel client, export PDF/CSV, tableau par site | Rapport final, matrice de conformite |

## Flux concrets a expliquer

| Flux | Source concrete | Destination concrete | Port / protocole | Ce que cela prouve |
|---|---|---|---|---|
| Agent endpoint | `PC-S01-AUDIO-01` | Wazuh Manager | TCP/UDP 1514 | Collecte poste utilisateur. |
| Enrolement agent | `PC-S01-AUDIO-01` | Wazuh Manager | TCP 1515 | Ajout controle d'un nouvel agent. |
| Syslog firewall | `FW-S01` / pfSense CE | Wazuh Manager | UDP/TCP 514 ou 5514 | Collecte reseau et firewall. |
| Logs applicatifs | `APP-S01-CRM` | Agent ou collecteur Wazuh | Fichier JSONL | Supervision application metier. |
| Logs messagerie | `MAIL-S02` | Agent ou collecteur Wazuh | Fichier JSONL ou API | Detection phishing. |
| Dashboard | Analyste SOC | Wazuh Dashboard | HTTPS 443 | Interface web exploitable. |
| API Wazuh | Dashboard/admin | Wazuh Manager | TCP 55000 | Administration interne du SIEM. |

## Detail firewall pfSense

Configuration cible pour un centre :

| Parametre | Valeur cible |
|---|---|
| Equipement | pfSense CE, VM ou appliance physique |
| Nom | `FW-SXX-PFSENSE` |
| Site exemple | `FW-S01-PFSENSE` pour Paris, `FW-S02-PFSENSE` pour Lyon |
| Transport | Syslog distant vers le SOC |
| Port | 514 UDP/TCP en lab, 5514 TCP ou tunnel VPN en production |
| Logs utiles | Deny/allow, NAT, connexions entrantes, scans, VPN, authentifications admin |
| Securisation | VPN site-a-site, filtrage IP source, horodatage NTP, retention cote Wazuh |

Ce que les alertes montrent :

| ID | Source | Scenario | Explication concrete |
|---|---|---|---|
| `100110` | `FW-S01` | Brute force acces distant | Plusieurs tentatives refusees vers RDP/SSH depuis une IP externe. |
| `100160` | `FW-S01` | Scan reseau | Une IP externe teste plusieurs ports sensibles. |

## Ce qu'il ne faut pas sur-vendre

- Ne pas dire qu'une VM pfSense complete est deja deployee si elle ne l'est pas.
- Dire clairement : "dans le MVP, les logs firewall sont simules ; en cible, ils viennent de pfSense CE ou d'un firewall client compatible syslog".
- Ne pas promettre que pfSense est obligatoire : l'architecture accepte Fortigate, Stormshield, Sophos ou Cisco si le client les utilise deja.
- Le point important pour ta partie est le **flux technique concret** : firewall du site -> syslog -> Wazuh Manager -> regles -> alerte -> dashboard -> playbook.
