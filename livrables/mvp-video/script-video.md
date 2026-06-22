# Script video MVP - SOC externalise Daylight

Objectif : video de 15 a 20 minutes, structuree besoin -> solution -> demonstration -> limites -> conclusion. Chaque membre doit parler avec son nom affiche a l'ecran.

## Deroule recommande

| Temps | Intervenant | Contenu | Support |
|---:|---|---|---|
| 0:00 - 2:00 | Kilyan FELIX | Presentation du client Daylight, besoin cyber et contexte multi-sites. | Cahier des charges, rapport. |
| 2:00 - 5:00 | Yvan FOCSA | Architecture SOC externalise, perimetre MVP, passage de 3 sites simules a 30 sites. | Schema architecture, guide onboarding. |
| 5:00 - 8:00 | Youssef GUERNIOU | Socle SIEM Wazuh, collecte agents/syslog/logs applicatifs, sources de logs. | Guide de deploiement, inventaire logs. |
| 8:00 - 13:00 | Mahamadou DIACOUMBA | Alertes SOC : `100100`, `100110`, `100120`, `100130`, `100140`. | Captures dashboard et table alertes. |
| 13:00 - 16:00 | Kilyan / Mahamadou | Playbooks et traitement incident : qualification, action, documentation, REX. | Playbooks, REX incidents. |
| 16:00 - 18:00 | Yvan FOCSA | Industrialisation, limites, couts, prochaines evolutions. | Checklist onboarding, couts, limites. |
| 18:00 - 20:00 | Tous | Conclusion et repartition des contributions. | Matrice conformite, rapport final. |

## Points a montrer a l'ecran

- `livrables/preuves/sprint-01/captures-dashboard/01-dashboard-home.png`
- `livrables/preuves/sprint-01/captures-dashboard/02-alertes-daylight-liste.png`
- `livrables/preuves/sprint-01/captures-dashboard/03-alerte-powershell-100100.png`
- `livrables/preuves/sprint-01/captures-dashboard/04-alerte-bruteforce-100110.png`
- `livrables/preuves/sprint-01/captures-dashboard/05-alerte-dossier-patient-100120.png`
- `livrables/preuves/sprint-01/captures-dashboard/06-alerte-groupe-privilegie-100130.png`
- `livrables/preuves/sprint-01/captures-dashboard/07-alerte-usb-100140.png`

## Rappel oral pour Yvan

Ma partie consiste a expliquer que le demonstrateur ne cherche pas a reproduire 30 sites complets, mais a prouver une chaine SOC industrialisable. Je dois insister sur trois idees : architecture centralisee, flux de collecte maitrises, onboarding standardise pour passer progressivement de 3 sites simules a 30 sites.

## Checklist avant export

- Chaque membre parle.
- Le nom du membre apparait pendant son passage.
- La video dure entre 15 et 20 minutes.
- Les IDs d'alertes sont coherents avec le rapport.
- Les captures sont lisibles en plein ecran.
- La conclusion rappelle la valeur client : centraliser, detecter, qualifier, repondre, documenter.
