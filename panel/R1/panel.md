# R1 critic panel: Compass & Trail

Evidence read: `panel/R1/EVIDENCE.md`; shots `index-1440-light`, `index-390-light`, `compass-1440-light-fold`, `compass-390-light`, `knots-1440-dark`, `first-aid-390-dark`, `about-1440-light`. I also read `site/css/handbook.css`, `site/js/handbook.js`, `site/about.html`, `site/index.html` (footer), and `_src/pages/compass.html`, `knots.html` and `first-aid.html`.

Note: at the size the tool shows them, the two tall 390 px shots (compass 13,809 px, first-aid 8,619 px) are too small to read text or check spacing. Findings about those pages come from the source files, not the pixels.

---

## 1. Massimo Vignelli (Unigrid, grid and type discipline)

The black band, the condensed sign face, the coloured chapter bars and the single body column form a real system, and Unigrid would recognise it. Two places break it.

- **About page column is off the grid** (`about-1440-light`). The H1 and lede start at x=156. Every section below starts at x=426, and nothing fills the 270 px to its left. The cause is `<div class="wrap prose about">`: `.prose { max-width: 72ch }` overrides `.wrap`'s `max-width`, so `margin: 0 auto` centres a narrow box. Fix: in the About markup, nest it as `<div class="wrap about"><div class="prose">…</div></div>`, so the text hangs from the same left edge as the page head. **must**
- **Chapter hues 1, 2 and 3 collapse into one warm family** (`index-1440-light` tiles and nav badges). Compass `#b2441a`, Maps `#8a5a2b` and Essentials `#a3392f` are all rust or brown, and Essentials is close to the `--blaze` accent too. Badges 1 and 3 cannot be told apart in the nav. Fix: in `chapters.json`, move Essentials to a distinct hue, for example teal `#1f6f6b` (white numerals about 5.9:1), then rerun the contrast check. **should**
- **The footer line breaks its own rhythm** (`index-1440-light`, `index-390-light`). It reads "Sources · Source on GitHub · MIT licensed ·", then the portfolio link wraps alone onto the next line, leaving a dangling separator. Fix: in the build footer template, put the portfolio link in its own `<p>` and drop the trailing " · ". **should**

## 2. Viktor Shklovsky (estrangement)

The contour hero does real work. A handbook for scouts that opens with a map rather than a photograph of a uniform makes the reader *see* terrain, and that is the device laid bare in the right way. The chapter collars are where it turns automatic.

- **The collar terrain repeats.** Compass (`compass-1440-light-fold`) and Knots (`knots-1440-dark`) both show the same composition: one concentric island at the top right, recoloured. After two chapters the eye stops reading it. Fix: in the build's contour generator, give each chapter its own landform and placement (a saddle for Maps, a ridge spur for Camping, two summits for First aid), seeded by chapter number, not just a new colour. **could**
- **Two counters for one idea.** Home uses coloured badges 1–6 for chapters, then `01 02 03 04` in monospace for "How to use". Using two numbering languages on one page undercuts the badge device. Fix: `.how-list li::before`, set it in `var(--sign)`, or drop the counter and let the four titles stand. **could**

## 3. Steve Krug (a 12-year-old, no thinking)

The home page passes the trunk test: name, sections, where to start ("Start with the compass"). The nav badges match the tile colours. The issues are about long pages and the zero state.

- **Empty progress bars look broken** (`index-1440-light`, `index-390-light`: six grey bars at 0). A new reader sees a loading or disabled bar. Fix: in `handbook.js`, when `n === 0`, hide the tile's `.bar` (or show "0 of 7 skills") and show the bar only once a skill is ticked. **should**
- **The payoff is far from the start on mobile.** The compass page is 13,809 px tall at 390, and the skills check is at the very bottom. The collar meta already says "0 of 7 ticked". Fix: in the build, make that meta text a link to `#skills`, so the reward is reachable from the top. **should**
- **Sideways nav on mobile** (`index-390-light`): only Compass, Maps and Essentials show, and "Kn" is cut off under a fade. That is acceptable as a scroll cue. No fix; noted.

## 4. Edward Tufte (the diagrams)

The resection figure is honest: I checked the geometry. Tower at 311° and summit at 43° from the "You" point match the drawn lines, and the back bearings of 131° and 223° are right. The parts diagram and the rope diagram are clear, with label halos on the card. The table is a different matter.

- **The traverse table does not close.** Plotting the four legs in `compass.html` `table.log` (064°/58 m, 151°/32 m, 232°/46 m, 336°/56 m) leaves the end 22 m from the start: 11.5 % of the 192 m walked. The page says "Under about 5% of the distance walked is good work", and leg 4's note says "Closes the loop". The example fails its own standard. Fix: leg 4 → **316°, 29 paces, 44 m**, which closes to 1.1 m (0.6 %). **must**
- **The declination diagram has no caption** (`compass.html`, `.split .fig-sm`). It draws an east declination of about 16° and does not say so, or that the angle is exaggerated. Fix: add `<figcaption>East declination shown; angles not to scale. Your map's diagram gives the real values.</figcaption>`. **should**
- **The "loop" in the rope figure has no over/under break** (`knots-1440-dark`). The page defines a loop as where the rope "crosses over itself", but the drawn curl has no gap at the crossing, so a reader cannot see which strand is on top. Fix: in the `fig-rope` SVG, add a short `--card`-coloured stroke under the upper strand at the crossing (a knockout gap). **could**

## 5. Wilderness first-aid and land-navigation instructor (technical accuracy)

I checked the arithmetic and doctrine and found them correct:
- 3° bezel clicks and 81° → 27 clicks.
- 1° error is about 17 m per km.
- Magnetic → true: add an east declination. True → magnetic: subtract it.
- The calculator default: M 75° with 10° E gives T 85°, back bearings 265° T and 255° M.
- Back bearing rule.
- Pace count of 60–70 double steps per 100 m.
- 30 × tan 35° = 21 m.
- TC 3-25.26 stand-off distances: 55 m, 18 m and 10 m.
- Square knot, bowline, clove hitch, taut-line hitch and sheet bend steps and checks. The taut-line instruction "slide away from the stake to tighten" is right.
- First aid: 20-minute burn cooling with no ice; nosebleed leaning forward; heat exhaustion "worse, or not better within an hour"; heat stroke "do not give them anything to drink"; hypothermia warming the centre; CDC tick steps; epinephrine. All of these match CDC and Red Cross.

Nothing I found is unsafe. Three lines need correcting:

- **Dial lock is the wrong part.** The page says: "Folding it under the closed compass locks the dial." (Thumb loop, `compass.html` `.parts`). In the lensatic compass, the **rear sight / lens bracket** locks the dial when it is folded down and the cover closed. The thumb loop holds the closed cover shut. Correct version: *"Thumb loop: Steadies the compass in your hand. When the compass is closed it folds over the cover. (The dial is locked by folding the lens bracket down before you close the cover.)"* **should**
- **The traverse example** fails its own 5 % rule (see Tufte): 11.5 % closure error. Correct leg 4: *316°, 29 paces, 44 m*. **must**
- **Ambiguous timber-hitch advice.** The page says: "To drag a long log straight, add a half hitch near the far end." (`knots.html` `#timber`). "Far end" can be read either way. The half hitch belongs at the **leading** end, the one you pull toward, with the timber hitch at the back. Correct version: *"To drag a long log straight, tie the timber hitch near the back end, then add a half hitch around the log near the front end, the end you pull toward."* **should**

Optional, not wrong: "Tourniquets are for trained people." This is consistent with Red Cross guidance. If you want to be current with Stop the Bleed, use: *"A commercial tourniquet is the right tool for life-threatening bleeding from an arm or leg. Learn to use one on a Stop the Bleed or first-aid course."* **could**

## 6. Robert Bringhurst (reading typography)

The text face is set the way it should be: 1.125 rem with 1.65 leading, a 72 ch measure (about 660 px at 1440, `compass-1440-light-fold`), `text-wrap: pretty`, and tabular mono figures in the bearing and pace columns. The condensed sign face is reserved for headings and labels, as a sign face should be.

- **The dangling separator in the footer** ("MIT licensed ·" at line end, `index-*`) is a typographic error, not a layout choice. Same fix as Vignelli. **should**
- **Caps headings set nearly solid.** `h1, h2, h3 { letter-spacing: .005em }` is applied to all-caps condensed text down to the 1.5 rem `h3` and the `.t-name` tile titles (`index-1440-light`: "THE TEN ESSENTIALS AND TRIP PLANNING" crowds). Caps want air at small sizes. Fix: `.prose h3, .t-name, .parts dt { letter-spacing: .03em }`, and keep the large H1 tight. **could**
- **A third face for a trivial counter.** The monospace `01–04` in `.how-list li::before` is the only mono outside tables and the calculator. Same fix as Shklovsky. **could**

---

## Verdicts

| Seat | Verdict |
|---|---|
| Vignelli | ship with fixes |
| Shklovsky | ship with fixes |
| Krug | ship with fixes |
| Tufte | ship with fixes |
| Field instructor | ship with fixes (no unsafe content; one wrong worked example) |
| Bringhurst | ship |

## Consensus must-fix list

1. **Traverse table closes outside its own tolerance.** In `_src/pages/compass.html`, `#mapping` `table.log`, change row 4 to `Water tap → gate | 316° | 29 | 44 | Closes the loop`. The closure error falls from 22 m (11.5 %) to 1.1 m (0.6 %).
2. **Dial-lock sentence is wrong.** In `_src/pages/compass.html` `.parts`, replace the Thumb loop `dd` with: "Steadies the compass in your hand. When the compass is closed it folds over the cover. (The dial is locked by folding the lens bracket down before you close the cover.)"
3. **Ambiguous timber-hitch advice.** In `_src/pages/knots.html` `#timber` `.check`, replace "To drag a long log straight, add a half hitch near the far end." with "To drag a long log straight, tie the timber hitch near the back end, then add a half hitch around the log near the front end, the end you pull toward."
4. **About column is off the grid.** In the About source/generator, change `<div class="wrap prose about">` to `<div class="wrap about"><div class="prose">…</div></div>`, so the sections align with the page head at the container's left edge, not centred at x=426.
5. **Chapter hues 1, 2 and 3 cannot be told apart.** In `_src/chapters.json`, change Essentials `#a3392f` to a hue clearly away from rust and brown (suggested teal `#1f6f6b`, white text about 5.9:1), then rerun the contrast measurement.
6. **Dangling footer separator.** In the `build.py` footer template, end the line after "MIT licensed" with no trailing " · ", and put "Part of the Ultimate Business Machines portfolio" in its own `<p>`.

Should-level items carried forward:
- Hide `.bar` at zero ticks in `handbook.js`.
- Link the collar meta "0 of N ticked" to `#skills`.
- Add a declination-diagram figcaption.

Could-level items:
- Per-chapter collar landforms.
- Sign-face `.how-list` counters.
- Caps tracking at .03em.
- Rope-figure crossing gap.
- Tourniquet wording.

**Convergence:** a second round would add little. The six critics overlap on the footer and the numbering, and nothing structural is in dispute. Once the six must-fixes are in, the panel has converged. A rerun would only be worth it to re-screenshot About and the home tiles and confirm items 4 and 5.
