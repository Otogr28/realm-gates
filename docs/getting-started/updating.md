# Updating the modpack

When the admin says there's a new version, you update so your game matches the server. How you do
it depends on how you installed:

- **Option A (script):** double-click **`sync.bat`** in your modpack folder.
- **Option B (ZIP):** download the ZIP again and re-copy `mods` and `config`.
- **Option C (Git):** fetch + merge (or run `git pull`), then re-copy `mods` and `config`.

---

## What gets reset vs. what is kept

Updating **resets the shared modpack files** to the server's version, so the whole group stays in
sync. This means:

!!! warning "Don't hand-edit the shared files"
    Don't manually change files in the modpack folder — an update will overwrite them with the
    server's version.

**Your own settings are kept across every update:**

- Your **worlds / saves** and **screenshots**.
- `options.txt` — your **keybinds** and **video settings**.
- Per-player `*-client` configs, including:
    - Your **language** choice (Voice Translate).
    - Your **microphone / push-to-talk** settings (Simple Voice Chat).

---

## When do I need to update?

Whenever the admin pushes new or changed mods/configs and asks the group to update. If you join
and something looks wrong (missing items, can't connect, version mismatch), updating is the first
thing to try.

!!! tip "Keeping mods matched with the server"
    You need the same **common** and **client-side** mods the server expects, or you may not be
    able to connect. The update keeps these in sync for you automatically — that's the whole point
    of doing it through the script or Git rather than picking mods by hand.
