# PB-001 - Brute force

## Objectif

Traiter une alerte d'authentifications echouees repetees sur un compte utilisateur ou un serveur.

## Declencheur

Alerte `SOC-AUDIO-BRUTEFORCE` ou detection d'un volume anormal d'echecs de connexion.

## Criticite

| Situation | Criticite |
|---|---|
| Echecs isoles | Faible |
| Plusieurs echecs sur un meme compte | Moyenne |
| Plusieurs echecs puis succes | Haute |
| Compte admin cible | Critique |

## Procedure

1. Identifier le compte cible.
2. Identifier la machine ou l'IP source.
3. Verifier le nombre d'echecs et la fenetre temporelle.
4. Chercher un succes de connexion apres les echecs.
5. Verifier si l'activite correspond a un usage legitime.
6. Si suspicion confirmee, bloquer temporairement la source ou le compte.
7. Demander une rotation de mot de passe si necessaire.
8. Rechercher des activites post-connexion.
9. Documenter l'incident dans le REX.

## Preuves a conserver

- Capture de l'alerte SIEM.
- Logs d'authentification.
- Compte cible.
- IP source ou machine source.
- Decision prise.

## Ameliorations possibles

- Ajuster le seuil de detection.
- Ajouter une correlation avec succes de connexion.
- Ajouter un dashboard des comptes les plus attaques.

