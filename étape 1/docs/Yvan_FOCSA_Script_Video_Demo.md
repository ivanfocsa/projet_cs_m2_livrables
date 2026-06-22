# Script video - Intervention Yvan FOCSA

## Objectif de mon passage

Mon intervention dans la video doit montrer que le projet est cadre, coherent et aligne avec le cahier des charges. Je presente le contexte client, la problematique, le perimetre retenu, l'architecture globale, l'organisation de l'equipe et la logique d'industrialisation.

Nom a afficher a l'ecran : **Yvan FOCSA - Coordinateur projet / Architecte securite**

## Passage 1 - Introduction du contexte

Bonjour, je suis Yvan FOCSA, coordinateur projet et architecte securite sur ce projet.

Notre client est un reseau de centres d'audioprothesistes reparti sur une trentaine de points de vente en France. Ces centres utilisent plusieurs briques sensibles : des postes de travail, des equipements reseau, des applications metiers, des serveurs internes et une messagerie professionnelle.

La difficulte principale est que le client fait face a une augmentation des menaces cyber, sans disposer en interne des ressources necessaires pour exploiter un SOC complet. Notre objectif est donc de proposer un SOC externalise, capable de centraliser les evenements de securite, de produire des alertes exploitables et de fournir une base industrialisable pour un futur service d'infogerance.

## Passage 2 - Problematique et perimetre

La problematique que nous avons retenue est la suivante : comment concevoir un SOC externalise, open-source, securise, lisible et industrialisable, capable de superviser plusieurs sites d'audioprothesistes et de detecter les evenements de securite critiques ?

Pour le MVP, nous avons choisi de ne pas simuler directement les trente points de vente. Nous modelisons trois sites representatifs, afin de prouver le fonctionnement de la solution tout en gardant un environnement maitrisable.

Ces trois sites permettent de representer les principales briques du cahier des charges : les postes de travail des audioprothesistes, les routeurs et firewalls, les applications metiers, les serveurs internes et la messagerie professionnelle.

## Passage 3 - Architecture globale

L'architecture repose sur un SOC centralise base sur Wazuh. Les sites clients simules envoient leurs evenements vers le SIEM central via plusieurs mecanismes de collecte : agents Wazuh pour les postes et serveurs, syslog pour les equipements reseau, et fichiers de logs pour les applications metiers simulees.

La plateforme SOC fournit ensuite une interface web, des regles de detection, des dashboards, des alertes et des playbooks de reponse.

Ce choix technique repond directement au cahier des charges, car Wazuh est open-source, accessible via navigateur, compatible avec une collecte multi-source et adapte a une logique de supervision externalisee.

## Passage 4 - Organisation de l'equipe

Nous avons reparti les roles de maniere a couvrir l'ensemble du cycle projet.

Je prends en charge le cadrage, l'architecture, le planning, le backlog, la gestion des couts et la coherence des livrables.

Youssef est responsable de l'integration SIEM : installation de Wazuh, connexion des agents, collecte des logs et documentation technique.

Kilyan prend le role d'analyste SOC : il travaille sur les cas d'usage, les regles de detection, les dashboards et la qualification des alertes.

Mahamadou prend en charge la partie Blue Team et reponse incident : playbooks, procedures, generation d'evenements et scripts de remediation.

Cette organisation nous permet de couvrir les attentes techniques, methodologiques et documentaires du projet.

## Passage 5 - Scenarios de demonstration

Pour demontrer la valeur du SOC, nous avons retenu cinq scenarios principaux.

Le premier est une tentative de brute force, pour montrer la detection d'authentifications echouees repetees.

Le deuxieme est une execution suspecte sur un poste utilisateur.

Le troisieme concerne l'usage USB suspect, important dans un contexte de postes de travail en centre.

Le quatrieme simule un acces anormal a un dossier patient ou a une ressource sensible.

Le cinquieme porte sur un scenario de phishing, avec qualification de l'alerte et playbook de reponse.

Chaque scenario doit produire une trace visible dans le SIEM, une alerte exploitable et une procedure de reaction documentee.

## Passage 6 - Industrialisation et conclusion

Au-dela du demonstrateur, notre solution est pensee pour etre industrialisable. Le principe est de valider le modele sur trois sites, puis de l'etendre progressivement aux trente centres du reseau.

Pour cela, nous prevoyons des templates de deploiement, une checklist d'onboarding, un guide d'exploitation, des procedures de reponse incident et une documentation complete.

L'objectif final est de livrer une solution qui ne soit pas seulement fonctionnelle en demonstration, mais aussi credible dans un contexte professionnel d'infogerance SOC.

## Version courte si le temps est limite

Bonjour, je suis Yvan FOCSA, coordinateur projet et architecte securite.

Mon role est de cadrer le projet, definir l'architecture, organiser l'equipe, planifier les travaux et garantir l'alignement avec le cahier des charges.

Le client est un reseau d'audioprothesistes reparti sur une trentaine de sites. Pour le MVP, nous simulons trois sites representatifs afin de demontrer un SOC externalise centralise, base sur Wazuh, capable de collecter des logs multi-sources, generer des alertes, afficher des dashboards et proposer des playbooks de reponse.

La solution couvre les postes de travail, les equipements reseau, les applications metiers, les serveurs internes et la messagerie. Elle est pensee pour etre reproductible et scalable, avec des templates de deploiement et une documentation complete.

Cette organisation permet de produire un demonstrateur operationnel tout en preparant une extension future aux trente centres du reseau.
