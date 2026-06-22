# PB-005 - Phishing

## Objectif

Traiter une alerte liee a un email suspect, un domaine malveillant, un lien de phishing ou une piece jointe dangereuse.

## Declencheur

Alerte `SOC-AUDIO-PHISHING`.

## Procedure

1. Identifier l'expediteur, le destinataire et l'objet.
2. Verifier la presence d'un lien, d'une piece jointe ou d'un domaine suspect.
3. Determiner si l'utilisateur a clique ou ouvert la piece jointe.
4. Rechercher les emails similaires dans les autres boites.
5. Bloquer l'expediteur ou le domaine si necessaire.
6. Si clic confirme, analyser le poste utilisateur.
7. Demander une rotation de mot de passe si identifiants exposes.
8. Sensibiliser l'utilisateur.
9. Documenter l'incident.

## Preuves a conserver

- Expediteur.
- Destinataire.
- Objet.
- URL ou piece jointe.
- Action utilisateur.
- Mesure de blocage.

## Ameliorations possibles

- Ajouter une regle sur domaines suspects.
- Ajouter un tableau des campagnes de phishing.
- Creer une procedure de signalement utilisateur.

