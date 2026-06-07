# Deploying the wiki (VPS + Cloudflare)

> Nothing here runs until you choose to set it up. It's the ready-to-use hosting recipe: a static
> site served by **Caddy** on the VPS, behind **Cloudflare's free plan** for DDoS/WAF/TLS, with
> port 443 firewalled to Cloudflare only.

```
Player ─► Cloudflare (DDoS, WAF, Bot Fight, TLS, hides your VPS IP)
                  │  SSL = Full (strict), Cloudflare Origin cert
                  ▼
        VPS  ufw allow 443 ONLY from Cloudflare IP ranges   (mc-cf-ufw)
                  ▼
        Caddy (Docker)  ──serves──►  /opt/wiki-site (static HTML)
                  ▲
        mc-wiki  ── git pull + docker mkdocs-material build ──┘
```

## Why this is "anti-attack"

- **Cloudflare proxy** absorbs DDoS, runs a managed WAF + Bot Fight Mode, and **hides your real
  VPS IP** so attackers can't target the origin directly.
- **Firewall lock** (`mc-cf-ufw`): only Cloudflare's published IP ranges may reach port 443, so even
  if someone learns the IP, direct hits are dropped.
- **Static site**: no database, no server-side code, no login panel → almost nothing to exploit.
- **Security headers + HTTPS** enforced end to end (Cloudflare → Origin cert on Caddy).

## One-time setup

### 1. Domain on Cloudflare (free)

1. Buy a domain (~$12/yr) at any registrar.
2. Add it to Cloudflare (free plan) and switch the registrar's nameservers to Cloudflare's.
3. DNS: add an `A` record `wiki → <VPS public IP>`, **Proxied (orange cloud)**.
4. SSL/TLS → **Full (strict)**. Create an **Origin Certificate** (15-year); save the cert and key.
5. Turn on **Always Use HTTPS**, **Bot Fight Mode**, and the default **Managed WAF** ruleset.

### 2. VPS — files

```bash
sudo mkdir -p /opt/wiki /opt/wiki-site
# clone the wiki repo somewhere stable:
sudo git clone https://github.com/<you>/realm-gates /opt/realm-gates

# copy this folder's compose + Caddyfile into /opt/wiki:
sudo cp deploy/docker-compose.yml deploy/Caddyfile /opt/wiki/
# drop the Cloudflare Origin cert/key here (chmod 600):
sudo install -m600 cf-origin.pem /opt/wiki/cf-origin.pem
sudo install -m600 cf-origin.key /opt/wiki/cf-origin.key
```

Edit `/opt/wiki/Caddyfile`: set your real domain, and a real `basic_auth` hash for `/private/`:

```bash
docker run --rm caddy caddy hash-password --plaintext 'YOUR-PRIVATE-PASSWORD'
# paste the resulting $2a$... hash into the Caddyfile
```

### 3. VPS — helpers

```bash
sudo install -m755 deploy/scripts/mc-wiki   /usr/local/bin/mc-wiki
sudo install -m755 deploy/scripts/mc-cf-ufw /usr/local/bin/mc-cf-ufw
```

### 4. Build + go live

```bash
sudo mc-wiki                       # build the static site into /opt/wiki-site
cd /opt/wiki && sudo docker compose up -d   # start Caddy on 443
sudo mc-cf-ufw                     # lock 443 to Cloudflare IPs
```

## Updating content later

Edit Markdown on your laptop → `git push` → on the VPS run **`mc-wiki`** (git pull + rebuild). No
Caddy restart needed (static files). Consider a weekly cron for `mc-cf-ufw` to refresh Cloudflare's
ranges.

## Blocked content

Pages under `docs/private/` are served behind the Caddyfile's `basic_auth` on the `/private/` path
— public visitors get a login prompt. See `docs/private/index.md` in the repo for the convention.

---

> ⚠️ Keep this wiki **public-safe**: no VPS IP, no Tailscale/Crafty/admin details, no tokens in any
> committed page. The firewall + Cloudflare protect the *server*; keeping secrets out protects *you*.
