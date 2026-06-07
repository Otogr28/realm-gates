<div class="sb-banner" style="background-image:linear-gradient(125deg,#16285c 0%,#0a1330 60%,#0a1736 100%)">
  <div class="sb-banner__inner">
    <p class="sb-eyebrow">Getting started</p>
    <h1>Install the modpack</h1>
  </div>
</div>

<div class="sb-lock" role="status">
  <span class="sb-lock__icon" aria-hidden="true"></span>
  <span class="sb-lock__tag"><span class="sb-soon__dot"></span>Locked</span>
  <h2 class="sb-lock__title">Coming soon</h2>
  <p class="sb-lock__text"><strong>Installation opens at release.</strong> The modpack &amp; server
  aren't out yet, so the install steps are sealed for now. Check back here when the gate opens.</p>
  <p class="sb-lock__note">Release date to be announced soon</p>
</div>

In the meantime, get a head start: read the **[Concepts](../concepts.md)** to learn the realms,
gates and the Blight — or browse **[the dimensions](../mods/index.md)** to see what's waiting
on the other side.

<!-- ============================================================
     RESTORE ON RELEASE: uncomment everything below this line and
     remove the <div class="sb-lock"> ... </div> gate above (and
     the "In the meantime" paragraph). The instructions are the
     real, working install steps — kept here verbatim so reactivating
     is a copy/paste, not a rewrite.
     ============================================================

You need **Minecraft: Java Edition** and a launcher with **Forge 1.20.1** installed. Then you add
the Realm Gates **mods** and **configs** to that Forge instance. Pick whichever method below
suits you — they all end with the same result.

!!! info "Before you start"
    1. Install **Forge 1.20.1** in your launcher (Prism, CurseForge, or the official Forge installer).
    2. Get the **server address** from the admin.
    3. The modpack lives on GitHub at **`Otogr28/MCserver`**.

---

## Option A — One script (recommended, auto-install + auto-update)

A single command installs Git (if you don't have it) and downloads the modpack into a folder.
You then point your Forge 1.20.1 instance **at that folder**.

Open **PowerShell** on Windows and paste:

```powershell
iwr -useb https://raw.githubusercontent.com/Otogr28/MCserver/master/install.ps1 | iex
```

This creates the modpack folder (default `C:\Users\YOU\summerBuddies`). In your launcher, set that
folder as your instance's **game directory** and launch from there.

To update later, just **double-click `sync.bat`** inside that folder. It force-updates everything
to match the server. That's it. See [Updating](updating.md) for what's kept and what's reset.

---

## Option B — Download a ZIP (easiest, no tools)

1. On the [GitHub page](https://github.com/Otogr28/MCserver), click the green **`<> Code`** button → **Download ZIP**.
2. Unzip it.
3. Copy the **`mods`** and **`config`** folders into your Forge 1.20.1 instance (the folder that
   already has a `mods` and `config` folder).
4. When something changes, download the ZIP again and re-copy.

---

## Option C — Git for Windows (graphical, easy updates)

This keeps the modpack updated with a couple of clicks instead of re-downloading every time.

**Install Git for Windows**

1. Download it from **[gitforwindows.org](https://gitforwindows.org)** and run the installer.
2. Accept all the defaults (just keep clicking **Next → Install**). This adds **Git GUI** and **Git Bash**.

**Clone the modpack (first time only)**

1. Open **Git GUI** → **Clone Existing Repository**.
2. Fill in:
    - **Source Location:** `https://github.com/Otogr28/MCserver.git`
    - **Target Directory:** an empty folder, e.g. `C:\Users\YOU\summerBuddies` *(it must not exist yet — Git creates it)*.
3. Click **Clone**.

**Copy the mods into your game**

- Copy the **`mods`** and **`config`** folders from the cloned folder into your Forge 1.20.1 instance.

!!! tip
    Some launchers let you point the instance directly at the cloned folder, so you never copy
    again. If unsure, just copy the two folders.

**Update later**

1. **Git GUI** → **Open Existing Repository** → pick your cloned folder.
2. **Remote → Fetch from → origin**.
3. **Merge → Local Merge…** → choose **origin/master** → **Merge**.
4. Re-copy the **`mods`** and **`config`** folders into your instance.

> Prefer the command line? Right-click the cloned folder → **Git Bash Here** → run `git pull`.

---

## Next steps

- Set up your language and microphone: **[Voice & chat translation](voice-and-chat.md)**.
- Understand what gets reset on updates: **[Updating](updating.md)**.
- Curious what a mod does? Browse **[The mods](../mods/index.md)**.

     ============================================================
     END RESTORE BLOCK
     ============================================================ -->
