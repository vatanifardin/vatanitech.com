#!/usr/bin/env python3
"""Builds every page of vatanitech.com as plain HTML, in three languages.

Run:  python3 -I _tools/build.py   (from the site folder)

English is the top of the site (/, /petrogram/ ...); Azerbaijani is the same
pages under /az/ and Russian under /ru/. Every text of the site is one row of
site_texts.py (English, Azerbaijani, Russian); the page layout is here.

Other inputs in this folder: flat_map.json (from make_land.py), terms.json
(the app's terms of use in 7 languages), privacy_old.html + privacy_texts.py
(the privacy policy and its 21 November 2026 changes), delete_texts.py (the
page for deleting an account, in 7 languages), georulers_texts.py (what the
privacy policy, delete page and terms of the two mining apps, Geo-Rulers and
OreGram, say differently from PetroGram's).
The folder name starts with "_", so GitHub Pages does not publish it.
"""
import html, json, os, re
from pathlib import Path
from urllib.parse import quote

T = Path(__file__).resolve().parent
OUT = T.parent


def app_folder(folder, env):
    """The folder of an app (some privacy texts are read from its docs): the
    Mac keeps it in ~/Developer/<folder>, the PC in ~/<folder>. Another place
    can be given for one run in the environment variable <env>, for example
    GEO_RULERS_APP=/path/to/geo-rulers python3 -I _tools/build.py"""
    places = [Path('/Users/fardinvatani/Developer') / folder,
              Path.home() / 'Developer' / folder, Path.home() / folder]
    if os.environ.get(env):
        places = [Path(os.environ[env]).expanduser()]
    return next((p for p in places if (p / 'docs').is_dir()), None)


APP = app_folder('petrogram', 'PETROGRAM_APP')
assert APP, 'PetroGram app folder not found'


def rd(p):
    """Read a text file (always UTF-8, on the Mac and on the PC)."""
    return Path(p).read_text(encoding='utf-8')


def wr(p, text):
    """Write a text file: UTF-8, Unix line ends, folders made as needed."""
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


# ------------------------------------------------------------- languages
SITE = 'https://vatanitech.com'
LANGS = ('en', 'az', 'ru')                  # the order of the rows in site_texts.py
NAMES = {'en': 'English', 'az': 'Azərbaycanca', 'ru': 'Русский'}
PRE = {'en': '', 'az': '/az', 'ru': '/ru'}  # where each language lives on the site
LOCALE = {'en': 'en_US', 'az': 'az_AZ', 'ru': 'ru_RU'}
L = 'en'                                    # the language being built (set in the loop at the end)

exec(rd(T / 'site_texts.py'))               # defines TX
for _k, _row in TX.items():
    assert len(_row) == len(LANGS) and all(_row), ('a text is missing in site_texts.py', _k)


def t(key):
    """A text of the site in the language being built."""
    return TX[key][LANGS.index(L)]


def e(key):
    """The same, made safe to sit inside an HTML attribute."""
    return html.escape(t(key))


def u(path):
    """A link to a page of the site, in the language being built."""
    return PRE[L] + path


def data(value):
    """A list or table handed to the scripts through a data- attribute."""
    return html.escape(json.dumps(value, ensure_ascii=False))


MARK = ('<svg viewBox="0 0 120 100" aria-hidden="true">'
        '<polyline points="15,15 60,85 105,15" fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
        '<polyline points="36.7,15 60,51.4 83.3,15" fill="none" stroke="#2cc4b8" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def fonts():
    # The italic accent font, Instrument Serif, has no Cyrillic letters and no
    # Azerbaijani "ə", so those two languages use Playfair Display instead.
    serif = 'Instrument+Serif:ital@1' if L == 'en' else 'Playfair+Display:ital@1'
    return ('<link rel="preconnect" href="https://fonts.googleapis.com">'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            f'<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family={serif}&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">')


def ico(body):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


I_OFFLINE = ico('<path d="M2 8.5a15 15 0 0 1 20 0"/><path d="M5.5 12.2a10 10 0 0 1 13 0"/><path d="M9 15.8a5 5 0 0 1 6 0"/><circle cx="12" cy="19.2" r=".9" fill="currentColor"/><path d="M4 3l16 18"/>')
I_FOCUS = ico('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1" fill="currentColor"/>')
I_CHECK = ico('<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.8 2.8L16 9.5"/>')
I_SHIELD = ico('<path d="M12 3l7 3v5.5c0 4.4-3 8-7 9.5-4-1.5-7-5.1-7-9.5V6l7-3z"/><path d="M9 12l2.2 2.2L15 10.5"/>')
I_SWAP = ico('<path d="M7 4v14m0 0l-3-3m3 3l3-3M17 20V6m0 0l-3 3m3-3l3 3"/>')
I_GLOBE = ico('<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9s1.3-6.4 3.8-9z"/>')
I_FLAME = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2.5c1 3.2 4.5 4.8 4.5 9.2a4.5 4.5 0 0 1-9 0c0-1.7.8-2.9 1.7-3.8.3 1.3 1 2 1.7 2C11 7.800 10.400 5.200 12 2.500z"/></svg>'


# The accent colour of an app's pages (a light tone of the app's own colour
# and a lighter one), in place of the studio's teal: see --acc in site.css.
ACCENT = {'oregram': ('226,176,64', '255,226,150'), 'geo-rulers': ('236,138,68', '255,200,156'),
          'petro-rulers': ('255,200,40', '255,232,150'), 'marinegram': ('86,156,255', '176,214,255'), 'quran-guardians': ('52,190,130', '160,236,200'),
          'domino-freedom': ('60,200,140', '170,240,205'), 'domino-global': ('178,120,255', '220,196,255')}


def lang_links(path):
    """The same page in each language (the one being read is marked)."""
    return ''.join(
        f'<a href="{PRE[l]}{path}" lang="{l}" hreflang="{l}"' + (' aria-current="true"' if l == L else '') + f'>{NAMES[l]}</a>'
        for l in LANGS)


def page(key, body, path='/', scripts=(), found=True, name=None, app=None):
    """One whole page. key picks its title and description in site_texts.py;
    path is its address in English ("/petrogram/"), the same in every language.
    name: another app, whose name replaces PetroGram (and Geo-Rulers) in the
    title and description; app: that app's folder on the site, for the footer."""
    title, desc = html.escape(t(key + '_title')), html.escape(t(key + '_desc'))
    if name:
        title, desc = (x.replace('PetroGram', name).replace('Geo-Rulers', name) for x in (title, desc))
    tags = ''.join(f'<script src="{s}" defer></script>\n' for s in scripts)
    if found:   # tell search engines where the page is and where its other languages are
        seo = (f'<link rel="canonical" href="{SITE}{u(path)}">\n'
               # proves to Google Search Console that the site is ours (not a secret)
               + '<meta name="google-site-verification" content="VTXQPLOQSYm-PyBicOfBXb4ScrtuZDwoSpe1uawuOJQ">\n'
               + ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{PRE[l]}{path}">\n' for l in LANGS)
               + f'<link rel="alternate" hreflang="x-default" href="{SITE}{path}">\n')
        switch = lang_links(path)
    else:       # the "not found" page: its language menu leads to the home pages
        seo = '<meta name="robots" content="noindex">\n'
        switch = lang_links('/')
        if L == 'en':
            # GitHub Pages shows this one page for every wrong address, so a
            # wrong address under /az/ or /ru/ is sent on to that language's own page.
            seo += ('<script>(function(){var m=location.pathname.match(/^\\/(az|ru)(\\/|$)/);'
                    "if(m&&!/\\/404\\.html$/.test(location.pathname))location.replace('/'+m[1]+'/404.html')})()</script>\n")
    # The footer leads to PetroGram's pages; on the pages of another app, to
    # that app's own page, privacy policy and terms of use.
    fname, fapp = (name or NAME[app], app) if app else ('PetroGram', 'petrogram')
    foot = f'''<a href="{u(f'/{fapp}/')}">{fname}</a>
      <a href="{u(f'/{fapp}/privacy/')}">{t('privacy')}</a>
      <a href="{u(f'/{fapp}/terms/')}">{t('terms')}</a>'''
    # An app's pages wear the app's own accent colour.
    tint = ' style="--acc:{};--acc2:{}"'.format(*ACCENT[app]) if app in ACCENT else ''
    return f'''<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#04060c">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://vatanitech.com/assets/img/icon-512.png">
<meta property="og:url" content="https://vatanitech.com{u(path)}">
<meta property="og:locale" content="{LOCALE[L]}">
{seo}<link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
{fonts()}
<link rel="stylesheet" href="/assets/site.css">
<script>document.documentElement.classList.add('js');setTimeout(function(){{if(!window.VL_READY)document.documentElement.classList.remove('js')}},4000)</script>
</head>
<body data-copied="{e('copied')}" data-write="{e('write_to')}"{tint}>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{u('/')}" aria-label="{e('home_aria')}">{MARK}<b>Vatani</b><span>Tech</span></a>
    <nav class="nav" aria-label="{e('nav_main')}">
      <a href="{u('/#apps')}">{t('nav_apps')}</a>
      <a href="{u('/#principles')}">{t('nav_how')}</a>
      <a class="btn" href="{u('/#contact')}">{t('nav_contact')}</a>
    </nav>
    <details class="lang">
      <summary aria-label="{e('lang')}: {NAMES[L]}">{I_GLOBE}<span>{L.upper()}</span></summary>
      <div class="lang-menu">{switch}</div>
    </details>
  </div>
</header>
{body}
<footer class="site-footer">
  <div class="wrap">
    <a class="brand" href="{u('/')}" aria-label="{e('home_aria')}">{MARK}<b>Vatani</b><span>Tech</span></a>
    <span>© 2026 Vatani Tech · {t('foot_place')}</span>
    <nav aria-label="{e('nav_footer')}">
      {foot}
      <a href="mailto:support@vatanitech.com">support@vatanitech.com</a>
    </nav>
    <nav class="foot-langs" aria-label="{e('lang')}">{switch}</nav>
  </div>
  <div class="wordmark" aria-hidden="true">Vatani Tech</div>
</footer>
{tags}</body>
</html>
'''


# ------------------------------------------------- the living feature tiles
# On another app's page the same tiles show that app's texts: V names, for a
# row of site_texts.py, the row to use instead (set in geo(), empty otherwise).
V = {}


def tt(key):
    return t(V.get(key, key))


def tile(cls, viz, cap, title, text, d=0):
    return (f'<article class="tile glow rv {cls}" style="--d:{d:.2f}s">\n<div class="viz">{viz}</div>\n'
            f'<div class="cap">{cap}</div><h4>{title}</h4><p>{text}</p>\n</article>')


def t_map(cls, d=0, pins=None):
    dots = ''.join(f'M{(lon + 180) * 2:g} {(84 - lat) * 2:g}h0' for lon, lat in json.loads(rd(T / 'flat_map.json')))
    # Well-known oil and gas regions (lon, lat).
    pins = pins or [(-102.5, 32), (-90, 27.5), (-113, 55.5), (-42, -24.5), (2.5, 58.5), (6, 4.8),
            (50.5, 40.3), (50.5, 27), (73, 61.5), (118.5, 38.5), (116, -20.5)]
    marks = ''.join(
        f'<g transform="translate({(lon + 180) * 2:g} {(84 - lat) * 2:g})"><circle class="ring" r="3" style="--d:{(i * 0.37) % 2.8:.2f}s"/><circle class="core" r="2.6"/></g>'
        for i, (lon, lat) in enumerate(pins))
    viz = (f'<div class="vmap"><svg viewBox="0 0 720 284" role="img" aria-label="{html.escape(tt("map_aria"))}">'
           f'<path class="dots" d="{dots}"/>{marks}</svg></div>')
    return tile(cls, viz, tt('map_cap'), tt('map_h'), tt('map_p'), d)


def t_conv(cls, d=0):
    pairs = tt('conv_pairs')     # site.js rolls through them; the first one is shown at the start
    viz = (f'<div class="conv" data-conv data-pairs="{data(pairs)}" aria-label="{e("conv_aria")}">'
           f'<div class="row"><span class="num" data-a>{pairs[0][0]}</span><span class="unit" data-ua>{pairs[0][1]}</span></div>'
           f'<div class="swap">{I_SWAP}</div>'
           f'<div class="row out"><span class="num" data-b>{pairs[0][2]}</span><span class="unit" data-ub>{pairs[0][3]}</span></div></div>')
    return tile(cls, viz, t('conv_cap'), tt('conv_h'), tt('conv_p'), d)


def t_flash(cls, d=0):
    cards = tt('flash_cards')    # site.js flips through them
    viz = (f'<div class="flash" data-cards="{data(cards)}" aria-label="{e("flash_aria")}"><div class="flash-in">'
           f'<div class="face front"><small>{t("flash_term")}</small><b>{cards[0][0]}</b></div>'
           f'<div class="face back"><small>{t("flash_meaning")}</small><span>{cards[0][1]}</span></div>'
           '</div></div>')
    return tile(cls, viz, tt('flash_cap'), tt('flash_h'), tt('flash_p'), d)


def t_quiz(cls, d=0, opts=('Bottom oil pressure', 'Blowout preventer', 'Barrel of petroleum')):
    viz = (f'<div class="quiz" aria-label="{e("quiz_aria")}">'
           f'<div class="q"><span>{tt("quiz_q")}</span>'
           '<span class="ringbox"><svg viewBox="0 0 44 44"><circle class="tr" cx="22" cy="22" r="18"/><circle class="pr" cx="22" cy="22" r="18"/></svg>8/10</span></div>'
           f'<div class="opt"><i></i>{opts[0]}</div>'
           f'<div class="opt ok"><i>✓</i>{opts[1]}</div>'
           f'<div class="opt"><i></i>{opts[2]}</div>'
           f'<span class="streak">{I_FLAME} {t("quiz_streak")}</span></div>')
    return tile(cls, viz, t('quiz_cap'), tt('quiz_h'), tt('quiz_p'), d)


def t_lang(cls, d=0, words='Knowledge|Bilik|Знание|معرفة|Conocimiento|Savoir|知识', codes=('EN', 'AZ', 'RU', 'AR', 'ES', 'FR', '中文')):
    chips = ''.join(f'<span class="chip{" on" if i == 0 else ""}">{c}</span>' for i, c in enumerate(codes))
    viz = (f'<div class="langs7"><div class="langword" data-words="{words}">{words.split("|")[0]}</div>'
           f'<div class="chips">{chips}</div></div>')
    return tile(cls, viz, t('lang_cap'), tt('lang_h'), tt('lang_p'), d)


def t_market(cls, d=0, chips=None):
    l1 = 'M0 122 C 30 112, 50 92, 80 98 S 130 62, 160 72 S 210 112, 240 94 S 300 32, 330 46 S 385 24, 410 30'
    l2 = 'M0 142 C 40 134, 70 122, 100 128 S 160 102, 200 110 S 260 132, 300 114 S 380 72, 410 80'
    viz = (f'<div class="chart"><svg viewBox="0 0 420 170" role="img" aria-label="{e("market_aria")}">'
           '<defs><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" style="stop-color:var(--teal)" stop-opacity=".32"/><stop offset="1" style="stop-color:var(--teal)" stop-opacity="0"/></linearGradient></defs>'
           '<line class="grid" x1="0" x2="420" y1="40" y2="40"/><line class="grid" x1="0" x2="420" y1="85" y2="85"/><line class="grid" x1="0" x2="420" y1="130" y2="130"/>'
           f'<path class="area" fill="url(#ar)" d="{l1} L410 170 L0 170 Z"/>'
           f'<path class="l2" pathLength="1" d="{l2}"/><path class="l1" pathLength="1" d="{l1}"/>'
           '<g class="end" transform="translate(410 30)"><circle class="ring" r="4"/><circle r="4" style="fill:var(--teal-2)"/></g>'
           '</svg><div class="chips">'
           + ''.join(f'<span class="chip{" on" if i == 0 else ""}">{c}</span>' for i, c in enumerate(chips or ['Brent', 'WTI', 'Henry Hub', t('market_rigs')]))
           + '</div></div>')
    return tile(cls, viz, t('market_cap'), tt('market_h'), tt('market_p'), d)


def t_talk(cls, d=0):
    viz = (f'<div class="talk" aria-label="{e("talk_aria")}">'
           f'<div class="ask">{tt("talk_q")}</div>'
           f'<div class="ans"><small>{t("talk_model")}</small><div class="ln"></div><div class="ln"></div><div class="ln"></div></div></div>')
    return tile(cls, viz, t('talk_cap'), tt('talk_h'), tt('talk_p'), d)


def t_offline(cls, d=0):
    viz = f'<div class="offline"><span></span><span></span><span></span><div class="core">{I_OFFLINE}</div></div>'
    return tile(cls, viz, t('off_cap'), t('off_h'), tt('off_p'), d)


def t_more(cls, d=0, width=520):
    viz = (f'<div class="chips" style="justify-content:center;max-width:{width}px">'
           + ''.join(f'<span class="chip">{i}</span>' for i in tt('more_items')) + '</div>')
    return tile(cls, viz, tt('more_cap'), tt('more_h'), tt('more_p'), d)


# ---- Geo-Rulers' own tiles: a ruler, a protractor, the camera scanner and
# the app it belongs with.
ROCK = 'M108 100 L132 62 L176 40 L236 36 L282 58 L300 92 L286 104 L122 106 Z'
FACETS = 'M132 62 L190 74 L236 36 M190 74 L176 40 M190 74 L282 58 M190 74 L210 105 M282 58 L286 104'


def t_ruler(cls, d=0, art=None):
    # 6 units to a millimetre; the sample lies from the 1 cm mark to 4.2 cm.
    ticks = ''.join(f'<line class="tick" x1="{48 + i * 6}" x2="{48 + i * 6}" y1="118" y2="{134 if i % 10 == 0 else 128 if i % 5 == 0 else 124}"/>' for i in range(57))
    nums = ''.join(f'<text x="{48 + i * 60}" y="150" text-anchor="middle">{i}</text>' for i in range(6))
    viz = (f'<div class="rulerviz"><svg viewBox="0 0 420 170" role="img" aria-label="{html.escape(tt("gx_ruler_aria"))}">'
           + (art or f'<path class="rock" d="{ROCK}"/><path class="facet" d="{FACETS}"/>') +
           f'<rect class="body" x="30" y="118" width="372" height="42" rx="7"/>{ticks}{nums}'
           '<line class="guide g1" x1="108" x2="108" y1="22" y2="118"/><line class="guide g2" x1="300" x2="300" y1="22" y2="118"/>'
           '<g class="read"><line x1="108" x2="300" y1="22" y2="22"/>'
           f'<text x="204" y="14" text-anchor="middle">{t("gx_ruler_read")}</text></g></svg></div>')
    return tile(cls, viz, t('cap_measure'), t('gx_ruler_h'), tt('gx_ruler_p'), d)


def t_angle(cls, d=0):
    import math
    ticks = ''
    for k in range(19):
        a, r = math.radians(k * 10), (98 if k % 3 == 0 else 108)
        ticks += (f'<line class="tick" x1="{150 + 120 * math.cos(a):.1f}" y1="{160 - 120 * math.sin(a):.1f}" '
                  f'x2="{150 + r * math.cos(a):.1f}" y2="{160 - r * math.sin(a):.1f}"/>')
    nums = ''.join(f'<text x="{150 + 84 * math.cos(math.radians(k)):.1f}" y="{164 - 84 * math.sin(math.radians(k)):.1f}" text-anchor="middle">{k}</text>'
                   for k in (30, 60, 90, 120, 150))
    viz = (f'<div class="angle"><svg viewBox="0 0 300 180" role="img" aria-label="{e("gx_angle_aria")}">'
           f'<path class="arc" d="M30 160 A120 120 0 0 1 270 160 Z"/>{ticks}{nums}'
           '<line class="base" x1="14" x2="286" y1="160" y2="160"/>'
           '<g class="needle"><line x1="150" y1="160" x2="262" y2="160"/><circle cx="262" cy="160" r="4"/></g>'
           '<circle class="hub" cx="150" cy="160" r="6"/>'
           '<text class="deg" x="150" y="128" text-anchor="middle">35°</text></svg></div>')
    return tile(cls, viz, t('cap_measure'), t('gx_angle_h'), t('gx_angle_p'), d)


def t_scan(cls, d=0, art=None):
    rows = ''.join(f'<div class="row" style="--w:{w}%;--d:{i * .18:.2f}s"><span>{n}</span><b>{w}%</b><i></i></div>'
                   for i, (n, w) in enumerate(zip(tt('gx_scan_names'), (82, 11, 5))))
    viz = (f'<div class="scan" aria-label="{e("gx_scan_aria")}"><div class="finder">'
           '<svg viewBox="100 28 208 86" aria-hidden="true">' + (art or f'<path class="rock" d="{ROCK}"/><path class="facet" d="{FACETS}"/>') + '</svg>'
           f'<div class="beam"></div></div><div class="guess">{rows}</div></div>')
    return tile(cls, viz, t('cap_camera'), tt('gx_h2'), tt('gx_p2'), d)


def t_pair(cls, d, slug, other, title, text, link=True):
    """Two apps that belong together; the heading leads to the other one's page (when it has one)."""
    img = lambda a: f'<img src="/assets/img/{a}-icon.png" alt="{html.escape(t("icon_alt_of").format(NAME.get(a, "PetroGram")))}" style="--glow:rgba({SOON_BY[a][3] if a in SOON_BY else "63,81,181"},.9)" loading="lazy">'
    viz = f'<div class="pair">{img(slug)}<span class="link"></span>{img(other)}</div>'
    head = f'<a href="{u(f"/{other}/")}">{title} <span class="arr">→</span></a>' if link else title
    return tile(cls, viz, t('cap_family'), head, text, d)


# ---- Petro-Rulers: a pipe with flanges on the ruler, a valve in the scanner.
PIPE = ('<path class="rock" d="M108 40h12v70h-12z M288 40h12v70h-12z M120 56h168v38h-168z"/>'
        '<path class="facet" d="M120 66h168 M150 56v38 M258 56v38"/>')
VALVE = ('<path class="rock" d="M112 72h10v36h-10z M286 72h10v36h-10z M122 80h54l10-10h36l10 10h54v20h-54l-10 10h-36l-10-10h-54z M196 46h16v24h-16z"/>'
         '<path class="facet" d="M204 46v-10 M174 34h60 M174 34a30 5 0 0 0 60 0a30 5 0 0 0-60 0"/>')


# ---- MarineGram: a ship on the waves, a propeller, a ship's frame turning.
def t_ship(cls, d=0):
    boxes = ''.join(f'<rect class="box{" a" if (i + r) % 3 == 0 else ""}" x="{140 + i * 23}" y="{88 - r * 18}" width="21" height="16"/>'
                    for r in range(3) for i in range(8 - r) if not (r == 2 and i < 2))
    wave = lambda y: 'M-90 %d ' % y + ' '.join('q20 -9 40 0 t40 0' for _ in range(8))
    viz = (f'<div class="ship"><svg viewBox="0 0 420 150" role="img" aria-label="{e("mg_ship_aria")}">'
           f'<g class="boat">{boxes}<path class="hullp" d="M92 60h30v46h-30z M100 46h12v14h-12z M70 106h290l-22 26h-246z"/></g>'
           f'<path class="sea" d="{wave(134)}"/><path class="sea b" d="{wave(144)}"/></svg>'
           '<div class="chips">' + ''.join(f'<span class="chip{" on" if c == t("mg_ship_types")[2] else ""}">{c}</span>' for c in t('mg_ship_types'))
           + '</div></div>')
    return tile(cls, viz, t('gr_cap_read'), t('mg_ships_h'), t('mg_ships_p'), d)


def t_prop(cls, d=0):
    blade = '<path d="M100 100C78 70 84 34 100 24c20 12 22 46 0 76z"{}/>'
    blades = ''.join(blade.format(f' transform="rotate({a} 100 100)"' if a else '') for a in (0, 90, 180, 270))
    viz = (f'<div class="prop"><svg viewBox="0 0 200 200" role="img" aria-label="{e("mg_tech_aria")}">'
           '<circle class="ring o" cx="100" cy="100" r="96"/><circle class="ring" cx="100" cy="100" r="82"/>'
           f'<g class="blades">{blades}</g><circle class="hub" cx="100" cy="100" r="13"/></svg></div>')
    return tile(cls, viz, t('lang_cap'), t('mg_tech_h'), t('mg_tech_p'), d)


def t_hull(cls, d=0):
    # the frames of a hull from stern to bow: place along the ship, width, depth
    ribs = [(-120, 26, 26), (-90, 56, 42), (-60, 70, 50), (-30, 76, 52), (0, 78, 52), (30, 76, 52), (60, 68, 50), (90, 50, 44), (120, 20, 30)]
    viz = ('<div class="hull3" aria-hidden="true"><div>'
           + ''.join(f'<i style="--z:{z}px;--w:{w}px;--h:{h}px"></i>' for z, w, h in ribs)
           + '<b class="keel"></b><b class="deck"></b></div></div>')
    return tile(cls, viz, t('cap_3d'), t('mg_3d_h'), t('mg_3d_p'), d)


# ---- Quran Guardians (first called Hafiz; its key and folder are "quran-guardians" since 28 November 2026): a verse with its translation, words hidden for memorising, the
# days of review. The verse is the first of the Quran, letter for letter as
# in the Tanzil text the app uses (never change it).
BASMALA = 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ'


def t_verse(cls, d=0):
    viz = (f'<div class="verse"><div class="ref">1 : 1</div>'
           f'<div class="ar" lang="ar" dir="rtl" role="img" aria-label="{e("hz_verse_aria")}">{BASMALA}</div>'
           '<div class="tr" aria-hidden="true"><i></i><i></i></div><div class="chips">'
           + ''.join(f'<span class="chip{" on" if i == 0 else ""}">{c}</span>' for i, c in enumerate(['EN', 'TR', 'FA', 'UR', 'ID', 'AZ']))
           + f'</div><a class="src" href="https://tanzil.net" rel="noopener">{t("hz_src")}</a></div>')
    return tile(cls, viz, t('gr_cap_read'), t('hz_h1'), t('hz_p1'), d)


def t_hide(cls, d=0):
    # the first word stays; the others fade one after another ("first words")
    words = ''.join('<span><b style="{}">{}</b></span>'.format(f'--d:{(i - 1) * .5:.1f}s' if i else 'animation:none', w)
                    for i, w in enumerate(BASMALA.split()))
    viz = (f'<div class="hidebox"><div class="hide" lang="ar" dir="rtl" role="img" aria-label="{e("hz_hide_aria")}">{words}</div>'
           '<div class="chips">' + ''.join(f'<span class="chip{" on" if i == 1 else ""}">{c}</span>' for i, c in enumerate(t('hz_modes'))) + '</div></div>')
    return tile(cls, viz, t('flash_cap'), t('hz_h2'), t('hz_hide_p'), d)


def t_sched(cls, d=0):
    days = (1, 3, 7, 14, 30, 60, 120)
    nodes = ''.join(f'<circle cx="{30 + i * 60}" cy="44" r="8" style="--d:{i * .75:.2f}s"/><text x="{30 + i * 60}" y="78" text-anchor="middle">{n}</text>'
                    for i, n in enumerate(days))
    viz = (f'<div class="sched"><svg viewBox="0 0 420 110" role="img" aria-label="{e("hz_sched_aria")}">'
           '<line class="rail" x1="30" x2="390" y1="44" y2="44"/><line class="go" pathLength="1" x1="30" x2="390" y1="44" y2="44"/>'
           f'{nodes}<text class="u" x="210" y="104" text-anchor="middle">{t("hz_days")}</text></svg></div>')
    return tile(cls, viz, t('quiz_cap'), t('hz_sched_h'), t('hz_sched_p'), d)


# ---- The domino games: a chain of dominoes being laid, players round a table.
PIPS = {1: ((15, 15),), 2: ((8, 8), (22, 22)), 3: ((8, 8), (15, 15), (22, 22)), 4: ((8, 8), (22, 8), (8, 22), (22, 22)),
        5: ((8, 8), (22, 8), (15, 15), (8, 22), (22, 22)), 6: ((8, 8), (22, 8), (8, 15), (22, 15), (8, 22), (22, 22))}


def domino(x, y, a, b, upright=False, i=0):
    """One domino at (x, y) with a and b pips; a double stands upright."""
    w, h = (30, 60) if upright else (60, 30)
    bx, by = (0, 30) if upright else (30, 0)
    pips = ''.join(f'<circle cx="{px}" cy="{py}" r="2.6"/>' for px, py in PIPS[a])
    pips += ''.join(f'<circle cx="{px + bx}" cy="{py + by}" r="2.6"/>' for px, py in PIPS[b])
    mid = '<line x1="5" x2="25" y1="30" y2="30"/>' if upright else '<line x1="30" x2="30" y1="5" y2="25"/>'
    return (f'<g transform="translate({x} {y})"><g class="pc" style="--d:{i * .7:.2f}s">'
            f'<rect width="{w}" height="{h}" rx="6"/>{mid}{pips}</g></g>')


def t_domino(cls, d, cap, title, text):
    chain = [(20, 60, 6, 4, False), (84, 45, 4, 4, True), (118, 60, 4, 1, False), (182, 60, 1, 3, False),
             (246, 45, 3, 3, True)]
    pieces = ''.join(domino(x, y, a, b_, up, i) for i, (x, y, a, b_, up) in enumerate(chain))
    viz = f'<div class="domino"><svg viewBox="0 30 296 90" role="img" aria-label="{e("dm_chain_aria")}">{pieces}</svg></div>'
    return tile(cls, viz, cap, title, text, d)


def t_table(cls, d, cap, title, text):
    seats = ''.join(
        f'<g class="seat" transform="translate({x} {y})" style="--d:{i * 1.5:.1f}s"><circle class="ring" r="21"/><circle class="bg" r="16"/>'
        '<circle class="me" cy="-4" r="5"/><path class="me" d="M-9 10a9 8 0 0 1 18 0z"/></g>'
        for i, (x, y) in enumerate(((150, 26), (256, 95), (150, 164), (44, 95))))
    viz = (f'<div class="dtable"><svg viewBox="0 0 300 190" role="img" aria-label="{e("dm_table_aria")}">'
           '<rect class="top" x="84" y="56" width="132" height="78" rx="20"/>'
           '<path class="bone" d="M112 88h24v14h-24z M138 88h24v14h-24z M164 81h14v28h-14z M124 88v14 M150 88v14 M164 95h14"/>'
           f'{seats}</svg></div>')
    return tile(cls, viz, cap, title, text, d)


# ---- Each app's own examples for the shared tiles (see V above), and the
# places on its map. The app's page and its tab on the home page both use them.
VSET = {
    'geo-rulers': dict(flash_cards='gx_flash_cards', flash_cap='gr_cap_read', flash_h='gx_guide_h', flash_p='gx_guide_p', off_p='gr_c9_p'),
    'oregram': dict(map_aria='gr_map_aria', map_h='gr_c5_h', map_p='gr_c5_p', conv_pairs='gr_conv_pairs', conv_h='gr_c1_h', conv_p='gr_c1_p',
                    flash_cards='gr_flash_cards', flash_h='gr_c2_h', flash_p='gr_c2_p', quiz_q='gr_quiz_q', quiz_h='gr_quiz_h', quiz_p='gr_quiz_p',
                    off_p='gr_c9_p', market_h='gr_c7_h', market_p='gr_c7_p', talk_q='gr_talk_q', more_items='gr_more_items'),
    'petro-rulers': dict(gx_ruler_aria='pr_ruler_aria', gx_ruler_p='pr_ruler_p', gx_scan_names='pr_scan_names', gx_h2='pr_h2', gx_p2='pr_p2',
                         flash_cards='pr_flash_cards', flash_cap='gr_cap_read', flash_h='pr_guide_h', flash_p='pr_guide_p'),
    'marinegram': dict(map_aria='mg_map_aria', map_h='mg_h1', map_p='mg_p1', flash_cards='mg_flash_cards', flash_h='mg_h2', flash_p='mg_p2', off_p='mg_off_p'),
    'quran-guardians': dict(lang_h='hz_lang_h', lang_p='hz_lang_p', off_p='hz_off_p', more_items='hz_free_items', more_cap='cap_free', more_h='hz_h3', more_p='hz_p3'),
    'domino-freedom': dict(off_p='df_p1'),
    'domino-global': dict(map_aria='dm_map_aria', map_cap='cap_together', map_h='dg_h2', map_p='dg_p2'),
}
# Well-known mining regions, great ports, and big cities (lon, lat).
MINES = [(118, -22), (121.5, -30.7), (-69, -24), (-76, -11), (-50, -6), (27.5, -26), (27, -12), (-2, 6),
         (-116, 40.7), (-81, 46.5), (88, 69.3), (67, 48), (110, 41), (137, -4)]
PORTS = [(103.8, 1.3), (4.5, 51.9), (121.5, 31.2), (32.5, 30), (-79.5, 9), (-118.2, 33.7), (-46.3, -24), (31, -29.9),
         (55.3, 25.2), (151.2, -33.9), (-74, 40.7), (49.9, 40.4)]
CITIES = [(-74, 40.7), (-99.1, 19.4), (-46.6, -23.5), (-0.1, 51.5), (29, 41), (49.9, 40.4), (31.2, 30), (3.4, 6.5),
          (55.3, 25.2), (77.2, 28.6), (116.4, 39.9), (139.7, 35.7), (106.8, -6.2), (151.2, -33.9), (37.6, 55.8)]
ORE_QUIZ = ('Nominal stripping ratio', 'Net smelter return', 'New surface reserve')
HAFIZ_LANGS = ('Read|Читать|Oku|بخوان|اقرأ|پڑھیں|Baca|Oxu', ('EN', 'RU', 'TR', 'FA', 'AR', 'UR', 'ID', 'AZ'))


def vset(slug):
    V.clear()
    V.update(VSET.get(slug, {}))


def panel_tiles(slug, k):
    """The living tiles of an app's tab on the home page (three to five)."""
    vset(slug)
    if slug in ('geo-rulers', 'petro-rulers'):
        pr = slug == 'petro-rulers'
        tiles = [t_ruler('w7', 0, PIPE if pr else None), t_scan('w5', .08, VALVE if pr else None), t_angle(''), t_flash('', .08),
                 t_pair('', .16, slug, 'petrogram' if pr else 'oregram', t(k + '_h3'), t(k + '_p3'))]
    elif slug == 'oregram':
        tiles = [t_map('w7', 0, MINES), t_conv('w5', .08), t_flash(''), t_quiz('', .08, ORE_QUIZ), t_lang('', .16)]
    elif slug == 'marinegram':
        tiles = [t_map('w7', 0, PORTS), t_ship('w5', .08), t_flash(''), t_prop('', .08), t_hull('', .16)]
    elif slug == 'quran-guardians':
        tiles = [t_verse('w7'), t_hide('w5', .08), t_sched('w8'), t_lang('', .08, *HAFIZ_LANGS)]
    elif slug == 'domino-freedom':
        tiles = [t_offline(''), t_table('', .08, t('cap_together'), t('df_h2'), t('df_p2')), t_domino('', .16, t('cap_light'), t('df_h3'), t('df_p3'))]
    else:
        tiles = [t_domino('', 0, t('more_cap'), t('dg_h1'), t('dg_p1')), t_map('', .08, CITIES),
                 t_pair('', .16, slug, 'domino-freedom', t('dg_h3'), t('dg_p3'), link=False)]
    V.clear()
    return tiles


def phone(img, alt, i=None):
    st = f' style="--i:{i};--a:{abs(i)}"' if i is not None else ''
    return f'<div class="phone"{st}><img src="/assets/img/{img}" alt="{html.escape(alt)}" loading="lazy"></div>'


def band(words):
    one = ''.join(f'<span class="{"f" if i % 2 == 0 else ""}">{w}<i>✦</i></span>' for i, w in enumerate(words))
    return f'<div class="band" aria-hidden="true"><div class="band-track">{one}{one}</div></div>'


# The apps that are still being made: address name, name, the colour of the
# glow under the icon, and the captions of its three cards (rows of
# site_texts.py; the texts of an app are its rows "<key>_sub", "<key>_lead",
# "<key>_h1" ... "<key>_p3"). The icon is assets/img/<address name>-icon.png.
# An app in PAGES has its own page at /<address name>/, and its panel links to it.
# OreGram is the small pocket reference for geology and mining and uses
# Geo-Rulers' old rows ("gr_..."). The "-Rulers" apps (Geo-Rulers, rows
# "gx_...", and Petro-Rulers, rows "pr_...") are measuring and camera tools
# only: the reference content is in their "-Gram" partner (owner, 26 and
# 27 November 2026). MarineGram (rows "mg_...") and Quran Guardians (rows "hz_...")
# joined on 27 November 2026.
SOON = [
    ('petro-rulers', 'Petro-Rulers', 'pr', '255,196,0', ('cap_measure', 'cap_camera', 'cap_family')),
    ('geo-rulers', 'Geo-Rulers', 'gx', '194,97,28', ('cap_measure', 'cap_camera', 'cap_family')),
    ('oregram', 'OreGram', 'gr', '184,134,11', ('conv_cap', 'flash_cap', 'map_cap')),
    ('marinegram', 'MarineGram', 'mg', '30,111,217', ('map_cap', 'flash_cap', 'more_cap')),
    ('quran-guardians', 'Quran Guardians', 'hz', '212,175,55', ('gr_cap_read', 'flash_cap', 'cap_free')),
    ('domino-freedom', 'Domino Freedom', 'df', '22,160,102', ('off_cap', 'cap_together', 'cap_light')),
    ('domino-global', 'Domino Global', 'dg', '139,53,201', ('more_cap', 'cap_together', 'cap_family')),
]
SOON_BY = {a[0]: a for a in SOON}
# The order of the tabs on the home page (owner, 26 November 2026; MarineGram
# and Quran Guardians added at the end on 27 November 2026). An app's
# number ("App 02") is its place in this list. The first tab is open at the start.
ORDER = ['petro-rulers', 'petrogram', 'geo-rulers', 'oregram', 'domino-global', 'domino-freedom', 'marinegram', 'quran-guardians']


def num(slug):
    return f'{ORDER.index(slug) + 1:02d}'
# The apps with their own pages (all mining apps, with the texts of
# Geo-Rulers): the app's folder on the computer, the environment variable
# that can name another folder for one run (see app_folder), and the name as
# the big heading of its page.
PAGES = {
    'geo-rulers': ('geo-rulers', 'GEO_RULERS_APP', 'Geo-<em class="s">Rulers</em>'),
    'oregram': ('oregram', 'OREGRAM_APP', 'Ore<em class="s">Gram</em>'),
}


# The apps with a page, a privacy policy and terms of use of their own (see
# solo() and solo_doc(); no page for deleting an account: they have none):
# the name as the big heading, and the shapes of the hero.
SOLO = {
    'petro-rulers': ('Petro-<em class="s">Rulers</em>', 'tools,drop'),
    'marinegram': ('Marine<em class="s">Gram</em>', 'anchor,globe'),
    'quran-guardians': ('Quran <em class="s">Guardians</em>', 'arch'),
}


def tn(key, name):
    """A text of a mining app: the rows "gr_..." are written for Geo-Rulers,
    and another app's name takes its place (also in lists)."""
    v = t(key)
    if isinstance(v, str):
        return v.replace('Geo-Rulers', name)
    return [x.replace('Geo-Rulers', name) for x in v]


def soon_tab(app):
    slug, name = app[0], app[1]
    on = slug == ORDER[0]
    return (f'      <button class="tab" role="tab" id="tab-{slug}" aria-controls="panel-{slug}" aria-selected="{str(on).lower()}"'
            f'{"" if on else TABOFF}><span class="n">{num(slug)}</span>{name}</button>\n')


def soon_panel(app):
    slug, name, k, glow, caps = app
    cards = '\n        '.join(panel_tiles(slug, k))
    acc = ACCENT[slug]
    subject = quote(t('next_subject') + ': ' + name)
    own = (f'<a class="btn solid" href="{u(f"/{slug}/")}">{t("discover_of").format(name)} <span class="arr">→</span></a>'
           if slug in PAGES or slug in SOLO else '')
    return f'''    <div class="panel" role="tabpanel" id="panel-{slug}" aria-labelledby="tab-{slug}" style="--acc:{acc[0]};--acc2:{acc[1]}"{"" if slug == ORDER[0] else " hidden"}>
      <div class="app-line">
        <img src="/assets/img/{slug}-icon.png" alt="{html.escape(t('icon_alt_of').format(name))}" style="--glow:rgba({glow},.9)">
        <div><h3 lang="en">{name}</h3><div class="sub">{tn(k + '_sub', name)}</div></div>
        <div class="chips"><span class="chip on">{t('dev')}</span><span class="chip" lang="en">Android</span><span class="chip" lang="en">iPhone</span></div>
      </div>
      <p class="app-lead">{tn(k + '_lead', name)}</p>
      <div class="bento">
        {cards}
      </div>
      <div class="actions" style="margin-top:26px">{own}<a class="btn" href="mailto:support@vatanitech.com?subject={subject}">{t('next_cta')} <span class="arr">→</span></a></div>
    </div>

'''


# ------------------------------------------------------------------ home
TABOFF = ' tabindex="-1"'   # a tab that is not open


def pg_tab():
    on = ORDER[0] == 'petrogram'
    return (f'      <button class="tab" role="tab" id="tab-petrogram" aria-controls="panel-petrogram" aria-selected="{str(on).lower()}"'
            f'{"" if on else TABOFF}><span class="n">{num("petrogram")}</span>PetroGram</button>\n')


def home():
    # Captions under the hero picture: number, text and, for the studio's
    # name, its language (so that capital letters follow English rules).
    caps = {'mark': ['01', 'Vatani Tech', 'en'], 'globe': ['02', t('cap_globe')], 'drop': ['03', t('cap_drop')]}
    return f'''<main>
<section class="hero" aria-label="{e('hero_aria')}">
  <div class="sculpt"><canvas id="sculpture" data-shapes="mark,globe,drop" data-captions="{data(caps)}" aria-hidden="true"></canvas><div class="sculpt-cap" id="sculpture-cap"></div></div>
  <div class="wrap">
    <div class="hero-copy">
      <span class="pill rv"><i></i>{t('hero_pill')}</span>
      <h1 class="rv" style="--d:.08s">{t('hero_h1')}</h1>
      <p class="lead rv" style="--d:.16s">{t('hero_lead')}</p>
      <div class="actions rv" style="--d:.24s">
        <a class="btn solid" href="#apps">{t('hero_cta1')} <span class="arr">→</span></a>
        <a class="btn" href="#contact">{t('hero_cta2')}</a>
      </div>
    </div>
  </div>
  <div class="scroll-hint" aria-hidden="true">{t('scroll')}</div>
</section>

<div class="stats">
  <div class="wrap">
    <div class="stat rv"><b data-count="500">500</b><span>{t('st_terms')}</span></div>
    <div class="stat rv" style="--d:.08s"><b data-count="600">600</b><span>{t('st_quiz')}</span></div>
    <div class="stat rv" style="--d:.16s"><b data-count="7">7</b><span>{t('st_langs')}</span></div>
    <div class="stat rv" style="--d:.24s"><b><span data-count="100">100</span><small>%</small></b><span>{t('st_offline')}</span></div>
  </div>
</div>
{band(t('band_home'))}

<section class="block" id="apps">
  <div class="wrap">
    <div class="block-head">
      <div class="rv">
        <p class="label"><span class="n">01 /</span> {t('apps_label')}</p>
        <h2>{t('apps_h2')}</h2>
      </div>
      <p class="rv" style="--d:.1s">{t('apps_p')}</p>
    </div>

    <div class="tabs rv" role="tablist" aria-label="{e('nav_apps')}">
{''.join(pg_tab() if s == 'petrogram' else soon_tab(SOON_BY[s]) for s in ORDER)}    </div>

    <div class="panel" role="tabpanel" id="panel-petrogram" aria-labelledby="tab-petrogram"{"" if ORDER[0] == 'petrogram' else " hidden"}>
      <div class="app-line rv">
        <img src="/assets/img/petrogram-icon.png" alt="{e('icon_alt')}">
        <div><h3>PetroGram</h3><div class="sub">{t('pg_sub')}</div></div>
        <div class="chips"><span class="chip on">{t('soon')}</span><span class="chip" lang="en">Android</span><span class="chip" lang="en">iPhone</span></div>
      </div>
      <div class="bento">
        {t_map('w7')}
        {t_conv('w5', .08)}
        {t_flash('', 0)}
        {t_quiz('', .08)}
        {t_lang('', .16)}
      </div>
      <div class="actions rv" style="margin-top:26px"><a class="btn solid" href="{u('/petrogram/')}">{t('discover')} <span class="arr">→</span></a></div>
    </div>

{''.join(soon_panel(SOON_BY[s]) for s in ORDER if s != 'petrogram')}
    <div class="showcase-foot">
      <span>{t('made')}</span>
      <div class="pager">
        <button type="button" id="prev" aria-label="{e('prev_app')}">←</button>
        <span id="count">01 / {len(ORDER):02d}</span>
        <button type="button" id="next" aria-label="{e('next_app')}">→</button>
      </div>
    </div>
  </div>
</section>

<section class="block" id="principles">
  <div class="wrap">
    <div class="block-head">
      <div class="rv">
        <p class="label"><span class="n">02 /</span> {t('nav_how')}</p>
        <h2>{t('how_h2')}</h2>
      </div>
      <p class="rv" style="--d:.1s">{t('how_p')}</p>
    </div>
    <div class="grid4">
      <div class="card glow rv"><div class="ico">{I_OFFLINE}</div><h3>{t('p1_h')}</h3><p>{t('p1_p')}</p></div>
      <div class="card glow rv" style="--d:.08s"><div class="ico">{I_FOCUS}</div><h3>{t('p2_h')}</h3><p>{t('p2_p')}</p></div>
      <div class="card glow rv" style="--d:.16s"><div class="ico">{I_CHECK}</div><h3>{t('p3_h')}</h3><p>{t('p3_p')}</p></div>
      <div class="card glow rv" style="--d:.24s"><div class="ico">{I_SHIELD}</div><h3>{t('p4_h')}</h3><p>{t('p4_p')}</p></div>
    </div>
  </div>
</section>

<section class="block" id="contact" style="padding-top:40px">
  <div class="wrap">
    <div class="contact-card rv">
      <p class="label"><span class="n">03 /</span> {t('nav_contact')}</p>
      <h2>{t('contact_h2')}</h2>
      <p>{t('contact_p')}</p>
      <a class="mail" href="mailto:support@vatanitech.com">support@vatanitech.com <span class="arr">→</span></a>
    </div>
  </div>
</section>
</main>'''


# ------------------------------------------------------------- PetroGram
def petro():
    shots = ['2_learn', '3_upstream', '1_home', '5_maps', '4_quiz']
    fan = '\n'.join(phone(f'pg-{n}.jpg', a, i - 2) for i, (n, a) in enumerate(zip(shots, t('shots'))))
    return f'''<main>
<section class="app-hero">
  <div class="sculpt"><canvas id="sculpture" data-shapes="drop" aria-hidden="true"></canvas></div>
  <div class="wrap">
    <div class="hero-copy">
      <span class="pill rv"><i></i>{t('pg_pill').format(num('petrogram'))}</span>
      <div class="top rv" style="--d:.08s">
        <img class="app-icon" src="/assets/img/petrogram-icon.png" alt="{e('icon_alt')}">
        <h1>Petro<em class="s">Gram</em></h1>
      </div>
      <p class="lead rv" style="--d:.16s">{t('pg_lead')}</p>
      <div class="actions rv" style="--d:.24s">
        <span class="btn" aria-disabled="true">{t('store_ios')}</span>
        <span class="btn" aria-disabled="true">{t('store_play')}</span>
      </div>
      <p class="store-note rv" style="--d:.3s">{t('store_note')}</p>
    </div>
  </div>
</section>
{band(t('band_pg'))}

<section class="block">
  <div class="wrap">
    <div class="block-head">
      <div class="rv">
        <p class="label"><span class="n">{t('feat_n')}</span> {t('feat_label')}</p>
        <h2>{t('feat_h2')}</h2>
      </div>
      <p class="rv" style="--d:.1s">{t('feat_p')}</p>
    </div>
    <div class="bento">
      {t_map('w8')}
      {t_conv('', .08)}
      {t_flash('')}
      {t_quiz('', .08)}
      {t_offline('', .16)}
      {t_market('w7')}
      {t_talk('w5', .08)}
      {t_lang('w5')}
      {t_more('w7', .08)}
    </div>
  </div>
</section>

<section class="block" style="padding-top:20px">
  <div class="wrap">
    <div class="block-head">
      <div class="rv">
        <p class="label"><span class="n">{t('scr_n')}</span> {t('scr_label')}</p>
        <h2>{t('scr_h2')}</h2>
      </div>
      <p class="rv" style="--d:.1s">{t('scr_p')}</p>
    </div>
    <div class="fan rv" aria-label="{e('scr_aria')}">
{fan}
    </div>
  </div>
</section>

<section class="block" style="padding-top:20px">
  <div class="wrap">
    <div class="grid3">
      <div class="card glow rv"><span class="label">{t('sup_label')}</span><h3>{t('sup_h')}</h3><p>{t('sup_p')}</p></div>
      <div class="card glow rv" style="--d:.08s"><span class="label">{t('prv_label')}</span><h3>{t('privacy')}</h3><p>{t('prv_p')} <a href="{u('/petrogram/privacy/')}">{t('read_it')}</a></p></div>
      <div class="card glow rv" style="--d:.16s"><span class="label">{t('trm_label')}</span><h3>{t('terms')}</h3><p>{t('trm_p')} <a href="{u('/petrogram/terms/')}">{t('read_them')}</a></p></div>
    </div>
  </div>
</section>
</main>'''


# ------------------------------------------- Geo-Rulers and OreGram pages
# The page of an app that is still being made: like PetroGram's, but with
# no store buttons and no screenshots (there are none yet). The hero shows
# a cluster of crystals (and, for OreGram, the turning Earth of its maps;
# for Geo-Rulers a protractor on a ruler); the icon stands
# where the screens would be. The slogans are English on the English page and rhyming translations on the others (owner, 26 Nov 2026).
# slug: the app (one of PAGES); its number ("App 02") is its place on the home page.
def geo(slug):
    _, name, k, glow = SOON_BY[slug][:4]
    n = num(slug)
    icon = f'/assets/img/{slug}-icon.png'
    alt = e('icon_alt_of').format(name)
    ore, _, dig = tn('gr_slogans', name)   # the second one heads the features (gr_feat_h2)
    mail = f'mailto:support@vatanitech.com?subject={quote(t("next_subject") + ": " + name)}'
    # The features as living tiles, like PetroGram's page. The tool app has
    # its own drawings; OreGram shows PetroGram's with mining examples.
    vset(slug)
    if k == 'gx':
        shapes = 'tools,crystal'
        tiles = [t_ruler('w7'), t_angle('w5', .08), t_scan('w7'), t_flash('w5', .08),
                 t_lang(''), t_offline('', .08), t_pair('', .16, slug, 'oregram', t('gx_h3'), t('gx_p3'))]
    else:
        shapes = 'crystal,globe'
        tiles = [t_map('w8', 0, MINES), t_conv('', .08), t_flash(''), t_quiz('', .08, ORE_QUIZ),
                 t_offline('', .16), t_market('w7', 0, t('gr_market_chips')), t_talk('w5', .08), t_lang('w5'), t_more('w7', .08)]
    V.clear()
    cards = '\n      '.join(tiles)
    return f'''<main>
<section class="app-hero">
  <div class="sculpt"><canvas id="sculpture" data-shapes="{shapes}" aria-hidden="true"></canvas></div>
  <div class="wrap">
    <div class="hero-copy">
      <span class="pill rv"><i></i>{tn('gr_pill', name).format(n)}</span>
      <div class="top rv" style="--d:.08s">
        <img class="app-icon" src="{icon}" alt="{alt}" style="--glow:rgba({glow},.95)">
        <h1>{PAGES[slug][2]}</h1>
      </div>
      <p class="slogan rv" style="--d:.12s"><em class="s">{ore}</em></p>
      <p class="lead rv" style="--d:.16s">{tn('gx_page_lead' if k == 'gx' else 'gr_page_lead', name)}</p>
      <div class="actions rv" style="--d:.24s">
        <span class="btn" aria-disabled="true">{t('dev')}</span>
        <a class="btn solid" href="{mail}">{t('next_cta')} <span class="arr">→</span></a>
      </div>
      <p class="store-note rv" style="--d:.3s">{tn('gr_note', name)}</p>
    </div>
  </div>
</section>
{band(tn('gx_band' if k == 'gx' else 'gr_band', name))}

<section class="block">
  <div class="wrap">
    <div class="block-head">
      <div class="rv">
        <p class="label"><span class="n">{t('feat_n')}</span> {t('feat_label')}</p>
        <h2>{tn('gr_feat_h2', name)}</h2>
      </div>
      <p class="rv" style="--d:.1s">{tn('gx_feat_p' if k == 'gx' else 'gr_feat_p', name)}</p>
    </div>
    <div class="bento">
      {cards}
    </div>
  </div>
</section>

<section class="block" style="padding-top:20px">
  <div class="wrap">
    <div class="soon rv">
      <div class="orbit"><img src="{icon}" alt="{alt}" style="--glow:rgba({glow},.9)"></div>
      <p class="label">{t('dev')}</p>
      <h3>{dig}</h3>
      <p>{tn('gr_soon_p', name)}</p>
      <div class="actions" style="justify-content:center;margin-top:28px"><a class="btn" href="{mail}">{t('next_cta')} <span class="arr">→</span></a></div>
    </div>
  </div>
</section>

<section class="block" style="padding-top:20px">
  <div class="wrap">
    <div class="grid3">
      <div class="card glow rv"><span class="label">{t('sup_label')}</span><h3>{t('sup_h')}</h3><p>{t('sup_p')}</p></div>
      <div class="card glow rv" style="--d:.08s"><span class="label">{t('prv_label')}</span><h3>{t('privacy')}</h3><p>{t('prv_p')} <a href="{u(f'/{slug}/privacy/')}">{t('read_it')}</a><br><a href="{u(f'/{slug}/delete-account/')}">{t('delete-account')} →</a></p></div>
      <div class="card glow rv" style="--d:.16s"><span class="label">{t('trm_label')}</span><h3>{t('terms')}</h3><p>{t('trm_p')} <a href="{u(f'/{slug}/terms/')}">{t('read_them')}</a></p></div>
    </div>
  </div>
</section>
</main>'''


# ------------------------------- Petro-Rulers, MarineGram and Quran Guardians pages
# The page of an app that is still being made (SOLO): hero, band, living
# tiles, the "coming soon" box and the links to its privacy policy and terms. Its
# texts are the rows "<key>_..." of site_texts.py (key: "pr", "mg" or "hz").
def solo(slug):
    _, name, k, glow = SOON_BY[slug][:4]
    icon, alt = f'/assets/img/{slug}-icon.png', e('icon_alt_of').format(name)
    mail = f'mailto:support@vatanitech.com?subject={quote(t("next_subject") + ": " + name)}'
    vset(slug)
    if slug == 'petro-rulers':
        tiles = [t_ruler('w7', 0, PIPE), t_angle('w5', .08), t_scan('w7', 0, VALVE), t_flash('w5', .08),
                 t_lang(''), t_offline('', .08), t_pair('', .16, slug, 'petrogram', t('pr_h3'), t('pr_p3'))]
    elif slug == 'marinegram':
        tiles = [t_map('w8', 0, PORTS), t_flash('', .08), t_ship('w7'), t_prop('w5', .08), t_hull('w5'), t_offline('w7', .08)]
    else:
        tiles = [t_verse('w7'), t_hide('w5', .08), t_sched('w7'), t_lang('w5', .08, *HAFIZ_LANGS),
                 t_offline('w5'), t_more('w7', .08)]
        # one more wide tile: what else the app has (recitations, tafsir, hadiths, the Prayer tab)
        V.update(more_items='hz_more_items', more_cap='more_cap', more_h='hz_more_h', more_p='hz_more_p')
        tiles.append(t_more('w12', 0, 900))
    V.clear()
    cards = '\n      '.join(tiles)
    return f'''<main>
<section class="app-hero">
  <div class="sculpt"><canvas id="sculpture" data-shapes="{SOLO[slug][1]}" aria-hidden="true"></canvas></div>
  <div class="wrap">
    <div class="hero-copy">
      <span class="pill rv"><i></i>{t(k + '_pill').format(num(slug))}</span>
      <div class="top rv" style="--d:.08s">
        <img class="app-icon" src="{icon}" alt="{alt}" style="--glow:rgba({glow},.95)">
        <h1 lang="en">{SOLO[slug][0]}</h1>
      </div>
      <p class="slogan rv" style="--d:.12s"><em class="s">{t(k + '_sub')}</em></p>
      <p class="lead rv" style="--d:.16s">{t(k + '_lead')}</p>
      <div class="actions rv" style="--d:.24s">
        <span class="btn" aria-disabled="true">{t('dev')}</span>
        <a class="btn solid" href="{mail}">{t('next_cta')} <span class="arr">→</span></a>
      </div>
      <p class="store-note rv" style="--d:.3s">{t('gr_note')}</p>
    </div>
  </div>
</section>
{band(t(k + '_band'))}

<section class="block">
  <div class="wrap">
    <div class="block-head">
      <div class="rv">
        <p class="label"><span class="n">{t('feat_n')}</span> {t('feat_label')}</p>
        <h2>{t(k + '_feat_h2')}</h2>
      </div>
      <p class="rv" style="--d:.1s">{t(k + '_feat_p')}</p>
    </div>
    <div class="bento">
      {cards}
    </div>
  </div>
</section>

<section class="block" style="padding-top:20px">
  <div class="wrap">
    <div class="soon rv">
      <div class="orbit"><img src="{icon}" alt="{alt}" style="--glow:rgba({glow},.9)"></div>
      <p class="label">{t('dev')}</p>
      <h3>{t('soon_h')}</h3>
      <p>{tn('gr_soon_p', name)}</p>
      <div class="actions" style="justify-content:center;margin-top:28px"><a class="btn" href="{mail}">{t('next_cta')} <span class="arr">→</span></a></div>
    </div>
  </div>
</section>

<section class="block" style="padding-top:20px">
  <div class="wrap">
    <div class="grid3">
      <div class="card glow rv"><span class="label">{t('sup_label')}</span><h3>{t('sup_h')}</h3><p>{t('sup3_p')}</p></div>
      <div class="card glow rv" style="--d:.08s"><span class="label">{t('prv_label')}</span><h3>{t('privacy')}</h3><p>{t('prv3_p')} <a href="{u(f'/{slug}/privacy/')}">{t('read_it')}</a></p></div>
      <div class="card glow rv" style="--d:.16s"><span class="label">{t('trm_label')}</span><h3>{t('terms')}</h3><p>{t('trm_p')} <a href="{u(f'/{slug}/terms/')}">{t('read_them')}</a></p></div>
    </div>
  </div>
</section>
</main>'''


# The privacy policy or the terms of use of an app in SOLO (kind: "privacy"
# or "terms"), from solo_texts.py: three languages on the English page, one
# on the others, like PetroGram's.
exec(rd(T / 'solo_texts.py'))               # defines SOLO_DOCS


def solo_doc(slug, kind):
    def section(l):
        parts, items = [], []
        def flush():
            if items:
                parts.append('<ul>\n' + '\n'.join(f'<li>{x}</li>' for x in items) + '\n</ul>')
                items.clear()
        for line in SOLO_DOCS[slug][kind][l].split('\n'):
            x = html.escape(line[2:] if line[:2] in ('# ', '@ ', '- ') else line[3:] if line.startswith('## ') else line, quote=False)
            x = x.replace('{MAIL}', MAILTO)
            if line.startswith('- '):
                items.append(x)
                continue
            flush()
            parts.append(f'<h1>{x}</h1>' if line.startswith('# ') else f'<h2>{x}</h2>' if line.startswith('## ')
                         else f'<p class="meta">{x}</p>' if line.startswith('@ ') else f'<p>{x}</p>')
        flush()
        return f'<section id="{l}" lang="{l}">\n' + '\n'.join(parts) + '\n</section>'

    def link(l):
        if L == 'en':
            return f'<a href="#{l}">'
        if l == L:
            return f'<a href="#{l}" aria-current="true">'
        return f'<a href="{PRE[l]}/{slug}/{kind}/">'
    nav = (f'<nav class="langs" aria-label="{e("doc_langs")}">'
           + ''.join(link(l) + DOC_LANGS[l] + '</a>' for l in LANGS) + '</nav>')
    return f'''<main class="doc">
<p class="label"><span class="n">{NAME[slug]} /</span> {t(kind)}</p>
{nav}
{chr(10).join(section(l) for l in (LANGS if L == 'en' else [L]))}
</main>'''


# ------------------------------------------------------ privacy and terms
# The app's two long texts exist in seven languages. The English page shows
# all seven, one after the other (the app links to it); the Azerbaijani and
# Russian pages show their own language and link to the others.
DOC_LANGS = {'en': 'English', 'az': 'Azərbaycanca', 'ru': 'Русский', 'ar': 'العربية',
             'es': 'Español', 'fr': 'Français', 'zh': '简体中文'}


def langnav(slug, app='petrogram'):
    def link(l):
        if L == 'en':
            return f'<a href="#{l}">'
        if l == L:
            return f'<a href="#{l}" aria-current="true">'
        if l in PRE and l != 'en':
            return f'<a href="{PRE[l]}/{app}/{slug}/">'
        return f'<a href="/{app}/{slug}/#{l}">'
    return (f'<nav class="langs" aria-label="{e("doc_langs")}">'
            + ''.join(link(l) + n + '</a>' for l, n in DOC_LANGS.items()) + '</nav>')


def doc(slug, sections, app='petrogram', name='PetroGram'):
    """A long text page: all languages in English, one language elsewhere.
    app and name: the app's folder on the site and the name people see."""
    shown = list(sections.values()) if L == 'en' else [sections[L]]
    sep = '\n' if slug == 'terms' else '\n\n'
    return f'''<main class="doc">
<p class="label"><span class="n">{name} /</span> {t(slug)}</p>
{langnav(slug, app)}
{sep.join(shown)}
</main>'''


def terms(name='PetroGram', changes=None):
    """The terms of use (language -> HTML). For another app: its name in place
    of PetroGram, then changes, a list of (old text, new text) per language."""
    secs = {}
    for l, m in json.loads(rd(T / 'terms.json')).items():
        m = {k: v.replace('PetroGram', name) for k, v in m.items()}
        if name != 'PetroGram':
            m = {k: name_grammar(v, l, name) for k, v in m.items()}
        for x, y in (changes or {}).get(l, []):
            hit = [k for k, v in m.items() if x in v]
            assert len(hit) == 1 and m[hit[0]].count(x) == 1, ('terms', name, l, x[:60])
            m[hit[0]] = m[hit[0]].replace(x, y)
        rtl = ' dir="rtl"' if l == 'ar' else ''
        hl = ' lang="zh-Hans"' if l == 'zh' else f' lang="{l}"'
        items = []
        for i in range(1, 13):
            if f'tm_{i}' not in m:
                break
            items.append(f'<h2>{i}. {html.escape(m[f"tm_{i}_t"])}</h2>\n<p>{html.escape(m[f"tm_{i}"])}</p>')
        secs[l] = f'''<section id="{l}"{hl}{rtl}>
<h1>{name} – {html.escape(m["tm_title"])}</h1>
<p>{html.escape(m["tm_intro"])}</p>
{chr(10).join(items)}
<p class="meta">{html.escape(m["tm_date"])}</p>
</section>'''
    return secs


terms_secs = terms()

exec(rd(T / 'privacy_texts.py'))  # defines PRIV and ZH_SECTION
old = rd(T / 'privacy_old.html')


def block_6b(app, lang_label):
    md = rd(app / 'docs/ACCOUNT_SETUP.md')
    i = md.index(f'**{lang_label}.** ')
    j = md.find('\n\n', i)
    txt = ' '.join(md[i:j].split('\n')).split('** ', 1)[1]
    num, rest = txt.split(' ', 1)
    title, body = rest.split('. ', 1)
    return f'<h2>{num.rstrip(".")}. {html.escape(title)}</h2>\n  <p>{html.escape(body)}</p>'


def blocks_6c(app, heading):
    md = rd(app / 'docs/PRIVACY_ADDITIONS.md')
    i = md.index(f'## {heading}\n')
    j = md.find('\n## ', i + 3)
    chunk = md[i:j if j > 0 else None]
    out = [f'<h2>{m.group(1).rstrip(".")}. {html.escape(m.group(2))}</h2>\n  <p>{html.escape(m.group(3))}</p>'
           for m in re.finditer(r'\*\*(6\S+?)\s(.+?)[.。]\*\*\s(.+)', chunk)]
    # 6c to 6g, and 6h (the certificate) in the apps that have it.
    assert len(out) in (5, 6), (heading, len(out))
    return '\n\n  '.join(out)


def policy(app):
    """The PetroGram privacy policy (language -> HTML), with sections 6b to 6g
    read from the docs of the app folder given."""
    secs = {}
    for l in ['en', 'az', 'ru', 'ar', 'es', 'fr']:
        a = old.index(f'<section id="{l}"')
        sec = old[a:old.index('</section>', a) + len('</section>')]
        p = PRIV[l]
        for x, y in p['replace']:
            assert sec.count(x) == 1, (l, x[:60], sec.count(x))
            sec = sec.replace(x, y)
        s0 = sec.index(p['sum_start'])
        s1 = sec.index(p['sum_end'], s0) + len(p['sum_end'])
        sec = sec[:s0] + p['summary'] + sec[s1:]
        k = sec.index('<h2>7.')
        sec = sec[:k] + block_6b(app, p['label6b']) + '\n\n  ' + blocks_6c(app, p['heading6c']) + '\n\n  ' + sec[k:]
        for marker, add in [(p['sec3'], p['bullet3']), (p['sec8'], p['bullets8'])]:
            m0 = sec.index(marker)
            m1 = sec.index('</ul>', m0)
            if marker == p['sec8']:          # the old last item ended the list with "."
                last = sec.rindex('.</li>', m0, m1)
                sec = sec[:last] + p['semi'] + sec[last + 1:]
                m1 = sec.index('</ul>', m0)
            sec = sec[:m1] + add + '\n  ' + sec[m1:]
        assert 'gmail' not in sec, l
        secs[l] = sec
    secs['zh'] = ZH_SECTION.replace('{BLOCKS6CF}', blocks_6c(app, '简体中文'))
    return secs


privacy_secs = policy(APP)

exec(rd(T / 'delete_texts.py'))   # defines delete_secs() and its rows of TX

# Geo-Rulers and OreGram (PAGES): the same policy with the sections 6b to 6g
# of each app's own folder, then the differences listed in georulers_texts.py
# (the same for both apps); and the terms of use with those differences.
exec(rd(T / 'georulers_texts.py'))  # defines name_grammar(), geo_adapt(), GEO_PRIV, GEO_DELETE, GEO_TERMS
NAME = {a[0]: a[1] for a in SOON}
geo_privacy_secs, geo_terms_secs = {}, {}
for _slug, (_folder, _env, _h1) in PAGES.items():
    _dir = app_folder(_folder, _env)
    assert _dir, f'{NAME[_slug]} app folder not found'
    geo_privacy_secs[_slug] = {l: geo_adapt(sec, GEO_PRIV[l], l, 28, NAME[_slug]) for l, sec in policy(_dir).items()}
    geo_terms_secs[_slug] = terms(NAME[_slug], GEO_TERMS)


def geo_delete_secs(slug):
    return {l: geo_adapt(sec, GEO_DELETE.get(l, []), l, 28, NAME[slug])
            for l, sec in delete_secs(slug).items()}


def notfound():
    return f'''<main class="doc" style="text-align:center;padding:160px 24px">
<p class="label">404</p>
<h1>{t('nf_h1')}</h1>
<p><a href="{u('/')}">{t('nf_go')}</a></p>
</main>'''


def certificate():
    """The page that shows one certificate of completion. The record is read
    in the visitor's browser (assets/certificate.js) from the app's public
    database, by the number in the address: /certificate/?id=pg-..."""
    row = lambda key, cls: f'<div class="cert-row"><dt>{t(key)}</dt><dd class="{cls}"></dd></div>'
    return f'''<main class="doc cert" data-noid="{e('cert_noid')}" data-none="{e('cert_none')}" data-error="{e('cert_error')}">
<p class="label"><span class="n">Vatani Tech /</span> {t('cert_label')}</p>
<div class="cert-state" data-state="loading">
  <p class="cert-wait">{t('cert_loading')}</p>
  <noscript><p>{t('cert_error')}</p></noscript>
</div>
<div class="cert-state" data-state="none" hidden>
  <h1>{t('cert_h_none')}</h1>
  <p class="cert-why"></p>
</div>
<div class="cert-state" data-state="ok" hidden>
  <h1>{t('cert_h_ok')}</h1>
  <p class="cert-valid"><span aria-hidden="true">✓</span> {t('cert_valid')}</p>
  <dl class="cert-card">
    <div class="cert-row cert-who"><dt>{t('cert_awarded')}</dt><dd class="c-name"></dd></div>
    {row('cert_for', 'c-course')}
    {row('cert_result', 'c-result')}
    {row('cert_date', 'c-date')}
    {row('cert_number', 'c-id')}
    <div class="cert-row"><dt>{t('cert_issuer')}</dt><dd>Vatani Tech · <a class="c-app" href="{u('/petrogram/')}"></a></dd></div>
  </dl>
  <h2>{t('cert_about_h')}</h2>
  <ul>
    <li>{t('cert_about_1')}</li>
    <li>{t('cert_about_2')}</li>
    <li>{t('cert_about_3')}</li>
    <li>{t('cert_about_4')}</li>
  </ul>
</div>
</main>'''


# ----------------------------------------------- write every page, 3 times
JS = ['/assets/site.js']
for L in LANGS:
    out = OUT / PRE[L].lstrip('/')
    wr(out / 'index.html', page('home', home(), '/', ['/assets/land.js', '/assets/hero.js'] + JS))
    wr(out / 'petrogram/index.html', page('pg', petro(), '/petrogram/', ['/assets/hero.js'] + JS))
    wr(out / 'petrogram/terms/index.html', page('terms', doc('terms', terms_secs), '/petrogram/terms/', JS))
    wr(out / 'petrogram/privacy/index.html', page('privacy', doc('privacy', privacy_secs), '/petrogram/privacy/', JS))
    wr(out / 'petrogram/delete-account/index.html',
       page('delete', doc('delete-account', delete_secs()), '/petrogram/delete-account/', JS))
    # Geo-Rulers and OreGram: each one's page, and its privacy policy, delete
    # page and terms of use.
    for slug in PAGES:
        name = NAME[slug]
        wr(out / slug / 'index.html',
           page('gx' if SOON_BY[slug][2] == 'gx' else 'gr', geo(slug), f'/{slug}/', ['/assets/land.js', '/assets/hero.js'] + JS, name=name, app=slug))
        wr(out / slug / 'privacy/index.html',
           page('privacy', doc('privacy', geo_privacy_secs[slug], slug, name), f'/{slug}/privacy/', JS, name=name, app=slug))
        wr(out / slug / 'delete-account/index.html',
           page('delete', doc('delete-account', geo_delete_secs(slug), slug, name), f'/{slug}/delete-account/', JS, name=name, app=slug))
        wr(out / slug / 'terms/index.html',
           page('terms', doc('terms', geo_terms_secs[slug], slug, name), f'/{slug}/terms/', JS, name=name, app=slug))
    # Petro-Rulers, MarineGram and Quran Guardians: each one's page, privacy policy and terms of use.
    for slug in SOLO:
        wr(out / slug / 'privacy/index.html', page('sprivacy', solo_doc(slug, 'privacy'), f'/{slug}/privacy/', JS, name=NAME[slug], app=slug))
        wr(out / slug / 'terms/index.html', page('terms', solo_doc(slug, 'terms'), f'/{slug}/terms/', JS, name=NAME[slug], app=slug))
        wr(out / slug / 'index.html',
           page(SOON_BY[slug][2], solo(slug), f'/{slug}/', (['/assets/land.js'] if 'globe' in SOLO[slug][1] else []) + ['/assets/hero.js'] + JS, app=slug))
    wr(out / '404.html', page('nf', notfound(), '/404.html', JS, found=False))
    # A certificate shows a person's name: search engines stay out, and the
    # page is not in the sitemap.
    wr(out / 'certificate/index.html',
       page('cert', certificate(), '/certificate/', JS + ['/assets/certificate.js'])
       .replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1))

# The list of pages for search engines, each with its other languages.
PATHS = ['/', '/petrogram/', '/petrogram/privacy/', '/petrogram/terms/', '/petrogram/delete-account/']
PATHS += [f'/{s}/{x}' for s in PAGES for x in ('', 'privacy/', 'terms/', 'delete-account/')]
PATHS += [f'/{s}/{x}' for s in SOLO for x in ('', 'privacy/', 'terms/')]
rows = ''.join(
    f'  <url><loc>{SITE}{PRE[l]}{p}</loc>'
    + ''.join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{SITE}{PRE[x]}{p}"/>' for x in LANGS)
    + '</url>\n' for p in PATHS for l in LANGS)
wr(OUT / 'sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n'
   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
   + rows + '</urlset>\n')
print('built', ', '.join(LANGS))
