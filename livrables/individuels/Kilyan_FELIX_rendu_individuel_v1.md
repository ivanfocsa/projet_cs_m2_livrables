# Rendu individuel - Kilyan FELIX - V1

## Informations generales

| Champ | Valeur |
|---|---|
| Nom | FELIX |
| Prenom | Kilyan |
| Projet | Mise en place d'un SOC externalise pour un reseau d'audioprothesistes |
| Role | Chef de projet / referent client / pilotage des livrables |
| Equipe | Yvan FOCSA, Youssef GUERNIOU, Kilyan FELIX, Mahamadou DIACOUMBA |

## 1. Presentation de mon role

Dans ce projet, mon role est centre sur le pilotage, le cadrage fonctionnel et la coherence globale des livrables. Le sujet demande de concevoir une solution technique, mais aussi de demontrer une posture professionnelle de prestataire SOC. Mon travail consiste donc a relier le besoin client, les choix techniques, les preuves produites et la forme finale du rendu.

Je suis responsable de la transformation du cahier des charges en objectifs concrets : perimetre MVP, exigences, organisation de l'equipe, planning, suivi des preuves, gestion des couts et structuration du rapport final. Ce role permet d'eviter que le projet devienne uniquement une installation technique sans lien clair avec les attentes du client.

## 2. Contributions principales

| Contribution | Description |
|---|---|
| Cadrage du besoin | Reformulation du contexte client, des enjeux et des objectifs du SOC externalise. |
| Organisation projet | Definition des roles, repartition des responsabilites et suivi d'avancement. |
| Backlog | Construction d'une liste de taches priorisees pour avancer par etapes. |
| Gestion des couts | Identification des couts MVP et des couts a anticiper en production. |
| Matrice exigences-preuves | Mise en relation entre cahier des charges, implementation et preuves. |
| Rapport final | Harmonisation des sections et verification de la coherence generale. |
| Video MVP | Preparation du deroule, de l'introduction, de la conclusion et du timing. |

## 3. Travail realise

J'ai commence par analyser le cahier des charges afin d'identifier les livrables attendus : analyse initiale, document d'architecture technique, demonstrateur operationnel, dashboards, alertes, playbooks, rapport technique complet, guide de deploiement et video de demonstration.

J'ai ensuite participe a la definition d'un perimetre MVP realiste. Le client cible environ 30 points de vente, mais il n'etait pas pertinent de vouloir tous les simuler dans le demonstrateur. Le choix a donc ete de valider une chaine SOC complete sur un environnement restreint, puis de decrire clairement la methode d'industrialisation vers 30 sites.

J'ai aussi travaille sur la structure documentaire. L'objectif etait que chaque element technique ait une preuve et que chaque preuve soit reutilisable dans le rapport final ou la video. Cela permet de montrer au jury que le projet n'est pas seulement theorique : il produit des resultats observables, des alertes, des regles, des playbooks et une organisation exploitable.

## 4. Perspectives d'evolution de la solution

La premiere perspective d'evolution est de renforcer le reporting client. Dans un modele d'infogerance SOC, le client doit comprendre les incidents sans entrer dans toute la complexite technique. Il faudrait donc produire des rapports mensuels avec un resume executif, les alertes critiques, les incidents confirmes, les faux positifs, les actions realisees et les recommandations.

La deuxieme evolution concerne la maturite projet. Pour passer du MVP a une offre industrialisable, il faudrait ajouter des indicateurs de pilotage : taux de couverture des sites, nombre d'agents actifs, sources silencieuses, delai moyen de qualification, nombre d'incidents par criticite et taux de faux positifs.

La troisieme evolution est l'amelioration de la gouvernance. Une fois la solution deployee sur plusieurs sites, il serait necessaire de definir des SLA, des responsabilites client/prestataire, une procedure d'escalade et un calendrier de revue securite.

## 5. Limites techniques et organisationnelles rencontrees

La principale limite est la difference entre un demonstrateur et une production reelle. Le MVP utilise des logs simules et un environnement de lab afin de prouver la chaine SOC. Cette approche est pertinente pour une soutenance, mais elle doit etre clairement expliquee pour ne pas donner l'impression que toute l'infrastructure finale est deja deployee.

Une autre limite concerne le temps de projet. Le sujet est large : SIEM, agents, firewall, applications metier, messagerie, detection, dashboards, playbooks, reporting et industrialisation. Il faut donc arbitrer en permanence entre ce qui est indispensable et ce qui peut rester en perspective.

Enfin, la coordination est un enjeu important. Chaque membre produit une partie differente ; si les preuves ne sont pas centralisees, le rapport final peut devenir incoherent. C'est pour cela que la matrice exigences-preuves est essentielle.

## 6. Analyse critique personnelle

Je pense que la valeur de ma contribution se situe dans la structuration. Un bon projet cyber ne se limite pas a faire fonctionner un outil : il doit expliquer pourquoi l'outil repond au besoin, comment il est exploite, quelles limites il presente et comment il peut evoluer.

Avec du recul, j'aurais pu formaliser encore plus tot un tableau unique de suivi des preuves. Cela aurait permis d'associer immediatement chaque capture, log ou fichier de configuration a une exigence precise du cahier des charges.

Je retiens aussi que la communication interne est centrale. Si l'equipe technique avance mais que le rapport ne suit pas, une partie de la valeur produite peut etre perdue. Il faut donc documenter au fur et a mesure.

## 7. Defis rencontres

- transformer un cahier des charges general en plan d'action concret ;
- garder un perimetre realiste malgre l'etendue du sujet SOC ;
- synchroniser les contributions techniques et documentaires ;
- construire un discours client comprehensible ;
- anticiper les attentes de la video MVP ;
- garantir que le rapport final soit conforme au cadre pedagogique.

## 8. Forces personnelles mobilisees

| Force | Application |
|---|---|
| Organisation | Structuration des taches, roles, planning et livrables. |
| Communication | Reformulation du besoin client et preparation du discours video. |
| Vision globale | Mise en coherence des choix techniques et des exigences. |
| Rigueur documentaire | Suivi des preuves, plan du rapport et controle des livrables. |
| Prise de recul | Identification des limites et perspectives. |

## 9. Points d'amelioration personnels

Je dois progresser sur la production de preuves en continu. Dans un futur projet, je mettrais en place des le debut un dossier de preuves avec une convention de nommage stricte, par exemple `preuve-01-dashboard`, `preuve-02-alerte-bruteforce`, `preuve-03-regle-wazuh`.

Je dois aussi approfondir certains aspects techniques du SOC afin de mieux challenger les choix techniques de l'equipe. Meme si mon role est plus oriente pilotage, comprendre finement Wazuh, les regles et les logs permet de mieux piloter le rendu final.

## 10. Competences developpees

- cadrage d'un besoin cyber ;
- organisation d'un projet technique ;
- gestion d'un backlog ;
- suivi de livrables ;
- formalisation d'une matrice exigences-preuves ;
- vulgarisation d'une solution technique ;
- preparation d'une soutenance video ;
- analyse critique d'un MVP.

## 11. Axes d'amelioration pour de futurs projets

Pour un futur projet, je mettrais en place des le depart un tableau de pilotage partage avec les colonnes suivantes : exigence, responsable, implementation, preuve, statut, lien vers capture, lien vers section du rapport. Cela permettrait de suivre la conformite en continu.

Je prevoirais aussi des jalons de validation plus frequents, notamment une revue technique toutes les deux semaines et une revue documentaire apres chaque scenario de detection.

Enfin, je travaillerais plus tot la mise en forme finale du rapport pour eviter d'avoir a harmoniser trop de contenus en fin de projet.

## 12. Conclusion personnelle

Ma contribution porte principalement sur le pilotage, la coherence et la transformation du cahier des charges en livrables concrets. Le projet m'a permis de comprendre qu'une solution SOC doit etre aussi bien documentee qu'elle est techniquement fonctionnelle.

La suite logique consisterait a maintenir la matrice de conformite, verifier que les captures restent alignees avec le rapport final, consolider la partie couts et preparer une introduction claire pour la video MVP.
