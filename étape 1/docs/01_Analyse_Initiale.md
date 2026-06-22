# 01 - Analyse initiale

## 1. Contexte

Le client est un reseau de centres d'audioprothesistes repartis sur une trentaine de points de vente en France. Les centres manipulent des donnees sensibles liees aux clients et aux dossiers patients, utilisent des postes de travail metier, des applications de rendez-vous, une messagerie professionnelle, des serveurs internes et des equipements reseau.

La direction souhaite renforcer sa posture de securite face a l'augmentation des cybermenaces, tout en tenant compte d'un manque de ressources internes pour exploiter un SOC complet. La solution attendue est donc un SOC externalise, pense pour etre exploite par un prestataire et deployable progressivement sur plusieurs centres.

## 2. Objectif general

L'objectif du projet est de concevoir une plateforme de demonstration fonctionnelle, securisee, documentee et industrialisable permettant de centraliser les evenements de securite, detecter des comportements suspects, produire des alertes et accompagner la reponse incident.

## 3. Probleme a resoudre

Le reseau client dispose de plusieurs sites, de plusieurs sources de logs et d'une surface d'attaque repartie. Sans centralisation, il est difficile de :

- detecter rapidement une attaque ;
- correler des evenements entre plusieurs sites ;
- suivre les activites suspectes sur les postes et serveurs ;
- controler les acces aux ressources sensibles ;
- produire un reporting simple pour la direction ;
- industrialiser l'exploitation securite.

La question principale est donc :

Comment mettre en place un SOC externalise open-source, capable de superviser plusieurs sites d'audioprothesistes, tout en restant clair, reproductible et exploitable dans un modele d'infogerance ?

## 4. Perimetre MVP

Le cahier des charges mentionne environ 30 points de vente. Pour le demonstrateur, nous retenons un MVP base sur 3 sites simules.

| Element | Choix MVP | Justification |
|---|---|---|
| Nombre de sites | 3 sites simules | Representer le fonctionnement multi-site sans complexite excessive. |
| Nombre de sources | Au moins 5 familles de logs | Couvrir les briques demandees dans le cahier des charges. |
| SIEM | Wazuh | Solution open-source adaptee au projet. |
| Interface | Web dashboard | Conforme a la demande d'interface web-based. |
| Detection | Regles personnalisees | Demontrer une vraie valeur SOC. |
| Reponse | Playbooks semi-automatises | Conforme au cahier des charges. |

## 5. Briques SI a couvrir

| Brique SI | Besoins de monitoring | Couverture prevue |
|---|---|---|
| Postes de travail | Authentifications locales, executions suspectes, usage USB | Agent Wazuh, logs endpoint, scenarios de test. |
| Routeurs / firewall | Flux reseau, acces non autorises, changements de configuration | Syslog firewall ou logs reseau simules. |
| Applications metiers | Logs applicatifs, erreurs, acces anormaux | Logs CRM/RDV/dossiers patients simules. |
| Serveurs internes | Acces partages, elevation de privileges | Agent serveur, logs systeme et fichiers. |
| Messagerie professionnelle | Phishing, spam, pieces jointes malveillantes | Logs mail simules et playbook phishing. |

## 6. Hypotheses de menace

| Menace | Impact potentiel | Detection attendue |
|---|---|---|
| Brute force compte utilisateur | Compromission de compte | Alerte sur echecs d'authentification repetes. |
| Execution suspecte | Infection malware ou script non autorise | Alerte endpoint sur processus ou commande. |
| Usage USB non autorise | Fuite de donnees ou introduction malware | Evenement USB et alerte de non-conformite. |
| Acces anormal dossier patient | Atteinte confidentialite | Alerte applicative ou fichier. |
| Phishing | Compromission initiale | Alerte messagerie et procedure SOC. |
| Scan reseau | Reconnaissance avant attaque | Alerte firewall / IDS. |

## 7. Contraintes

| Contrainte | Reponse projet |
|---|---|
| Ressources limitees | Utilisation d'outils open-source. |
| Environnement de demo | Simulation des sites et des logs. |
| Donnees sensibles | Donnees fictives uniquement. |
| Besoin d'industrialisation | Templates, guides et checklist. |
| Besoin de lisibilite | Dashboards segmentes par role. |
| Soutenance / video | Scenarios simples, visibles et repetables. |

## 8. Objectifs de securite

| Objectif | Application |
|---|---|
| Confidentialite | Ne pas utiliser de donnees reelles, proteger les acces au dashboard. |
| Integrite | Journaliser les modifications et conserver les preuves. |
| Disponibilite | Prevoir supervision et procedure de redemarrage. |
| Tracabilite | Conserver les logs, alertes et actions SOC. |
| Reproductibilite | Documenter chaque etape d'installation et test. |

## 9. Resultat attendu

A la fin du projet, le demonstrateur doit permettre de montrer :

- un SIEM central fonctionnel ;
- plusieurs sources de logs connectees ;
- des alertes visibles dans l'interface ;
- des dashboards exploitables ;
- des playbooks de reponse incident ;
- un guide de deploiement ;
- un guide d'utilisation ;
- un rapport technique complet ;
- une video claire avec demonstration du MVP.
