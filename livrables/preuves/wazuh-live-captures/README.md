# Captures Wazuh live

Ces fichiers remplacent les anciennes captures de demonstrateur generees.
Ils proviennent d'une vraie stack Wazuh 4.14.5 lancee localement avec Docker/Colima depuis le depot officiel `wazuh/wazuh-docker`, mode `single-node`.

Acces local utilise pour les captures :

- URL : `https://localhost`
- Login : `admin`
- Mot de passe : `SecretPassword`

Preuves principales :

| Fichier | Preuve |
| --- | --- |
| `01-wazuh-login-real.png` | Vraie page de connexion Wazuh. |
| `03-wazuh-after-login-real.png` | Vue Wazuh apres authentification. |
| `04-wazuh-overview-with-daylight-alerts-real.png` | Overview Wazuh apres injection des logs Daylight. |
| `05-wazuh-discover-high-alerts-real.png` | Data Explorer avec alertes `SOC AUDIO`, dont `100110`. |
| `06-wazuh-threat-hunting-real.png` | Dashboard Threat Hunting Wazuh. |
| `07-wazuh-firewall-portscan-100160-real.png` | Preuve firewall/syslog `FW-S01`, alerte `100160`, source `firewall_syslog.log`. |
| `wazuh-docker-ps-live.txt` | Etat des conteneurs Wazuh Manager, Indexer, Dashboard. |
| `wazuh-manager-status-live.txt` | Etat des services internes Wazuh. |
| `wazuh-daylight-alerts-live.jsonl` | Extraits JSON des alertes Daylight `100100` a `100160`. |
| `wazuh-firewall-100160-live.jsonl` | Extrait JSON prouvant le scan reseau firewall `FW-S01`. |

Note pfSense :

pfSense CE n'est pas lance ici comme interface web separee, car pfSense est une appliance FreeBSD a installer en VM, pas un conteneur Docker. La preuve firewall livrable pour le MVP est donc l'integration syslog de firewalls cibles `FW-S01/FW-S02` dans Wazuh, avec le decoder `daylight-firewall` et les alertes `100110` / `100160`.
