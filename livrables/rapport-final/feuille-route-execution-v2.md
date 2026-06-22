# Feuille de route execution - V2

Objectif : suivre la consolidation du rendu final avec preuves, captures, video et rapports individuels.

## 1. Etat des priorites

| Priorite | Action | Responsable | Statut |
|---|---|---|---|
| 1 | Produire la vue dashboard d'accueil | Youssef | Capture de demonstrateur disponible |
| 2 | Capturer l'etat des alertes Daylight | Kilyan / Mahamadou | Capture liste alertes disponible |
| 3 | Capturer le detail d'une alerte `100100` | Mahamadou | Capture detail disponible |
| 4 | Capturer le detail d'une alerte `100110` | Mahamadou | Capture detail disponible |
| 5 | Ajouter les captures au dossier de rendu | Yvan / Kilyan | Dossier preuves consolide |
| 6 | Verifier les schemas Mermaid | Yvan | Sources Mermaid disponibles |
| 7 | Rejouer les logs si necessaire | Youssef / Mahamadou | Script et logs disponibles |

## 2. Ce qu'il faut faire pour le rapport technique

| Section | Statut consolide | Controle final |
|---|---|---|
| Resume executif | Redige | Relire apres enregistrement video |
| Contexte client | Redige | Ajouter le code promotion si necessaire |
| Problematique | Redige | Valider avec equipe |
| Architecture | Redige | Afficher le schema pendant la video |
| Implementation MVP | Redige avec preuves | Remplacer par captures Wazuh live si possible |
| Regles detection | Redige | Extrait XML disponible en preuves |
| Alertes obtenues | Redige | Captures principales disponibles |
| Playbooks | Redige | Chemins harmonises |
| Couts | Redige | Estimation production a defendre oralement |
| Industrialisation | Redige | Checklist onboarding disponible |
| Limites | Redige | Discours MVP a assumer |

## 3. Ce qu'il faut faire pour le rapport individuel Yvan

| Section | Statut | Controle final |
|---|---|---|
| Role | Redige | Cohérent avec rapport groupe |
| Contributions | Redige | Preuves reliees au rapport |
| Perspectives | Redige | Garder en soutien oral |
| Limites | Redige | Assumer le statut MVP |
| Analyse critique | Redige | Ton personnel conserve |
| Competences | Redige | A relier aux cours si question jury |
| Conclusion | Redige | PDF regenere |

## 4. Captures disponibles

Enregistrer les captures dans `livrables/preuves/sprint-01/captures-dashboard/`.

| Nom de fichier conseille | Capture |
|---|---|
| `01-dashboard-home.png` | Supervision globale |
| `02-alertes-daylight-liste.png` | Liste des alertes Daylight |
| `03-alerte-powershell-100100.png` | Detail execution PowerShell |
| `04-alerte-bruteforce-100110.png` | Detail brute force |
| `05-alerte-dossier-patient-100120.png` | Detail acces dossier patient |
| `06-alerte-groupe-privilegie-100130.png` | Detail modification groupe privilegie |
| `07-alerte-usb-100140.png` | Detail USB |
| `08-alerte-phishing-100150.png` | Detail phishing |
| `09-alerte-scan-100160.png` | Detail scan reseau |

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
- les captures dashboard sont disponibles ;
- les playbooks sont disponibles ;
- les regles Wazuh sont en annexe ;
- la matrice cahier des charges -> preuves est complete ;
- le zip final respecte la nomenclature demandee.
