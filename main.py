"""
mkdocs-macros hooks for the Realm Gates wiki.

Single responsibility here: render mod cards/badges from data
(docs/_data/mods.yml) instead of hand-written HTML. That's what
fixes the "every card says AINCRAD" bug — the dimension pill is now
derived from each mod's `dimension:` field, and mods with no
dimension get a neutral "Unassigned" badge (never Aincrad).

Assign a mod to a realm by editing its `dimension:` in mods.yml.
"""

import html as _html

from markupsafe import Markup

# Map a dimension key -> (badge text, css variant, tag slug) using the data file.
# The `tag` is a stable filter slug for the browse page:
#   - an assigned dimension  -> its key (e.g. "aincrad", "all")
#   - no dimension assigned   -> "unassigned"
def _badge_for(data, mod):
    dim = mod.get("dimension")
    if dim:
        d = data["dimensions"].get(dim)
        if d:
            return d["badge"], d.get("variant", ""), dim
    # No realm assigned yet -> neutral badge, NOT Aincrad.
    u = data["unassigned"]
    return u["badge"], u.get("variant", "unassigned"), "unassigned"


def _media_classes(mod):
    """Extra classes on .mod-card__media (icon / empty placeholders)."""
    classes = ["mod-card__media"]
    m = mod.get("media")
    if m == "icon":
        classes.append("is-icon")
    elif m == "empty":
        classes.append("is-empty")
    return " ".join(classes)


def _tier_classes(variant):
    classes = ["mod-card__tier"]
    if variant:
        classes.append(f"mod-card__tier--{variant}")
    return " ".join(classes)


def define_env(env):
    data = env.variables.get("mods", {})

    def _card_html(mod, href, cta, img_base, external=False, show_tier=True,
                   group_key=None):
        """Build one .mod-card.

        `href` is the fully-resolved link. `img_base` is the relative prefix
        to the docs root for the artwork (e.g. "" on home, "../../" on the
        all-mods page). `show_tier=False` hides the dimension pill (used on the
        home showcase, where the pill would just be noise).

        When `group_key` is given the card also emits the data-attributes the
        browse page filters on (data-name / data-desc / data-group / data-tag).
        """
        media_cls = _media_classes(mod)
        tag = "unassigned"
        if show_tier:
            badge, variant, tag = _badge_for(data, mod)
            pill = f'<span class="{_tier_classes(variant)}">{badge}</span>'
        else:
            pill = ""

        # Filter hooks for the browse page (only emitted when a group is given).
        data_attrs = ""
        if group_key is not None:
            name = _html.escape(mod.get("name", "").lower(), quote=True)
            desc = _html.escape(mod.get("desc", "").lower(), quote=True)
            data_attrs = (
                f' data-name="{name}" data-desc="{desc}"'
                f' data-group="{group_key}" data-tag="{tag}"'
            )

        # Media: image, emoji glyph, or empty.
        if mod.get("img"):
            img = mod["img"]
            inner = (
                f"{pill}"
                f'<img src="{img_base}{img}" alt="{mod["name"]}" loading="lazy">'
            )
        elif mod.get("emoji"):
            # emoji placeholder: glyph first, pill after (matches old markup)
            inner = f'{mod["emoji"]}{pill}'
        else:
            inner = pill

        rel = ' target="_blank" rel="noopener"' if external else ""
        return (
            f'<a class="mod-card" href="{href}"{rel}{data_attrs}>'
            f'<span class="{media_cls}">{inner}</span>'
            f'<span class="mod-card__body">'
            f'<span class="mod-card__h">{mod["name"]}</span>'
            f'<span class="mod-card__p">{mod.get("desc", "")}</span>'
            f'<span class="mod-card__link">{cta}</span>'
            f"</span></a>"
        )

    @env.macro
    def mod_grid(group_key, href_base="../", img_base="../../", cta="Details →"):
        """Render the whole <div class="mod-grid"> for a named group.

        Defaults target the All-mods page (docs/mods/all-dimensions.md):
        mod pages live at docs/mods/<slug>/ -> "../<slug>/", and artwork at
        docs/assets/... -> "../../assets/...".
        """
        group = data["groups"].get(group_key, {})
        cards = "".join(
            _card_html(m, f'{href_base}{m["href"]}/', cta, img_base)
            for m in group.get("mods", [])
        )
        return Markup(f'<div class="mod-grid">{cards}</div>')

    @env.macro
    def group_title(group_key):
        return data["groups"].get(group_key, {}).get("title", "")

    @env.macro
    def mod_browser(href_base="../", img_base="../../", cta="Details →"):
        """Render EVERY mod (all groups) into one filterable .mod-grid.

        Each card carries data-name / data-desc / data-group / data-tag so the
        browse page's vanilla-JS filter can search + facet without touching the
        DOM blindly. Mirrors mod_grid's link/artwork resolution.
        """
        cards = []
        for group_key, group in data.get("groups", {}).items():
            for m in group.get("mods", []):
                cards.append(
                    _card_html(
                        m, f'{href_base}{m["href"]}/', cta, img_base,
                        group_key=group_key,
                    )
                )
        grid = "".join(cards)
        return Markup(f'<div class="mod-grid" id="mod-browser-grid">{grid}</div>')

    @env.macro
    def mod_count():
        """Total number of mods across all groups (for the live counter)."""
        return sum(len(g.get("mods", [])) for g in data.get("groups", {}).values())

    @env.macro
    def group_facets():
        """[(key, title)] for the category filter chips — in data order."""
        return [(k, g.get("title", k)) for k, g in data.get("groups", {}).items()]

    @env.macro
    def tag_facets():
        """[(slug, label)] for the dimension/tag filter chips.

        Only the dimensions actually used by at least one mod, plus the
        neutral "Unassigned" facet when any mod is unassigned. Keeps the
        chip row honest if the data changes.
        """
        used = set()
        has_unassigned = False
        for g in data.get("groups", {}).values():
            for m in g.get("mods", []):
                dim = m.get("dimension")
                if dim and dim in data.get("dimensions", {}):
                    used.add(dim)
                else:
                    has_unassigned = True
        facets = [
            (k, data["dimensions"][k]["badge"])
            for k in data.get("dimensions", {})
            if k in used
        ]
        if has_unassigned:
            facets.append(("unassigned", data["unassigned"]["badge"]))
        return facets

    @env.macro
    def home_teaser(img_base=""):
        """The 4-card teaser on the home page (links out to Modrinth).

        Home page is at the docs root, so artwork is "assets/..." (img_base="").
        """
        cards = "".join(
            _card_html(m, m["url"], "Mod page ↗", img_base,
                       external=True, show_tier=False)
            for m in data.get("home_teaser", [])
        )
        return Markup(f'<div class="mod-grid">{cards}</div>')
