# Projet M2 Cybersecurite - SOC externalise audioprothesistes

## Objectif

Concevoir un demonstrateur de SOC externalise pour un reseau d'audioprothesistes disposant d'environ 30 points de vente en France.

Le MVP simule 3 sites representatifs et montre une solution industrialisable capable de :

- centraliser les evenements de securite ;
- superviser les postes, serveurs, firewalls, applications metier et messagerie ;
- detecter des comportements suspects ;
- produire des alertes et dashboards exploitables ;
- documenter des playbooks de reponse incident ;
- fournir un guide de deploiement et d'utilisation.

## Stack cible

| Besoin | Choix de depart |
|---|---|
| SIEM open-source | Wazuh |
| Interface web | Wazuh Dashboard / OpenSearch |
| Collecte endpoint | Agents Wazuh |
| Logs reseau | Syslog firewall / routeur simule |
| Logs applicatifs | Application metier simulee CRM/RDV/dossiers patients |
| Scenarios attaque/safe | Logs generes et actions controlees |
| Reponse incident | Playbooks + scripts simples |

## Equipe

| Membre | Role |
|---|---|
| Yvan FOCSA | Coordinateur projet / Architecte securite |
| Youssef GUERNIOU | Ingenieur SIEM / Integration technique |
| Kilyan FELIX | Analyste SOC / Detection et dashboards |
| Mahamadou DIACOUMBA | Blue Team / Reponse incident et automatisation |

## Par ou commencer

1. Lire [docs/00_Index.md](docs/00_Index.md).
2. Valider l'architecture dans [docs/02_Dossier_Architecture_Technique.md](docs/02_Dossier_Architecture_Technique.md).
3. Installer le socle Wazuh avec le guide [docs/07_Guide_Deploiement_Utilisation.md](docs/07_Guide_Deploiement_Utilisation.md).
4. Generer des logs de demo avec [scripts/generate_demo_logs.py](scripts/generate_demo_logs.py).
5. Configurer les premieres regles a partir de [detection/wazuh/local_rules.xml](detection/wazuh/local_rules.xml).
6. Tester les scenarios de [docs/05_Scenarios_Detection.md](docs/05_Scenarios_Detection.md).
7. Completer les preuves dans le rapport final.

## Livrables couverts

| Livrable attendu | Fichiers de depart |
|---|---|
| Analyse initiale | `docs/01_Analyse_Initiale.md` |
| Document Architecture Technique | `docs/02_Dossier_Architecture_Technique.md` + `diagrams/` |
| Demonstrateur operationnel | `infra/`, `detection/`, `scripts/` |
| Dashboards & alertes | `docs/05_Scenarios_Detection.md`, `dashboard/` |
| Playbooks / procedures | `docs/06_Playbooks_Reponse_Incident.md`, `playbooks/` |
| Rapport technique complet | `docs/00_Index.md` et documents associes |
| Guide de deploiement & utilisation | `docs/07_Guide_Deploiement_Utilisation.md` |
| Video de demonstration | `docs/08_Script_Video_MVP.md` |
