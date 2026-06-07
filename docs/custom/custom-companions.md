# Custom Companions

!!! abstract "Custom mod — made for summerBuddies"
    A **personal companion** that fights alongside you, levels up, and grows into a build you
    design. Logistics (fetching items) is a handy bonus.

!!! warning "In development"
    Custom Companions is a work in progress built specifically for this server. Details below
    describe the design — some parts may not be live yet or may change. Ask the admin what's
    currently enabled.

## The idea

Each player gets **one personal companion**, created by talking to an NPC when you first join. You
choose its **class**, **look**, **size**, and **name** — even a custom skin. From there it's mainly
a **combat assistant**: it fights with you, gains levels from kills, and casts abilities you put
together yourself.

Everything about your companion lives **on the server**, so it's consistent and grief-safe — your
companion can't hurt other players or their companions.

## Classes

Pick one at creation. Classes are **light archetypes** — real power comes from the abilities you
build, so no class is overpowered.

| Class | Plays like | Notes |
| --- | --- | --- |
| **Warrior** | Frontline bruiser — gap-closes, taunts, body-blocks for you | Toughest; grounded |
| **Range** | Marksman — best single-target damage at range | Squishy; kites |
| **Summoner** | Conjurer — summons minions to tank and distract | Gentle hover |
| **Mage** | Battlemage — AoE, crowd control, and the **only owner-heal** | Squishiest; gentle hover |

## How it grows

- **Two separate XP pools.** Your companion earns its **own XP** from kills, which pays for
  *everything that grows* — stats, ability slots, unlocks. Your **normal (green-orb) XP** only pays
  for *using* the convenience features (like fetching items). Mnemonic: *unlocking* teleport costs
  companion XP; *using* it costs your XP.
- **Abilities you compose.** Abilities are built from **components** (damage, area-of-effect,
  projectile, status effect, knockback, heal, summon…). You assemble a main ability plus side
  abilities, balancing **cooldowns** and an **energy** pool.
- **AI modes.** Set it to **Passive** (never fights), **Defensive** (retaliates), or **Aggressive**
  (hunts nearby hostiles). You can also force a specific ability with a keybind.
- **Death & respawn.** If it falls, a respawn timer runs (shorter as it levels), then you pick a
  visible block for it to reappear on.

## Pictos & Luminas (the build layer)

On top of the active combat kit, companions have a **passive build system** inspired by
*Clair Obscur: Expedition 33*. Two pieces, explained simply:

- **Pictos** — equippable pieces (up to **3**) that give **stat bonuses + a special passive**.
  Think of them like build-defining badges. Rarer pictos are stronger.
- **Luminas** — the **passive part of a picto, learned permanently**. Keep a picto equipped and let
  your companion **deal damage** with it; once it's "learned," that passive becomes a **Lumina** you
  can equip *without* taking up a picto slot.
    - Equipping Luminas spends **Lumen**, a separate capacity budget that grows with your level.
    - The trade-off: a **Picto** gives stats *and* a passive but uses one of your 3 slots; a
      **Lumina** gives only the passive but costs Lumen — freeing a picto slot for stats.

You manage all of this in the **companion panel** (a themed arcane gold/black UI), opened from your
companion item.

## Logistics (bonus utility)

Point your companion at a chest to "remember" it, then ask it to **fetch or deposit** items even
from afar. Each fetch costs a little of **your** normal XP (more items = more XP). Low-level
companions walk; higher-level ones can **teleport** once that's unlocked. It also respects
**[Realm Gates](realmgates.md)** — it won't fetch from a dimension you can't reach.
