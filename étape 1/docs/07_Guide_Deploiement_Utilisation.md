# 07 - Guide de deploiement et d'utilisation

## 1. Objectif

Ce guide decrit les etapes pour deployer le demonstrateur SOC, connecter les premieres sources de logs et utiliser l'interface pour analyser les alertes.

## 2. Prerequis MVP

| Element | Besoin |
|---|---|
| Machine SOC | VM Linux recommandee, ressources suffisantes pour Wazuh. |
| Reseau | Connectivite entre sites simules et SOC. |
| Postes clients | Windows ou Linux avec agent Wazuh. |
| Logs reseau | pfSense CE cible (`FW-S01`/`FW-S02`) ou logs syslog simules. |
| Logs applicatifs | Fichiers generes par `scripts/generate_demo_logs.py`. |
| Navigateur | Acces au dashboard Wazuh. |

## 3. Etapes de deploiement

### Etape 1 - Installer le socle Wazuh

Responsable : Youssef.

Actions :

1. Installer Wazuh Manager.
2. Installer OpenSearch / indexer.
3. Installer Wazuh Dashboard.
4. Verifier l'acces web.
5. Capturer une preuve du dashboard accessible.

Documentation interne : [../infra/wazuh/README.md](../infra/wazuh/README.md)

Snippets concrets a appliquer : [../implementation/README.md](../implementation/README.md)

Automatisation disponible :

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup-siem-lab.ps1
```

Cette commande reprend le perimetre SIEM documente par Youssef : conteneur `serveur-01`, agent Wazuh, collecte `/var/log/auth.log`, simulation brute force SSH, comptes RBAC `analyste` et `supervision`, puis generation des logs/preuves Daylight selon les scripts npm presents dans le depot.

### Etape 2 - Connecter un premier agent

Actions :

1. Installer l'agent sur `PC-S01-AUDIO-01`.
2. Enregistrer l'agent cote Wazuh Manager.
3. Verifier le statut `active`.
4. Generer un evenement simple.
5. Verifier que l'evenement apparait dans le dashboard.

### Etape 3 - Collecter les logs firewall

Actions :

1. Sur pfSense CE, ouvrir `Status > System Logs > Settings`.
2. Activer `Remote Logging`.
3. Renseigner l'adresse du Wazuh Manager comme serveur syslog distant.
4. Envoyer les categories firewall/filterlog vers le SOC.
5. En lab, utiliser aussi `logs/generated/firewall_syslog.log` pour rejouer des evenements `FW-S01` et `FW-S02`.
6. Verifier la reception dans Wazuh.
7. Creer un filtre dashboard pour les evenements reseau.

### Etape 4 - Collecter les logs applicatifs

Actions :

1. Generer les logs de demo :

```bash
python scripts/generate_demo_logs.py --out logs/generated --count 200
```

2. Configurer Wazuh pour surveiller le fichier de log.
3. Verifier que les champs utiles sont visibles.
4. Tester une regle applicative.

### Etape 5 - Ajouter les regles SOC

Point de depart : [../detection/wazuh/local_rules.xml](../detection/wazuh/local_rules.xml)

Decoders et collecte concrete : [../implementation/wazuh/](../implementation/wazuh/)

Actions :

1. Copier les regles dans la configuration locale Wazuh.
2. Redemarrer le service Wazuh si necessaire.
3. Generer les logs de test.
4. Verifier les alertes.
5. Ajuster les seuils.

### Verification concrete

Depuis la racine du depot :

```bash
npm run verify:concrete-stack
```

Cette commande verifie que les fichiers d'implementation, les regles `100100` a `100160`, les logs de demonstration et les scenarios attendus sont presents.

## 4. Utilisation SOC

| Action | Interface |
|---|---|
| Consulter les alertes | Wazuh Dashboard |
| Filtrer par site | Champ `site` ou nom machine |
| Filtrer par criticite | Niveau d'alerte |
| Analyser un evenement | Detail de l'alerte |
| Exporter une preuve | Capture ou export CSV/PDF |
| Appliquer une procedure | Playbook correspondant |

## 5. Checklist onboarding site

Voir [../infra/templates/client_onboarding_checklist.md](../infra/templates/client_onboarding_checklist.md).

Resume :

- creer l'identifiant site ;
- declarer les machines ;
- installer les agents ;
- configurer syslog ;
- verifier collecte ;
- tester une alerte ;
- ajouter le site au dashboard ;
- documenter la validation.

## 6. Guide utilisateur court

Pour un analyste SOC :

1. Ouvrir le dashboard.
2. Filtrer les alertes recentes.
3. Trier par criticite.
4. Ouvrir l'alerte.
5. Identifier la source, l'utilisateur, le site et l'heure.
6. Rechercher les evenements lies.
7. Appliquer le playbook.
8. Documenter la decision.

Pour un administrateur :

1. Verifier l'etat des agents.
2. Controler la reception des logs.
3. Ajuster les regles.
4. Maintenir les comptes et roles.
5. Sauvegarder la configuration.

## 7. Preuves attendues

| Preuve | Responsable |
|---|---|
| Dashboard accessible | Youssef |
| Agent actif | Youssef |
| Log syslog recu | Youssef |
| Alerte SSH brute force `5712` | Youssef |
| RBAC `analyste` / `supervision` lecture seule | Youssef |
| Log applicatif recu | Mahamadou |
| Alerte brute force | Kilyan |
| Dashboard supervision | Kilyan |
| Playbook applique | Mahamadou |
| Capture finale pour rapport | Yvan |
