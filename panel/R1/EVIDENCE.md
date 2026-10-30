# R1 evidence: Guides → "Compass & Trail", an open web handbook for scouts

Site: `H:/UBM/_guides/site` (9 pages: index, compass, maps, essentials, knots, camping, first-aid, about, 404).
Source: `_src/build.py`, `_src/chapters.json`, `_src/pages/*.html`; CSS `site/css/handbook.css`; JS `site/js/handbook.js`.
Screenshots: `H:/UBM/_guides/panel/shots/<page>-<1440|390>-<light|dark>.png` (1440-light also has a `-fold` crop). Measurements are in `panel/shots/measure.json`.

Brief from the user: keep the original guide (a lensatic compass surveying JSON) and make the repo a modern web handbook for scouts.

Measured after the last edit (36 runs, 9 pages × 2 widths × 2 schemes):
- Horizontal overflow: none.
- Contrast failures (AA): none.
- Targets under 24 px: five, all inline links in sentences, which WCAG 2.5.8 exempts.
- Build check: no dead local links, no duplicate ids, every in-page anchor resolves.
- External sources: verified in a browser. These include TC 3-25.26, NOAA, USGS, Mountaineers, LNT, CDC (water, ticks, heat, winter), Red Cross and Animated Knots.

Concept: a topographic sheet in a park-service binding.
- Black masthead band (NPS Unigrid).
- Contour linework drawn procedurally by the build as the hero and chapter collars, with every 5th ring an index contour.
- Chapters numbered with coloured badges, and nav items as numbered badges.
- Chapters end in a "Skills check" with checkboxes saved to localStorage, and home tiles show progress.
- Compass chapter: line diagrams (compass parts, declination diagram, resection) and a bearing calculator.
- Print stylesheet.
- About keeps the original JSON verbatim, lists what was corrected and gives sources.
- Independence disclaimer: not affiliated with any scouting organisation.

Inline premortem:
1. Wrong safety or medical content: conservative wording, sourced to CDC and Red Cross, with a "refresher, not training" callout.
2. Looks like an official scouting organisation handbook (trademark or impersonation): an independent name, no emblems, and a footer disclaimer.
3. Wordy and textbook-like: steps as numbered rings, rules as diamonds, skills check as the payoff.

BREAK move: the hero is not a photo of kids in uniform but a generated contour map. The site's own illustration is cartography.
