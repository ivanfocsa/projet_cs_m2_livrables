# 08 - Script video MVP

## Objectif

La video doit durer 15 a 20 minutes et montrer une posture professionnelle. Chaque membre doit parler, avec son nom affiche a l'ecran.

Structure recommandee :

1. presentation de l'entreprise et de l'equipe ;
2. analyse de la problematique ;
3. organisation et methodologie ;
4. architecture de la solution ;
5. demonstration technique ;
6. resultats, limites et perspectives.

## Deroule propose

| Partie | Duree | Intervenant | Contenu |
|---|---|---|---|
| Introduction | 2 min | Yvan | Contexte client, besoin SOC, objectif du MVP. |
| Architecture | 3 min | Yvan / Youssef | Schema global, sites simules, flux de logs. |
| Installation SIEM | 3 min | Youssef | Wazuh, agents, collecte, dashboard. |
| Detection | 4 min | Kilyan | Regles, alertes, dashboards, cas d'usage. |
| Reponse incident | 3 min | Mahamadou | Playbooks, procedures, remediation. |
| Conclusion | 2 min | Yvan | Industrialisation, extension 30 sites, limites, prochaines etapes. |

## Script Yvan - Introduction

Bonjour, je suis Yvan FOCSA, coordinateur projet et architecte securite.

Notre client est un reseau de centres d'audioprothesistes reparti sur une trentaine de points de vente en France. Face a l'augmentation des menaces et au manque de ressources internes, l'objectif du projet est de concevoir un SOC externalise capable de centraliser les evenements de securite, detecter les comportements suspects et fournir un reporting exploitable.

Pour le MVP, nous avons choisi de simuler trois sites representatifs. Cette approche nous permet de demontrer la valeur de la solution tout en gardant un environnement controlable et reproductible.

## Script Youssef - Socle SIEM

Bonjour, je suis Youssef GUERNIOU, ingenieur SIEM sur le projet.

Ma partie consiste a deployer le socle technique du SOC. Nous utilisons Wazuh comme SIEM open-source centralise. Il permet de connecter des agents sur les postes et serveurs, de recevoir des logs reseau via syslog et de visualiser les alertes dans une interface web.

Je vais maintenant montrer le dashboard, l'etat des agents et un exemple de log collecte depuis un site simule.

## Script Kilyan - Detection

Bonjour, je suis Kilyan FELIX, analyste SOC sur le projet.

Ma partie concerne la detection et l'exploitation des alertes. Nous avons defini plusieurs cas d'usage adaptes au contexte du client : brute force, execution suspecte, usage USB, acces anormal a un dossier patient, phishing et scan reseau.

Je vais montrer comment une alerte apparait dans le SIEM, comment on retrouve les informations importantes et comment les dashboards permettent de prioriser l'analyse.

## Script Mahamadou - Reponse incident

Bonjour, je suis Mahamadou DIACOUMBA, responsable Blue Team et reponse incident.

Mon role est de preparer les scenarios de test, les playbooks et les procedures de reaction. Lorsqu'une alerte est confirmee, l'analyste doit pouvoir suivre une procedure claire : qualifier l'incident, identifier l'impact, proposer une action de confinement et documenter la resolution.

Je vais presenter un exemple de playbook applique a une alerte de phishing ou de brute force.

## Script Yvan - Conclusion

Pour conclure, notre demonstrateur montre qu'il est possible de mettre en place un SOC externalise open-source, centralise et industrialisable.

Le modele a ete valide sur trois sites simules, mais il est pense pour etre etendu aux trente points de vente du client grace a des templates de deploiement, une checklist d'onboarding, des dashboards par site et des playbooks standardises.

Les prochaines evolutions possibles seraient l'ajout d'une brique IDS plus avancee, l'automatisation de certaines reponses et la mise en place d'un reporting mensuel client.

## Captures a integrer

| Capture | Moment de la video |
|---|---|
| Schema architecture | Introduction architecture |
| Dashboard Wazuh | Socle SIEM |
| Agent actif | Socle SIEM |
| Alerte brute force | Detection |
| Dashboard par criticite | Detection |
| Playbook | Reponse incident |
| Matrice conformite | Conclusion |

