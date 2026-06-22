# Supports a montrer pendant le passage Yvan

## Ordre conseille

| Ordre | Support | Pourquoi le montrer |
|---:|---|---|
| 1 | `supports/architecture_soc_externalise.mmd` | Montrer l'architecture globale SOC externalise. |
| 2 | `supports/01-dashboard-home.png` | Montrer que le SOC produit une vue lisible. |
| 3 | `supports/client_onboarding_checklist.md` | Prouver l'industrialisation vers plusieurs sites. |
| 4 | `supports/site_inventory.example.yml` | Montrer la logique d'inventaire site/machines. |
| 5 | `supports/09_Matrice_Conformite_Cahier_Charges.md` | Relier le projet au cahier des charges. |

## Phrase de transition entre les supports

### Architecture

> Ici, on voit que le SOC est centralise cote prestataire. Les sites clients restent producteurs de logs, et Wazuh centralise la collecte, l'analyse et la visualisation.

### Dashboard global

> Cette vue permet de rendre la supervision lisible : alertes par scenario, criticite, site et source. C'est important parce qu'un SOC doit etre exploitable, pas seulement technique.

### Checklist onboarding

> Pour passer de trois sites simules a trente sites, il faut standardiser le deploiement. La checklist evite de refaire chaque integration manuellement.

### Inventaire site

> L'inventaire permet de savoir quelles machines, applications et firewalls sont rattaches a chaque site. C'est indispensable pour filtrer les dashboards et fiabiliser le reporting.

### Matrice de conformite

> Cette matrice montre que chaque exigence du cahier des charges a une reponse projet : collecte, SIEM, dashboards, playbooks, reporting et reproductibilite.

## Supports a eviter pendant ton passage

- Ne rentre pas trop dans les regles Wazuh ligne par ligne : c'est plutot la partie detection.
- Ne passe pas trop de temps sur les playbooks : c'est plutot la partie reponse incident.
- Ne promets pas une production 30 sites deja faite : presente-le comme une trajectoire industrialisable.

