# Compass & Trail

A free, open web handbook of outdoor skills for scouts. It has six chapters, each ending in a skills check you can tick off:

1. Compass navigation
2. Reading a topographic map
3. The Ten Essentials and trip planning
4. Knots and rope
5. Camping and Leave No Trace
6. First aid in the field

The handbook grew from this repository's original guide, *Surveying and Mapping with a Lensatic Compass*. That guide is kept unchanged in [`docs/`](docs/SurveyingAndMappingWithLensaticCompass.json) and is the seed of Chapter 1. The About page lists what was corrected and where every fact comes from.

Compass & Trail is independent. It is not affiliated with or endorsed by any scouting organisation.

## Layout

```
_src/
  chapters.json       # chapter order, colours, blurbs and skills checks
  pages/*.html        # one body per page (front matter, then HTML)
  layout.html         # shared masthead and footer
  build.py            # writes site/ (standard-library Python, no dependencies)
site/                 # the deployable static site (committed)
  css/handbook.css
  js/handbook.js      # skills-check ticks (saved in the browser) and the bearing calculator
  original/           # downloadable copy of the original JSON guide
  favicon.svg
docs/                 # the original guide, unchanged
index.html            # redirects to site/
vercel.json           # static deploy config (root and site/)
```

## Editing

Change a chapter in `_src/pages/`, or the chapter list and skills checks in `_src/chapters.json`. Then rebuild:

```bash
python _src/build.py
```

The build adds each chapter's "On this page" list from its `<h2 id>` headings. It stops with an error on a dead local link, a duplicate id or a broken in-page anchor. Commit the rebuilt `site/` along with your change.

Please give a source for any safety, navigation or first-aid fact you add.

## Deploying

The repo deploys as a plain static site on Vercel or Shadw with no build step. `vercel.json` serves `site/` whether the project's root directory is blank or set to `site`. There is deliberately no `package.json` or framework config at the root.

## Contributing and licence

See [CONTRIBUTING.md](CONTRIBUTING.md). MIT licensed; see [LICENSE](LICENSE).
