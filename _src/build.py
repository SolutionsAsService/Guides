"""Build Compass & Trail, an open handbook for scouts, into site/.

    python _src/build.py

Chapters are listed in _src/chapters.json (order, colour, skills check) and written
as HTML bodies in _src/pages/<slug>.html. Each body starts with a front-matter block:

    title: Page title
    description: One sentence for search results
    ---
    <h2 id="...">...</h2> ...

Every <h2 id> becomes an entry in the chapter's "On this page" list. Standard library
only; refuses to finish on a dead local link or a duplicate id.
"""
import html
import json
import math
import pathlib
import re

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
SITE = ROOT / "site"
BOOK = json.loads((SRC / "chapters.json").read_text(encoding="utf-8"))
CHAPTERS = BOOK["chapters"]
e = html.escape


def read_page(slug):
    raw = (SRC / "pages" / f"{slug}.html").read_text(encoding="utf-8")
    head, body = raw.split("\n---\n", 1)
    meta = dict(line.split(": ", 1) for line in head.strip().splitlines())
    return meta, body.strip()


def layout(title, desc, body, current=None):
    out = (SRC / "layout.html").read_text(encoding="utf-8")
    nav = "".join(
        f'<li><a href="{c["slug"]}.html" style="--c:{c["color"]}"{" aria-current=\"page\"" if current == c["slug"] else ""}>'
        f'<span class="n" aria-hidden="true">{c["num"]}</span>{e(c["short"])}</a></li>' for c in CHAPTERS)
    out = (out.replace("{{nav}}", nav).replace("{{title}}", e(title)).replace("{{description}}", e(desc))
           .replace("{{cur:about}}", ' aria-current="page"' if current == "about" else "").replace("{{body}}", body))
    assert "{{" not in out, title
    return out


def contours(w, h, hills, levels=9, step=26, seed=0.0):
    """Closed, wobbly rings around each hill: a topographic map drawn from a formula.
    Every fifth ring is an index contour, drawn heavier, as on a USGS sheet."""
    paths = []
    for hi, (cx, cy, base) in enumerate(hills):
        for k in range(1, levels + 1):
            r0 = base + step * k
            pts = []
            for i in range(73):
                t = 2 * math.pi * i / 72
                r = r0 * (1 + .10 * math.sin(3 * t + seed + hi) + .06 * math.sin(5 * t + 1.7 * seed + k * .21)
                          + .03 * math.sin(9 * t + hi * 2.3))
                pts.append(f"{cx + r * math.cos(t):.1f} {cy + r * .72 * math.sin(t):.1f}")
            cls = "ct ix" if k % 5 == 0 else "ct"
            paths.append(f'<path class="{cls}" d="M{" L".join(pts)}Z"/>')
    return f'<svg class="topo" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">{"".join(paths)}</svg>'


def checks(c):
    items = "".join(
        f'<li><label><input type="checkbox" data-check="{c["slug"]}-{i}"><span>{e(t)}</span></label></li>'
        for i, t in enumerate(c["checks"]))
    return f'''<section class="skills" aria-labelledby="skills-h" data-chapter="{c["slug"]}" data-total="{len(c["checks"])}">
  <h2 id="skills-h">Skills check</h2>
  <p>Tick each skill once you can do it without the book, in front of a leader or a friend who already can. Your ticks are saved in this browser only.</p>
  <ol class="checklist">{items}</ol>
  <p class="skills-foot"><span class="progress-text" data-progress="{c["slug"]}">0 of {len(c["checks"])} skills</span> <button type="button" class="link-btn" data-reset="{c["slug"]}">Clear my ticks</button></p>
</section>'''


def chapter_page(c, i):
    meta, body = read_page(c["slug"])
    ids = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    toc = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in ids) + '<li><a href="#skills-h">Skills check</a></li>'
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    prev_c = CHAPTERS[i - 1] if i else None
    next_c = CHAPTERS[i + 1] if i + 1 < len(CHAPTERS) else None
    pager = "".join([
        f'<a class="pg prev" href="{prev_c["slug"]}.html"><small>Chapter {prev_c["num"]}</small>{e(prev_c["name"])}</a>' if prev_c else "",
        f'<a class="pg next" href="{next_c["slug"]}.html"><small>Chapter {next_c["num"]}</small>{e(next_c["name"])}</a>' if next_c else
        '<a class="pg next" href="index.html"><small>Finished</small>Back to all chapters</a>'])
    page = f'''<header class="collar" style="--c:{c["color"]}">
  {contours(1400, 420, [(1180, 230, 10), (1380, 40, 30)], levels=7, step=24, seed=c["num"])}
  <div class="wrap collar-in">
    <p class="chap-no"><span class="badge" aria-hidden="true">{c["num"]}</span>Chapter {c["num"]} of {len(CHAPTERS)}</p>
    <h1>{e(c["name"])}</h1>
    <p class="lede">{e(c["blurb"])}</p>
    <p class="meta">About {max(1, round(words / 200))} minutes to read · {len(c["checks"])} skills · <a href="#skills-h" class="progress-text" data-progress="{c["slug"]}">0 of {len(c["checks"])} ticked</a></p>
  </div>
</header>
<div class="wrap chapter" style="--c:{c["color"]}">
  <nav class="toc" aria-label="On this page"><p class="toc-h">On this page</p><ol>{toc}</ol></nav>
  <article class="prose">
{body}
{checks(c)}
  </article>
</div>
<div class="wrap"><nav class="pager" aria-label="Chapters">{pager}</nav></div>'''
    return layout(meta["title"], meta["description"], page, c["slug"])


def main():
    SITE.mkdir(exist_ok=True)
    written = []
    for i, c in enumerate(CHAPTERS):
        (SITE / f'{c["slug"]}.html').write_text(chapter_page(c, i), encoding="utf-8", newline="\n")
        written.append(f'{c["slug"]}.html')

    tiles = "".join(f'''<li class="tile" style="--c:{c["color"]}"><a href="{c["slug"]}.html">
  <span class="badge" aria-hidden="true">{c["num"]}</span>
  <span class="t-name">{e(c["name"])}</span>
  <span class="t-blurb">{e(c["blurb"])}</span>
  <span class="t-prog"><span class="bar" aria-hidden="true" hidden><i data-bar="{c["slug"]}" data-total="{len(c["checks"])}"></i></span><span class="progress-text" data-progress="{c["slug"]}">{len(c["checks"])} skills</span></span>
</a></li>''' for c in CHAPTERS)
    meta, intro = read_page("index")
    home = f'''<header class="hero">
  {contours(1600, 640, [(1260, 330, 14), (1560, 40, 40), (180, 620, 60)], levels=10, step=26, seed=.6)}
  <div class="wrap hero-in">
    <p class="kicker">{e(BOOK["tagline"])}</p>
    <h1>Compass<br><span class="amp">&amp;</span> Trail</h1>
    <p class="lede">Find your way with a map and compass, pack for the day, tie the knots that matter, camp lightly and look after each other. Six chapters, each ending in a skills check you can tick off as you learn.</p>
    <p class="actions"><a class="btn" href="{CHAPTERS[0]["slug"]}.html">Start with the compass</a> <a class="btn btn-quiet" href="#chapters">All chapters</a></p>
  </div>
</header>
<section class="wrap" id="chapters" aria-labelledby="ch-h">
  <h2 id="ch-h" class="sec-h">Chapters</h2>
  <ol class="tiles">{tiles}</ol>
</section>
{intro}'''
    (SITE / "index.html").write_text(layout(meta["title"], meta["description"], home), encoding="utf-8", newline="\n")

    meta, about = read_page("about")
    original = (ROOT / "docs" / "SurveyingAndMappingWithLensaticCompass.json").read_text(encoding="utf-8")
    about = about.replace("{{original}}", e(original))
    (SITE / "about.html").write_text(layout(meta["title"], meta["description"], about, "about"), encoding="utf-8", newline="\n")

    meta, nf = read_page("404")
    (SITE / "404.html").write_text(layout(meta["title"], meta["description"], nf), encoding="utf-8", newline="\n")
    written += ["index.html", "about.html", "404.html"]

    problems = []
    for w in written:
        text = (SITE / w).read_text(encoding="utf-8")
        for ref in re.findall(r'(?:href|src)="([^"#?]+)', text):
            if not re.match(r"[a-z]+:|//", ref) and not (SITE / ref).is_file():
                problems.append(f"{w}: dead link {ref}")
        ids = re.findall(r'\sid="([^"]+)"', text)
        problems += [f"{w}: duplicate id {i}" for i in {i for i in ids if ids.count(i) > 1}]
        problems += [f"{w}: missing anchor #{a}" for a in re.findall(r'href="#([^"]+)"', text) if a not in ids and a != "main"]
    assert not problems, "\n".join(problems)
    print(f"built {len(written)} pages")


if __name__ == "__main__":
    main()
