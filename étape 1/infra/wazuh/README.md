# Deploiement Wazuh - Socle SOC

## Objectif

Ce dossier sert de point de depart pour le deploiement du SIEM Wazuh.

## Recommandation de mise en place

Pour eviter les problemes de version et garder une installation propre, l'equipe doit s'appuyer sur la documentation officielle Wazuh au moment du deploiement, puis noter la version retenue dans le rapport.

Approche conseillee :

1. Choisir une VM Linux dediee au SOC.
2. Installer Wazuh Manager, Wazuh Indexer et Wazuh Dashboard.
3. Verifier l'acces web.
4. Creer les comptes et roles.
5. Installer un premier agent.
6. Capturer les preuves.

## Script SIEM integre - Youssef

Le travail SIEM de Youssef est integre dans le depot via le script :

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup-siem-lab.ps1
```

Ce script est a lancer depuis la racine du depot, avec Docker Desktop ouvert et la stack Wazuh single-node deja active.

Il automatise :

- le conteneur Linux `serveur-01` ;
- l'installation de l'agent Wazuh 4.14.5-1 ;
- la collecte de `/var/log/auth.log` ;
- une simulation brute force SSH pour obtenir l'alerte Wazuh `5712` ;
- les comptes RBAC `analyste` et `supervision` avec le role lecture seule `soc_readonly` ;
- les scripts npm disponibles dans ce depot pour regenerer les logs et preuves Daylight.

Documentation support : `livrables/youssef/supports/Documentation_SIEM_Youssef_GUERNIOU.pdf`.

## Variables a documenter

| Variable | Exemple |
|---|---|
| Version Wazuh | 4.14.5 pour la stack Docker, agent 4.14.5-1 pour `serveur-01` |
| IP serveur SOC | Lab local / `localhost` |
| Port dashboard | HTTPS `https://localhost` |
| Nom admin | `admin` pour le lab |
| Methode installation | Docker single-node + script PowerShell d'integration |

## Preuves a produire

- capture de l'interface web ;
- capture de l'etat des services ;
- capture d'un agent actif ;
- capture d'un log recu ;
- capture d'une alerte de test.
- capture RBAC du role `soc_readonly` ;
- capture de l'alerte SSH brute force `5712`.
