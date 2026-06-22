# Dossier final Yvan FOCSA - a lire en premier

## Role individuel

Yvan FOCSA - Architecte securite / infrastructure, flux reseau et industrialisation du SOC externalise.

Mon perimetre couvre surtout :

- l'analyse du besoin client et des 30 centres ;
- le cadrage du MVP a 3 sites representatifs ;
- l'architecture SOC externalisee ;
- les flux de collecte des logs ;
- la coherence avec les briques SI du cahier des charges ;
- l'industrialisation vers un modele repetable ;
- la partie couts a expliquer simplement a l'oral.

## Livrables principaux a ouvrir

| Priorite | Livrable | Utilite |
|---:|---|---|
| 1 | `pdf/Yvan_FOCSA_Cadrage_Architecture_Organisation.pdf` | Document principal de ma partie architecture et besoin client. |
| 2 | `pdf/Yvan_FOCSA_Rendu_Individuel_Source.pdf` | Version PDF de mon rendu individuel source. |
| 3 | `diagrams/architecture_soc_externalise.png` | Schema principal a montrer en video. |
| 4 | `diagrams/topologie_sites_mvp.png` | Schema qui explique 30 centres cibles versus 3 sites MVP. |
| 5 | `diagrams/architecture_soc_externalise.drawio` | Source editable Draw.io du schema d'architecture. |
| 6 | `pdf/06_Script_Video_Yvan_Final.pdf` | Script final pret a lire pour la video. |
| 7 | `pdf/07_Stack_Technique_Concrete_Yvan.pdf` | Reponses concretes si le jury demande les produits, flux et ports. |
| 8 | `pdf/08_Argumentaire_Solutions_Concretes_Yvan.pdf` | Choix concrets argumentes pour chaque notion de ma partie. |

## Message cle a defendre

Le cahier des charges parle d'un reseau d'environ 30 centres. Le MVP ne simule pas 30 sites un par un : il prouve le modele sur 3 sites representatifs, puis documente comment le deploiement est repetable vers les autres centres via inventaire, templates, conventions de nommage, checklist d'onboarding et dashboards filtrables par site.

## Ce qui est complet dans ma partie

| Attendu | Statut | Preuve |
|---|---|---|
| Analyse du besoin client | Complete | Cadrage architecture + rendu individuel. |
| Organisation par brique SI | Complete | Postes, firewall, applications, serveurs, messagerie. |
| Architecture technique | Complete | Schema PNG + Draw.io + document architecture. |
| Flux de collecte | Complete | Schema flux + section ports/protocoles. |
| Stack concrete | Complete | pfSense CE, Wazuh agents, serveurs, apps, logs et ports. |
| Argumentaire technique | Complete | Choix concrets, alternatives, limites et phrases jury. |
| Industrialisation | Complete | Checklist onboarding + inventaire site exemple. |
| Couts | Complete pour ma partie | Phrase courte integree au script et au rendu. |
| Script video | Pret | `06_script_video_yvan_final.md` et PDF associe. |

## Ce qui reste hors dossier Yvan

Ces elements restent a finaliser avec le groupe :

- enregistrer la video finale 15 a 20 minutes ;
- afficher le nom de chaque membre pendant son passage ;
- ajouter le lien YouTube non repertorie ou la video dans le zip ;
- integrer les vraies captures Wazuh finales de Youssef ;
- verifier une derniere fois les IDs d'alertes entre rapport, regles, captures et video.
