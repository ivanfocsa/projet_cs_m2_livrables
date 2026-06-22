# Script oral Yvan - 3 a 5 minutes

## A afficher pendant ton passage

Yvan FOCSA - Architecte securite / infrastructure et industrialisation

## Script conseille

Bonjour, je suis Yvan FOCSA. Sur ce projet, mon role porte principalement sur l'architecture securite, le cadrage du perimetre MVP, les flux entre les sites clients et le SOC central, ainsi que l'industrialisation de la solution.

Le client represente un reseau d'audioprothesistes avec environ 30 points de vente. Chaque centre utilise des postes de travail, des applications metier, une messagerie, des serveurs internes et des equipements reseau. Le besoin principal est de centraliser les evenements de securite et de permettre a un SOC externalise de detecter, qualifier et traiter les incidents.

Pour le MVP, nous avons choisi de ne pas reproduire directement les 30 sites. Nous avons retenu trois sites simules, parce que cela permet de prouver la chaine SOC sans complexifier inutilement l'environnement. L'objectif est de demontrer le modele : collecte, detection, alerte, investigation, playbook et reporting.

L'architecture repose sur un SOC centralise base sur Wazuh. Les sources de logs sont multiples : agents pour les postes et serveurs, syslog pour les firewalls, logs applicatifs pour les dossiers patients, logs annuaire pour les droits et logs messagerie pour le phishing. Ces evenements sont centralises dans le SIEM, puis transformes en alertes et dashboards.

Ce choix repond au cahier des charges parce que Wazuh est open-source, dispose d'une interface web, permet les regles personnalisees et peut etre integre dans un modele d'infogerance. Le demonstrateur reste volontairement limite, mais il montre une architecture reproductible et scalable.

Ma contribution a aussi ete de preparer la logique d'industrialisation. Pour passer de trois sites simules a trente sites, il faut une convention de nommage, une checklist d'onboarding, des templates de configuration, des dashboards filtrables par site et une procedure de validation de la collecte. Le but est qu'un nouveau centre puisse etre integre de maniere standardisee.

Les limites sont assumees : certains logs sont simules, le MVP n'est pas un SOC 24/7 complet, et l'architecture de production demanderait plus de travail sur le dimensionnement, la retention, la haute disponibilite et la supervision des agents. Mais le projet prouve l'essentiel : une chaine SOC complete, documentee et defendable.

Pour conclure, ma partie montre que le projet n'est pas seulement une installation Wazuh. C'est une proposition d'architecture SOC externalisee, pensee pour etre lisible, reproductible et industrialisable dans un contexte professionnel.

## Version tres courte si tu dois aller vite

Mon role est de cadrer l'architecture et l'industrialisation du SOC externalise. Le MVP simule trois sites pour representer un reseau cible d'environ 30 centres. L'architecture centralise les logs dans Wazuh via agents, syslog et logs applicatifs. Le projet prouve la chaine collecte, detection, alerte, investigation, playbook et documentation. La limite principale est que le demonstrateur reste un environnement de lab, mais il est pense pour etre etendu grace aux templates, conventions de nommage, checklist d'onboarding et dashboards filtrables par site.

