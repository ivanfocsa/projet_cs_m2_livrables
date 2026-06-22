# PB-002 - Execution suspecte

## Objectif

Qualifier une alerte liee a l'execution d'un processus, script ou binaire suspect sur un poste.

## Declencheur

Alerte `SOC-AUDIO-SUSPICIOUS-PROCESS`.

## Procedure

1. Identifier le poste, l'utilisateur et l'horodatage.
2. Relever le nom du processus, le chemin et la ligne de commande.
3. Verifier si l'execution est attendue dans le contexte metier.
4. Chercher des evenements associes : creation fichier, connexion reseau, elevation de droits.
5. Si l'activite est suspecte, isoler le poste ou demander son retrait du reseau.
6. Collecter les logs utiles pour analyse.
7. Supprimer ou neutraliser le fichier si l'activite est confirmee comme malveillante.
8. Documenter l'incident.

## Preuves a conserver

- Nom du processus.
- Ligne de commande.
- Utilisateur.
- Machine.
- Evenements lies.
- Capture de l'alerte.

## Ameliorations possibles

- Enrichir la regle avec des chemins interdits.
- Surveiller PowerShell, scripts temporaires et dossiers utilisateur.
- Ajouter une liste blanche pour les outils legitimes.

