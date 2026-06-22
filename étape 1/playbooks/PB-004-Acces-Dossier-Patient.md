# PB-004 - Acces anormal a un dossier patient

## Objectif

Qualifier un acces inhabituel a des donnees sensibles dans l'application metier ou sur un serveur de fichiers.

## Declencheur

Alerte `SOC-AUDIO-PATIENT-ACCESS-ANOMALY`.

## Procedure

1. Identifier l'utilisateur concerne.
2. Identifier les dossiers ou ressources consultees.
3. Verifier le volume d'acces et l'horaire.
4. Comparer avec le role metier de l'utilisateur.
5. Rechercher d'autres evenements suspects sur le meme compte.
6. Si l'acces semble non legitime, limiter temporairement le compte.
7. Prevenir le responsable securite ou metier.
8. Documenter l'analyse et les preuves.

## Preuves a conserver

- Logs applicatifs.
- Ressources consultees.
- Utilisateur et site.
- Volume d'acces.
- Decision de qualification.

## Ameliorations possibles

- Ajouter des seuils par role.
- Detecter les acces hors horaires.
- Mettre en place un reporting donnees sensibles.

