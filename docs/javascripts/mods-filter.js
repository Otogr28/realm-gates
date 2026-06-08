/* ============================================================
 * Realm Gates — live search + faceted filter for the Mods page.
 * Vanilla JS, no deps. Filters .mod-card elements by:
 *   - free text   -> matches data-name / data-desc
 *   - category    -> data-group  (single-select toggle, "" = All)
 *   - dimension   -> data-tag    (single-select toggle, "" = All)
 * Re-binds on every page render so it survives Material's
 * instant-loading (SPA) navigation.
 * ============================================================ */
(function () {
  "use strict";

  function initModsFilter() {
    var root = document.querySelector("[data-mods-filter]");
    var grid = document.getElementById("mod-browser-grid");
    if (!root || !grid) return; // not the browse page

    // Guard against double-binding if init runs twice for the same DOM.
    if (root.dataset.bound === "1") return;
    root.dataset.bound = "1";

    var search = root.querySelector("[data-mods-search]");
    var chips = Array.prototype.slice.call(root.querySelectorAll(".sb-chip[data-facet]"));
    var shownEl = root.querySelector("[data-shown]");
    var countWrap = root.querySelector("[data-mods-count]");
    var cards = Array.prototype.slice.call(grid.querySelectorAll(".mod-card"));
    var empty = document.querySelector("[data-mods-empty]");
    var resetBtn = empty ? empty.querySelector("[data-mods-reset]") : null;

    // Active single-select value per facet ("" = no filter / All).
    var active = { group: "", tag: "" };

    function setChip(chip, on) {
      chip.classList.toggle("is-active", on);
      chip.setAttribute("aria-pressed", on ? "true" : "false");
    }

    function apply() {
      var q = (search.value || "").trim().toLowerCase();
      var shown = 0;

      cards.forEach(function (card) {
        var matchesText =
          !q ||
          (card.dataset.name || "").indexOf(q) !== -1 ||
          (card.dataset.desc || "").indexOf(q) !== -1;
        var matchesGroup = !active.group || card.dataset.group === active.group;
        var matchesTag = !active.tag || card.dataset.tag === active.tag;

        var visible = matchesText && matchesGroup && matchesTag;
        card.hidden = !visible;
        if (visible) shown++;
      });

      if (shownEl) shownEl.textContent = String(shown);
      if (countWrap) countWrap.hidden = false;
      if (empty) empty.hidden = shown !== 0;
    }

    function onChip(chip) {
      var facet = chip.dataset.facet; // "group" | "tag"
      var value = chip.dataset.value; // "" | slug

      // Toggle: clicking the active value (other than All) clears back to All.
      if (value && active[facet] === value) {
        active[facet] = "";
      } else {
        active[facet] = value;
      }

      // Reflect state on the chip row for this facet.
      chips
        .filter(function (c) { return c.dataset.facet === facet; })
        .forEach(function (c) {
          var isAll = c.dataset.value === "";
          var on = active[facet] === "" ? isAll : c.dataset.value === active[facet];
          setChip(c, on);
        });

      apply();
    }

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () { onChip(chip); });
    });

    search.addEventListener("input", apply);

    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        search.value = "";
        active.group = "";
        active.tag = "";
        chips.forEach(function (c) { setChip(c, c.dataset.value === ""); });
        apply();
        search.focus();
      });
    }

    apply();
  }

  // Material for MkDocs exposes the RxJS `document$` observable when instant
  // loading is on; it fires on every page swap. Use it so the filter re-binds
  // after SPA navigation. Fall back to DOMContentLoaded otherwise.
  if (typeof window.document$ !== "undefined" && window.document$.subscribe) {
    window.document$.subscribe(function () { initModsFilter(); });
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initModsFilter);
  } else {
    initModsFilter();
  }
})();
