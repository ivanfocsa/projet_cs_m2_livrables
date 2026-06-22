# Index du projet

Ce dossier contient la base de travail du projet d'etudes M2 Cybersecurite : mise en place d'un SOC externalise pour un reseau d'audioprothesistes.

## Documents principaux

| Document | Usage |
|---|---|
| [01_Analyse_Initiale.md](01_Analyse_Initiale.md) | Comprendre le contexte client, les besoins et le perimetre MVP. |
| [02_Dossier_Architecture_Technique.md](02_Dossier_Architecture_Technique.md) | Presenter l'architecture SOC, les composants et les flux. |
| [03_Organisation_Planning_Backlog.md](03_Organisation_Planning_Backlog.md) | Repartition des roles, planning, backlog et methodologie. |
| [04_Gestion_Couts.md](04_Gestion_Couts.md) | Estimation des couts MVP et production. |
| [05_Scenarios_Detection.md](05_Scenarios_Detection.md) | Cas d'usage SOC, hypotheses d'attaque et preuves attendues. |
| [06_Playbooks_Reponse_Incident.md](06_Playbooks_Reponse_Incident.md) | Procedures de traitement des alertes. |
| [07_Guide_Deploiement_Utilisation.md](07_Guide_Deploiement_Utilisation.md) | Installation, onboarding site et exploitation. |
| [08_Script_Video_MVP.md](08_Script_Video_MVP.md) | Deroule de la video 15-20 min. |
| [09_Matrice_Conformite_Cahier_Charges.md](09_Matrice_Conformite_Cahier_Charges.md) | Preuve que le projet respecte le cahier des charges. |
| [10_REX_Template.md](10_REX_Template.md) | Trame de retour d'experience pour incidents simules. |

## Schemas

| Schema | Usage |
|---|---|
| [architecture_soc_externalise.mmd](../diagrams/architecture_soc_externalise.mmd) | Architecture globale du SOC externalise. |
| [topologie_sites_mvp.mmd](../diagrams/topologie_sites_mvp.mmd) | Topologie des 3 sites simules. |
| [flux_collecte_logs.mmd](../diagrams/flux_collecte_logs.mmd) | Flux de collecte et exploitation des logs. |
| [processus_incident_soc.mmd](../diagrams/processus_incident_soc.mmd) | Cycle de traitement d'une alerte SOC. |
| [gantt_planning.mmd](../diagrams/gantt_planning.mmd) | Planning projet. |

## Ordre de travail conseille

| Priorite | Action | Responsable |
|---|---|---|
| 1 | Valider le perimetre 3 sites MVP | Yvan |
| 2 | Installer le SIEM Wazuh | Youssef |
| 3 | Connecter une premiere source de logs | Youssef |
| 4 | Generer les logs de demonstration | Mahamadou |
| 5 | Creer les regles et dashboards initiaux | Kilyan |
| 6 | Tester les scenarios de detection | Kilyan / Mahamadou |
| 7 | Capturer les preuves et consolider le rapport | Toute l'equipe |
