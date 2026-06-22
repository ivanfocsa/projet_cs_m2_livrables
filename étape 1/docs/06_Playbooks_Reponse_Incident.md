# 06 - Playbooks de reponse incident

## 1. Objectif

Les playbooks decrivent la reaction attendue lorsqu'une alerte est generee par le SOC. Ils doivent aider l'analyste a qualifier l'evenement, limiter l'impact, documenter les actions et ameliorer la detection.

## 2. Processus general

Source Mermaid : [../diagrams/processus_incident_soc.mmd](../diagrams/processus_incident_soc.mmd)

| Etape | Action |
|---|---|
| Detection | L'alerte apparait dans le dashboard. |
| Qualification | L'analyste verifie la source, le contexte et la criticite. |
| Enrichissement | Recherche d'evenements lies : meme IP, meme compte, meme machine. |
| Decision | Faux positif, incident mineur ou incident confirme. |
| Reponse | Application du playbook correspondant. |
| Documentation | Capture, timeline, actions realisees. |
| Amelioration | Ajustement de regle ou procedure si besoin. |

## 3. Playbook brute force

Resume : verifier les echecs de connexion, identifier la source, bloquer si necessaire et forcer la rotation du mot de passe si compromission suspectee.

Actions principales :

1. Identifier le compte cible.
2. Verifier le nombre d'echecs, la source et l'horaire.
3. Chercher un succes de connexion apres les echecs.
4. Si succes suspect : isoler le compte ou forcer un changement de mot de passe.
5. Bloquer l'IP source si elle est externe ou non legitime.
6. Documenter l'incident.

Fichier detaille : [../playbooks/PB-001-Brute-Force.md](../playbooks/PB-001-Brute-Force.md)

## 4. Playbook execution suspecte

Actions principales :

1. Identifier la machine et l'utilisateur.
2. Relever le processus, le chemin, la ligne de commande et l'heure.
3. Verifier si l'action correspond a une tache legitime.
4. Si doute : isoler la machine du reseau de production.
5. Collecter les journaux utiles.
6. Supprimer ou neutraliser l'element malveillant si confirme.
7. Documenter les preuves.

Fichier detaille : [../playbooks/PB-002-Execution-Suspecte.md](../playbooks/PB-002-Execution-Suspecte.md)

## 5. Playbook USB suspect

Actions principales :

1. Identifier le poste et l'utilisateur.
2. Verifier le type de peripherique.
3. Demander confirmation au responsable local si usage legitime.
4. Si non autorise : retirer le peripherique et analyser le poste.
5. Rappeler la politique d'utilisation des supports amovibles.
6. Documenter l'incident.

Fichier detaille : [../playbooks/PB-003-USB-Suspect.md](../playbooks/PB-003-USB-Suspect.md)

## 6. Playbook acces dossier patient

Actions principales :

1. Identifier l'utilisateur et les dossiers consultes.
2. Verifier si l'acces correspond a son role.
3. Rechercher un volume anormal ou un horaire inhabituel.
4. Si suspicion : suspendre temporairement le compte ou limiter les droits.
5. Prevenir le responsable securite.
6. Documenter l'analyse et les preuves.

Fichier detaille : [../playbooks/PB-004-Acces-Dossier-Patient.md](../playbooks/PB-004-Acces-Dossier-Patient.md)

## 7. Playbook phishing

Actions principales :

1. Identifier expediteur, destinataire, objet et piece jointe.
2. Verifier si l'utilisateur a clique ou ouvert la piece jointe.
3. Bloquer l'expediteur ou le domaine si necessaire.
4. Rechercher les emails similaires dans la messagerie.
5. Si clic confirme : analyser le poste utilisateur.
6. Sensibiliser l'utilisateur et documenter.

Fichier detaille : [../playbooks/PB-005-Phishing.md](../playbooks/PB-005-Phishing.md)

