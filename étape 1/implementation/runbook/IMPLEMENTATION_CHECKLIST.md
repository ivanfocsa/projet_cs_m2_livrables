# Checklist implementation concrete

## 1. Wazuh

- [ ] Stack Wazuh demarree.
- [ ] Dashboard accessible en HTTPS.
- [ ] Script `scripts/setup-siem-lab.ps1` execute.
- [ ] Agent `serveur-01` visible.
- [ ] Comptes `analyste` et `supervision` crees.
- [ ] Role `soc_readonly` mappe.

## 2. Logs

- [ ] Logs endpoint generes.
- [ ] Logs application generes.
- [ ] Logs AD generes.
- [ ] Logs messagerie generes.
- [ ] Logs firewall `FW-S01/FW-S02` generes ou pfSense configure.

## 3. Wazuh configuration

- [ ] `local_rules.xml` copie.
- [ ] `local_decoders_daylight.xml` ajoute.
- [ ] `ossec-manager-daylight.conf` adapte dans `ossec.conf`.
- [ ] Service Wazuh redemarre.
- [ ] Alertes `100100` a `100160` visibles.

## 4. pfSense

- [ ] pfSense CE ou logs simules disponibles.
- [ ] Remote syslog configure vers Wazuh.
- [ ] Filtrage IP source applique en production.
- [ ] Test brute force ou scan visible.

## 5. Production cible

- [ ] VPN site-a-site prevu pour les sites.
- [ ] Retention index documentee.
- [ ] Sauvegarde des regles/playbooks prevue.
- [ ] Dashboards par role crees.
- [ ] Checklist onboarding site remplie.

