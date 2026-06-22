# PB-006 - Scan reseau

## Objectif

Qualifier une alerte de scan reseau ou de reconnaissance sur un firewall ou un equipement expose.

## Declencheur

Alerte `SOC-AUDIO-PORT-SCAN`.

## Procedure

1. Identifier l'IP source et l'IP cible.
2. Identifier les ports testes.
3. Verifier la frequence et la duree du scan.
4. Determiner si la source est interne ou externe.
5. Si la source est externe et non legitime, bloquer l'IP.
6. Si la source est interne, identifier la machine et verifier son etat.
7. Rechercher d'autres signes de compromission.
8. Documenter l'incident.

## Preuves a conserver

- Logs firewall.
- IP source.
- IP cible.
- Ports testes.
- Decision de blocage ou investigation.

## Ameliorations possibles

- Ajouter une correlation IDS.
- Ajouter un seuil par nombre de ports uniques.
- Ajouter un dashboard des IP sources suspectes.

