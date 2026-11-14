---
name: bang-motion
description: Builds cinematic motion graphics in the browser (promo videos, openers, intros, bumpers, kinetic typography, illustrated explainers/explanatory videos in 16:9 or 9:16) using HTML + CSS + GSAP (+ Three.js when needed), with results that move like real video — not presentation slides. Use this skill whenever the user asks for a "promo video", "opener", "animated intro", "motion graphic", "bumper", "kinetic typography", "cinematic text animation" (animasi teks sinematik), "explainer", "explanatory video" (video penjelasan) (visual journalism, educational cartoon, collage), or shows a promo/explainer reference video and wants a web version of it — even if they do not explicitly say "motion graphic". Also use it when the user complains that a web animation looks "like PPT/a presentation" (seperti PPT/presentasi) and wants it more cinematic, or wants to render a web animation into an MP4 video file, or wants a cartoon/animated explainer built DIRECTLY in After Effects via the Higgsfield bridge/MCP.
license: MIT
metadata:
  author: Bang Tutorial
  author_url: https://youtube.com/bangtutorial
  version: "1.19.0"
  updated: "2026-09-14"
  homepage: https://github.com/bangtutorial/bang-motion
---

# Bang Motion — web motion graphics that are not PPT

*English translation of `SKILL.md` (v1.19.0). `SKILL.md` stays the source of truth; the files in `references/` are in Indonesian, and agents read them as they are.*

**v1.19.0 · by [Bang Tutorial](https://youtube.com/bangtutorial) · MIT.** Change history in `CHANGELOG.md`;
how to install in `README.md`.

This skill is for any AI coding agent (open Agent Skills format).
It contains laws and recipes for motion graphics that move like video, not
like a presentation — follow them before writing code.

## Prerequisites — a browser only

The deliverable (`index.html`) needs only a modern browser + internet for the CDN
(GSAP, fonts). Python and Node are **optional**, used only for working tools:
`scripts/serve.py` (no-cache server, only needed when using local modules),
puppeteer (automated snapshots/verification, `scripts/export-frames.mjs` → MP4).
If the user has neither: (1) still build a single file, opened by
double-clicking; (2) verify visually through `?debug=1` (scrub panel) and
manual screenshots at each key second; (3) MP4 through screen recording (OBS / browser
tab recording) — explain that a screen recording can drop frames, and that
frame-by-frame rendering needs Node. Never create a deliverable that needs
`npm install` to be WATCHED.

**ffmpeg is optional too.** Check first (`ffmpeg -version`); if it is missing:

| Need | With ffmpeg | Without ffmpeg |
|---|---|---|
| VO sync (sentence/paragraph boundaries) | `silencedetect` | `scripts/vo-pauses.html` — open it in the browser, pick the audio, copy `SEG`/`PARA`; the result is exactly the same (Web Audio, no install) |
| Audio duration/format | `ffprobe` | the `DUR` number from vo-pauses.html; the browser plays wav/mp3/m4a/ogg directly |
| MP4 export | join the PNGs from export-frames.mjs | no MP4 — offer a one-command install (`winget install Gyan.FFmpeg` / `brew install ffmpeg`) or screen recording |
| Studying a reference video (extracting frames) | `fps=` + `tile=` | ask the user to send screenshots at key seconds, or open the video in the browser and capture it at specific seconds |

Without ffmpeg the explainer flow is still complete up to VO sync; only MP4
needs an install.

## Player — none, autoplay, loop

Default deliverable: **no panel/player of any kind on screen**, plays immediately
when opened, and loops from the start when it ends (`onComplete →
play(0)`; if there is sound, the audio loops too). Hidden controls: R restarts,
Space pauses. The scrub panel/clock appears only with `?debug=1` (a review tool),
and `?clean=1` holds back autoplay for export. Sound? Try `play()`
directly; if the browser blocks it, hold on frame 0 and start on the first
click — with no "tap to start" text. This is already built into both
starters.

## Structural bans — a PPT test you can check mechanically

Other models (and you, when tired) will fall into these patterns even after reading
the laws below. Before handing over, check the CODE, not your feelings:

1. `grep -c "class=\"scene\"\|<section" index.html` — if ≥ 3 scenes
   are `<section>` elements switched on and off with `autoAlpha`/opacity
   → that is a slide deck. Scenes must change because the WORLD/CAMERA moves
   (the camera moves, a whip to another angle, a push-through, the background changes),
   not because a section fades. The valid exception: **cartoon stage**
   (`references/kartun-panggung.md`) uses a cut/96 px slide between stages
   — allowed, because each stage is fully alive (≥10 objects in action), not
   a still image being faded.
2. There is a persistent visual through-line: one subject (continuous action) OR
   one collage/paper/white world that the camera travels through (cartoon, photo,
   catalog, sketch). Full-bleed photos swapping with no shared world →
   PPT. One image + one sentence per scene, swapped every scene →
   still a slideshow even if the camera moves: each scene has 3–5 elements that
   enter step by step, phrase by phrase (explainer.md "One scene = 3–5 elements" ["Satu adegan = 3–5 elemen"]).
3. Per scene, count the text nodes: eyebrow/kicker + title + body/credit = 3
   levels → PPT. Maximum two: one big number/sentence + one world label.
   Documents/stamps/date blocks holding ≤ 3 short lines count as objects,
   not text levels.
4. Ken Burns (scale 1.0→1.05 on a photo) as the only motion → PPT.
   Motion every second must come from the BACKGROUND MOTION LANGUAGE chosen in
   the style brief from the menu in `techniques.md` §7c (a breathing camera over a textured
   background, shifting gradients, floating blobs, live grain, a light sweep
   per segment, large shapes rotating slowly, rising particles, a breathing
   grid, drifting ghost text, Ken Burns + parallax…). Bars/lines/
   pieces crossing sideways ("lane", "range", "streak", horizontal particle
   rain) have ALREADY been used by two projects in a row under different names
   — that is not a default; only when the theme really is speed/flow,
   and never in two projects in a row.
5. Only fade + scale bump + light leak on every cut → PPT template.
   Whip to another angle, cut to an instrument (map/speedometer/profile), push-through.
6. An explainer starts from its STYLE's starter: `starter-explainer-kartun`,
   `-jurnalisme`, `-katalog`, `-sketsa` (collage mode: the camera travels over still
   assets), `starter-explainer` (continuous action: the world flows), or
   `starter-explainer-panggung` (cartoon stage: one stage per scene,
   joint rig, camera only inside the stage). The collage starters share one rig; the
   stage starter has a different rig. NOT from `assets/starter-opener.html`
   (text opener), and not from scratch.

7. **A miniature is a slide.** Camera zoom < 1.08 so that a house is the size of a
   thumb and empty ground fills half the screen → PPT even if everything moves.
   The world is split into frame-sized stages, not one big map that gets
   explored (`kartun-panggung.md` Law 1).

8. **Template skeleton (opener/promo).** Check the rundown and the code: the first scene
   is text that scales up and then exits to the left; three feature tiles/cards
   side by side; an input box/search bar being typed into; the sequence hook → feature → feature →
   promise → logo → CTA. Two or more of these without the concept demanding them → template, even if
   the skin is new. Re-pick the skeleton from `references/opener-konsep.md`.

Fail even one point → rework it before showing it to the user.

## Types of work covered

This skill is for web motion graphics IN GENERAL. Explainers are only one
type — they have their own document because their structure is different, not because they
are the main one.

Starters are named after their category: `starter-opener.html` for openers, promos,
bumpers, intros, and kinetic typography; `starter-explainer-*.html` for explainers,
with a mode/style suffix (`-kartun`, `-jurnalisme`, `-katalog`, `-sketsa` = collage;
no suffix = continuous action; `-panggung` = cartoon stage). Cartoon stage is an
explainer mode (style 6), not a category of its own: the goal is still to explain with
VO; only the way it is produced is different.

| Type | Typical length | Traits | Recipe |
|---|---|---|---|
| Opener / product promo | 25–40 s | one concept from the menu (the skeleton grows out of the product, not a fixed sequence), one special moment, a brand ending | `references/opener-konsep.md` + the workflow below + `references/techniques.md` |
| Bumper / ident / logo sting | 3–8 s | logo build-on, one signature motion, done before the viewer notices | `techniques.md` (logo build-on, light leak) |
| Channel intro / outro | 5–12 s | channel name + the same signature motion every episode | the workflow below |
| Kinetic typography / lyrics | 15–60 s | the text is the subject; split per word/letter; the rhythm follows the audio | `techniques.md` (split + directional blur, 3D pan per word) |
| Title / lower third / segment bumper | 2–6 s | a small element over footage, clean in and out, transparent background | `techniques.md` |
| Explainer / explanatory video | 30–90 s | sourced facts, entities shown, changing viewpoints, five styles | `references/explainer.md` + the starter for each style |

## Explainers and characters: read before deciding shots

For flat educational cartoon explainers with characters (the sixth style, **cartoon
stage**), or a revision that feels like a slideshow/miniature, read
`references/kartun-panggung.md`: one stage per scene, zoom 1.08–1.95,
continuous inside a stage and a cut/96 px slide between stages, a joint rig with
manual transforms, zero captions, a bright flat palette. Distinguish between sentences, visual beats,
framing, and stage changes. To build it directly in After Effects, read
`references/ae-bridge-higgsfield.md`. These explainer-specific guidelines clarify the
opener rules below; the example fonts, scene counts, and effects are not universal recipes.

## Law #1 — This is video, not slides

The most common disease: the model lays out scenes like slides — title + subtitle
+ body copy + a row of badges. That instantly reads as "PPT" and will be rejected.

The hard rules:

- **For openers: one short sentence + at most one main object per scene.** No
  kicker ("01 — FEATURE"), subtitle, caption paragraph, feature chips/badges,
  or technical metadata (package name, long URL). Chips, buttons, and labels that
  are part of the product UI being used do not count.
- **New information = a new visual response.** In explainers, change the state/action
  in the same world when it is still related; a new sentence does not have to change the shot.
- **A bullet list becomes visuals, not automatically three tiles.** Pick a way from
  the feature menu in `references/opener-konsep.md` (one feature demoed, a word
  changing, an object transforming, cards being shuffled, a tile grid…); two openers
  in a row do not use the same way.
- **Scenes must be alive.** The camera may hold still while objects carry the action.
  Move the camera to follow or reveal something; do not rely on
  text fading/sliding over a still background, or a repeated pan/zoom in every segment.
- **"Zoom in-out" = shot size, not camera breathing.** If the video feels static or
  the user asks for zoom, the camera moves in to the element that is telling the story (medium close-up
  / close-up) and then pulls back to wide following the beats of the content; a breathing of a few percent is almost
  invisible (`techniques.md` §3b).

Read `references/anti-ppt.md` BEFORE designing scenes — it contains a list of
real violations together with their fixes.

## Law #2 — Deterministic or dead

Not a single line reads the system clock. Every visual is a pure function
of `tl.time()` (GSAP timeline time): spectrum, running numbers,
particles, camera shake (high-frequency sine, not `Math.random()`),
the position of objects that "flow" (tween the DISTANCE, not accumulated velocity per
frame). The consequence: scrubbing is accurate like an After Effects timeline, and
frame-by-frame rendering to MP4 produces identical images every time.

## Law #3 — Style is born from the theme, not from the starter, not from the reference

A common failure: an opener for another product comes out with EXACTLY the skin of
the previous product's opener — dark, blue accent, glow, nebula, the same font —
because the model took its style from the starter. The animation can be good and it still
fails: an opener is the face of a product, and two products must not share a face.

1. **Style brief first, code later.** Before touching the starter, write
   these six lines and show them to the user together with the scene rundown:
   - theme/product + three adjectives for the feeling you want to leave behind;
   - **concept & structure fingerprint** (opener/promo): three concept candidates from
     `references/opener-konsep.md`, one picked with a reason taken from the product, then
     `concept · number of scenes · main object of each scene · opening · ending`;
   - palette: one main color FROM the brand/theme (logo, app icon, website,
     packaging), one background color, one accent — state the hex AND the source of each
     color; a color that does not come from the brand is written as "derived: reason";
   - a display font with character that fits that feeling (not
     Poppins/Inter/Roboto/Montserrat/Arial) + a companion font; exception:
     the claim → how → result concept uses the product's own UI font
     (`references/opener-konsep.md`);
   - text emphasis: no word highlight, or one highlight form (name it) —
     word highlights are OPTIONAL, not a default in every opener;
   - background language per segment: one direction from the "Style direction" table for all of them,
     or a plan of changes (which segment changes, to what, why, triggered by what);
   - signature motion: one kind of motion repeated as an identity
     (object wipe, 3D roll per word, flying paper, a line that draws itself,
     color blocks slamming into the edge…);
   - background motion: one language from the menu in `techniques.md` §7c — not the
     same thing as the signature motion, and not automatically "objects crossing";
   - background surface: from the §7d menu (gradient/light/texture/grainy gradient,
     ≥ 2 layers) — not flat;
   - object render style: one family from the menu in `techniques.md` §7e (flat, clay,
     glossy, glass, isometric, realistic, neon line…);
   - photo assets (when the concept uses photos of people/places/products): their source — the
     user's photos, generated through the Higgsfield MCP, or licensed stock — ASKED of the
     user, plus a shot list per act (`references/opener-konsep.md` "Photos in
     openers" ["Foto dalam opener"]);
   - transitions: decide which boundaries need an effect and which only need a cut;
     pick from the §4c menu to fit the context, with no requirement of two kinds and no requirement of 3D;
   - one special moment (where the most expensive effect is used, once).
2. **The starter is architecture, not style.** The grey colors, system fonts,
   and WebGL background in `assets/starter-opener.html` are PLACEHOLDERS. If any
   of them is still visible in the result, the style has not been derived. The WebGL
   background (nebula, dust, grid, bloom) is only one background language out of eight;
   turn it off when the style direction is different.
3. **Reference = rhythm, not skin.** From a reference video take: the duration of each
   shot, the type of transitions, the attention hierarchy, energy, motion language. DO NOT take:
   palette, fonts, textures, layout, ornament shapes, sentences, scene order,
   or unique moments (a signature opening/ending, a one-off gimmick). "Make it
   like this" means "this energetic", not "these colors";
   "use style X" means X's skin and motion language, not X's scenes. The example
   sequences in `references/opener-konsep.md` are treated the same way: principles, not
   a script (skeleton law #7 ["Hukum kerangka #7"]).
   Copying the skin of a reference = a violation, even when the user is the one who handed it over —
   say so in one sentence and then offer a version born from the theme.
4. **Different from previous projects — skin AND skeleton.** Two different products must differ in
   at least three of the four: palette, font, background language, signature motion —
   including the word-highlight form if one is used (one project's pill + star
   must not appear again in another project). The skeleton too: a different
   concept, or ≥ 3 of the 5 structure-fingerprint elements different
   (`references/opener-konsep.md`). New colors over an old scene order
   are still a template.
   Do not open old project folders for "examples" — the only thing that may be inherited
   is the rules in this skill.
5. **The background is not dark by default.** Without this rule every opener tends to
   come out dark with a nebula, because the starter and its examples are dark. The background follows
   the theme: a light gradient, soft colors, color blocks, paper, photos, or dark
   — the "Style direction" table has ten options and most of them are not dark.
   The examples in this skill (light paper, nebula) are only examples, not
   locked templates.
   **The background is never static.** There is always background motion (§7c), and the background
   color MAY change whenever needed: the mood/topic of a segment changes
   (entering the product, problem → solution, claim → CTA), a colorful brand
   calls for a color rhythm, or the on-screen action actually changes it (a toggle
   switched on, an object covering the lens, an icon growing to fill the frame). Only two
   things are guarded: the change has a visible trigger (wipe, object, UI
   action, push into a color field, cut on the beat) — not a cross-fade without a cause
   that feels like "next slide" — and the background is not left as one still color
   just because nobody considered it. The plan is written in the style brief.
6. **Free to express.** The laws here lock STRUCTURE (not
   slides), CONTRAST (readable text), and NOVELTY (no repeating of other
   projects) — not expression. Rich gradients, light, 3D, depth, texture,
   bold colors are encouraged when they fit the theme. The only thing forbidden is
   taking the cheapest default and repeating it: flat bars sweeping, lines
   crossing, flat backgrounds, another project's skin. If two options both
   satisfy the laws, pick the bolder one.
7. **What may be the same across all work:** the anti-PPT laws, the camera rig,
   determinism, the asymmetric in-out rhythm, the minimum text sizes.

### Style direction (pick one; you may combine two deliberately)

| Direction | Background | Typography | Signature motion | Good for |
|---|---|---|---|---|
| Cinematic dark | near-black gradient, WebGL particles/nebula, bloom only on objects | clean bold grotesk | push-through, light in front of the lens | creative tools, gaming, technology |
| Poster color-block | large solid color fields changing every scene, no gradients | very heavy display, giant letters cropped by the edge | block wipes, text slamming into the frame edge | consumer apps, music, events |
| Editorial light | white/cream, wide empty space, thin lines | display serif + small grotesk | smooth slides, lines that draw, calm camera | productivity, finance, SaaS |
| Paper & print | paper texture, collage cutouts, stamps, tape | handwriting + serif | objects flying in and then landing, tilted angles | education, community, food |
| Retro / analog | faded colors, grain, scan lines, VHS frame | 70s–90s geometric | controlled glitch, rough zoom, freeze | nostalgia, music, entertainment |
| Brutalist mono | black and white, hard grid, ruled boxes | monospace + condensed | hard cuts, shifting blocks, blinking cursor | developer tools, technical |
| Pastel playful | stacked pastels, big round shapes | heavy rounded sans | elastic bounce, blooming shapes | kids, health, lifestyle |
| Luxury dark | black + gold/bronze, soft shadows, sheen | tall wide-spaced serif | slow motion, sweeping light, depth | fashion, automotive, property |
| Flat pop with photos | light neutral alternating with the user's solid brand color fields; flat shapes and stickers derived from the geometry of the user's logo + soft 3D illustration | heavy rounded geometric sans + giant words cropped by the edge | pop-cutout photos of people rising from below, stickers popping elastically, color fields sweeping/snapping on the beat | consumer apps, fintech, e-commerce, youth brands |
| Grainy gradient | dark/deep-color base; saturated 2–3-color gradient shapes glowing from within; fine grain across the whole frame | small clean grotesk, or minimal heavy display | layers of shapes opening/rotating slowly, the camera passing through a hole in a shape, a guiding orb of light | tech, AI, music, fintech, creative launches |

Two openers in a row using the same table row = a warning sign;
pick another row or combine two rows in a way that has not been used yet.

## Law #4 — Text lives, background yields

Two openers with the same rig can end up very good or very bad
just because of their typography and contrast. The bad one: every title in ALL
CAPS, weight 800, centered, entering the same way, over a field of white
light that is brighter than the letters. The good one: sentence case, weight
500, emphasis on key words (e.g. pill + star — that is the signature of
one project, not a rule; word highlights themselves are optional), punctuation
only when needed, size/direction/
position alternating, a calm background under the text, a background that changes with the
segment. The full recipe with code: `techniques.md`
sections 1 and 1b. In short:

- Sentence case, weight 500–600. Bold caps only for one emphasis scene.
- Titles, claims, and short phrases have NO PERIOD BY DEFAULT — especially phrases of ≤ 4 words
  and one-line sentences. Punctuation only when it changes the meaning or the rhythm: `?`
  for real questions, periods for a deliberate style of two short sentences in a row,
  `!` very rarely. The punctuation style is decided once in the style
  brief and kept consistent; when used, it is a separate element that appears last.
- Word highlights (pill, underline, marker, box, color, strikethrough) are OPTIONAL and
  decided in the style brief. Even without highlights a sentence still has emphasis:
  word by word from dim to full, size/weight, pauses, or an object (icon,
  UI) standing next to the word. When used: one form per video,
  not required in every sentence, different from other projects; ornaments only when
  derived from a brand shape.
- Two scenes in a row must not be the same in size, entry direction, and
  text position.
- In the TEXT ZONE (kantong teks; not the whole frame), the background must be DARK (≤ 25 %
  luminance) or LIGHT (≥ 80 %), never "medium busy". Outside the
  zone, the background must, on the contrary, be rich: gradients, light, texture (§7d) — a flat
  single color is rejected. Any background element (particles, shapes,
  texture, lines): color from the dark side of the palette, opacity ≤ .35 in the text
  zone, ≤ 40 bright elements visible.
- Consider alternating dark–light when the segments really do change
  mood; not a mechanical obligation.

## Workflow

0. **Identify the type** (the "Types of work" table). Explainer → open
   `references/explainer.md` and follow "Step zero" ["Langkah nol"] there: ONE
   question covering style (five options + a recommendation), ratio, duration,
   sound, plus the duration guardrail. Other types → continue; ask only about things that
   truly cannot be derived from the brief (ratio, duration, whether there is
   music/VO or not), in one question.
0b. **Write the style brief** (Law #3) and show it together with the rundown. Without
   an approved style brief, do not touch the code.
1. **Absorb the references & brand sources.** Ask for reference screenshots/video
   clips if there are any; map them shot by shot (duration, movement, transition type,
   attention order) — only their RHYTHM, not their skin (Law #3). Colors, logo
   (the ORIGINAL vector path, do not redraw it), fonts, and feature claims are taken
   from the official sources of the PRODUCT being made — not from the reference, not
   from another project, not made up.
2. **Write the rundown from the chosen concept** — a table `second | scene |
   sentence | visual`. The number and kind of scenes follow the concept
   (`references/opener-konsep.md`), not the pattern hook → feature → feature → promise →
   logo → CTA. Total 25–40 seconds. Ask the user to approve this rundown
   before writing code; reworking a rundown is cheap, reworking code is expensive.
3. **Scaffold the architecture.** Opener/promo/bumper/typography: copy
   `assets/starter-opener.html` (1920×1080 stage, `#world` camera rig, stateful Three.js
   scene, timeline helpers) and then IMMEDIATELY replace the color tokens, fonts,
   and background language to match the style brief — the starter is grey on purpose. Explainer: copy the starter for the style —
   `starter-explainer-kartun/-jurnalisme/-katalog/-sketsa.html` (collage
   mode: camera into/settle/look/home over cutouts/photos, say/unsay per
   word, draw annotations, push-through between scenes) or
   `starter-explainer.html` (continuous action: the world flows, hero, world
   objects, map view, whip). All of them already autoplay + loop with no player. The multi-file structure and
   the explanation of each decision are in `references/architecture.md`.
4. **Build the scenes one by one** with the recipes in
   `references/techniques.md` (split per letter + directional motion blur,
   3D pan per word, transition menu, UI mockups). Recipes are tools, not a
   shopping list: use only what the concept demands.
5. **Verify VISUALLY, not just "the code runs".** You cannot watch
   video; you can only look at FRAMES. Capture 6–20 key seconds (the start of
   each scene, when text appears, transitions) with `scripts/snap.mjs`
   (puppeteer, opens `file://`, no server), lay them out as a contact sheet, and
   judge like a director: text cut off? overlapping? text appearing
   before the camera has finished? still feels like slides? Fix it, capture again.
   DO NOT render every frame to check — that is thousands of images and not
   verification; a full render is only for MP4 export (step 6) when the user
   asks for it. Without Node: open `?debug=1`, scrub by hand, take screenshots.
6. **Hand over ONE `index.html` that can be double-clicked.** The final
   output must not need a server/Node: CSS and JS are written INLINE in the
   file (a local module `<script type="module" src="…">` is blocked by CORS when
   opened via `file://`, an inline module is not), libraries from a CDN, assets
   (icons/images) relative, in the same folder. The no-cache server
   (`scripts/serve.py`) is only a WORKING tool while editing, not a requirement for
   watching. No player on screen (see "Player"); mention `?debug=1`
   for scrubbing. **Export MP4 only when the user asks for it**: `scripts/
   export-frames.mjs` renders every frame (60 fps) to PNG and then ffmpeg
   joins them — this way has no frame drops, but it is expensive, so it is not a
   routine step and not a checking tool.

7. **Explainers only: VO script + an invitation to record** — the closing message must
   contain the full VO script and ask the user to record/generate it and then send
   the audio back to be synced. Details on the script format, recording tips,
   and retiming are in `references/explainer.md` → "Handover" ["Penyerahan"].

## Checklist before handing over

- [ ] Style brief (theme, palette from the brand, display font with character, one
      background language, signature motion, special moment) written and approved
      BEFORE code
- [ ] No starter placeholders left (grey, system font, nebula when the
      style direction is different) and no reference skin copied (palette,
      fonts, texture, layout, sentences)
- [ ] Different from previous openers/promos: at least three of palette, font,
      background language, signature motion
- [ ] Opener/promo: three concept candidates written and one picked; structure
      fingerprint written down and different from the previous opener; at most two
      canonical components (zoomed text → exits left, three tiles, typed input,
      push-through, light leak, centered logo + CTA), each one demanded by the
      concept (`references/opener-konsep.md`); the concept example is not copied
      (opening/ending different from its example, ≤ 1 ✦ moment, and it is transformed,
      palette and shapes from the user's brand)
- [ ] App/SaaS: at least one living-UI act — assembled, used, producing results —
      from the user's product components, not a still screenshot being zoomed
      (`references/opener-konsep.md`, UI animation section); if the demo feels
      static, important clicks are followed by the camera (close → click → pull back/slide),
      not on every click (`techniques.md` §8)
- [ ] Text lives (Law #4): sentence case, weight 500–600, clear emphasis,
      no automatic periods (punctuation only when it changes the meaning/rhythm),
      size/direction/position alternating between scenes;
      bold caps in only one scene. Word highlights only when the style brief
      picks them (not automatically in every sentence, not a pill + star
      inherited from another project)
- [ ] Background yields (Law #4): under the text, luminance ≤ 25 % or ≥ 80 %,
      background elements dim and dark-colored in the text zone; grayscale test —
      no background as bright as the letters
- [ ] Transitions chosen at the boundaries that need them; not automatically an effect on
      every boundary, nor every effect removed. Sweeping objects have a meaning
      in the scene; speed, amplitude, and pauses have been checked.
- [ ] Background surface from the §7d menu: ≥ 2 layers (base + light/texture/
      blob), colors from the palette — not a flat single color, not pure black/white
- [ ] Object render style is one family (§7e), or the switch between families is made into a moment
- [ ] Opener with photos: photo source agreed with the user (user's photos / MCP generation /
      licensed stock), fictional faces when generated, logo/brand text added
      in code, photos animated (pop, parallax, container) — not Ken Burns alone
- [ ] When using grainy gradient/grain: the grain is still visible in the encoded MP4
      and the gradient does not band
- [ ] When using video: clips placed through `clip()` (no `autoplay`/`loop`), wrapped in
      an animated element, their source agreed with the user, the `assets/` folder mentioned at
      handover, and the seconds containing clips have been captured (`snap.mjs`)
- [ ] Background motion picked from the §7c menu and DIFFERENT from the previous project;
      no bars/lines crossing sideways unless the theme is speed/
      flow and they have not been used in the previous project
- [ ] The background moves in every scene (no still background); background color
      changes are allowed whenever needed, as long as they have a visible trigger
- [ ] Passes the 6 points of "Structural bans" (not sections being faded, a visual
      through-line exists, ≤ 2 text levels, motion every second, varied
      transitions, the right starter)
- [ ] No player on screen; autoplay; loop; `?debug=1` for scrubbing
- [ ] Opener: one main idea without a pile of badges; explainer: one
      event may hold several beats and related objects.
- [ ] Camera, cuts, and object motion chosen to fit the context; there is no requirement
      to move the camera in every segment. When the camera moves, the whole world moves with it.
- [ ] No long dead holds: an act without a big object action gets a
      shot-size change to an element (wide ↔ medium close-up ↔ close-up) or a slow push;
      camera breathing alone does not count. On-screen labels outside the rig, not cut off by the zoom
- [ ] Directional motion blur on all text entering/exiting
- [ ] Background born from the theme (not automatically dark; light can be a gradient,
      soft colors, color blocks, paper), has depth (not a single flat
      color), NOT busier than the subject; background changes decided
      per segment in the style brief and, if there are any, happen behind a wipe/cut
- [ ] Glow is used on objects (tiles, bars, decorative icons) — text titles stay CLEAN
      (full white + a thin drop shadow), unless the user asks otherwise
- [ ] Display font ≠ UI mockup font; mockups use the product's real font
      (claim → how → result concept: all text uses the product's UI font)
- [ ] Zero use of `Date.now()` / `Math.random()` in the render path
- [ ] Captured at key seconds (snap.mjs / ?debug=1) and looked at with your own
      eyes — not a full render; MP4 only when asked
- [ ] Sound? The page holds on the first frame when autoplay is blocked and starts
      together with the sound on the first gesture — never starts without sound; no
      launcher file (`.cmd`/`.bat`)
- [ ] Collage explainer: the camera has choreography (close-up → glide → zoom
      out), not just elements in/out — see explainer.md "Explainer camera" ["Kamera explainer"].
      Cartoon stage: no frame with zoom < 1.08; the camera only
      moves inside a stage; between stages, a cut or a 96/72 px slide
- [ ] Cartoon stage: joints rotated through a manual transform proxy (no
      GSAP `transformOrigin`/`rotation` on joints, no `x/y` tweens
      on groups that have `translate`); each stage has ≥10 moving objects; zero
      captions; raster heads have blink + expression variants
- [ ] Build through the AE bridge: CAM zeroed before parenting, every world layer
      parented to CAM, layers created back → front, body-part keyframes
      in the parent's space, contact sheet of each stage + the master looked at,
      closing message contains Ctrl+S + deleting the test comps + the aerender command
      (`references/ae-bridge-higgsfield.md`)
- [ ] Explainer: the closing message contains the full VO script + an invitation to record /
      generate it themselves and send the audio back to be synced;
      `vo-script.md` saved in the project folder
- [ ] Explainer: style, ratio, duration, and sound asked in ONE
      question (except what the user already stated) before writing code;
      duration follows the brief/VO; the number of scenes follows the context, not duration ÷ 6
- [ ] Ratio defaults to 16:9 / follows the screen; 9:16 only when asked. No
      subtitles/captions unless asked. The reference's layout (panels, subtitles)
      is not copied — only its principles
- [ ] Explainer on an action/speed topic: one subject present from start to
      end, the background keeps flowing, numbers live inside the world (the subject
      passes in front of them) — see explainer.md "The fifth style: continuous action" ["Gaya kelima: aksi kontinu"]
- [ ] Viewpoints change: no three scenes in a row with
      the same angle; each fact gets its instrument (speedometer, map,
      elevation profile, map race, interior, front view) — see
      explainer.md "Viewpoint MUST change" ["Sudut pandang WAJIB berganti"]; breathing camera
- [ ] No text below 30 px on a 1080 stage (body ≥ 44, label ≥ 34,
      credit ≥ 30) — it is watched on phones; ghost text & annotations vary, not
      always an outline / a dashed circle
- [ ] Explainer: every person/company/place/product that is MENTIONED has
      its photo shown in that scene (see explainer.md → "Entities mentioned" ["Entitas yang disebut"])
- [ ] `index.html` opens directly through `file://` (double-click) without a
      server — CSS/JS inline, no local module `src`
- [ ] Numbers that change every frame (clocks, counters) use
      `font-variant-numeric:tabular-nums` + `min-width` so that their container
      does not change width

## Pitfalls that have already claimed victims

Details and fixes in `references/techniques.md`, the "Pitfalls" ["Jebakan"] section:
low bloom threshold → white screen; additive nebula → piles up through bloom;
a more specific CSS selector overrides the initial `opacity:0` state → the element
appears before its animation; JS modules cached by the browser → edits "have no
effect" (use a `Cache-Control: no-store` server); a flat 3D object rotated
fully around the Y axis → turns into a single line (wobble it, do not rotate it fully);
the default SVG filter box clips the blur tail (widen `x/y/width/height`).

## After Effects — directly through the Higgsfield bridge

When After Effects is already open, Higgsfield's `ae_*` MCP bridge is connected, and the user
asks for an animation/explainer to be built in AE, build it directly through bridge commands. Read
`references/ae-bridge-higgsfield.md`: comp skeleton through one small Lottie, a `CAM`
null per stage (anchor & position zeroed BEFORE parenting), illustrations
from code-SVG → 2× PNG (`scripts/ae/bridge/aset-svg.py` + `svg2png.cjs`), characters
as native jointed AE shapes (`scripts/ae/bridge/rig-tokoh.py`, ±90 ops per character),
body-part keyframes in the parent's space, verification through a contact sheet (relay
when r2.dev is blocked). The cartoon stage laws still apply in full. The bridge cannot
save/render and cannot reorder layers — say so
and create layers from back to front. Building 10 stages ≈ 1 hour, 0 credits.

## Package contents

| File | When to read |
|---|---|
| `references/kartun-panggung.md` | CARTOON STAGE: one stage per scene, camera ≥1.08, cut/96 px slide, joint rig + manual transforms, raster head + local expressions, zero captions, flat palette |
| `assets/starter-explainer-panggung.html` | EXPLAINER, cartoon stage: stage system + per-stage camera, `J()` joints, `character()` (vector or raster head), 96 px whoosh, example with two stages |
| `scripts/kepala-ekspresi.py` | generated head → happy/anxious/surprised + blink variants, made locally (pupil & mouth detection) |
| `references/ae-bridge-higgsfield.md` | BRIDGE: building a cartoon stage directly in AE through the Higgsfield MCP — bridge limits, pitfalls (null at 960,540; parenting to a keyframed CAM; broken reorder), per-stage CAM architecture, native rig, contact sheet relay, handover |
| `scripts/ae/bridge/aset-svg.py`, `svg2png.cjs`, `rig-tokoh.py` | BRIDGE: illustration assets from code → SVG + manifest → 2× PNG (puppeteer); a generator of ±90 `ae_batch` ops for one jointed character |
| `references/anti-ppt.md` | before designing scenes |
| `references/opener-konsep.md` | OPENER/PROMO before the rundown: three concept candidates, a menu of 19 concepts (including object relay, brand system showcase, claim → how → result, living UI ecosystem, flat pop with photos, through the gradient shapes, and product tour with claims, all derived from the brand's services/assets/products), layout-color-rhythm guides, a UI animation guide for apps/SaaS, a guide to photos in openers (user input / generation through MCP), feature menu, openings, endings, transitions without a cut that are carried by objects, structure fingerprint — prevents template skeletons |
| `references/explainer.md` | when the request is an explainer/explanatory video (cartoon + VO, photo-based visual journalism, white catalog, vintage sketch, or continuous action; default 16:9, 9:16 only when asked) |
| `references/architecture.md` | when scaffolding / when you need the reasons behind the structure |
| `references/techniques.md` | when building scenes & effects (including shot size §3b, grainy gradient §7d, the object render style menu §7e, and video as a footage layer §9b) |
| `references/roadmap.md` | when developing this skill further |
| `assets/starter-opener.html` | starting point for OPENERS/promos — architecture + tools (8 text entrances [pintu teks], optional transitions); DELIBERATELY without an example scene sequence, the skeleton comes from `opener-konsep.md` |
| `assets/starter-explainer.html` | EXPLAINER, continuous action style (vector): flow mode (strip + hero + world objects) + map view + whip + a collage mode example |
| `assets/starter-explainer-kartun.html` | EXPLAINER, cartoon collage: cream paper + grain + stains, illustration cutouts, Bricolage + Caveat, color pills |
| `assets/starter-explainer-jurnalisme.html` | EXPLAINER, visual journalism: black + grain, real photos + source tags, Barlow Condensed + Plex Mono, yellow/red highlighter, dashed annotations |
| `assets/starter-explainer-katalog.html` | EXPLAINER, white catalog: faint grid, photo cutouts, Archivo Black + Caveat + Inter, yellow highlighter |
| `assets/starter-explainer-sketsa.html` | EXPLAINER, vintage sketch: sepia paper (CSS texture), multiply engraving cutouts, Playfair + Garamond + Cinzel, rust & gold |
| `scripts/serve.py` | no-cache dev server (optional, needs Python; only when using local modules) |
| `scripts/snap.mjs` | VERIFICATION: capture key seconds → contact sheet (optional, needs Node + puppeteer) |
| `scripts/vo-pauses.html` | VO pause detection in the browser (replaces ffmpeg silencedetect, no install) |
| `scripts/export-frames.mjs` | EXPORT: render all frames → MP4, only when asked (optional, needs Node + puppeteer + ffmpeg) |
