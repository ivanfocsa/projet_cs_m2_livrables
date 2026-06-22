# 09 - Matrice de conformite au cahier des charges

## 1. Objectif

Cette matrice prouve que le projet est aligne avec les attentes du cahier des charges.

## 2. Conformite fonctionnelle

| Exigence | Reponse projet | Preuve attendue |
|---|---|---|
| Deployer un SOC externalise | Architecture SOC centralisee cote prestataire | Schema architecture + dashboard. |
| Centraliser les evenements de securite | Wazuh recoit agents, syslog et logs applicatifs | Capture logs multi-source. |
| Creer un environnement de demonstration | 3 sites simules | Topologie MVP. |
| Systeme industrialisable | Templates et checklist onboarding | Guide de deploiement. |
| SIEM open-source centralise | Wazuh | Installation et interface. |
| Regles de detection personnalisables | Regles locales SOC audio | Fichier `local_rules.xml`. |
| Dashboards lisibles et segmentes | Dashboard supervision / analyste / admin | Captures dashboard. |
| Playbooks semi-automatises | Procedures incident | Dossier `playbooks/`. |
| Reporting simple et exportable | Captures, exports, rapport | Annexes rapport. |
| Interface web | Wazuh Dashboard | Capture acces navigateur. |
| Reproductibilite et scalabilite | Guide + extension 30 sites | Section architecture. |

## 3. Couverture des briques SI

| Brique SI | Couverture MVP | Statut |
|---|---|---|
| Postes de travail | Agent Wazuh, scenarios endpoint | Prevu |
| Routeurs / firewall | Syslog ou logs reseau simules | Prevu |
| Applications metiers | Logs CRM/RDV/dossiers patients simules | Prevu |
| Serveurs internes | Agent serveur, logs privilege/fichiers | Prevu |
| Messagerie pro | Logs phishing simules | Prevu |

## 4. Couverture livrables pedagogiques

| Livrable attendu | Fichier projet |
|---|---|
| Analyse initiale | `docs/01_Analyse_Initiale.md` |
| Architecture technique | `docs/02_Dossier_Architecture_Technique.md` |
| Demonstrateur operationnel | `infra/`, `scripts/`, `detection/` |
| Dashboards et alertes | `dashboard/`, `docs/05_Scenarios_Detection.md` |
| Playbooks / procedures | `docs/06_Playbooks_Reponse_Incident.md`, `playbooks/` |
| Rapport technique complet | Tous les documents `docs/` |
| Guide de deploiement | `docs/07_Guide_Deploiement_Utilisation.md` |
| Video de demonstration | `docs/08_Script_Video_MVP.md` |

## 5. Points de vigilance

| Risque | Action preventive |
|---|---|
| Trop gros perimetre | Rester sur 3 sites MVP. |
| Demo instable | Preparer des logs simules en secours. |
| Faux positifs nombreux | Ajuster les seuils de regles. |
| Documentation tardive | Documenter a chaque test. |
| Manque de preuves | Capturer chaque etape technique. |

