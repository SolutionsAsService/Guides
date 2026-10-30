# Design log: Guides → Compass & Trail (DADA-lite, Adaptive)

The previous version is kept on the branch `legacy-2026-10-30`: one JSON file, *Surveying and Mapping with a Lensatic Compass*.

## Brief
Keep the original guide and turn the repo into a modern web handbook for scouts. It is multi-page: one page per chapter, plus home, About and 404.

## Anchors
- **NPS Unigrid (Vignelli).** A black masthead band, condensed signage type, and a strict column.
- **USGS topographic sheet.** Contour linework with index contours every fifth ring, the map-margin declination diagram, and the brown, blue, green and black colour code.
- **The field notebook.** A traverse log table, worked examples and skills you sign off.

## Concept
A topographic sheet in a park-service binding.
- **Contours as illustration.** The build draws contour rings from a formula, as the home hero and as each chapter's collar.
- **Navigation.** Chapters are numbered badges in the masthead.
- **Skills check.** Every chapter ends with one, saved in the browser, and the home tiles show progress.
- **Original guide.** Chapter 1 is the original guide, corrected and expanded, with line diagrams and a bearing calculator.
- **About page.** The original JSON is kept verbatim on About and in `docs/`, along with what was corrected and the sources.

## Premortem (inline)
1. **Wrong safety or medical advice.** First aid is framed as "a refresher, not training". Every first-aid and water point is sourced to the CDC or Red Cross, and the sources were verified in a browser.
2. **Mistaken for an official scouting handbook.** The handbook has an independent name and no emblems, and the footer and About page carry a disclaimer.
3. **A wall of textbook text.** Steps are numbered rings, rules are diamonds, and parts and landforms are definition rows. Each chapter has a sticky "On this page" list, and the skills check gives a reason to finish.

## BREAK move
There are no stock photos of kids in uniform. The handbook's only illustration is cartography and line drawing, which is also what it teaches.

## Panel R1 (Vignelli, Shklovsky, Krug, Tufte, a navigation and wilderness first-aid instructor, Bringhurst)
All six critics said "ship" or "ship with fixes"; the full text is in `panel/R1/panel.md`. Must-fixes and how each was resolved:

| Must-fix | Resolution |
|---|---|
| The traverse example closed 22 m off (11.5%) against the page's own "under 5%" rule | Leg 4 is now 316°, 44 m. It closes about 1 m off (0.6%), checked by computation |
| "Folding the thumb loop locks the dial" was wrong | It is the lens bracket that locks the dial when folded down |
| The timber-hitch drag tip was ambiguous | It now names the back end (hitch) and the front end (half hitch) |
| The About column was off the grid | `.prose` is nested inside `.wrap` |
| Chapters 1–3 had near-identical rust colours | Essentials is now teal `#1f6f6b`; contrast was re-measured |
| A dangling separator in the footer | The portfolio link has its own line |

"Should" items that were also done:
- Empty progress bars are hidden.
- The chapter-header tick count links to the skills check.
- The declination diagram has a caption ("east declination, not to scale").
- The home step numbers use the heading face.

The panel converged, so there was no R2.

Fixes made before the panel, from screenshots:
- The index-line leader on the compass diagram pointed at the needle; it now points at the index line.
- Resection lines overshot the observer; they now end at the observer, and labels have halos.
- Wide diagrams scroll sideways on phones instead of shrinking to unreadable sizes.
- The TOC columns no longer split items.
- The calculator's select labels were cut off; they are shorter now.

## Measured after the last edit
- **Pages:** 9 pages × 2 widths × 2 colour schemes.
- **Horizontal overflow:** none.
- **AA contrast failures:** none.
- **Targets under 24 px:** five inline links inside sentences, which WCAG 2.5.8 exempts.
- **Build:** no dead links, no duplicate ids, every in-page anchor resolves.
- **Behaviour test in Chrome:**
  - Ticks save and update the chapter, footer and home tile counts, and reset clears them.
  - Calculator: 10° magnetic with 12° W declination gives 358° true; 85° true with 10° E gives 75° magnetic, with correct back bearings.
  - No script errors.

## Open items
- Knot steps are text only. Drawing the knots accurately was out of scope, so each knot links to its Animated Knots animation instead (the taut-line hitch links to the related midshipman's hitch).
- The contour collar uses the same landform for every chapter, with only a seed change.
