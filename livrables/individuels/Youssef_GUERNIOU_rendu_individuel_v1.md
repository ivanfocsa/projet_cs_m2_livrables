# Rendu individuel - Youssef GUERNIOU - V1

## Informations generales

| Champ | Valeur |
|---|---|
| Nom | GUERNIOU |
| Prenom | Youssef |
| Projet | Mise en place d'un SOC externalise pour un reseau d'audioprothesistes |
| Role | Ingenieur SIEM / integration Wazuh / collecte et dashboards |
| Equipe | Yvan FOCSA, Youssef GUERNIOU, Kilyan FELIX, Mahamadou DIACOUMBA |

## 1. Presentation de mon role

Dans ce projet, mon role est de mettre en place le socle technique du SOC. Cela comprend l'installation et la configuration de Wazuh, la verification des services, l'integration des sources de logs, la preparation des regles locales et la mise a disposition d'une interface web exploitable par les analystes.

Le cahier des charges demande un SIEM open-source centralise, une collecte multi-source, des dashboards lisibles et une interface web. Mon travail est donc directement lie a la faisabilite technique du MVP. Sans SIEM fonctionnel, les scenarios de detection, les playbooks et la video ne peuvent pas etre correctement demontres.

## 2. Contributions principales

| Contribution | Description |
|---|---|
| Installation Wazuh | Mise en place du manager, de l'indexer et du dashboard. |
| Verification services | Controle de l'etat des conteneurs et des services internes Wazuh. |
| Integration des logs | Preparation de l'ingestion des logs endpoint, firewall, applicatifs et AD. |
| Regles locales | Support a l'ajout des regles personnalisees dans Wazuh. |
| Dashboards | Preparation des vues techniques pour suivre les alertes et la collecte. |
| Automatisation SIEM | Script `setup-siem-lab.ps1` pour deployer `serveur-01`, tester SSH et configurer le RBAC. |
| Guide technique | Documentation des prerequis, commandes et preuves. |
| Support demo | Preparation de l'interface pour la video MVP. |
| Documentation personnelle | Integration de `Documentation_SIEM_Youssef_GUERNIOU.pdf` et du dossier `livrables/youssef/`. |

## 3. Travail realise

La premiere etape a ete de deployer Wazuh en mode single-node Docker. Ce choix permet de disposer rapidement d'un environnement reproductible contenant les composants principaux : Wazuh Manager, Wazuh Indexer et Wazuh Dashboard. Il facilite aussi les tests, car l'environnement peut etre relance ou redeploye plus facilement qu'une installation manuelle complexe.

J'ai ensuite verifie l'etat des services. Les preuves du sprint 01 montrent que les conteneurs Wazuh Dashboard, Wazuh Indexer et Wazuh Manager sont actifs. Les services internes essentiels comme `wazuh-logcollector`, `wazuh-remoted`, `wazuh-analysisd`, `wazuh-execd`, `wazuh-db`, `wazuh-authd` et `wazuh-apid` sont egalement presents.

J'ai aussi travaille sur l'integration des logs Daylight. Les sources utilisees couvrent plusieurs briques du cahier des charges : endpoint, firewall/syslog, application metier et Active Directory simule. Cette integration permet de tester les regles de detection et de produire des alertes visibles dans le SIEM.

En complement, j'ai fourni un script PowerShell `scripts/setup-siem-lab.ps1` pour rendre le lab plus reproductible. Ce script cree ou redemarre le conteneur Linux `serveur-01`, installe l'agent Wazuh 4.14.5-1, active SSH et rsyslog, ajoute la collecte de `/var/log/auth.log`, simule une brute force SSH et configure deux comptes de consultation `analyste` et `supervision` via le role lecture seule `soc_readonly`.

La documentation SIEM fournie dans `livrables/youssef/supports/Documentation_SIEM_Youssef_GUERNIOU.pdf` consolide les preuves de mon perimetre : Wazuh 4.14.5, sources `poste-01`, `serveur-01` et Daylight, dashboards technique/executive, RBAC et procedure de reprise du lab.

Les captures Wazuh live disponibles dans `livrables/preuves/wazuh-live-captures/` completent cette documentation. Elles montrent une interface Wazuh reelle, des alertes Daylight indexees, une vue Threat Hunting et une alerte firewall/syslog `100160`.

## 4. Perspectives d'evolution de la solution

La premiere evolution technique serait de connecter de vrais agents Wazuh sur des VMs Windows et Linux. Les logs rejoues sont utiles pour le MVP, mais des agents reels permettraient de montrer des evenements systeme plus proches d'une production.

La deuxieme evolution concerne le RBAC. Une premiere base de demonstration existe deja avec les profils `analyste` et `supervision` en lecture seule. Pour une production, il faudrait aller plus loin : comptes nominatifs, MFA, separation des tenants, journalisation des actions et revue periodique des droits.

La troisieme evolution serait d'ameliorer les dashboards. Il faudrait creer des vues par criticite, par site, par source, par scenario et par machine afin de faciliter le travail de supervision et de qualification.

## 5. Limites techniques rencontrees

La premiere limite est la complexite de Wazuh. La plateforme est puissante, mais elle demande de bien comprendre la difference entre collecte, decoders, rules, indexation et dashboards. Une erreur dans un champ ou une regle peut empecher l'alerte d'apparaitre correctement.

La deuxieme limite vient de l'environnement Docker. Il est tres pratique pour un demonstrateur, mais il ne represente pas completement un parc client compose de postes Windows, serveurs internes, firewalls et applications de production.

La troisieme limite concerne les agents reels. Les captures Wazuh live existent maintenant pour la stack centrale et les alertes Daylight, mais il faudrait encore relancer le lab complet `poste-01` / `serveur-01` pour produire des captures supplementaires sur les agents actifs et l'alerte SSH `5712`.

## 6. Analyse critique personnelle

Je pense que la partie SIEM est la colonne vertebrale du projet. Elle permet de passer d'une idee de SOC a une demonstration concrete. L'enjeu est de montrer que des logs issus de sources differentes peuvent etre centralises, analyses et transformes en alertes exploitables.

Avec du recul, il est important de documenter chaque commande et chaque fichier modifie. Dans un outil comme Wazuh, les configurations sont nombreuses ; sans documentation, il devient difficile de reproduire l'installation ou d'expliquer les choix.

Je retiens aussi que la stabilite de la demo est essentielle. Pour une video ou une soutenance, il vaut mieux avoir des logs rejouables et des alertes deja validees que de dependere uniquement d'une attaque en direct.

## 7. Defis rencontres

- installer une stack Wazuh complete ;
- comprendre les roles du manager, de l'indexer et du dashboard ;
- automatiser une partie du lab avec PowerShell et Docker ;
- integrer plusieurs familles de logs ;
- faire correspondre les champs des logs aux regles ;
- obtenir des alertes exploitables ;
- preparer des captures claires pour le rapport.

## 8. Forces personnelles mobilisees

| Force | Application |
|---|---|
| Rigueur technique | Verification des services et des composants. |
| Autonomie | Installation et prise en main du SIEM. |
| Methode | Avancement par tests et preuves. |
| Sens du detail | Controle des logs, regles et alertes. |
| Esprit d'analyse | Diagnostic des problemes d'ingestion ou de detection. |

## 9. Points d'amelioration personnels

Je dois approfondir la creation de decoders et de regles Wazuh. Les regles locales fonctionnent pour le MVP, mais une solution plus robuste demanderait de normaliser proprement les logs et d'eviter les detections trop dependantes de simples chaines de caracteres.

Je dois aussi progresser sur les dashboards. Une bonne interface SOC ne doit pas seulement afficher des alertes ; elle doit permettre a l'analyste de prioriser, filtrer, comprendre et agir rapidement.

## 10. Competences developpees

- installation d'une stack SIEM ;
- comprehension de Wazuh Manager, Indexer et Dashboard ;
- integration de logs multi-source ;
- verification de services Docker ;
- configuration d'un agent Linux `serveur-01` ;
- mise en place d'un RBAC de demonstration ;
- lecture et test de regles de detection ;
- documentation technique ;
- preparation d'une demonstration SIEM.

## 11. Axes d'amelioration pour de futurs projets

Pour un futur projet, je completerais l'automatisation existante avec un demarrage complet de la stack Wazuh, un controle automatique des agents et une verification automatique des alertes attendues. Cela reduirait les risques d'erreur et faciliterait la reproduction par l'equipe.

Je preparerais aussi un jeu de donnees de test pour chaque source de logs, avec un evenement normal et un evenement suspect. Cela permettrait de valider rapidement chaque regle.

Enfin, je mettrais en place une checklist de controle apres chaque modification : services actifs, logs recus, regle chargee, alerte detectee, capture realisee.

## 12. Conclusion personnelle

Ma contribution est centree sur le socle SIEM. J'ai travaille sur la mise en place de Wazuh, l'integration des logs et la validation des alertes. Cette partie est essentielle car elle rend le projet demonstrable.

La suite logique consisterait a completer les captures agents `poste-01` et `serveur-01`, renforcer les dashboards par role, documenter l'installation et preparer une presentation claire de la plateforme pour la video MVP.
