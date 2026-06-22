# Specification dashboards SOC

## Objectif

Definir les vues a creer dans Wazuh Dashboard pour la demonstration.

## Dashboard 1 - Supervision globale

Public : client, direction, superviseur.

Widgets :

| Widget | Description |
|---|---|
| Alertes par criticite | Nombre d'alertes faible, moyenne, haute, critique. |
| Alertes par site | Repartition Site 1, Site 2, Site 3. |
| Alertes par type | Brute force, phishing, USB, endpoint, applicatif, reseau. |
| Timeline 24h | Evolution des alertes dans le temps. |
| Top machines | Machines avec le plus d'alertes. |

## Dashboard 2 - Analyste SOC

Public : analyste.

Widgets :

| Widget | Description |
|---|---|
| Alertes recentes | Liste detaillee des alertes recentes. |
| Compte cible | Utilisateurs les plus touches. |
| IP sources suspectes | IP avec le plus d'evenements. |
| Evenements lies | Correlation par machine ou compte. |
| Statut investigation | A traiter, en cours, clos. |

## Dashboard 3 - Administration technique

Public : administrateur SOC.

Widgets :

| Widget | Description |
|---|---|
| Etat agents | Agents actifs, deconnectes, jamais connectes. |
| Volume logs | Nombre d'evenements par source. |
| Sources silencieuses | Machines ou sites sans logs recents. |
| Erreurs collecte | Problemes de parsing ou communication. |
| Capacite stockage | Volume d'indexation. |

## Filtres communs

- site ;
- machine ;
- utilisateur ;
- criticite ;
- scenario ;
- source de logs ;
- periode.

## Captures attendues

| Capture | Usage |
|---|---|
| Supervision globale | Rapport et video. |
| Alerte brute force | Scenario detection. |
| Alerte phishing | Scenario detection. |
| Etat agents | Preuve collecte. |
| Volume par source | Preuve multi-source. |

