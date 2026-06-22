# Dossier Youssef GUERNIOU - SIEM Wazuh

## Objectif

Ce dossier centralise les elements fournis par Youssef pour la partie SIEM/Wazuh du projet Daylight. Il complete le dossier de preuves global avec une documentation specifique au deploiement, a la collecte et a l'exploitation du lab Wazuh.

## Fichiers integres

| Fichier | Role |
|---|---|
| `01_partie_wazuh_youssef.md` | Synthese livrable de la partie Wazuh/SIEM de Youssef, prete a relire avant soutenance. |
| `02_script_video_youssef_3_min.md` | Script oral court pour tenir environ 3 minutes dans la video groupe. |
| `supports/Documentation_SIEM_Youssef_GUERNIOU.pdf` | Documentation SIEM fournie par Youssef : architecture Wazuh, sources de logs, dashboards, RBAC et procedure de reprise. |
| `../../scripts/setup-siem-lab.ps1` | Script PowerShell canonique dans le depot projet. |
| `supports/setup-siem-lab.ps1` | Copie du script dans le dossier Youssef pour le zip final et la soutenance. |
| `supports/setup-siem-lab-original-youssef.ps1` | Script original envoye par Youssef, conserve pour tracer son travail initial. |
| `pdf/01_Partie_Wazuh_Youssef.pdf` | Version PDF de la synthese Wazuh. |
| `pdf/02_Script_Video_Youssef_3_Min.pdf` | Version PDF du script video Youssef. |

## Ce que couvre la partie SIEM

| Perimetre | Etat |
|---|---|
| Stack Wazuh | Wazuh single-node Docker en version 4.14.5. |
| Interface | Dashboard accessible en HTTPS local. |
| Endpoint Windows | Agent `poste-01`, SCA CIS Windows 11, evenements endpoint. |
| Serveur Linux | Conteneur `serveur-01`, agent Wazuh, SSH, rsyslog et suivi de `/var/log/auth.log`. |
| Scenario brute force | Simulation SSH avec alertes Wazuh attendues `5710`, `5503` et `5712`. |
| Logs applicatifs Daylight | Alertes applicatives `100100` a `100160` selon les logs et regles du projet. |
| RBAC | Comptes `analyste` et `supervision` en lecture seule via le role `soc_readonly`; admin conserve les droits complets. |
| Dashboards | Vue technique et vue executive pour supervision et demonstration. |

## Execution du script

Prerequis :

- Docker Desktop lance ;
- stack Wazuh single-node deja demarree ;
- lancement depuis la racine du depot ;
- PowerShell disponible.

Commande :

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup-siem-lab.ps1
```

Le script execute les etapes suivantes :

1. cree ou redemarre le conteneur `serveur-01` ;
2. installe l'agent Wazuh 4.14.5-1 dans ce conteneur ;
3. configure SSH, rsyslog et la collecte de `/var/log/auth.log` ;
4. simule 15 echecs SSH pour declencher une alerte brute force ;
5. configure les utilisateurs RBAC `analyste` et `supervision` ;
6. lance les scripts npm disponibles dans ce depot, notamment `generate:logs` et `prepare:preuves`.

## Note importante

La documentation initiale de Youssef mentionne des commandes `npm run lab:start`, `npm run lab:deploy-daylight` et `npm run lab:replay-daylight`. Ces commandes ne sont pas presentes dans le `package.json` actuel du depot. Le script integre a donc ete adapte : il execute les scripts existants et ignore proprement les scripts absents pour eviter un echec inutile.

## Captures Wazuh live disponibles

Les vraies captures Wazuh live sont disponibles dans `../preuves/wazuh-live-captures/`.

Captures prioritaires pour la video :

- `04-wazuh-overview-with-daylight-alerts-real.png` : dashboard Wazuh apres injection des logs.
- `05-wazuh-discover-high-alerts-real.png` : Data Explorer avec alertes fortes.
- `06-wazuh-threat-hunting-real.png` : vue Threat Hunting.
- `07-wazuh-firewall-portscan-100160-real.png` : preuve firewall/syslog avec regle `100160`.

Captures utiles si le lab complet Youssef est relance :

- liste des agents avec `poste-01` et `serveur-01` actifs ;
- detail de l'agent `serveur-01` ;
- evenements `/var/log/auth.log` recus ;
- alerte brute force SSH `5712` ;
- vue RBAC montrant le role `soc_readonly` ;
- connexion en lecture seule avec `analyste` ou `supervision`.
