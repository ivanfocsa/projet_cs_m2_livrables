# =====================================================================
#  setup-siem-lab.ps1  --  Perimetre Ingenieur SIEM (Youssef GUERNIOU)
# ---------------------------------------------------------------------
#  Integre le travail SIEM de Youssef dans le depot projet et reproduit
#  en UNE commande la partie Wazuh du lab SOC :
#    1. serveur-01  : conteneur Linux + agent Wazuh + SSH/rsyslog
#                     + fix auth.log + test brute force (alerte 5712)
#    2. RBAC        : utilisateurs supervision / analyste + role
#                     lecture seule "soc_readonly" + mapping
#    3. (optionnel) : logs Daylight via les scripts npm disponibles
#
#  PREREQUIS : Docker Desktop lance + lab Wazuh demarre
#              (stack Wazuh single-node active). A lancer depuis la racine
#              du projet. Les comptes ci-dessous sont reserves au lab.
#
#  USAGE :     powershell -ExecutionPolicy Bypass -File .\scripts\setup-siem-lab.ps1
# =====================================================================

$ErrorActionPreference = "Stop"
$serverContainer  = "serveur-01"
$indexerContainer = "single-node-wazuh.indexer-1"

function Write-Step($msg) { Write-Host "`n=== $msg ===" -ForegroundColor Cyan }
function Write-Skip($msg) { Write-Host "[SKIP] $msg" -ForegroundColor Yellow }

function Test-NpmScript($scriptName) {
    if (-not (Test-Path ".\package.json")) { return $false }

    try {
        $pkg = Get-Content ".\package.json" -Raw | ConvertFrom-Json
        return ($pkg.scripts.PSObject.Properties.Name -contains $scriptName)
    } catch {
        return $false
    }
}

function Invoke-NpmScriptIfPresent($scriptName) {
    if (-not (Test-NpmScript $scriptName)) {
        Write-Skip "npm script absent : $scriptName"
        return $false
    }

    if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
        Write-Skip "npm introuvable : $scriptName non execute"
        return $false
    }

    Write-Host "[*] npm run $scriptName" -ForegroundColor Green
    npm run $scriptName
    if ($LASTEXITCODE -ne 0) {
        throw "npm run $scriptName a echoue"
    }
    return $true
}

# ---------------------------------------------------------------------
# 0. Verification Docker
# ---------------------------------------------------------------------
try { docker info | Out-Null }
catch {
    Write-Host "[X] Docker ne repond pas. Lance Docker Desktop puis reessaie." -ForegroundColor Red
    exit 1
}

# ---------------------------------------------------------------------
# 1. serveur-01  (source 2 : serveur Linux simule)
# ---------------------------------------------------------------------
Write-Step "1/3  Serveur simule serveur-01"

$exists = docker ps -a --format '{{.Names}}' | Select-String -Pattern "^$serverContainer$"
if ($exists) {
    Write-Host "[*] $serverContainer existe deja -> demarrage." -ForegroundColor Yellow
    docker start $serverContainer | Out-Null
} else {
    Write-Host "[*] Creation du conteneur $serverContainer (Ubuntu 22.04)..." -ForegroundColor Green
    docker run -d --name $serverContainer --hostname $serverContainer ubuntu:22.04 sleep infinity | Out-Null
}

$serverBash = @'
#!/usr/bin/env bash
AGENT_VERSION="4.14.5-1"
DEB="wazuh-agent_${AGENT_VERSION}_amd64.deb"
MANAGER="host.docker.internal"
NAME="serveur-01"

echo "[*] Mise a jour des paquets..."
apt-get update -qq

echo "[*] Installation des prerequis de telechargement..."
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ca-certificates wget gnupg lsb-release

echo "[*] Telechargement de l'agent Wazuh ${AGENT_VERSION}..."
cd /tmp
wget -q "https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/${DEB}"

echo "[*] Installation de l'agent (manager=${MANAGER})..."
WAZUH_MANAGER="$MANAGER" WAZUH_AGENT_NAME="$NAME" dpkg -i "./${DEB}" || true

echo "[*] Resolution des dependances..."
apt-get -y -qq --fix-broken install
WAZUH_MANAGER="$MANAGER" WAZUH_AGENT_NAME="$NAME" dpkg --configure -a || true

echo "[*] Installation de SSH et rsyslog..."
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq openssh-server openssh-client rsyslog sshpass
mkdir -p /run/sshd

echo "[*] Ajout du suivi de /var/log/auth.log (si absent)..."
CONF="/var/ossec/etc/ossec.conf"
if ! grep -q "/var/log/auth.log" "$CONF"; then
  cp "$CONF" "${CONF}.bak.$(date +%s)"
  tmpconf="$(mktemp)"
  awk '
    /<\/ossec_config>/ && !done {
      print "  <localfile>";
      print "    <log_format>syslog</log_format>";
      print "    <location>/var/log/auth.log</location>";
      print "  </localfile>";
      done=1
    }
    { print }
  ' "$CONF" > "$tmpconf"
  cat "$tmpconf" > "$CONF"
  rm -f "$tmpconf"
  echo "    -> directive ajoutee."
else
  echo "    -> deja present."
fi

echo "[*] Demarrage des services..."
rsyslogd 2>/dev/null || true
service ssh start
/var/ossec/bin/wazuh-control restart
sleep 5

echo "[*] Simulation brute force SSH (15 tentatives)..."
for i in $(seq 1 15); do
  sshpass -p wrong ssh -o StrictHostKeyChecking=no -o ConnectTimeout=3 hacker@localhost true 2>/dev/null || true
done
NB=$(grep -c "Failed password" /var/log/auth.log 2>/dev/null || echo 0)
echo "[OK] $NB echecs d'authentification ecrits dans auth.log -> alerte Wazuh 5712 attendue."
'@

$serverBash = $serverBash -replace "`r`n", "`n"
$tmp1 = Join-Path $env:TEMP "setup-serveur-01.sh"
[IO.File]::WriteAllText($tmp1, $serverBash)
docker cp $tmp1 "${serverContainer}:/tmp/setup-serveur-01.sh" | Out-Null
docker exec $serverContainer bash /tmp/setup-serveur-01.sh

# ---------------------------------------------------------------------
# 2. RBAC  (vues supervision / analyste / admin)
# ---------------------------------------------------------------------
Write-Step "2/3  RBAC : utilisateurs + role lecture seule"

$indexerRunning = docker ps --format '{{.Names}}' | Select-String -Pattern "^$indexerContainer$"
if (-not $indexerRunning) {
    Write-Host "[X] Conteneur $indexerContainer introuvable ou arrete. Demarre d'abord la stack Wazuh single-node." -ForegroundColor Red
    exit 1
}

$rbacBash = @'
#!/usr/bin/env bash
IDX="https://localhost:9200"
AUTH="admin:SecretPassword"

echo "[*] Utilisateur supervision..."
curl -k -s -u "$AUTH" -X PUT "$IDX/_plugins/_security/api/internalusers/supervision" \
  -H 'Content-Type: application/json' \
  -d '{"password":"Supervision2026!SOC"}'; echo

echo "[*] Utilisateur analyste..."
curl -k -s -u "$AUTH" -X PUT "$IDX/_plugins/_security/api/internalusers/analyste" \
  -H 'Content-Type: application/json' \
  -d '{"password":"Analyste2026!SOC"}'; echo

echo "[*] Role lecture seule soc_readonly..."
curl -k -s -u "$AUTH" -X PUT "$IDX/_plugins/_security/api/roles/soc_readonly" \
  -H 'Content-Type: application/json' \
  -d '{"cluster_permissions":["cluster_composite_ops_ro","cluster_monitor"],"index_permissions":[{"index_patterns":["wazuh-*"],"allowed_actions":["read","indices_monitor"]},{"index_patterns":[".kibana*"],"allowed_actions":["read"]}],"tenant_permissions":[{"tenant_patterns":["global_tenant"],"allowed_actions":["kibana_all_read"]}]}'; echo

echo "[*] Mapping supervision + analyste -> soc_readonly..."
curl -k -s -u "$AUTH" -X PUT "$IDX/_plugins/_security/api/rolesmapping/soc_readonly" \
  -H 'Content-Type: application/json' \
  -d '{"users":["analyste","supervision"]}'; echo

echo "[OK] RBAC configure : admin (complet) / analyste + supervision (lecture seule)."
'@

$rbacBash = $rbacBash -replace "`r`n", "`n"
$tmp2 = Join-Path $env:TEMP "setup-rbac.sh"
[IO.File]::WriteAllText($tmp2, $rbacBash)
docker cp $tmp2 "${indexerContainer}:/tmp/setup-rbac.sh" | Out-Null
docker exec $indexerContainer bash /tmp/setup-rbac.sh

# ---------------------------------------------------------------------
# 3. (optionnel) Source applicative Daylight via les scripts npm
# ---------------------------------------------------------------------
Write-Step "3/3  Source applicative Daylight (optionnel)"
if (Test-Path ".\package.json") {
    try {
        Invoke-NpmScriptIfPresent "generate:logs" | Out-Null
        Invoke-NpmScriptIfPresent "prepare:preuves" | Out-Null

        $deployed = Invoke-NpmScriptIfPresent "lab:deploy-daylight"
        if ($deployed) {
            Start-Sleep -Seconds 45
        }
        Invoke-NpmScriptIfPresent "lab:replay-daylight" | Out-Null

        Write-Host "[OK] Etape Daylight terminee selon les scripts disponibles dans ce depot." -ForegroundColor Green
    } catch {
        Write-Host "[!] Etape Daylight non bloquante : $($_.Exception.Message)" -ForegroundColor Yellow
    }
} else {
    Write-Host "[!] package.json introuvable : lance ce script depuis la racine du projet pour l'etape Daylight." -ForegroundColor Yellow
}

# ---------------------------------------------------------------------
Write-Host "`n=== TERMINE ===" -ForegroundColor Cyan
Write-Host "Dashboard : https://localhost   (admin / SecretPassword)" -ForegroundColor Cyan
Write-Host "Comptes RBAC : analyste / Analyste2026!SOC   -   supervision / Supervision2026!SOC" -ForegroundColor Cyan
Write-Host "Verifie : Agents (poste-01, serveur-01 Active) + alertes 5712 et alertes Daylight 100100-100160 si rejouees." -ForegroundColor Cyan
