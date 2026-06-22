# REX incidents simules - SOC Daylight

## Objectif

Ce REX synthetise les incidents simules dans le MVP SOC Daylight. Il relie chaque alerte a une source de logs, une analyse SOC, une reponse attendue et une piste d'amelioration.

## Synthese des incidents

| ID alerte | Incident | Source | Gravite | Decision SOC |
|---|---|---|---|---|
| 100100 | Execution PowerShell suspecte | Endpoint | Haute | Investigation poste et verification utilisateur. |
| 100110 | Brute force acces distant | Firewall/syslog | Haute | Blocage source suspecte et verification succes de connexion. |
| 100120 | Acces anormal dossiers patients | Application metier | Haute | Verification metier et escalade confidentialite. |
| 100130 | Modification groupe privilegie | Active Directory | Critique | Controle admin, retrait si non autorise, audit droits. |
| 100140 | Usage USB detecte | Endpoint | Moyenne | Verification politique USB et controle poste. |
| 100150 | Suspicion phishing messagerie | Messagerie | Haute | Recherche emails similaires et sensibilisation utilisateur. |
| 100160 | Suspicion scan reseau | Firewall/syslog | Moyenne | Verification IP source et blocage si externe non legitime. |

## Analyse transverse

Les incidents montrent que le SOC ne doit pas seulement collecter des logs. Il doit produire une alerte lisible, contextualisee et rattachee a un playbook. Les champs les plus utiles pour l'analyste sont le site, la machine, l'utilisateur, la source, le scenario, le niveau d'alerte et le message technique.

## Points positifs

- Les scenarios couvrent les briques principales du cahier des charges : poste, firewall, application metier, serveur/AD et messagerie.
- Les IDs d'alertes sont harmonises entre regles, rapport, preuves et script video.
- Les captures Wazuh live permettent de derouler la video avec une vraie interface SIEM.
- Les playbooks donnent une procedure exploitable pour chaque type d'incident.

## Limites

- Les logs sont simules ou rejoues, ce qui stabilise la demo mais ne remplace pas une production reelle.
- Les captures generees restent une solution de secours, mais les captures Wazuh live sont maintenant disponibles.
- Le dimensionnement production, la haute disponibilite et le SOAR restent des perspectives.

## Ameliorations proposees

1. Utiliser en priorite les captures Wazuh live du dossier `livrables/preuves/wazuh-live-captures/`.
2. Ajouter un decoder Wazuh plus strict pour chaque famille de logs.
3. Ajouter TheHive ou Shuffle pour tracer les tickets et semi-automatiser certaines reponses.
4. Mettre en place un reporting mensuel par site et par criticite.
5. Tester le passage de 3 sites MVP a un inventaire type 30 sites.
