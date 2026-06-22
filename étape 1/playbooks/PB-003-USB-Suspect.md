# PB-003 - Usage USB suspect

## Objectif

Traiter une alerte de connexion d'un support USB non autorise sur un poste d'audioprothesiste.

## Declencheur

Alerte `SOC-AUDIO-USB-SUSPECT`.

## Procedure

1. Identifier le poste et l'utilisateur.
2. Identifier le peripherique USB si l'information est disponible.
3. Verifier si l'usage est autorise par la politique interne.
4. Demander confirmation au responsable du centre.
5. Si usage non autorise, demander le retrait du support.
6. Verifier si des fichiers sensibles ont ete copies ou consultes.
7. Lancer une verification antivirus/EDR si disponible.
8. Documenter l'incident et rappeler la procedure utilisateur.

## Preuves a conserver

- Evenement USB.
- Utilisateur.
- Machine.
- Heure de connexion.
- Decision de traitement.

## Ameliorations possibles

- Mettre en place une politique de blocage USB.
- Ajouter une liste de peripheriques autorises.
- Sensibiliser les centres.

