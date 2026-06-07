"""
mkdocs-macros hooks for the Realm Gates wiki.

Single responsibility here: render mod cards/badges from data
(docs/_data/mods.yml) instead of hand-written HTML. That's what
fixes the "every card says AINCRAD" bug — the dimension pill is now
derived from each mod's `dimension:` field, and mods with no
dimension get a neutral "Unassigned" badge (never Aincrad).

Assign a mod to a realm by editing its `dimension:` in mods.yml.
"""

from markupsafe import Markup

# Map a dimension key -> (badge text, css variant) using the data file.
def _badge_for(data, mod):
    dim = mod.get("dimension")
    if dim:
        d = data["dimensions"].get(dim)
        if d:
            return d["badge"], d.get("variant", "")
    # No realm assigned yet -> neutral badge, NOT Aincrad.
    u = data["unassigned"]
    return u["badge"], u.get("variant", "unassigned")


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

    def _card_html(mod, href, cta, img_base, external=False, show_tier=True):
        """Build one .mod-card.

        `href` is the fully-resolved link. `img_base` is the relative prefix
        to the docs root for the artwork (e.g. "" on home, "../../" on the
        all-mods page). `show_tier=False` hides the dimension pill (used on the
        home showcase, where the pill would just be noise).
        """
        media_cls = _media_classes(mod)
        if show_tier:
            badge, variant = _badge_for(data, mod)
            pill = f'<span class="{_tier_classes(variant)}">{badge}</span>'
        else:
            pill = ""

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
            f'<a class="mod-card" href="{href}"{rel}>'
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
