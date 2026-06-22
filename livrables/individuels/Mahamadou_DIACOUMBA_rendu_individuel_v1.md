# Rendu individuel - Mahamadou DIACOUMBA - V1

## Informations generales

| Champ | Valeur |
|---|---|
| Nom | DIACOUMBA |
| Prenom | Mahamadou |
| Projet | Mise en place d'un SOC externalise pour un reseau d'audioprothesistes |
| Role | Analyste SOC / detection / playbooks / REX incidents |
| Equipe | Yvan FOCSA, Youssef GUERNIOU, Kilyan FELIX, Mahamadou DIACOUMBA |

## 1. Presentation de mon role

Dans ce projet, mon role est de construire la partie detection et reponse incident. Cela signifie definir des scenarios d'attaque realistes, adapter ou creer des regles de detection, tester les alertes dans le SIEM, rediger les playbooks et produire les retours d'experience des incidents simules.

Le SOC ne doit pas seulement collecter des logs. Il doit permettre a un analyste de comprendre rapidement ce qui se passe, d'evaluer la criticite et d'appliquer une procedure de reponse. Mon travail se concentre donc sur la transformation des logs en decisions operationnelles.

## 2. Contributions principales

| Contribution | Description |
|---|---|
| Scenarios d'attaque | Definition des cas d'usage SOC prioritaires. |
| Regles de detection | Participation a la creation et au test des regles Wazuh. |
| Alertes | Validation des alertes Daylight detectees. |
| Playbooks | Redaction des procedures brute force, phishing, acces patient, privileges et USB. |
| REX incidents | Analyse des incidents simules et des actions de reponse. |
| Demo SOC | Preparation de la sequence attaque -> detection -> investigation -> reponse. |

## 3. Travail realise

J'ai commence par identifier les menaces les plus pertinentes pour un reseau d'audioprothesistes : phishing, execution suspecte, brute force, acces anormal aux dossiers patients, elevation de privileges et usage USB. Ces scenarios couvrent a la fois les postes utilisateurs, les acces reseau, les applications metier, les donnees sensibles et les comptes privilegies.

J'ai ensuite travaille sur la logique de detection. Les regles Wazuh du sprint 01 permettent de declencher cinq alertes : execution PowerShell suspecte, brute force sur acces distant, acces anormal aux dossiers patients, modification d'un groupe privilegie et usage USB. Ces alertes sont documentees dans les preuves techniques du projet.

Enfin, j'ai formalise les playbooks de reponse. Chaque playbook precise les etapes de qualification, les controles a realiser, les actions possibles et les preuves a conserver. Cette partie est importante car elle montre la posture professionnelle du SOC.

## 4. Perspectives d'evolution de la solution

La premiere evolution serait d'ameliorer la qualite des regles. Pour un MVP, les detections sont volontairement simples et lisibles. En production, il faudrait ajouter plus de correlation, des seuils adaptes, des exceptions legitimes et une reduction des faux positifs.

La deuxieme evolution serait d'ajouter une solution de gestion d'incidents comme TheHive. Cela permettrait de transformer une alerte Wazuh en ticket, de suivre les actions, d'assigner un analyste et de conserver l'historique de traitement.

La troisieme evolution serait d'integrer une source de threat intelligence comme MISP. Les alertes pourraient etre enrichies avec des indicateurs connus : IP malveillantes, domaines suspects, hashes ou campagnes de phishing.

## 5. Limites techniques rencontrees

La principale limite est que les incidents sont simules. Cela permet de maitriser la demo, mais cela reste different d'une attaque reelle ou les evenements sont incomplets, bruyants et parfois ambigus.

Une autre limite concerne les faux positifs. Une regle trop large peut declencher beaucoup d'alertes non pertinentes, tandis qu'une regle trop stricte peut manquer une attaque. L'equilibre entre detection et bruit est un vrai sujet SOC.

Enfin, certains scenarios comme l'USB ou la messagerie sont difficiles a reproduire parfaitement sans vrai poste Windows ou serveur mail. Il faut donc expliquer clairement ce qui est simule et ce qui serait fait en production.

## 6. Analyse critique personnelle

Je pense que la detection doit toujours etre reliee a une action. Une alerte qui n'a pas de playbook ou de contexte est difficilement exploitable. C'est pour cela que les scenarios du projet sont construits avec une logique complete : evenement, alerte, qualification, reponse et REX.

Avec du recul, j'aurais pu commencer encore plus tot par rediger les hypotheses de compromission. Cela aurait facilite l'ecriture des regles et des playbooks, car chaque detection aurait ete reliee a un risque precis.

Je retiens aussi que la preuve est essentielle. Pour une soutenance, il faut pouvoir montrer une alerte, expliquer pourquoi elle est importante et presenter la procedure associee.

## 7. Defis rencontres

- choisir des scenarios realistes et demonstrables ;
- produire des alertes visibles dans Wazuh ;
- eviter des regles trop generiques ;
- relier chaque alerte a un risque metier ;
- rediger des playbooks simples mais professionnels ;
- produire un REX clair pour chaque incident.

## 8. Forces personnelles mobilisees

| Force | Application |
|---|---|
| Esprit SOC | Raisonnement attaque, detection, investigation et reponse. |
| Analyse | Qualification des alertes et interpretation des logs. |
| Methode | Structuration des playbooks. |
| Sens du risque | Priorisation des incidents critiques. |
| Communication | Explication des scenarios dans la video et le rapport. |

## 9. Points d'amelioration personnels

Je dois approfondir la correlation d'evenements. Les alertes individuelles sont utiles, mais un SOC mature doit pouvoir relier plusieurs signaux : par exemple phishing, execution PowerShell, connexion sortante et modification de compte.

Je dois aussi progresser sur l'ecriture de regles plus robustes, notamment avec des decoders plus propres, des niveaux de criticite coherents et des exceptions pour limiter les faux positifs.

Enfin, je dois travailler la presentation des incidents. Un bon analyste SOC doit expliquer rapidement ce qui s'est passe, pourquoi c'est important, quelles actions ont ete prises et quel risque reste ouvert.

## 10. Competences developpees

- definition de scenarios d'attaque ;
- creation et test de regles de detection ;
- analyse d'alertes SIEM ;
- redaction de playbooks SOC ;
- production de REX incidents ;
- comprehension du lien entre logs et risques metier ;
- preparation d'une demo de detection.

## 11. Axes d'amelioration pour de futurs projets

Pour un futur projet, je construirais une matrice detection des le debut avec les colonnes suivantes : scenario, source de logs, condition de detection, regle, criticite, faux positifs possibles, playbook et preuve attendue.

Je mettrais aussi en place des tests de detection reproductibles. Chaque regle devrait avoir un log de test normal et un log de test malveillant.

Enfin, j'ajouterais une phase d'amelioration continue apres chaque incident simule : ce que la regle a bien detecte, ce qu'elle a manque, ce qu'il faut ajuster.

## 12. Conclusion personnelle

Ma contribution porte principalement sur la detection et la reponse incident. J'ai travaille sur les scenarios, les alertes, les playbooks et les REX. Cette partie permet de montrer que le SOC ne se contente pas de stocker des logs : il produit des informations exploitables et guide la reaction.

La suite de mon travail consistera a renforcer les regles, produire les captures Wazuh, finaliser les REX et preparer la demonstration de l'analyse SOC pour la video MVP.

