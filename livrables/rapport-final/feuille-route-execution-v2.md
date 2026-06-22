# Feuille de route execution - V2

Objectif : transformer la V1 documentaire et le sprint 01 technique en rendu final complet avec preuves, captures, video et rapports individuels.

## 1. Priorite immediate

| Priorite | Action | Responsable | Preuve attendue |
|---|---|---|---|
| 1 | Ouvrir Wazuh Dashboard et capturer la page d'accueil | Youssef | Capture dashboard |
| 2 | Capturer l'etat des alertes Daylight | Kilyan / Mahamadou | Capture alertes |
| 3 | Capturer le detail d'une alerte `100100` | Mahamadou | Capture detail alerte |
| 4 | Capturer le detail d'une alerte `100110` | Mahamadou | Capture detail brute force |
| 5 | Ajouter les captures au rapport technique | Yvan / Kilyan | Rapport mis a jour |
| 6 | Verifier les schemas Mermaid | Yvan | Images PNG/SVG pour rapport |
| 7 | Rejouer les logs si necessaire | Youssef / Mahamadou | Alertes visibles |

## 2. Ce qu'il faut faire pour le rapport technique

| Section | Statut V1 | A completer |
|---|---|---|
| Resume executif | Redige | Ajuster apres demo finale |
| Contexte client | Redige | Ajouter eventuellement nom promotion |
| Problematique | Redige | Valider avec equipe |
| Architecture | Redige | Ajouter schema exporte en image |
| Implementation MVP | Redige avec preuves texte | Ajouter captures dashboard |
| Regles detection | Redige | Ajouter extrait XML en annexe |
| Alertes obtenues | Redige | Ajouter captures pour chaque alerte majeure |
| Playbooks | Redige | Harmoniser avec playbooks finaux |
| Couts | Redige | Ajouter estimation chiffre production si besoin |
| Industrialisation | Redige | Ajouter tableau ports/protocoles |
| Limites | Redige | Ajuster selon ce qui marche vraiment |

## 3. Ce qu'il faut faire pour le rapport individuel Yvan

| Section | Statut | A faire |
|---|---|---|
| Role | Redige | Valider le role final avec l'equipe |
| Contributions | Redige | Ajouter preuves personnelles |
| Perspectives | Redige | Garder ou raccourcir |
| Limites | Redige | Ajouter experience reelle apres Wazuh |
| Analyse critique | Redige | Personnaliser le ton |
| Competences | Redige | Ajouter cours associes si utile |
| Conclusion | Redige | Ajuster avant PDF |

## 4. Captures a produire

Enregistrer les captures dans `livrables/preuves/sprint-01/captures-dashboard/`.

| Nom de fichier conseille | Capture |
|---|---|
| `01-dashboard-login-or-home.png` | Acces Wazuh Dashboard |
| `02-alertes-daylight-liste.png` | Liste des alertes Daylight |
| `03-alerte-powershell-100100.png` | Detail execution PowerShell |
| `04-alerte-bruteforce-100110.png` | Detail brute force |
| `05-alerte-dossier-patient-100120.png` | Detail acces dossier patient |
| `06-alerte-groupe-privilegie-100130.png` | Detail modification groupe privilegie |
| `07-alerte-usb-100140.png` | Detail USB |

## 5. Video MVP

| Passage | Intervenant | Support |
|---|---|---|
| Contexte et besoin | Kilyan | Rapport + cahier des charges |
| Architecture SOC | Yvan | Schema architecture |
| Wazuh et collecte | Youssef | Dashboard + etat services |
| Alertes et investigation | Mahamadou | Alertes Wazuh |
| Playbooks | Mahamadou / Kilyan | Playbook brute force ou PowerShell |
| Industrialisation | Yvan | Checklist onboarding + extension 30 sites |
| Conclusion | Tous | Matrice conformite |

## 6. Definition de fini

Le projet est pret a rendre si :

- le rapport technique groupe est exporte en PDF ;
- chaque membre a son rapport individuel en PDF ;
- la video dure entre 15 et 20 minutes ;
- chaque membre parle avec son nom affiche ;
- les captures Wazuh sont inserees ;
- les playbooks sont disponibles ;
- les regles Wazuh sont en annexe ;
- la matrice cahier des charges -> preuves est complete ;
- le zip final respecte la nomenclature demandee.

