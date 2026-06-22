# 05 - Scenarios de detection SOC

## 1. Objectif

Ce document decrit les scenarios de detection a implementer dans le demonstrateur. Chaque scenario doit produire :

- un evenement source ;
- une alerte dans le SIEM ;
- une preuve visible dans le dashboard ;
- une procedure de reponse associee ;
- une conclusion pour le REX.

## 2. Scenario 1 - Brute force

| Element | Detail |
|---|---|
| Objectif | Detecter des echecs d'authentification repetes sur un compte. |
| Source | Poste utilisateur ou serveur interne. |
| Log attendu | Plusieurs echecs de connexion dans un court intervalle. |
| Alerte | `SOC-AUDIO-BRUTEFORCE` |
| Criticite | Haute si plusieurs echecs puis succes. |
| Preuve | Capture alerte Wazuh + detail utilisateur/source. |
| Playbook | [playbooks/PB-001-Brute-Force.md](../playbooks/PB-001-Brute-Force.md) |

Test de demo :

1. Generer 6 echecs de connexion sur un compte fictif.
2. Envoyer les logs vers Wazuh.
3. Verifier que l'alerte apparait.
4. Qualifier l'alerte.
5. Appliquer le playbook.

## 3. Scenario 2 - Execution suspecte

| Element | Detail |
|---|---|
| Objectif | Detecter une commande ou un processus inhabituel sur un poste. |
| Source | Endpoint agent Wazuh / logs simules. |
| Log attendu | Execution d'un script suspect, PowerShell anormal ou binaire inconnu. |
| Alerte | `SOC-AUDIO-SUSPICIOUS-PROCESS` |
| Criticite | Moyenne a haute. |
| Preuve | Nom du processus, poste, utilisateur, horodatage. |
| Playbook | [playbooks/PB-002-Execution-Suspecte.md](../playbooks/PB-002-Execution-Suspecte.md) |

## 4. Scenario 3 - Usage USB suspect

| Element | Detail |
|---|---|
| Objectif | Surveiller le branchement d'un support USB non autorise. |
| Source | Poste audioprothesiste. |
| Log attendu | Evenement de connexion peripherique USB. |
| Alerte | `SOC-AUDIO-USB-SUSPECT` |
| Criticite | Moyenne. |
| Preuve | Identifiant peripherique, utilisateur, machine. |
| Playbook | [playbooks/PB-003-USB-Suspect.md](../playbooks/PB-003-USB-Suspect.md) |

## 5. Scenario 4 - Acces anormal dossier patient

| Element | Detail |
|---|---|
| Objectif | Detecter un acces inhabituel a un dossier patient ou un volume d'acces excessif. |
| Source | Application metier simulee ou serveur fichiers. |
| Log attendu | Plusieurs consultations de dossiers par un meme utilisateur. |
| Alerte | `SOC-AUDIO-PATIENT-ACCESS-ANOMALY` |
| Criticite | Haute. |
| Preuve | Utilisateur, dossier, nombre d'acces, horaire. |
| Playbook | [playbooks/PB-004-Acces-Dossier-Patient.md](../playbooks/PB-004-Acces-Dossier-Patient.md) |

## 6. Scenario 5 - Phishing

| Element | Detail |
|---|---|
| Objectif | Detecter un email suspect ou une piece jointe dangereuse. |
| Source | Messagerie simulee. |
| Log attendu | Email marque phishing, domaine suspect, piece jointe bloquee. |
| Alerte | `SOC-AUDIO-PHISHING` |
| Criticite | Haute si utilisateur a clique ou ouvert la piece jointe. |
| Preuve | Expediteur, destinataire, objet, URL ou piece jointe. |
| Playbook | [playbooks/PB-005-Phishing.md](../playbooks/PB-005-Phishing.md) |

## 7. Scenario 6 - Scan reseau

| Element | Detail |
|---|---|
| Objectif | Detecter une phase de reconnaissance reseau. |
| Source | Firewall / IDS / syslog simule. |
| Log attendu | Connexions refusees sur plusieurs ports. |
| Alerte | `SOC-AUDIO-PORT-SCAN` |
| Criticite | Moyenne. |
| Preuve | IP source, IP cible, ports testes. |
| Playbook | [playbooks/PB-006-Scan-Reseau.md](../playbooks/PB-006-Scan-Reseau.md) |

## 8. Synthese des preuves

| Scenario | Preuve SIEM | Preuve documentaire |
|---|---|---|
| Brute force | Alerte + logs authentification | REX incident simule. |
| Execution suspecte | Alerte endpoint | Capture processus. |
| USB suspect | Evenement USB | Procedure utilisateur. |
| Acces dossier patient | Alerte applicative | Analyse confidentialite. |
| Phishing | Alerte messagerie | Playbook phishing. |
| Scan reseau | Logs firewall | Mesure de blocage. |

