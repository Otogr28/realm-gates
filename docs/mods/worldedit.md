---
hide:
  - toc
---

<a class="mod-hero mod-hero--icon" href="https://modrinth.com/mod/worldedit" target="_blank" rel="noopener">
  <span class="mod-hero__art"><img src="../../assets/mods/worldedit.webp" alt="WorldEdit"></span>
  <span class="mod-hero__inner">
    <p class="sb-eyebrow">Unassigned · build tool</p>
    <h1>WorldEdit</h1>
    <span class="mod-hero__cta">Open the official mod page ↗</span>
  </span>
</a>
<p class="mod-hero-note">Click the image to open the official download &amp; documentation page.</p>

**WorldEdit** is the classic in-game map editor by EngineHub. It lets you select regions and reshape the world from chat — filling thousands of blocks at once, copying and pasting structures, generating spheres and cylinders, smoothing terrain, and undoing it all in a click. It doesn't add any blocks, items or mobs; it just manipulates the world that's already there.

!!! warning "It's a builder / admin tool"
    WorldEdit commands only work for **operators** (`/op`) or players with the right permissions. A normal player can't use it — it's meant for shaping the world, building arenas and editing maps, not for everyday survival play.

<p class="sb-eyebrow">The basics</p>

WorldEdit works on a **selection** — two corners defining a box you then operate on.

1. Type **`//wand`** to get the selection tool (a wooden axe).
2. **Left-click** a block for corner 1, **right-click** for corner 2.
3. Run a command on the box you just selected.

<p class="sb-eyebrow">The commands you'll use most</p>

<div class="md-typeset"><table>
<thead><tr><th>Command</th><th>What it does</th></tr></thead>
<tbody>
<tr><td><strong>//set &lt;block&gt;</strong></td><td>Fills the whole selection (use <code>//set air</code> to clear it out).</td></tr>
<tr><td><strong>//replace &lt;from&gt; &lt;to&gt;</strong></td><td>Swaps one block for another inside the selection.</td></tr>
<tr><td><strong>//walls &lt;block&gt;</strong></td><td>Builds just the four walls of the box.</td></tr>
<tr><td><strong>//copy / //paste</strong></td><td>Copy the selection and paste it elsewhere.</td></tr>
<tr><td><strong>//sphere / //cyl / //pyramid</strong></td><td>Generate geometric shapes (add <code>-h</code> for hollow).</td></tr>
<tr><td><strong>//smooth</strong></td><td>Erodes harsh steps to make natural-looking terrain.</td></tr>
<tr><td><strong>//undo / //redo</strong></td><td>Step back or forward through your edits (15 steps of history).</td></tr>
</tbody></table></div>

!!! tip "Brushes and schematics"
    **Brushes** (`//brush sphere ...`) let you sculpt terrain from a distance by pointing and clicking — great for mountains and caves. And you can save any copied build as a **schematic** (`//schem save`) to reuse it later.

[← Back to all mods](all-dimensions.md)
