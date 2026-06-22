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

## Variables a documenter

| Variable | Exemple |
|---|---|
| Version Wazuh | A renseigner |
| IP serveur SOC | A renseigner |
| Port dashboard | A renseigner |
| Nom admin | A renseigner |
| Methode installation | Packages / Docker / Script officiel |

## Preuves a produire

- capture de l'interface web ;
- capture de l'etat des services ;
- capture d'un agent actif ;
- capture d'un log recu ;
- capture d'une alerte de test.

