# Script video - Youssef GUERNIOU - Partie Wazuh

## Objectif

Tenir environ 3 minutes dans la video groupe et montrer que la partie SIEM est concrete, installee et reliee aux preuves Wazuh.

## Script oral

Bonjour, je suis Youssef GUERNIOU, et dans ce projet mon role est ingenieur SIEM. Ma responsabilite est de mettre en place le socle Wazuh qui permet au SOC de centraliser les evenements, de les analyser et de produire des alertes exploitables.

Le choix technique retenu est Wazuh en version 4.14.5, deploye en single-node Docker pour le MVP. On retrouve les trois composants principaux : le Wazuh Manager pour recevoir et analyser les logs, le Wazuh Indexer pour stocker les evenements, et le Wazuh Dashboard pour l'interface web.

J'ai travaille sur plusieurs sources de logs. La premiere source est l'endpoint, avec un agent Wazuh qui permet de remonter des informations poste de travail. La deuxieme est le serveur Linux `serveur-01`, cree dans un conteneur, avec SSH, rsyslog et la surveillance de `/var/log/auth.log`. Ce serveur sert a rejouer une attaque brute force SSH et a verifier que Wazuh genere bien une alerte. La troisieme source est l'application metier Daylight, avec des logs CRM, rendez-vous et dossiers patients. On ajoute aussi les logs firewall/syslog pour couvrir la partie reseau.

Pour rendre le lab reproductible, j'ai fourni le script `setup-siem-lab.ps1`. Il verifie Docker, cree ou redemarre `serveur-01`, installe l'agent Wazuh, active la collecte SSH, simule des echecs d'authentification et configure un RBAC simple avec les profils `analyste` et `supervision` en lecture seule. L'administrateur garde les droits complets.

A l'ecran, on peut voir le vrai dashboard Wazuh. Les captures live montrent que la stack est lancee, que les alertes Daylight remontent dans Wazuh, et qu'on peut filtrer les evenements comme l'alerte firewall `100160`. Cela prouve que le MVP ne se limite pas a un rapport : il y a une chaine technique fonctionnelle entre les logs, les regles et l'interface de supervision.

La limite principale, c'est que ce lab reste un demonstrateur. En production, il faudrait connecter de vrais postes et serveurs sur les 30 centres, durcir le SIEM, definir une retention de logs, superviser la sante de Wazuh et automatiser le deploiement agent. Mais pour le MVP, la partie SIEM valide bien le besoin principal : centraliser les logs, detecter les comportements suspects et fournir une interface claire aux analystes.

## Supports a montrer pendant sa prise de parole

1. `scripts/setup-siem-lab.ps1`
2. `livrables/youssef/supports/Documentation_SIEM_Youssef_GUERNIOU.pdf`
3. `livrables/preuves/wazuh-live-captures/04-wazuh-overview-with-daylight-alerts-real.png`
4. `livrables/preuves/wazuh-live-captures/05-wazuh-discover-high-alerts-real.png`
5. `livrables/preuves/wazuh-live-captures/07-wazuh-firewall-portscan-100160-real.png`

## Phrase courte si le temps manque

Ma partie prouve le socle SIEM : Wazuh tourne en vrai, les logs sont injectes, les alertes remontent, les roles sont separes et le script permet de reproduire la partie serveur Linux et RBAC.

