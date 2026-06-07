<div class="sb-banner" style="background-image:url('/assets/mods/simple-voice-chat-banner.webp')">
  <div class="sb-banner__inner">
    <p class="sb-eyebrow">Custom mod · made for summerBuddies</p>
    <h1>Voice Translate</h1>
  </div>
</div>

!!! abstract "Real-time voice &amp; chat translation"
    Real-time **voice and chat translation** with **floating subtitles** above the speaker's head,
    inspired by QSMP. It lets friends who speak different languages play together naturally.

For the quick setup, see **[Voice & chat translation](../getting-started/voice-and-chat.md)**. This
page explains how it works under the hood.

## What it feels like

When someone talks, a subtitle appears **floating above their head** and in a chat-style transcript
— already translated into **your** chosen language. Text chat is translated too. You read everyone
in your own language, and they read you in theirs.

## How it works

1. **Capture.** It uses **Simple Voice Chat** (proximity voice) to grab the audio of whoever's
   speaking.
2. **Smart gating (saves resources).** It only translates when it's actually useful — when someone
   nearby is set to a **different language** and is **within range**. If everyone around already
   shares your language, nothing is translated.
3. **Translate on the server.** The audio is turned into text and translated **on the server side**.
   You don't need any API key or setup beyond choosing your languages.
4. **Show subtitles.** The translated text appears as floating subtitles and a transcript, in each
   listener's chosen language.

## Two settings you control

| Setting | Meaning |
| --- | --- |
| **Language you speak** | Lets the server skip translating you when nobody nearby needs it. |
| **Language to read** | What everything gets translated **into** for you. |

Set both in **Mods → Voice Translate → Config** (or bind the "Voice Translate: Open settings" key).
Your choices are **saved per-player** and survive modpack updates.

!!! info "Why this server runs in offline mode"
    Voice Translate is being tested with friends, some of whom don't have premium Minecraft
    accounts — so the server runs in **offline mode** to let them join. Because of that, the
    **whitelist** is what keeps the server private. See [Server info](../server-info.md).

!!! tip "Get the best results"
    Use **push-to-talk** and speak clearly in full phrases. Background noise and overlapping talkers
    make speech-to-text harder, just like any voice assistant.
