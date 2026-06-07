# Restricted area (example)

!!! danger "This page is an example of *blocked content*"
    Anything placed under the **`private/`** folder is served by the web server **behind a
    password** (HTTP Basic Auth). Public visitors get a login prompt; only people with the
    credentials can read it.

    This page is intentionally **not** linked in the main navigation. Use this area for content you
    want online but not public — event spoilers, build-team notes, draft guides, etc.

## How to use it (admin)

1. Put any `.md` page inside `docs/private/`.
2. The deployment's web server (Caddy) requires a username + password for the `/private/` path.
3. Share the credentials only with the people who should see it.

## Why not just "hide" a page?

Leaving a page unlinked is **not** security — anyone who guesses the URL can open it. The
password on `/private/` is what actually blocks it. For content that should never be public at
all, simply **don't publish it** (keep it out of the built site).

*(Replace this placeholder with real restricted content whenever you need it.)*
