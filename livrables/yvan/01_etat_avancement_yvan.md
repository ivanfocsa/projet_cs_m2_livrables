# Etat d'avancement - Yvan FOCSA

## Deja realise

| Domaine | Ce qui est fait | Niveau |
|---|---|---|
| Cadrage | Besoin client, contexte audioprothesistes, objectifs SOC externalise | Solide |
| Architecture | SOC centralise, Wazuh, collecte agents/syslog/logs applicatifs | Solide |
| Perimetre MVP | 3 sites simules pour representer un modele extensible vers 30 sites | Solide |
| Industrialisation | Convention de nommage, onboarding site, templates, guide d'exploitation | Solide |
| Couts | Couts MVP, couts de production et leviers de standardisation | Solide |
| Documentation | Rapport individuel, contribution architecture, matrice de conformite | Solide |
| Video | Script Yvan final, plan de passage et supports disponibles | A enregistrer |
| Preuves | Captures dashboard de demonstrateur disponibles | A remplacer par Wazuh live si possible |

## Ce qui manquait et a ete ajoute

| Manque identifie | Correction ajoutee |
|---|---|
| Pas de dossier Yvan centralise | Creation de `livrables/yvan/` |
| Pas de checklist personnelle claire | Ajout de `05_checklist_finale_yvan.md` |
| Script oral trop long pour une video groupe | Ajout d'un script 3-5 minutes |
| Pas de phrase couts pour l'oral | Ajout d'une phrase couts courte et defendable |
| Pas de reponses aux questions jury | Ajout d'une FAQ jury orientee architecture |
| Supports eparpilles | Copie des supports utiles dans `supports/` |

## Ce que tu peux finir sans attendre les autres

1. Lire le script oral deux fois a voix haute.
2. Chronometrer ton passage : vise 3 minutes 30 a 4 minutes.
3. Preparer ton affichage : nom + role.
4. Ouvrir les supports dans l'ordre conseille.
5. Connaitre par coeur les limites du MVP : logs simules, pas 30 sites reels, pas HA, mais chaine SOC prouvee.
6. Connaitre la phrase couts : open-source pour le MVP, couts production surtout infra, stockage, exploitation SOC et onboarding.

## Niveau de risque pour ta partie

| Risque | Niveau | Reponse |
|---|---|---|
| Le jury demande pourquoi seulement 3 sites | Faible | C'est un MVP representatif, concu pour etre etendu. |
| Le jury demande si Docker = production | Moyen | Docker est un choix de lab ; la production utiliserait agents, serveurs et firewalls reels. |
| Le jury demande ou sont les preuves | Moyen | Montrer `livrables/preuves/sprint-01/` et les captures dashboard. |
| Le jury demande ton apport personnel | Faible | Architecture, flux, industrialisation, coherence des livrables. |
