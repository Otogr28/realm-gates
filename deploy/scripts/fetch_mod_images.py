#!/usr/bin/env python3
"""Fetch official mod icons (+ a gallery image when available) from Modrinth.

Saves into docs/assets/mods/<key>.<ext> and <key>-banner.<ext>.
Run once locally:  python3 deploy/scripts/fetch_mod_images.py
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

UA = "realm-gates/1.0 (static modpack wiki; contact admin)"
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "assets", "mods")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

# key -> known Modrinth slug (preferred). If it 404s we fall back to search(key-as-name).
SLUGS = {
    "alexs-caves": "alexs-caves",
    "ars-nouveau": "ars-nouveau",
    "amendments": "amendments",
    "creeper-overhaul": "creeper-overhaul",
    "ice-and-fire": "ice-and-fire-dragons",
    "small-ships": "smallships",
    "supplementaries": "supplementaries",
    "corail-tombstone": "corail-tombstone",
    "travelers-backpack": "travelers-backpack",
    "waystones": "waystones",
    "zombie-awareness": "",            # search
    "biomes-weve-gone": "",            # search "oh the biomes we've gone"
    "yungs-better-end-island": "yungs-better-end-island",
    "yungs-better-nether-fortresses": "yungs-better-nether-fortresses",
    "yungs-better-strongholds": "yungs-better-strongholds",
    "carry-on": "carry-on",
    "clumps": "clumps",
    "controlling": "controlling",
    "curios": "curios",
    "easy-villagers": "easy-villagers",
    "epic-fight": "",                  # search (CurseForge mod; may miss)
    "entity-culling": "entityculling",
    "ferrite-core": "ferrite-core",
    "highlighter": "",                 # search
    "immediatelyfast": "immediatelyfast",
    "jade": "jade",
    "jei": "jei",
    "journeymap": "journeymap",
    "appleskin": "appleskin",
    "just-enough-resources": "just-enough-resources-jer",
    "just-enough-breeding": "just-enough-breeding",
    "vanilla-backport": "",            # search
    "enhanced-visuals": "",            # search
    "spawn-animations": "",            # search
    "fancymenu": "fancymenu",
    "simple-voice-chat": "simple-voice-chat",
    "no-chat-reports": "no-chat-reports",
}

# Friendly search terms for the ones without a known slug
SEARCH_TERMS = {
    "zombie-awareness": "zombie awareness",
    "biomes-weve-gone": "oh the biomes we've gone",
    "epic-fight": "epic fight",
    "highlighter": "highlighter",
    "vanilla-backport": "vanilla backport",
    "enhanced-visuals": "enhanced visuals",
    "spawn-animations": "spawn animations",
}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


def resolve(key):
    slug = SLUGS.get(key) or ""
    if slug:
        try:
            return get(f"https://api.modrinth.com/v2/project/{slug}")
        except Exception:
            pass
    term = SEARCH_TERMS.get(key, key.replace("-", " "))
    q = urllib.parse.quote(term)
    facets = urllib.parse.quote('[["project_type:mod"]]')
    res = get(f"https://api.modrinth.com/v2/search?query={q}&facets={facets}&limit=1")
    hits = res.get("hits", [])
    if not hits:
        return None
    return get(f"https://api.modrinth.com/v2/project/{hits[0]['project_id']}")


report = []
for key in SLUGS:
    try:
        p = resolve(key)
        if not p:
            report.append((key, "NO MATCH", "", ""))
            continue
        title = p.get("title", "?")
        icon = p.get("icon_url") or ""
        ext = os.path.splitext(urllib.parse.urlparse(icon).path)[1] or ".webp"
        if icon:
            download(icon, os.path.join(OUT, key + ext))
        banner = ""
        gal = p.get("gallery") or []
        feat = [g for g in gal if g.get("featured")] or gal
        if feat:
            burl = feat[0]["url"]
            bext = os.path.splitext(urllib.parse.urlparse(burl).path)[1] or ".webp"
            download(burl, os.path.join(OUT, key + "-banner" + bext))
            banner = key + "-banner" + bext
        report.append((key, title, key + ext if icon else "—", banner or "—"))
        time.sleep(0.2)
    except Exception as e:
        report.append((key, f"ERROR {e}", "", ""))

print(f"{'KEY':28} {'MATCHED TITLE':34} {'ICON':22} BANNER")
for k, t, i, b in report:
    print(f"{k:28} {t[:33]:34} {i:22} {b}")
