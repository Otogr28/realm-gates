---
hide:
  - toc
---

<div class="sb-banner" style="background-image:url('../../assets/mods/biomes-weve-gone-banner.webp')">
  <div class="sb-banner__inner">
    <p class="sb-eyebrow">The pack · search &amp; filter</p>
    <h1>Browse the mods</h1>
  </div>
</div>

Every gameplay mod in the pack, in one searchable grid. Type to find a mod by **name or what it
does**, or tap a chip to filter by **category** or **dimension**. Click any card to read a short,
friendly page about it.

<div class="sb-filter" data-mods-filter>
  <div class="sb-filter__search">
    <label class="sb-filter__searchlabel" for="mod-search">Search mods</label>
    <span class="sb-filter__searchicon" aria-hidden="true"></span>
    <input
      type="search"
      id="mod-search"
      class="sb-filter__input"
      placeholder="Search mods…"
      autocomplete="off"
      aria-controls="mod-browser-grid"
      data-mods-search>
  </div>

  <div class="sb-filter__row" role="group" aria-label="Filter by category">
    <span class="sb-filter__legend">Category</span>
    <button type="button" class="sb-chip is-active" data-facet="group" data-value="" aria-pressed="true">All</button>
    {% for key, title in group_facets() %}
    <button type="button" class="sb-chip" data-facet="group" data-value="{{ key }}" aria-pressed="false">{{ title }}</button>
    {% endfor %}
  </div>

  <div class="sb-filter__row" role="group" aria-label="Filter by dimension">
    <span class="sb-filter__legend">Dimension</span>
    <button type="button" class="sb-chip is-active" data-facet="tag" data-value="" aria-pressed="true">All</button>
    {% for slug, label in tag_facets() %}
    <button type="button" class="sb-chip sb-chip--{{ slug }}" data-facet="tag" data-value="{{ slug }}" aria-pressed="false">{{ label }}</button>
    {% endfor %}
  </div>

  <p class="sb-filter__count" data-mods-count aria-live="polite">
    Showing <strong data-shown>{{ mod_count() }}</strong> of <span data-total>{{ mod_count() }}</span> mods
  </p>
</div>

{{ mod_browser() }}

<div class="sb-empty" data-mods-empty hidden>
  <span class="sb-empty__glyph" aria-hidden="true"></span>
  <p class="sb-empty__title">No mods match your search</p>
  <p class="sb-empty__hint">Try a different word, or reset the filters above.</p>
  <button type="button" class="sb-chip sb-empty__reset" data-mods-reset>Reset filters</button>
</div>
