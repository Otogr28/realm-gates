# summerBuddies Wiki

Player-facing documentation for the **summerBuddies** Minecraft modpack (Forge 1.20.1), built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Navy + gold theme. Static site —
no database, no login panel, minimal attack surface.

🌐 **Live:** <https://otogr28.github.io/summerBuddies-wiki/> — hosted free on **GitHub Pages**.
Every push to `master` rebuilds and redeploys automatically (`.github/workflows/deploy.yml`).

> ⚠️ **This site is (will be) public. Never put server secrets here** — no IPs, no admin/infra
> details, no tokens. Player-facing content only. Those secrets live elsewhere and stay there.

## Edit & preview locally

The whole wiki is Markdown under `docs/`. To preview with live-reload:

```bash
# Option 1 — Python venv
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
mkdocs serve            # open http://127.0.0.1:8000

# Option 2 — Docker (no Python install)
docker run --rm -it -p 8000:8000 -v "$PWD":/docs squidfunk/mkdocs-material
```

Build the static site into `site/`:

```bash
mkdocs build --strict
# or: docker run --rm -v "$PWD":/docs squidfunk/mkdocs-material build --strict
```

## Structure

```
mkdocs.yml                 # config, nav, theme
docs/
  index.md                 # home
  getting-started/         # install, voice & chat, updating
  concepts.md              # plain-language glossary ("explain it simply")
  mods/                    # mods grouped by 0–10 progression tier
  custom/                  # Realm Gates, Custom Companions, Voice Translate
  server-info.md           # rules, whitelist, etiquette (NO secrets)
  private/                 # example BLOCKED content (password-gated at the web server)
  stylesheets/extra.css    # navy + gold theme
deploy/                    # ready-to-use VPS hosting (Caddy + Cloudflare) — see deploy/README.md
```

## Blocking / gating content

- **Password-protect a section:** put pages under `docs/private/` (or any path you choose). The
  deployment's web server (Caddy) requires HTTP Basic Auth for `/private/`. See `deploy/`.
- **Keep a page fully private:** just don't add it to the build / nav. Unlinked ≠ secure, but
  *unbuilt* never reaches the public site.

## Deploying

**GitHub Pages (current).** A push to `master` triggers `.github/workflows/deploy.yml`, which runs
`mkdocs build --strict` and publishes to Pages. To update the site: edit Markdown, commit, push.
That's it.

> ⚠️ **No password-gating on GitHub Pages.** Pages is static hosting with no server-side auth, so
> the `docs/private/` section **cannot** be protected there — it is excluded from the published
> build (`exclude_docs` in `mkdocs.yml`). To keep something private, just don't publish it. If you
> ever need real per-section passwords, use the self-hosted option below.

**VPS + Cloudflare (optional self-host).** A ready alternative behind **Cloudflare (free plan)**:
Caddy serves the files with `basic_auth` on `/private/`, port 443 firewalled to Cloudflare IPs, plus
DDoS/WAF/TLS. See [`deploy/README.md`](deploy/README.md). Nothing in `deploy/` runs unless you set it up.
