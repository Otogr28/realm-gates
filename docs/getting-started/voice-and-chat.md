<div class="sb-banner" style="background-image:url('/assets/mods/simple-voice-chat-banner.webp')">
  <div class="sb-banner__inner">
    <p class="sb-eyebrow">Getting started</p>
    <h1>Voice &amp; chat translation</h1>
  </div>
</div>

This server runs **Voice Translate** (`voicetrans`), a real-time translator inspired by QSMP. It
shows **floating subtitles above a speaker's head** plus a chat-style transcript, each translated
into **your** chosen language — and it translates **text chat** too.

!!! success "You don't need an API key"
    All the translation happens **on the server**. You only need the two mods (both already in the
    pack's `mods/` folder): **`voicetrans`** and **Simple Voice Chat** (which carries the voice).

---

## 1. Set your languages (in-game)

Open the Voice Translate settings:

- From the **main menu** or **pause menu** → **Mods → Voice Translate → Config**, **or**
- Bind a key under **Options → Controls → "Voice Translate: Open settings"**.

Set two things:

| Setting | What it does |
| --- | --- |
| **Language you speak** — e.g. `en`, `es`, `fr` | Lets the server **skip** translation (and save resources) when nobody nearby needs another language. |
| **Language to read** | What your subtitles and chat get translated **into**. |

---

## 2. Set up your microphone (Simple Voice Chat)

Press the **Simple Voice Chat** settings key (default **`V`**), then:

1. Pick your **microphone**.
2. Choose **push-to-talk** (and a key) or **voice activation**.
3. Test the mic with the built-in level meter.

Voice is **proximity-based**: people close to you sound louder, and the sound fades with distance.

---

## How it works (the short version)

1. You speak; Simple Voice Chat captures your audio.
2. Voice Translate sends it to the server, which turns speech into text and translates it.
3. Everyone nearby sees a **subtitle in their own chosen language**, floating above your head and
   in a chat transcript.

!!! tip "Why nothing gets translated sometimes"
    If everyone nearby already speaks your language, nothing is translated — **that's on purpose**,
    to save resources. Translation kicks in when someone nearby is set to a different language.

For a deeper look at this custom mod, see **[Voice Translate](../custom/voice-translate.md)**.
