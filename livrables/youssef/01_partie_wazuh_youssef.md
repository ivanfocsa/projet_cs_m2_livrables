# Partie Youssef GUERNIOU - SIEM Wazuh

## Objectif de la partie

Youssef prend le role d'ingenieur SIEM. Sa partie consiste a rendre le SOC demonstrable avec une plateforme Wazuh exploitable : deploiement de la stack, raccordement des sources de logs, generation des alertes, dashboards et controle d'acces par role.

Cette partie repond directement aux attentes du cahier des charges :

| Attente | Reponse apportee |
|---|---|
| SIEM open-source centralise | Wazuh 4.14.5 en mode single-node Docker. |
| Collecte multi-source | Endpoint, serveur Linux, logs applicatifs Daylight et syslog firewall. |
| Dashboards lisibles | Vues Wazuh / OpenSearch par alertes, sources, severites et sites. |
| Interface web | Wazuh Dashboard accessible en HTTPS. |
| Roles supervision / analyste / admin | RBAC avec comptes `admin`, `analyste`, `supervision`. |
| Reproductibilite | Script `setup-siem-lab.ps1` et procedure de redemarrage. |

## Elements repris du travail envoye

| Element | Integration dans le depot |
|---|---|
| Documentation SIEM PDF | `livrables/youssef/supports/Documentation_SIEM_Youssef_GUERNIOU.pdf` |
| Script original envoye | `livrables/youssef/supports/setup-siem-lab-original-youssef.ps1` |
| Script adapte au depot | `scripts/setup-siem-lab.ps1` |
| Copie support du script adapte | `livrables/youssef/supports/setup-siem-lab.ps1` |
| Preuves Wazuh live | `livrables/preuves/wazuh-live-captures/` |

Le script original est conserve pour tracer le travail transmis. Le script adapte est celui a presenter dans le depot : il garde l'intention de Youssef, mais evite l'echec si certains scripts npm absents de ce depot ne sont pas disponibles.

## Architecture Wazuh couverte

| Composant | Role concret |
|---|---|
| Wazuh Manager | Reception des logs, decodage, application des regles, generation des alertes. |
| Wazuh Indexer | Stockage et recherche des evenements de securite. |
| Wazuh Dashboard | Interface web pour supervision, recherche, dashboards et evidence. |
| Agents Wazuh | Collecte endpoint et serveur. |
| Syslog | Collecte des evenements firewall/pfSense representes par `FW-S01` et `FW-S02`. |
| Regles Daylight | Detection des scenarios metier du projet avec IDs `100100` a `100160`. |

## Sources de logs

| Source | Preuve / scenario | Interet SOC |
|---|---|---|
| `poste-01` | Agent endpoint, controle SCA CIS Windows 11 dans la documentation Youssef. | Prouver la collecte poste de travail. |
| `serveur-01` | Conteneur Linux, SSH, rsyslog, `/var/log/auth.log`. | Prouver la collecte serveur et l'alerte brute force SSH. |
| Daylight applicatif | Logs CRM, RDV, dossiers patients. | Prouver la detection sur application metier sensible. |
| Firewall/syslog | Logs `FW-S01`, scenario `port_scan` / `brute_force`. | Prouver la collecte reseau attendue pour les centres. |

## Script `setup-siem-lab.ps1`

Le script automatise la partie SIEM demonstrable :

1. verification de Docker ;
2. creation ou redemarrage du conteneur `serveur-01` ;
3. installation de l'agent Wazuh `4.14.5-1` ;
4. activation de SSH et rsyslog ;
5. ajout de la collecte `/var/log/auth.log` dans l'agent ;
6. simulation de 15 echecs SSH pour generer une alerte brute force ;
7. creation des comptes `analyste` et `supervision` ;
8. creation du role `soc_readonly` ;
9. execution des scripts npm disponibles pour generer les preuves Daylight.

Commande :

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup-siem-lab.ps1
```

## Preuves a montrer en video

| Preuve | Chemin |
|---|---|
| Login Wazuh reel | `livrables/preuves/wazuh-live-captures/01-wazuh-login-real.png` |
| Dashboard Wazuh apres injection Daylight | `livrables/preuves/wazuh-live-captures/04-wazuh-overview-with-daylight-alerts-real.png` |
| Data Explorer avec alertes hautes | `livrables/preuves/wazuh-live-captures/05-wazuh-discover-high-alerts-real.png` |
| Threat Hunting Wazuh | `livrables/preuves/wazuh-live-captures/06-wazuh-threat-hunting-real.png` |
| Alerte firewall/syslog `100160` | `livrables/preuves/wazuh-live-captures/07-wazuh-firewall-portscan-100160-real.png` |
| Etat Docker live | `livrables/preuves/wazuh-live-captures/wazuh-docker-ps-live.txt` |
| Etat manager Wazuh live | `livrables/preuves/wazuh-live-captures/wazuh-manager-status-live.txt` |

## Points forts

- Le SIEM est un vrai Wazuh, pas une interface simulee.
- Le projet dispose de captures live Wazuh exploitables dans le rapport et la video.
- Le script donne une methode reproductible pour ajouter un serveur Linux et tester une attaque SSH.
- La documentation de Youssef couvre aussi les dashboards, le RBAC et la reprise apres redemarrage.

## Limites a annoncer proprement

Le lab reste un MVP : il ne reproduit pas les 30 centres complets avec tous les firewalls et postes reels. Il prouve en revanche la chaine SOC attendue : collecter, centraliser, detecter, visualiser, restreindre les roles et documenter. En production, il faudrait industrialiser le deploiement agent, la retention, les sauvegardes, le durcissement du SIEM et le controle des acces.

