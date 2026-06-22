# Configuration pfSense CE vers Wazuh

## Parametres lab

| Parametre | Valeur |
|---|---|
| Firewall site 1 | `FW-S01-PFSENSE` |
| Firewall site 2 | `FW-S02-PFSENSE` |
| Destination syslog | IP du Wazuh Manager |
| Port lab | UDP `514` |
| Port cible production | TCP `5514` ou syslog dans VPN site-a-site |
| Categories | Firewall/filterlog, system, VPN si disponible |
| Horodatage | NTP actif sur pfSense et Wazuh |

## Etapes pfSense

1. Aller dans `Status > System Logs > Settings`.
2. Cocher `Enable Remote Logging`.
3. Renseigner l'adresse IP du Wazuh Manager.
4. Choisir `IPv4`.
5. Selectionner les logs firewall/filterlog.
6. Sauvegarder.
7. Generer un trafic refuse pour valider la collecte.
8. Dans Wazuh, filtrer sur `FW-S01`, `FW-S02`, `brute_force` ou `port_scan`.

## Securisation production

- Ne pas exposer le port syslog publiquement.
- Transporter les logs via VPN site-a-site ou reseau prive.
- Filtrer les IP sources autorisees cote Wazuh.
- Conserver une convention de nommage `FW-SXX-PFSENSE`.
- Tester une alerte apres chaque onboarding site.

## Equivalent MVP

Si pfSense n'est pas deploye pendant la demo, rejouer :

```bash
etape 1/logs/generated/firewall_syslog.log
```

Ce fichier represente les evenements envoyes par `FW-S01` et `FW-S02`.

