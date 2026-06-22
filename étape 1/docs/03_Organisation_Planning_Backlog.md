# 03 - Organisation, planning et backlog

## 1. Organisation de l'equipe

| Membre | Role principal | Responsabilites |
|---|---|---|
| Yvan FOCSA | Coordinateur projet / Architecte securite | Cadrage, architecture, planning, backlog, couts, coherence des livrables, video. |
| Youssef GUERNIOU | Ingenieur SIEM | Installation Wazuh, agents, syslog, integration technique, guide de deploiement. |
| Kilyan FELIX | Analyste SOC | Regles de detection, dashboards, qualification alertes, preuves SOC. |
| Mahamadou DIACOUMBA | Blue Team / Reponse incident | Scenarios d'attaque, logs de demo, playbooks, scripts, remediation. |

## 2. RACI simplifie

| Activite | Yvan | Youssef | Kilyan | Mahamadou |
|---|---|---|---|---|
| Cadrage besoin | R | C | C | C |
| Architecture | R | C | C | C |
| Installation SIEM | C | R | C | C |
| Collecte logs | C | R | C | C |
| Generation logs demo | C | C | C | R |
| Regles detection | C | C | R | C |
| Dashboards | C | C | R | C |
| Playbooks | C | C | C | R |
| Rapport technique | R | C | C | C |
| Video demo | R | C | C | C |

R = responsable, C = contributeur.

## 3. Methodologie

L'equipe adopte une methode agile hybride :

- backlog partage ;
- points d'avancement hebdomadaires ;
- validation par preuves techniques ;
- documentation continue ;
- repetition de demo en fin de phase.

## 4. Planning

Source Mermaid : [../diagrams/gantt_planning.mmd](../diagrams/gantt_planning.mmd)

| Phase | Objectif | Responsable |
|---|---|---|
| 1 - Cadrage | Perimetre, architecture, backlog | Yvan |
| 2 - Socle technique | Wazuh installe, dashboard accessible | Youssef |
| 3 - Collecte logs | Agents, syslog, logs applicatifs | Youssef / Mahamadou |
| 4 - Detection | Regles et alertes | Kilyan |
| 5 - Dashboards | Vues supervision, analyste, admin | Kilyan |
| 6 - Reponse incident | Playbooks et procedures | Mahamadou |
| 7 - Consolidation | Rapport, preuves, guide, video | Toute l'equipe |

## 5. Backlog initial

| ID | Tache | Priorite | Responsable | Statut |
|---|---|---|---|---|
| B01 | Valider le perimetre MVP 3 sites | Haute | Yvan | A faire |
| B02 | Finaliser le schema d'architecture | Haute | Yvan | En cours |
| B03 | Creer l'inventaire des sites simules | Haute | Yvan | A faire |
| B04 | Installer le serveur Wazuh | Haute | Youssef | A faire |
| B05 | Acceder au dashboard Wazuh | Haute | Youssef | A faire |
| B06 | Connecter un premier agent endpoint | Haute | Youssef | A faire |
| B07 | Configurer la collecte syslog | Haute | Youssef | A faire |
| B08 | Generer les logs applicatifs metier | Haute | Mahamadou | A faire |
| B09 | Creer le scenario brute force | Haute | Kilyan | A faire |
| B10 | Creer le scenario execution suspecte | Haute | Kilyan | A faire |
| B11 | Creer le scenario USB suspect | Moyenne | Kilyan | A faire |
| B12 | Creer le scenario phishing | Haute | Mahamadou | A faire |
| B13 | Creer les dashboards SOC | Haute | Kilyan | A faire |
| B14 | Rediger le playbook brute force | Haute | Mahamadou | A faire |
| B15 | Rediger le playbook phishing | Haute | Mahamadou | A faire |
| B16 | Rediger le guide de deploiement | Haute | Youssef | A faire |
| B17 | Rediger la gestion des couts | Moyenne | Yvan | En cours |
| B18 | Capturer les preuves techniques | Haute | Toute l'equipe | A faire |
| B19 | Rediger le REX incidents simules | Haute | Yvan / equipe | A faire |
| B20 | Preparer la video MVP | Haute | Toute l'equipe | A faire |

## 6. Definition of Done

Une tache est terminee si :

- elle est testee ;
- une preuve est disponible ;
- la procedure est documentee ;
- le resultat est reproductible ;
- elle repond a une exigence du cahier des charges.

## 7. Points de controle

| Point de controle | Question |
|---|---|
| Fin cadrage | Le perimetre repond-il au cahier des charges ? |
| Fin installation | Le dashboard SOC est-il accessible ? |
| Fin collecte | Les logs arrivent-ils depuis plusieurs sources ? |
| Fin detection | Les alertes sont-elles visibles et exploitables ? |
| Fin playbooks | Les procedures permettent-elles de reagir ? |
| Fin projet | La demo raconte-t-elle clairement besoin, solution, preuves ? |

