# Script video final - Yvan FOCSA

## Objectif

Ce script est la version prete a lire pour la video. Il couvre mon role, l'analyse du besoin, l'architecture, les flux, l'industrialisation, les couts et les limites.

## Carton a afficher

Yvan FOCSA  
Architecte securite / infrastructure et industrialisation

## Timing conseille

| Temps | Action ecran | Message |
|---:|---|---|
| 0:00 - 0:20 | Afficher nom + role | Presentation personnelle. |
| 0:20 - 0:55 | Schema architecture | Besoin client et 30 centres. |
| 0:55 - 1:35 | Schema architecture | MVP 3 sites et flux de collecte. |
| 1:35 - 2:15 | Dashboard global | Valeur SOC : alertes et supervision. |
| 2:15 - 3:00 | Checklist onboarding | Industrialisation vers 30 sites. |
| 3:00 - 3:30 | Inventaire site ou matrice | Couts, limites et conclusion. |

## Texte a lire

Bonjour, je suis Yvan FOCSA. Sur ce projet, mon role est d'intervenir sur l'architecture securite, le cadrage du perimetre MVP, les flux de collecte entre les sites clients et le SOC central, ainsi que l'industrialisation de la solution.

Le client represente un reseau d'audioprothesistes compose d'environ 30 points de vente. Chaque centre utilise des postes de travail, des applications metier, une messagerie, des serveurs internes et des equipements reseau. Le probleme est que les evenements de securite sont disperses, alors que le client a besoin d'une supervision centralisee et exploitable.

Pour le MVP, nous ne reproduisons pas directement les 30 sites. Nous utilisons trois sites simules qui representent les principales briques du systeme d'information : postes, firewall, applications metier, serveurs internes et messagerie. Ce choix permet de prouver la chaine SOC tout en gardant une demonstration stable.

L'architecture repose sur un SOC externalise centralise autour de Wazuh. Les postes et serveurs remontent leurs evenements via agents Wazuh, les firewalls pfSense CE via syslog, et les applications metier via des logs applicatifs. Dans le MVP, pfSense est represente par `FW-S01` et `FW-S02` avec des logs syslog simules. Ces evenements sont centralises, analyses par des regles de detection, puis affiches dans des dashboards pour les profils supervision, analyste et administration.

La valeur de cette architecture est qu'elle relie les besoins du cahier des charges a une chaine technique concrete : collecte, detection, alerte, investigation, playbook et reporting. Elle permet aussi d'avoir une interface web lisible pour suivre les alertes et prioriser les incidents.

Ma partie porte aussi sur l'industrialisation. Pour passer de trois sites simules a trente centres, il faut une methode repetable : convention de nommage, inventaire des sites, checklist d'onboarding, templates de configuration, dashboards filtrables par site et procedure de validation de la collecte.

Concernant les couts, le MVP limite les couts logiciels grace au choix d'un SIEM open-source. En production, les couts principaux seraient plutot l'infrastructure, le stockage des logs, l'exploitation SOC, la maintenance et le deploiement sur chaque site. C'est pour cela que la standardisation est importante : elle reduit le temps d'integration et donc le cout par centre.

Les limites sont assumees. Certains logs sont simules, le MVP ne correspond pas encore a un deploiement reel sur 30 sites, et une production demanderait de renforcer la haute disponibilite, la retention, le RBAC et la supervision de sante des agents. Mais le demonstrateur prouve l'essentiel : un modele SOC externalise clair, documente, reproductible et industrialisable.

## A ne pas dire

- Ne pas dire que les 30 sites sont deja deployes.
- Ne pas dire que Docker est la production finale.
- Ne pas rentrer dans le detail des regles Wazuh ligne par ligne.
- Ne pas promettre un SOC 24/7 complet.
