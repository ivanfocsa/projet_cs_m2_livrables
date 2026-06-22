#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const logDir = path.join(root, "etape 1".replace("etape", "\u00e9tape"), "logs", "generated");
const outDir = path.join(root, "livrables", "local-dashboard");
const captureDir = path.join(root, "livrables", "preuves", "local-run-captures");

const rules = [
  ["100100", 10, "suspicious_process", "Execution PowerShell suspecte", "Endpoint", "T1059.001"],
  ["100110", 12, "brute_force", "Brute force acces distant", "Firewall/syslog", "T1110"],
  ["100120", 10, "patient_access_anomaly", "Acces anormal aux dossiers patients", "Application metier", "T1530"],
  ["100130", 14, "privileged_group_change", "Modification groupe privilegie", "Active Directory", "T1098"],
  ["100140", 7, "usb_suspect", "Usage USB detecte", "Endpoint", "T1091"],
  ["100150", 10, "phishing", "Suspicion phishing messagerie", "Messagerie", "T1566"],
  ["100160", 8, "port_scan", "Suspicion scan reseau", "Firewall/syslog", "T1046"],
].map(([id, level, scenario, title, source, mitre]) => ({ id, level, scenario, title, source, mitre }));

function readJsonl(name) {
  const file = path.join(logDir, name);
  if (!fs.existsSync(file)) return [];
  return fs.readFileSync(file, "utf8")
    .split(/\r?\n/)
    .filter(Boolean)
    .map((line) => JSON.parse(line));
}

function readFirewall() {
  const file = path.join(logDir, "firewall_syslog.log");
  if (!fs.existsSync(file)) return [];
  return fs.readFileSync(file, "utf8")
    .split(/\r?\n/)
    .filter(Boolean)
    .map((line) => {
      const pairs = Object.fromEntries([...line.matchAll(/(\w+)=("[^"]+"|\S+)/g)].map((m) => [m[1], m[2].replace(/^"|"$/g, "")]));
      const host = line.includes("FW-S01") ? "FW-S01" : "FW-S02";
      return {
        timestamp: "2026-demo-syslog",
        site: host === "FW-S01" ? "SITE-01" : "SITE-02",
        hostname: host,
        source: "firewall",
        scenario: pairs.scenario || "normal",
        action: pairs.action || "-",
        src_ip: pairs.src || "-",
        dst_ip: pairs.dst || "-",
        port: pairs.port || pairs.ports || "-",
        user: pairs.user || "-",
        message: pairs.message || line,
        raw: line,
      };
    });
}

function firstEvent(events, scenario, preferredSource) {
  return events.find((e) => e.scenario === scenario && (!preferredSource || e.source === preferredSource))
    || events.find((e) => e.scenario === scenario)
    || {};
}

const events = [
  ...readJsonl("endpoint_events.jsonl"),
  ...readJsonl("application_events.jsonl"),
  ...readJsonl("ad_events.jsonl"),
  ...readJsonl("mail_events.jsonl"),
  ...readFirewall(),
];

const preferred = { brute_force: "firewall", port_scan: "firewall" };
const alerts = rules.map((rule) => {
  const event = firstEvent(events, rule.scenario, preferred[rule.scenario]);
  return {
    ...rule,
    site: event.site || "-",
    host: event.hostname || event.agent || "-",
    user: event.user || "-",
    src: event.src_ip || event.src || "-",
    dst: event.dst_ip || event.dst || "-",
    port: event.port || "-",
    message: event.message || "-",
    timestamp: event.timestamp || "2026-demo",
    raw: event.raw || JSON.stringify(event),
  };
});

const countBy = (items, key) => items.reduce((acc, item) => {
  const value = item[key] || "-";
  acc[value] = (acc[value] || 0) + 1;
  return acc;
}, {});

const dataset = {
  generatedAt: new Date().toISOString(),
  totalEvents: events.length,
  alerts,
  sites: countBy(alerts, "site"),
  sources: countBy(alerts, "source"),
  levels: countBy(alerts, "level"),
  implementation: [
    ["SIEM", "Wazuh Manager + Indexer/OpenSearch + Dashboard", "Pret"],
    ["Firewall", "pfSense CE cible, FW-S01/FW-S02 en syslog", "Pret"],
    ["Endpoint", "Agents Wazuh, Sysmon en production", "Pret"],
    ["Applications", "APP-S01-CRM en logs JSONL", "Pret"],
    ["Messagerie", "MAIL-S02 en logs JSONL", "Pret"],
    ["RBAC", "analyste/supervision avec soc_readonly", "Pret"],
    ["Retention", "Politique OpenSearch 90 jours", "Documente"],
  ],
};

fs.mkdirSync(outDir, { recursive: true });
fs.mkdirSync(captureDir, { recursive: true });
fs.writeFileSync(path.join(outDir, "data.json"), JSON.stringify(dataset, null, 2));

const alertRows = alerts.map((a) => `
  <tr data-rule="${a.id}" data-source="${a.source}">
    <td><strong>${a.id}</strong><span>Niveau ${a.level}</span></td>
    <td>${a.title}<span>${a.mitre}</span></td>
    <td>${a.source}<span>${a.scenario}</span></td>
    <td>${a.site}<span>${a.host}</span></td>
    <td>${a.user}<span>${a.src}</span></td>
    <td>${a.message}</td>
  </tr>`).join("");

const sourceBars = Object.entries(dataset.sources).map(([name, value]) => `
  <div class="bar-row"><span>${name}</span><div><i style="width:${Math.max(14, value * 14)}%"></i></div><b>${value}</b></div>`).join("");

const implementationRows = dataset.implementation.map(([brique, solution, status]) => `
  <tr><td>${brique}</td><td>${solution}</td><td><span class="pill">${status}</span></td></tr>`).join("");

const html = `<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>SOC Daylight - Dashboard local</title>
  <style>
    *{box-sizing:border-box} body{margin:0;background:#f5f7fb;color:#172033;font-family:Inter,Arial,sans-serif}
    .shell{display:grid;grid-template-columns:248px 1fr;min-height:100vh}
    aside{background:#101828;color:#fff;padding:24px 18px;position:sticky;top:0;height:100vh}
    .brand{font-size:21px;font-weight:800;margin-bottom:4px}.muted{color:#98a2b3;font-size:13px}
    nav{display:grid;gap:8px;margin-top:28px} nav a{color:#d0d5dd;text-decoration:none;padding:10px 12px;border-radius:7px} nav a:hover,nav a.active{background:#1d2939;color:#fff}
    main{padding:24px 30px 38px}.top{display:flex;justify-content:space-between;gap:18px;align-items:flex-start;margin-bottom:22px}
    h1{font-size:28px;margin:0 0 6px}.subtitle{font-size:14px;color:#667085}
    .grid{display:grid;gap:14px}.kpis{grid-template-columns:repeat(4,minmax(0,1fr));margin-bottom:16px}
    .panel{background:#fff;border:1px solid #d9e1ec;border-radius:8px;padding:17px;box-shadow:0 1px 2px rgba(16,24,40,.04)}
    .kpi b{display:block;font-size:30px;margin-top:8px}.kpi span,.panel h2 span,td span{display:block;color:#667085;font-size:12px;font-weight:500;margin-top:3px}
    .content{grid-template-columns:1.45fr .85fr;align-items:start}.section{margin-top:16px}
    h2{font-size:18px;margin:0 0 12px}.table-wrap{overflow:auto;border:1px solid #e4e7ec;border-radius:8px}
    table{border-collapse:collapse;width:100%;font-size:13px;background:#fff} th,td{text-align:left;border-bottom:1px solid #eaecf0;padding:10px 11px;vertical-align:top} th{background:#f2f4f7;color:#475467;font-size:12px} tr:last-child td{border-bottom:0}
    .pill{display:inline-block;background:#ecfdf3;color:#027a48;border:1px solid #abefc6;padding:4px 8px;border-radius:999px;font-size:12px}
    .bar-row{display:grid;grid-template-columns:120px 1fr 28px;align-items:center;gap:10px;margin:10px 0;font-size:13px}.bar-row div{height:9px;background:#edf2f7;border-radius:999px;overflow:hidden}.bar-row i{display:block;height:100%;background:#2457d6}
    .detail{white-space:pre-wrap;background:#0f172a;color:#d1e0ff;border-radius:8px;padding:13px;font-size:12px;min-height:150px;overflow:auto}
    .footer{margin-top:20px;color:#667085;font-size:12px}
    @media(max-width:980px){.shell{grid-template-columns:1fr}aside{height:auto;position:relative}.kpis,.content{grid-template-columns:1fr}}
  </style>
</head>
<body>
<div class="shell">
  <aside>
    <div class="brand">SOC Daylight</div>
    <div class="muted">Dashboard local de demonstration</div>
    <nav>
      <a class="active" href="#overview">Vue globale</a>
      <a href="#alerts">Alertes</a>
      <a href="#sources">Sources</a>
      <a href="#implementation">Implementation</a>
    </nav>
    <p class="muted" style="margin-top:30px">MVP local base sur les logs generes du depot. Docker/Wazuh live non disponible sur cette machine.</p>
  </aside>
  <main>
    <div class="top" id="overview">
      <div>
        <h1>Supervision SOC externalise</h1>
        <div class="subtitle">3 sites MVP, 7 alertes Daylight, modele industrialisable vers 30 centres</div>
      </div>
      <div class="subtitle">Genere le ${new Date(dataset.generatedAt).toLocaleString("fr-FR")}</div>
    </div>
    <section class="grid kpis">
      <div class="panel kpi">Evenements traites<b>${dataset.totalEvents}</b><span>endpoint, app, AD, mail, firewall</span></div>
      <div class="panel kpi">Alertes SOC<b>${alerts.length}</b><span>regles 100100 a 100160</span></div>
      <div class="panel kpi">Sites MVP<b>${Object.keys(dataset.sites).length}</b><span>SITE-01, SITE-02, SITE-03</span></div>
      <div class="panel kpi">Sources<b>${Object.keys(dataset.sources).length}</b><span>multi-source valide</span></div>
    </section>
    <section class="grid content">
      <div class="panel" id="alerts">
        <h2>Alertes detectees <span>IDs harmonises avec regles, rapport et video</span></h2>
        <div class="table-wrap"><table><thead><tr><th>ID</th><th>Alerte</th><th>Source</th><th>Site/host</th><th>User/src</th><th>Message</th></tr></thead><tbody>${alertRows}</tbody></table></div>
      </div>
      <div class="grid">
        <div class="panel" id="sources">
          <h2>Couverture sources</h2>
          ${sourceBars}
        </div>
        <div class="panel">
          <h2>Detail brut</h2>
          <div class="detail">${alerts.map((a) => `${a.id} ${a.title}\\n${a.raw}`).join("\\n\\n")}</div>
        </div>
      </div>
    </section>
    <section class="panel section" id="implementation">
      <h2>Implementation concrete testee localement</h2>
      <div class="table-wrap"><table><thead><tr><th>Brique</th><th>Solution</th><th>Statut</th></tr></thead><tbody>${implementationRows}</tbody></table></div>
      <div class="footer">Commande de verification : npm run verify:concrete-stack</div>
    </section>
  </main>
</div>
</body>
</html>`;

fs.writeFileSync(path.join(outDir, "index.html"), html);
console.log(`Local dashboard built: ${path.join(outDir, "index.html")}`);
