# Dossier Yvan FOCSA

Ce dossier regroupe ta partie individuelle et tes supports de soutenance pour le projet de SOC externalise Daylight.

Commence par ouvrir `00_A_LIRE_DOSSIER_YVAN_FINAL.md` ou sa version PDF dans `pdf/00_A_LIRE_DOSSIER_YVAN_FINAL.pdf`.

## Role a annoncer

Yvan FOCSA - Architecte securite / infrastructure, flux reseau et industrialisation.

Formulation conseillee a l'oral :

> Mon role a ete de cadrer l'architecture SOC externalisee, de definir le perimetre MVP, de structurer les flux de collecte et de montrer comment le demonstrateur peut etre industrialise vers environ 30 sites.

## Ce qui est deja fait

| Element | Statut | Fichier |
|---|---|---|
| Rendu individuel Yvan | Pret | `supports/Yvan_FOCSA_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf` |
| Source du rendu individuel | Pret | `supports/Yvan_FOCSA_rendu_individuel_v1.md` |
| Partie cadrage / architecture / organisation | Pret | `supports/Yvan_FOCSA_Cadrage_Architecture_Organisation.md` |
| Script video Yvan existant | Pret | `supports/Yvan_FOCSA_Script_Video_Demo.md` |
| Script oral court consolide | Pret | `02_script_oral_yvan_3_5_min.md` |
| Script video final pret a lire | Pret | `06_script_video_yvan_final.md` |
| Supports a montrer pendant ton passage | Pret | `03_supports_a_montrer.md` |
| Questions / reponses jury | Pret | `04_questions_reponses_jury_yvan.md` |
| Checklist finale Yvan | Pret | `05_checklist_finale_yvan.md` |
| Pack PDF de tes Markdown | Pret | `pdf/` |
| Schemas PNG et Draw.io | Pret | `diagrams/` |

## Livrables PDF generes

Les fichiers Markdown importants ont ete convertis en PDF dans `pdf/`.

| PDF | Usage |
|---|---|
| `pdf/00_A_LIRE_DOSSIER_YVAN_FINAL.pdf` | Point d'entree du dossier Yvan. |
| `pdf/Yvan_FOCSA_Cadrage_Architecture_Organisation.pdf` | Document principal architecture, besoin client et industrialisation. |
| `pdf/Yvan_FOCSA_Rendu_Individuel_Source.pdf` | Version PDF du rendu individuel source. |
| `pdf/06_Script_Video_Yvan_Final.pdf` | Script final pour enregistrer ton passage video. |
| `pdf/07_Stack_Technique_Concrete_Yvan.pdf` | Reponses concretes : pfSense, agents, serveurs, logs, ports. |
| `pdf/08_Argumentaire_Solutions_Concretes_Yvan.pdf` | Argumentaire complet : choix, preuves et phrases a dire. |
| `pdf/Matrice_Conformite_Cahier_Charges.pdf` | Correspondance entre cahier des charges et preuves. |
| `pdf/Checklist_Onboarding_Client.pdf` | Support industrialisation vers les sites clients. |

## Schemas fournis

| Schema | Format | Usage |
|---|---|---|
| `diagrams/architecture_soc_externalise.png` | PNG | Schema principal a montrer dans la video. |
| `diagrams/architecture_soc_externalise.drawio` | Draw.io | Source editable du schema principal. |
| `diagrams/flux_collecte_logs.png` | PNG | Explication des flux agents, syslog et logs applicatifs. |
| `diagrams/processus_incident_soc.png` | PNG | Chaine alerte, qualification, playbook, preuve. |
| `diagrams/topologie_sites_mvp.png` | PNG | Clarifie 30 centres cibles versus 3 sites MVP. |

## Ce qui reste a faire par toi

| Priorite | Action | Pourquoi |
|---|---|---|
| 1 | Enregistrer ou preparer ton passage oral de 3 a 5 minutes | La video doit montrer ta contribution individuelle. |
| 2 | Afficher ton nom pendant ton passage | C'est demande dans le cadre pedagogique. |
| 3 | Montrer au moins un schema architecture ou dashboard global | Cela prouve ton role architecture/industrialisation. |
| 4 | Dire une phrase courte sur les couts | Le rendu M2 demande une gestion des couts. |
| 5 | Verifier le code promotion exact | Le zip utilise `M2CS` par defaut. |
| 6 | Remplacer le lien YouTube placeholder quand la video est prete | Sans lien reel, le rendu video n'est pas valide. |

## Message cle a faire passer

Le MVP ne cherche pas a reproduire 30 sites en production. Il prouve une chaine SOC complete et industrialisable : collecte, detection, alerte, analyse, reponse, documentation et extension progressive vers plusieurs centres.

Phrase couts a connaitre :

> Le MVP limite les couts logiciels grace a Wazuh et aux outils open-source. En production, les couts principaux seraient l'infrastructure, le stockage des logs, l'exploitation SOC, la maintenance et l'onboarding des sites.
