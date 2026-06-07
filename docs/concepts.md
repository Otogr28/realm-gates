<div class="sb-banner" style="background-image:linear-gradient(125deg,#1a2a6b 0%,#0a1330 55%,#0a1736 100%)">
  <div class="sb-banner__inner">
    <p class="sb-eyebrow">The basics</p>
    <h1>Concepts explained</h1>
  </div>
</div>

A plain-language glossary of the things you'll run into in Realm Gates. No jargon — just "what
is this and why do I care?"

---

## Forge

The mod loader. Realm Gates runs on **Minecraft Forge 1.20.1**. Your launcher needs a Forge
1.20.1 instance before any mod will load. See [Install the modpack](getting-started/install.md).

## Mods, configs, and the modpack

- A **mod** is a `.jar` file that adds or changes something in the game.
- A **config** tells a mod how to behave (numbers, toggles).
- The **modpack** is just the agreed-upon set of mods + configs that everyone on the server uses,
  so we all play the same game. You keep yours in sync by [updating](getting-started/updating.md).

## Client-side vs. server-side mods

- **Server-side** mods run on the server (world generation, monsters, rules).
- **Client-side** mods run on your computer (menus, visuals, maps).
- Most mods are **both**. A few are **client-only** — they'd crash the server, so the server
  filters those out automatically, but you still keep them in your `mods/` folder. You don't have
  to think about this; the [update process](getting-started/updating.md) handles it.

## Online vs. offline mode

This server currently runs in **offline mode** so friends without a premium Minecraft account can
join the beta. Practically, that means access is controlled by the **whitelist** (by player name),
so your in-game name matters — log in with the **exact** name the admin added. More on
[Server info](server-info.md).

## Whitelist

A list of who is allowed on the server. If you're not on it, you can't join — ask the admin to add
your **exact** in-game name. See [Server info](server-info.md).

---

## Things you'll see in-game

### Waystones (fast travel)

Stone blocks you **activate** by clicking them. Once activated, a waystone joins your travel list
so you can teleport between any waystones you've discovered. They spawn in villages and out in the
world, which makes the huge modded map manageable. *(Mod: [Waystones](mods/dimension-1.md).)*

### Curios (extra equipment slots)

Some items aren't armor or held tools — they're **charms, rings, belts, backpacks** and the like.
**Curios** adds dedicated slots for them, opened with a key in your inventory screen. It's a shared
system many mods plug into.

### Jade (the tooltip overlay)

Look at a block or creature and a small panel appears showing **what it is**, its health, the tool
needed to mine it, and more. Great for learning a modded world quickly. *(See
[Dimension 1](mods/dimension-1.md).)*

### JEI — Just Enough Items (recipe lookup)

A searchable list of **every item and recipe**. Click an item to see how to craft it, or what it
crafts into. Your first stop whenever you wonder "how do I make this?" *(See
[Dimension 1](mods/dimension-1.md).)*

### JourneyMap (the map)

A live **minimap** and full-screen map. Mark waypoints, see explored terrain, and find your way
back home. *(See [Dimension 1](mods/dimension-1.md).)*

### Voice subtitles (Voice Translate)

The floating text above a speaker's head is **Voice Translate**, translating their voice into your
chosen language in real time. Set it up in [Voice & chat translation](getting-started/voice-and-chat.md).

### Realm Gates (dimensions & progression)

A custom system that decides **which dimensions you can travel to and when**. On this server you
spawn in a custom overworld and unlock further realms as you progress. See
[Realm Gates](custom/realmgates.md).

### Performance mods (FPS helpers)

Some mods add **no content** — they just make the game run smoother (less memory, faster rendering,
fewer hiccups). You'll never "use" them directly; they work in the background. *(See
[Dimension 1](mods/dimension-1.md).)*

---

## Dimensions & the mod tags

The pack is organized by **dimension** — the realms you travel between (see
[Dimensions](mods/index.md)). On each mod card you'll see one of two tags:

- **Dimension 1** (and later Dimension 2, 3…) — content that belongs to that specific realm: its
  biomes, creatures, structures and caves.
- **All dimensions** — universal mods that work everywhere and follow you between realms: the UI,
  performance, combat, social and gear systems.

Right now only **Dimension 1** (a familiar overworld) is open, so all current content lives there.
New realms unlock over time through **[Realm Gates](custom/realmgates.md)**.
