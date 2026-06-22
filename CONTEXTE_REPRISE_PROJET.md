# CONTEXTE DE REPRISE - PROJET M2 CYBERSECURITE

Ce fichier sert a reprendre le projet dans un autre chat sans perdre le contexte.

Projet GitHub : `ivanfocsa/projet_cs_m2_livrables`

Chemin local principal :

```text
/Users/yvanfocsa/Documents/PROJET M2/projet_cs_m2_livrables
```

Chemin du runtime Wazuh Docker local :

```text
/Users/yvanfocsa/Documents/PROJET M2/runtime/wazuh-docker/single-node
```

## 1. Prompt a coller dans un nouveau chat

Copier-coller ce bloc dans un nouveau chat si besoin :

```text
Je travaille sur un projet M2 Cybersecurite Sup de Vinci a rendre tres vite.
Sujet : mise en place d'un SOC externalise pour un reseau d'audioprothesistes, environ 30 centres en France.
Repo : /Users/yvanfocsa/Documents/PROJET M2/projet_cs_m2_livrables
GitHub : https://github.com/ivanfocsa/projet_cs_m2_livrables

Equipe :
- Yvan FOCSA : architecte securite/infrastructure, cadrage, flux, industrialisation, couts, coherence des livrables.
- Youssef GUERNIOU : ingenieur SIEM Wazuh, collecte, agents, dashboards, RBAC, script setup-siem-lab.ps1.
- Mahamadou DIACOUMBA : analyste SOC, scenarios, regles, alertes, playbooks, REX.
- Kilyan FELIX : chef de projet/referent client, cadrage, planning, rapport, video.

Etat actuel :
- Les livrables PDF groupe et individuels sont generes.
- Le zip final existe : livrables/PE_2526_M2CS_FOCSA_GUERNIOU_FELIX_DIACOUMBA.zip
- Le dossier PDF_TRIES separe les PDF a deposer, les supports techniques et les notes Yvan.
- Un vrai Wazuh 4.14.5 a ete lance localement via Docker/Colima.
- Les captures Wazuh live sont dans livrables/preuves/wazuh-live-captures/.
- L'ancien dashboard HTML de secours a ete supprime/remplace par des preuves Wazuh reelles.

Ce qu'il reste surtout a faire :
- Faire la video finale 15 a 20 min.
- Chaque membre doit parler et son nom doit etre affiche.
- Mettre la video sur YouTube en Non repertorie ou deposer le MP4 dans le zip.
- Remplacer le placeholder TXT YouTube par un vrai lien.
- Eventuellement produire quelques captures Wazuh supplementaires si le lab complet poste-01/serveur-01 est relance.
```

## 2. But du projet

Le client fictif est un reseau de centres d'audioprothesistes repartis sur environ 30 points de vente en France.

Le besoin client :

- centraliser les evenements de securite ;
- detecter les comportements suspects ;
- avoir une interface web claire pour les analystes ;
- produire des alertes, dashboards et preuves ;
- industrialiser la solution dans un modele d'infogerance SOC ;
- documenter la solution pour qu'elle soit reproductible.

Le projet ne doit pas seulement etre un rapport. Il doit montrer une plateforme de demonstration fonctionnelle, securisee, documentee et industrialisable.

## 3. Consignes importantes

Les consignes pedagogiques demandent deux grandes familles de livrables :

1. Video et demonstration MVP :
   - duree imposee : 15 a 20 minutes ;
   - chaque membre doit parler ;
   - le nom de chaque membre doit apparaitre pendant sa prise de parole ;
   - format : MP4 dans un zip ou lien YouTube Non repertorie dans un TXT ;
   - structure attendue : besoin client, solution, demonstration.

2. Document technique final :
   - un zip contenant un PDF groupe et un PDF par membre ;
   - rapport technique complet ;
   - analyse, architecture, configurations, logs, procedures, REX, planning, roles ;
   - rendu groupe : entreprise/equipe, problematique, couts M2, organisation, planning, methodologie, solution technique ;
   - rendu individuel : perspectives, limites techniques, analyse personnelle, competences, axes d'amelioration.

Il n'y a pas de minimum ou maximum officiel de pages trouve dans les consignes. Le volume actuel est correct :

- rapport groupe : 50 pages ;
- Yvan : 5 pages ;
- Youssef : 4 pages ;
- Kilyan : 3 pages ;
- Mahamadou : 3 pages.

## 4. Roles de l'equipe

| Membre | Role | Responsabilites principales |
|---|---|---|
| Yvan FOCSA | Architecte securite / infrastructure | Besoin client, architecture SOC, flux de collecte, passage MVP vers 30 centres, couts, coherence des livrables. |
| Youssef GUERNIOU | Ingenieur SIEM | Wazuh, collecte, agents, dashboard, RBAC, script `setup-siem-lab.ps1`. |
| Mahamadou DIACOUMBA | Analyste SOC | Scenarios, regles de detection, alertes, playbooks, REX incidents. |
| Kilyan FELIX | Chef de projet / referent client | Cadrage fonctionnel, planning, organisation, rapport, video, coherence client. |

## 5. Architecture actuelle du MVP

Le MVP repose sur un SOC centralise.

Sources simulees ou integrees :

- postes de travail ;
- serveurs internes ;
- applications metier Daylight : CRM, RDV, dossiers patients ;
- Active Directory simule ;
- messagerie ;
- firewall/syslog represente par `FW-S01` et `FW-S02`.

Stack SOC :

- Wazuh Manager : reception des logs, analyse, regles, alertes ;
- Wazuh Indexer : stockage et recherche ;
- Wazuh Dashboard : interface web ;
- agents Wazuh ou logs rejoues ;
- syslog pour la partie firewall ;
- playbooks de reponse incident.

Important : le MVP ne reproduit pas 30 centres complets. Il prouve une chaine SOC industrialisable sur un perimetre reduit, puis explique comment l'etendre a 30 sites via onboarding standardise.

## 6. Wazuh live

Un vrai Wazuh 4.14.5 a ete lance localement avec Docker/Colima.

URL locale :

```text
https://localhost
```

Identifiants demo :

```text
admin / SecretPassword
```

Conteneurs attendus :

- `single-node-wazuh.manager-1`
- `single-node-wazuh.indexer-1`
- `single-node-wazuh.dashboard-1`

Chemin runtime Wazuh officiel clone :

```text
/Users/yvanfocsa/Documents/PROJET M2/runtime/wazuh-docker/single-node
```

Commandes utiles :

```bash
cd "/Users/yvanfocsa/Documents/PROJET M2/runtime/wazuh-docker/single-node"
docker-compose ps
docker-compose up -d
docker-compose down
```

Pour arreter Colima si besoin :

```bash
colima stop
```

## 7. Preuves Wazuh live

Dossier principal :

```text
livrables/preuves/wazuh-live-captures/
```

Captures existantes :

| Fichier | Utilite |
|---|---|
| `01-wazuh-login-real.png` | Vrai ecran de login Wazuh. |
| `02-wazuh-login-filled-real.png` | Login Wazuh rempli. |
| `03-wazuh-after-login-real.png` | Wazuh apres connexion. |
| `04-wazuh-overview-with-daylight-alerts-real.png` | Vue Wazuh avec alertes Daylight injectees. |
| `05-wazuh-discover-high-alerts-real.png` | Data Explorer avec alertes hautes. |
| `06-wazuh-threat-hunting-real.png` | Vue Threat Hunting. |
| `07-wazuh-firewall-portscan-100160-real.png` | Alerte firewall/syslog `100160`. |
| `wazuh-docker-ps-live.txt` | Etat Docker live. |
| `wazuh-manager-status-live.txt` | Etat du manager Wazuh. |
| `wazuh-daylight-alerts-live.jsonl` | Extraits alertes Daylight live. |
| `wazuh-firewall-100160-live.jsonl` | Extraits alerte firewall 100160. |

Point important : ces preuves remplacent le vieux dashboard HTML de secours. Pour parler au jury, dire que les captures prioritaires sont maintenant les vraies interfaces Wazuh.

## 8. pfSense / firewall

Le projet parle de firewalls par centre et de flux reseau. La partie concrete actuelle est :

- logs firewall/syslog avec hosts `FW-S01` et `FW-S02` ;
- scenarios `brute_force` et `port_scan` ;
- detection Wazuh avec l'ID `100160` pour scan reseau/firewall ;
- preuve visible dans Wazuh live : `07-wazuh-firewall-portscan-100160-real.png`.

Il n'y a pas de vraie interface pfSense capturee dans le depot, car aucune VM/ISO pfSense locale n'a ete fournie. Il ne faut pas inventer une fausse interface pfSense. Si le jury demande, repondre :

```text
Pour le MVP, pfSense est represente par des logs syslog firewall envoyes au SOC. La preuve attendue cote SOC est que Wazuh recoit, indexe et detecte ces logs. Une interface pfSense reelle serait une evolution si une VM pfSense etait disponible.
```

## 9. Alertes et IDs importants

Les IDs sont harmonises entre regles, rapport, captures et video.

| ID | Scenario | Source | Criticite |
|---|---|---|---|
| `100100` | Execution PowerShell suspecte | Endpoint | Haute |
| `100110` | Brute force acces distant | Firewall/syslog | Haute |
| `100120` | Acces anormal dossier patient | Application metier | Haute |
| `100130` | Modification groupe privilegie | Active Directory | Critique |
| `100140` | Usage USB detecte | Endpoint | Moyenne |
| `100150` | Phishing | Messagerie | Haute |
| `100160` | Scan reseau / port scan firewall | Firewall/syslog | Haute |

Fichiers techniques associes :

```text
étape 1/detection/wazuh/local_rules.xml
étape 1/implementation/wazuh/local_decoders_daylight.xml
étape 1/logs/generated/
livrables/preuves/sprint-01/daylight-alerts-table.md
```

Note technique : le decoder Wazuh a ete corrige pour eviter les groupes regex non supportes par Wazuh, notamment `(?:...)`.

## 10. Partie Yvan

Dossier principal :

```text
livrables/yvan/
```

Role a annoncer :

```text
Yvan FOCSA - architecte securite / infrastructure, flux reseau et industrialisation.
```

Message cle :

```text
Mon role a ete de cadrer l'architecture SOC externalisee, de definir le perimetre MVP, de structurer les flux de collecte et de montrer comment le demonstrateur peut etre industrialise vers environ 30 sites.
```

Fichiers importants :

| Fichier | Usage |
|---|---|
| `livrables/yvan/00_A_LIRE_DOSSIER_YVAN_FINAL.md` | Point d'entree du dossier Yvan. |
| `livrables/yvan/01_etat_avancement_yvan.md` | Etat de la partie Yvan. |
| `livrables/yvan/02_script_oral_yvan_3_5_min.md` | Script oral Yvan. |
| `livrables/yvan/06_script_video_yvan_final.md` | Script final video Yvan. |
| `livrables/yvan/07_stack_technique_concrete_yvan.md` | Choix techniques concrets. |
| `livrables/yvan/08_argumentaire_solutions_concretes_yvan.md` | Argumentaire technique. |
| `livrables/yvan/diagrams/architecture_soc_externalise.png` | Schema principal. |
| `livrables/yvan/diagrams/topologie_sites_mvp.png` | 3 sites MVP vers 30 centres. |
| `livrables/yvan/diagrams/flux_collecte_logs.png` | Flux de collecte. |

PDF Yvan a deposer :

```text
livrables/individuels/Yvan_FOCSA_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf
```

## 11. Partie Youssef

Dossier principal :

```text
livrables/youssef/
```

Role :

```text
Youssef GUERNIOU - ingenieur SIEM Wazuh.
```

Fichiers importants :

| Fichier | Usage |
|---|---|
| `livrables/youssef/01_partie_wazuh_youssef.md` | Synthese livrable de sa partie Wazuh. |
| `livrables/youssef/02_script_video_youssef_3_min.md` | Script 3 minutes pour la video. |
| `livrables/youssef/supports/Documentation_SIEM_Youssef_GUERNIOU.pdf` | Documentation Wazuh fournie par Youssef. |
| `livrables/youssef/supports/setup-siem-lab-original-youssef.ps1` | Script original envoye par Youssef. |
| `scripts/setup-siem-lab.ps1` | Script adapte au depot. |

Ce que couvre sa partie :

- Wazuh 4.14.5 ;
- Manager, Indexer, Dashboard ;
- agent endpoint `poste-01` dans sa doc ;
- conteneur Linux `serveur-01` ;
- SSH, rsyslog, `/var/log/auth.log` ;
- simulation brute force SSH ;
- RBAC : `admin`, `analyste`, `supervision` ;
- dashboards technique et executive ;
- sources Daylight et firewall/syslog.

PDF Youssef a deposer :

```text
livrables/individuels/Youssef_GUERNIOU_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf
```

## 12. Partie Mahamadou

Role :

```text
Mahamadou DIACOUMBA - analyste SOC.
```

Il porte surtout :

- les scenarios de detection ;
- les alertes ;
- les playbooks ;
- l'analyse SOC ;
- le REX incidents simules.

Fichiers utiles :

```text
étape 1/playbooks/
livrables/rapport-final/rex-incidents-simules.md
livrables/individuels/Mahamadou_DIACOUMBA_rendu_individuel_v1.md
```

PDF Mahamadou a deposer :

```text
livrables/individuels/Mahamadou_DIACOUMBA_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf
```

## 13. Partie Kilyan

Role :

```text
Kilyan FELIX - chef de projet / referent client.
```

Il porte surtout :

- cadrage client ;
- planning ;
- organisation ;
- coherence du rapport ;
- introduction et conclusion video ;
- posture prestataire.

PDF Kilyan a deposer :

```text
livrables/individuels/Kilyan_FELIX_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf
```

## 14. Livrables principaux

Rapport groupe final :

```text
livrables/rapport-final/Rapport_Technique_Final_50p_V1_SANS_PAGES_BLANCHES.pdf
```

PDF individuels :

```text
livrables/individuels/Yvan_FOCSA_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf
livrables/individuels/Youssef_GUERNIOU_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf
livrables/individuels/Kilyan_FELIX_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf
livrables/individuels/Mahamadou_DIACOUMBA_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf
```

Zip final :

```text
livrables/PE_2526_M2CS_FOCSA_GUERNIOU_FELIX_DIACOUMBA.zip
```

Dossier de tri PDF :

```text
livrables/PDF_TRIES/
```

Structure du tri :

- `01_A_DEPOSER_OBLIGATOIRE/` : PDF groupe + 4 PDF individuels ;
- `02_SUPPORTS_TECHNIQUES_SI_BESOIN/` : annexes techniques utiles ;
- `03_NOTES_YVAN_POUR_ORAL_ET_REPERAGE/` : notes pour l'oral et la video.

## 15. Video finale

Consigne : 15 a 20 minutes.

Script principal :

```text
livrables/mvp-video/script-video.md
```

Deroule conseille :

| Temps | Intervenant | Sujet |
|---|---|---|
| 0:00 - 2:00 | Kilyan | Client Daylight, besoin cyber, contexte 30 centres. |
| 2:00 - 5:00 | Yvan | Architecture, MVP, flux, industrialisation vers 30 sites. |
| 5:00 - 8:00 | Youssef | Wazuh, script SIEM, sources de logs, RBAC, captures live. |
| 8:00 - 13:00 | Mahamadou | Alertes, scenarios, regles, analyse SOC. |
| 13:00 - 16:00 | Kilyan / Mahamadou | Playbooks, traitement incident, REX. |
| 16:00 - 18:00 | Yvan | Couts, limites, evolutions. |
| 18:00 - 20:00 | Tous | Conclusion. |

Attention :

- afficher le nom de chaque membre pendant son passage ;
- montrer les vraies captures Wazuh live ;
- ne pas dire que pfSense est en vraie interface si ce n'est pas le cas ;
- mettre le lien YouTube Non repertorie dans le TXT une fois la video prete.

Fichier TXT video actuel :

```text
livrables/mvp-video/PE_2526_M2CS_FOCSA_GUERNIOU_FELIX_DIACOUMBA.txt
```

Il contient encore un placeholder a remplacer par le vrai lien YouTube.

## 16. Commandes projet

Depuis la racine du repo :

```bash
cd "/Users/yvanfocsa/Documents/PROJET M2/projet_cs_m2_livrables"
```

Generer les logs :

```bash
npm run generate:logs
```

Generer les preuves de secours :

```bash
npm run prepare:preuves
```

Generer les PDF :

```bash
npm run generate:pdf
```

Verifier la stack concrete :

```bash
npm run verify:concrete-stack
```

Tester le zip :

```bash
unzip -t livrables/PE_2526_M2CS_FOCSA_GUERNIOU_FELIX_DIACOUMBA.zip
```

## 17. Scripts importants

| Script | Role |
|---|---|
| `scripts/generate-rapports-v1.mjs` | Genere le rapport groupe et les PDF individuels. |
| `scripts/generate-yvan-pack.py` | Genere le pack PDF/schemas Yvan. |
| `scripts/prepare-final-deliverables.py` | Genere les preuves de secours. |
| `scripts/run-python-with-pillow.mjs` | Lance le Python bundle avec Pillow si besoin. |
| `scripts/setup-siem-lab.ps1` | Integre la partie SIEM/Wazuh de Youssef. |
| `scripts/verify-concrete-stack.py` | Verifie coherence concrete : regles, scenarios, firewall, decoder. |

## 18. Fichiers techniques Wazuh

Regles :

```text
étape 1/detection/wazuh/local_rules.xml
```

Decoder :

```text
étape 1/implementation/wazuh/local_decoders_daylight.xml
```

Config localfile manager :

```text
étape 1/implementation/wazuh/ossec-manager-daylight.conf
```

Filtres dashboard :

```text
étape 1/implementation/dashboards/dashboard-filters.md
```

pfSense/syslog :

```text
étape 1/implementation/pfsense/syslog-settings.md
```

## 19. Ce qui est deja termine

- Repo clone et organise.
- Rapport groupe 50 pages genere.
- 4 rendus individuels generes.
- Dossier Yvan complet : scripts, schemas, PDF, argumentaire.
- Dossier Youssef complet : doc SIEM, script original, script integre, synthese Wazuh, script video.
- Vraie stack Wazuh lancee localement.
- Captures Wazuh live produites.
- Alertes Daylight injectees dans Wazuh.
- Regles `100100` a `100160` harmonisees.
- Zip final reconstruit et teste.
- Push GitHub effectue apres chaque grosse etape.

## 20. Ce qui reste a faire

Priorite absolue :

1. Enregistrer la video finale de 15 a 20 minutes.
2. Faire parler les 4 membres.
3. Afficher le nom de chaque membre.
4. Heberger la video sur YouTube en Non repertorie ou mettre le MP4 dans le zip.
5. Remplacer le TXT placeholder par le vrai lien YouTube.
6. Refaire le zip final si le lien video est modifie.
7. Push final apres modification du lien video.

Optionnel si temps disponible :

- capture Wazuh Agents avec `serveur-01` actif ;
- capture alerte SSH Wazuh `5712` ;
- capture RBAC `analyste` / `supervision` ;
- vraie interface pfSense uniquement si une VM pfSense est disponible.

## 21. Reponse courte si le jury demande si l'architecture est trop simple

```text
Le MVP est volontairement reduit, mais l'architecture cible est industrialisable. On ne simule pas 30 centres complets ; on prouve une chaine SOC complete sur un perimetre maitrise : collecte multi-source, SIEM centralise, regles, alertes, dashboards, playbooks, preuves et documentation. Le passage a 30 centres repose sur des templates d'onboarding, des agents Wazuh, du syslog firewall et une organisation SOC standardisee.
```

## 22. Reponse courte sur les couts

```text
Le MVP limite les couts logiciels grace a Wazuh et aux outils open-source. En production, les couts principaux seraient l'infrastructure, le stockage des logs, l'exploitation SOC, la maintenance, la sauvegarde, la supervision du SIEM et le temps d'onboarding par centre.
```

## 23. Reponse courte sur Wazuh

```text
Wazuh est le coeur du SOC. Le Manager centralise et analyse les logs, l'Indexer stocke les evenements, et le Dashboard permet aux analystes de visualiser les alertes. Dans le MVP, on prouve la chaine avec des logs Daylight, firewall/syslog et des captures Wazuh live.
```

## 24. Reponse courte sur pfSense

```text
Dans le MVP, pfSense est represente par des logs firewall/syslog issus de `FW-S01` et `FW-S02`. La preuve SOC n'est pas l'interface pfSense, mais la reception, l'indexation et la detection de ces evenements dans Wazuh. Une VM pfSense reelle serait une evolution possible si l'environnement etait fourni.
```

## 25. Historique recent important

Dernieres grosses etapes realisees :

- remplacement du dashboard HTML de secours par de vraies captures Wazuh ;
- lancement de Wazuh 4.14.5 en Docker ;
- correction du decoder Wazuh firewall ;
- integration du travail Youssef : PDF SIEM, script `setup-siem-lab.ps1`, synthese Wazuh et script video ;
- reconstruction du zip final.

Pour connaitre le dernier commit :

```bash
git log -1 --oneline
```

Pour verifier que tout est pousse :

```bash
git status --short
git status --branch --short
```

## 26. Regle de prudence pour la suite

Ne pas inventer de preuve.

Ce qui est vrai :

- Wazuh live a ete lance ;
- Wazuh Dashboard a ete capture ;
- des alertes Daylight et firewall/syslog existent dans Wazuh ;
- pfSense n'a pas de vraie interface capturee ;
- `poste-01` et `serveur-01` sont documentes par Youssef, mais les captures live actuelles prioritaires sont surtout Wazuh central et alertes.

Si une nouvelle preuve est ajoutee, il faut :

1. mettre la capture dans `livrables/preuves/` ;
2. mettre a jour le rapport ou le README concerne ;
3. regenerer les PDF si necessaire ;
4. reconstruire le zip ;
5. verifier ;
6. commit/push.
