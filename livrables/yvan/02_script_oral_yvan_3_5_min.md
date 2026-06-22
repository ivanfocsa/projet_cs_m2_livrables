# Script oral Yvan - version finale 3 a 5 minutes

## A afficher pendant mon passage

Yvan FOCSA - Architecte securite / infrastructure et industrialisation

## Supports a ouvrir avant de parler

1. `livrables/yvan/supports/architecture_soc_externalise.mmd`
2. `livrables/yvan/supports/01-dashboard-home.png`
3. `livrables/yvan/supports/client_onboarding_checklist.md`
4. `livrables/yvan/supports/site_inventory.example.yml`

## Script final conseille

Bonjour, je suis Yvan FOCSA. Sur ce projet, mon role est d'intervenir sur l'architecture securite, le cadrage du perimetre MVP, les flux entre les sites clients et le SOC central, ainsi que l'industrialisation de la solution.

Le client represente un reseau d'audioprothesistes avec environ 30 points de vente. Chaque centre utilise plusieurs briques sensibles : des postes de travail, des applications metier pour les rendez-vous et dossiers patients, une messagerie professionnelle, des serveurs internes et des equipements reseau. Le besoin principal est de centraliser les evenements de securite et de permettre a un SOC externalise de detecter, qualifier et traiter les incidents.

Pour le MVP, nous avons fait un choix volontaire : ne pas reproduire directement les 30 sites. Nous avons retenu trois sites simules, car cela permet de prouver la chaine SOC sans complexifier inutilement l'environnement. L'objectif est de demontrer le modele complet : collecte, detection, alerte, investigation, playbook et reporting.

Sur le schema d'architecture, on voit que le SOC est centralise cote prestataire autour de Wazuh. Les sites clients restent producteurs de logs. Les postes et serveurs remontent leurs evenements via agents Wazuh, les firewalls via syslog, et les applications metier via des fichiers de logs applicatifs. Pour le firewall, le choix cible concret est pfSense CE ; dans le MVP, il est represente par `FW-S01` et `FW-S02` avec des logs syslog simules. Ces evenements sont ensuite centralises dans le SIEM, indexes, analyses par les regles de detection et rendus visibles dans les dashboards.

Ce choix repond au cahier des charges parce que Wazuh est open-source, accessible via navigateur, compatible avec une collecte multi-source et adapte a une logique d'infogerance. Le demonstrateur reste volontairement limite, mais il montre une architecture reproductible et scalable.

Ma contribution porte aussi sur l'industrialisation. Pour passer de trois sites simules a trente sites, il faut standardiser le deploiement : convention de nommage, inventaire des sites, checklist d'onboarding, templates de configuration, dashboards filtrables par site et procedure de validation de la collecte. L'objectif est qu'un nouveau centre puisse etre integre de maniere repetable, sans repartir de zero.

Sur la partie couts, le choix open-source permet de limiter le cout logiciel du MVP. En production, les vrais postes de cout seraient plutot l'infrastructure, le stockage des logs, l'exploitation SOC, les sauvegardes, la maintenance et le deploiement sur chaque site. La standardisation est donc importante, car plus l'onboarding est repetable, plus le cout par site diminue.

Les limites sont assumees : certains logs sont simules, le MVP n'est pas un SOC 24/7 complet, et une architecture de production demanderait plus de travail sur le dimensionnement, la retention, la haute disponibilite, le RBAC et la supervision de sante des agents. Mais le projet prouve l'essentiel : une chaine SOC complete, documentee et defendable.

Pour conclure, ma partie montre que le projet n'est pas seulement une installation Wazuh. C'est une proposition d'architecture SOC externalisee, pensee pour etre lisible, reproductible et industrialisable dans un contexte professionnel.

## Version courte 90 secondes

Bonjour, je suis Yvan FOCSA, architecte securite et infrastructure sur le projet. Mon role est de cadrer l'architecture du SOC externalise, de definir le perimetre MVP, de structurer les flux de collecte et de montrer comment la solution peut etre industrialisee.

Le client represente environ 30 centres d'audioprothesistes. Pour le MVP, nous simulons trois sites representatifs afin de prouver une chaine SOC complete sans reproduire toute la complexite de la production.

L'architecture centralise les evenements dans Wazuh. Les postes et serveurs utilisent des agents, les firewalls pfSense CE envoient du syslog, et les applications metier produisent des logs applicatifs. Ces evenements alimentent les regles, les alertes, les dashboards et les playbooks.

Ma partie consiste aussi a montrer le passage a l'echelle : conventions de nommage, inventaire, checklist onboarding, templates et dashboards filtrables par site. Cote couts, Wazuh limite le cout logiciel du MVP, mais en production il faudrait anticiper l'infrastructure, le stockage, l'exploitation SOC et la maintenance.

Le demonstrateur est limite, mais il prouve un modele clair : collecter, detecter, qualifier, repondre et documenter.

## Phrases de secours

Si on me demande pourquoi seulement trois sites :

> Les trois sites sont un modele representatif. L'objectif du MVP est de prouver la chaine SOC et la methode d'industrialisation, pas de reproduire manuellement les 30 centres.

Si on me demande si Docker suffit pour la production :

> Non, Docker est un choix de lab. En production, les postes, serveurs et firewalls seraient reels ou virtualises, avec durcissement, filtrage reseau, retention et supervision de sante.

Si on me demande les couts :

> Le MVP limite les couts logiciels grace a Wazuh. En production, les couts principaux seraient l'infrastructure, le stockage des logs, l'exploitation SOC et l'onboarding des sites.
