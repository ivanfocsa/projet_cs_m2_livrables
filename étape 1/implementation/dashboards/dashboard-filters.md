# Filtres concrets Wazuh Dashboard

## Supervision globale

```text
rule.groups:soc_audio
```

Visualisations :

- alertes par `rule.level`;
- alertes par `data.site`;
- alertes par `data.scenario`;
- top machines par `agent.name` ou `data.hostname`;
- timeline sur `timestamp`.

## Analyste SOC

```text
rule.id:(100100 or 100110 or 100120 or 100130 or 100140 or 100150 or 100160)
```

Colonnes utiles :

- `timestamp`;
- `rule.id`;
- `rule.description`;
- `data.site`;
- `data.hostname`;
- `data.user`;
- `data.src_ip`;
- `data.scenario`.

## Firewall pfSense

```text
data.hostname:(FW-S01 or FW-S02) or data.source:firewall
```

Alertes attendues :

- `100110` brute force acces distant ;
- `100160` scan reseau.

## Application metier

```text
data.hostname:(APP-S01-CRM or APP-S03-LOGS) or data.source:application
```

Alertes attendues :

- `100120` acces anormal dossier patient.

## Messagerie

```text
data.hostname:MAIL-S02 or data.source:mail
```

Alertes attendues :

- `100150` suspicion phishing.

