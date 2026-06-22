# 04 - Gestion des couts

## 1. Strategie

Le projet privilegie une approche open-source first afin de proposer une solution credible pour un reseau de centres d'audioprothesistes, sans dependance immediate a des licences couteuses.

Le demonstrateur vise a prouver la valeur technique et operationnelle du SOC. En production, les couts principaux ne seront pas les licences du SIEM mais l'infrastructure, le stockage, l'exploitation humaine et le deploiement sur les sites.

## 2. Couts du MVP

| Poste | Hypothese | Cout estime |
|---|---|---|
| SIEM | Wazuh open-source | 0 EUR licence |
| Dashboard / indexation | OpenSearch inclus dans l'architecture Wazuh | 0 EUR licence |
| Agents endpoints | Agents Wazuh | 0 EUR licence |
| VMs de demonstration | Machines locales ou environnement de lab | 0 EUR si materiel disponible |
| Generation logs | Scripts internes | 0 EUR |
| Documentation | Markdown / PDF | 0 EUR |
| Temps equipe | 4 membres projet | Cout pedagogique non facture |

## 3. Couts a prevoir en production

| Poste | Description | Facteurs de variation |
|---|---|---|
| Hebergement SOC | Serveur dedie, cloud ou infrastructure prestataire | Nombre de sites, haute disponibilite, politique sauvegarde. |
| Stockage logs | Conservation et indexation des evenements | Volume de logs, duree de retention, compression. |
| Exploitation SOC | Analystes, supervision, astreinte | Horaires de service, SLA, criticite client. |
| Deploiement sites | Installation agents, configuration syslog, validation | Nombre de postes et equipements par centre. |
| Maintenance | Mises a jour, durcissement, surveillance du SIEM | Frequence de patch, complexite integrations. |
| Reporting | Rapports mensuels, exports, comites | Niveau de detail et frequence. |

## 4. Hypothese de dimensionnement

| Element | MVP | Production cible |
|---|---|---|
| Sites supervises | 3 | 30 |
| Postes par site | 1 a 2 | 3 a 10 selon centre |
| Serveurs internes | 1 simule | Variable |
| Firewalls | 2 simules | 1 par site minimum |
| Applications | 1 a 2 simulees | CRM, RDV, dossiers patients |
| Retention logs | Courte, pour demo | A definir selon politique securite |

## 5. Optimisation des couts

| Levier | Effet |
|---|---|
| Standardiser les agents | Reduit le temps d'onboarding. |
| Utiliser des templates syslog | Evite les configurations manuelles differentes par site. |
| Filtrer les logs inutiles | Reduit stockage et bruit SOC. |
| Prioriser les cas d'usage critiques | Evite une explosion de faux positifs. |
| Mutualiser le SOC | Repartit les couts sur plusieurs sites. |

## 6. Conclusion couts

Le MVP montre une solution techniquement viable a faible cout logiciel. Pour une mise en production, le budget devra surtout tenir compte de l'infrastructure, du stockage et du temps d'exploitation SOC.

La solution reste pertinente car elle est industrialisable : plus les deploiements sont standardises, plus le cout par site diminue.

