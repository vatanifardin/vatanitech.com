# vatanitech.com

The Vatani Tech website. Plain HTML, CSS and a little JavaScript: no
framework, nothing to install.

The site is in three languages. English is the top of the site, Azerbaijani
is the same pages under `/az/` and Russian under `/ru/`. The language menu
in the header (and the links in the footer) lead to the same page in the
other languages.

- `index.html`: home. The hero is a cloud of light points that forms the
  logo, a turning Earth (real coastlines from PetroGram's own map) and an
  oil drop (`assets/hero.js`). Then the app showcase, principles, contact.
  The showcase has one tab per app (`ORDER` in `_tools/build.py`), in the
  order the owner chose on 26 November 2026, with the two apps of
  27 November 2026 added at the end: Petro-Rulers, PetroGram, Geo-Rulers,
  OreGram, Domino Global, Domino Freedom, MarineGram, Quran Guardians
  (first called Hafiz, renamed on 28 November 2026: its folder `/hafiz/`,
  its key `hafiz` and its text rows `hz_...` keep the old name). The first
  tab is open at the start; an app's number ("App 02") is its place in that
  list. The "-Gram" apps are reference books; the "-Rulers" apps are
  measuring and camera tools only (ruler, protractor, camera scanner and a
  short guide), each the partner of a "-Gram" app (owner, 26 and
  27 November 2026). Every tab shows moving tiles in the app's own
  colour, like PetroGram's (`panel_tiles` in `_tools/build.py`; the
  colours are `ACCENT`, each app's examples are `VSET`, shared with the
  app's page). The two domino games have their own drawings: a chain of
  dominoes being laid and four players taking turns.
  The apps still being made are the `SOON` list in `_tools/build.py`.
  Icons and logo come from the PetroGram repository's `branding/` folder
  (PetroGram's icon since 26 November 2026: a hexagon with an oil drop and
  a gas flame); the Petro-Rulers icon (`assets/img/petro-rulers-icon.png`,
  256 × 256) from the Petro-Rulers repository's `branding/icon-1024.png`;
  the Geo-Rulers icon (`assets/img/geo-rulers-icon.png`, 256 × 256) from
  the Geo-Rulers repository's `branding/apps/geo-rulers/icon-1024.png`,
  and the OreGram icon (`assets/img/oregram-icon.png`, 256 × 256) from the
  OreGram repository's `branding/apps/oregram/icon-1024.png`; the
  MarineGram icon (`assets/img/marinegram-icon.png`, 256 × 256) from
  `branding/icon.png` of its repository; the Quran Guardians icon
  (`assets/img/hafiz-icon.png`, 256 × 256) from
  `branding/quran_guardians_icon.png` of the hafiz repository.
- `certificate/`: the page that shows one certificate of completion
  (28 November 2026). The PetroGram app links to it as
  `/certificate/?id=pg-...` (also from a person's LinkedIn profile).
  `assets/certificate.js` reads that one record in the visitor's browser
  from the app's public database (Firebase project `petrogram-9bc6a`,
  collection `certificates`; the rules are `firestore.rules` in the
  PetroGram repository) and shows the name, result, date and number. The
  page is closed to search engines and is not in the sitemap. A new app
  with certificates gets a row in `APPS` at the top of that script. Never
  move this page: its address is built into the app and saved on LinkedIn
  profiles.
- `petrogram/`: the PetroGram page, its privacy policy and terms of use
  (7 languages on one page; the app links to these).
- `geo-rulers/`: the Geo-Rulers page (the app is still being made: no
  store buttons, no screenshots yet; the slogans "Ore what?", "Mine your
  business." and "Dig it." stay in English in every language), its privacy
  policy, terms of use and page for deleting an account (7 languages on
  one page; the app links to these).
- The pages of Geo-Rulers and OreGram are built like PetroGram's (since
  27 November 2026): a hero of light points (`data-shapes` in `geo()`:
  crystals and the Earth for OreGram, a protractor on a ruler and crystals
  for Geo-Rulers; shapes `crystal` and `tools` in `assets/hero.js`) and a
  grid of living tiles. OreGram shows PetroGram's tiles with mining
  examples (rows `gr_...`; the table `V` in `_tools/build.py` swaps the
  texts); Geo-Rulers has tiles of its own (`t_ruler`, `t_angle`, `t_scan`,
  `t_pair`). Each app's pages wear its own accent colour instead of the
  studio's teal: `ACCENT` in `_tools/build.py` sets `--acc` and `--acc2`
  on the page, and `assets/site.css` takes every accent from those two.
- `petro-rulers/`, `marinegram/`, `hafiz/`: one page each (27 November
  2026), built by `solo()` in `_tools/build.py` from the `SOLO` list: hero
  (shapes `tools`, `anchor`, `arch` in `assets/hero.js`), band, living
  tiles and the "coming soon" box, in the app's accent colour. Each has its
  own privacy policy and terms of use (`/<app>/privacy/`, `/<app>/terms/`),
  written for that app in the site's three languages in
  `_tools/solo_texts.py` (read the notes at its top: Petro-Rulers' terms
  are the app's own words, the policy of Quran Guardians follows the app's own privacy
  texts; since 28 November 2026 it also covers location, microphone and gifts). They have no account, so no page for deleting one. When an app
  changes what it stores or sends, change its text and date there. The
  apps' other languages are not written yet. MarineGram's page gives the app's own numbers as of 28 November 2026
  (1,130 terms, 36 ship types, 36 ship systems, a 3D model of every ship type): change them when the app changes. Hafiz's page shows the first
  verse of the Quran exactly as in the Tanzil text the app uses (`BASMALA`
  in `_tools/build.py`: never change it) with a link to tanzil.net.
- `oregram/`: the same four pages for OreGram (26 November 2026), a twin
  of Geo-Rulers: the same app and texts with another name, icon (ore on
  gold) and colour (gold, `#B8860B`). Since 27 November 2026 Geo-Rulers'
  page and tab describe the tool app (rows `gx_...` in
  `_tools/site_texts.py`: its own lead, band and six cards); its privacy
  policy, terms and delete page still follow the Geo-Rulers repository's
  `master`, and must be redone when the tool version is merged there. The build makes them from the same
  code and the same rows of text as Geo-Rulers' pages (the `PAGES` list in
  `_tools/build.py`), with OreGram in place of Geo-Rulers.
- `az/`, `ru/`: the same pages in Azerbaijani and Russian. Their privacy
  and terms pages show that one language and link to the others.
- `assets/`: `site.css` (all styles), `site.js` (scroll effects and the small
  animated feature tiles), `hero.js`, `land.js` (globe points), images.
  Shared by all three languages.
  `assets/img/email-logo.png` (440 × 128, white background, made from
  `branding/vatani-tech/vatani-tech-logo.png` of the PetroGram repository)
  is the logo in the Gmail signature (28 November 2026): sent emails load
  it from this address, so never move or rename it.
- `_tools/`: the scripts that write the pages. Not published (GitHub Pages
  skips folders that start with "_").
  - `python3 -I _tools/build.py` rebuilds every page in every language, and
    `sitemap.xml`. Never edit the built pages by hand.
  - `_tools/site_texts.py`: every text of the site, one row per text:
    English, Azerbaijani, Russian. To change or add a text, edit it there
    and rebuild. The build stops if a language is missing.
  - `_tools/georulers_texts.py`: what the privacy policy, delete page and
    terms of use of the two mining apps, Geo-Rulers and OreGram, say
    differently from PetroGram's (name, date, what the app is about,
    prices), in seven languages; the same differences for both apps (there
    is no separate `oregram_texts.py`). Everything else in those three
    pages is PetroGram's text, so a change to PetroGram's policy or terms
    reaches both apps too; the build stops if a text to be replaced is no
    longer found. Their terms must say what the apps' own terms say
    (`lib/strings_services.dart` and `lib/zh/zh_services.dart` in the
    Geo-Rulers and OreGram repositories): change them together.
  - `python3 -I _tools/make_land.py` rebuilds the globe and map dots.
- `CNAME`: the custom domain for GitHub Pages.
- `geo-rulers/data/prices.json` and `oregram/data/prices.json`: the
  monthly metal and mineral prices that the Geo-Rulers and OreGram apps
  read (World Bank "Pink Sheet" data, CC BY 4.0, adapted; monthly
  averages, not live prices). The two files are always the same. **A robot
  rewrites them once a month**: the GitHub Actions workflow
  `.github/workflows/geo-rulers-prices.yml` runs on the 6th and the 16th,
  downloads the current World Bank file, runs
  `_tools/geo-rulers/build_prices.py`, copies the result to
  `oregram/data/prices.json` and commits both files if they changed. Nobody has to do anything. Because the robot commits to `main`,
  **always `git pull` before changing the site**. To run it by hand: on
  GitHub, Actions → "Geo-Rulers monthly prices" → Run workflow. If a run
  fails, GitHub sends an email and the old file stays. The script's master
  copy is in the Geo-Rulers repository (`tool/prices/`); copy it here
  after changing it there. Never edit `prices.json` by hand, and do not
  move it: each app has its address built in.

The build reads a few privacy texts (sections 6b to 6h of each policy; 6h, the certificate, only where the app has it) from
the three app folders: PetroGram (`~/Developer/petrogram` on the Mac,
`~/petrogram` on the PC), Geo-Rulers (`~/Developer/geo-rulers`,
`~/geo-rulers`) and OreGram (`~/Developer/oregram`, `~/oregram`), from
`docs/ACCOUNT_SETUP.md` part 3 and `docs/PRIVACY_ADDITIONS.md` of each. All
three folders must be there and up to date (`git pull`). To read an app
from another folder for one run, name it in `PETROGRAM_APP`,
`GEO_RULERS_APP` or `OREGRAM_APP`:
`GEO_RULERS_APP=/path/to/geo-rulers python3 -I _tools/build.py`. The PC has no
Python of its own; the one inside the Android SDK works:
`%LOCALAPPDATA%\Android\Sdk\ndk\<version>\toolchains\llvm\prebuilt\windows-x86_64\python3\python.exe -I _tools\build.py`.

Preview: `python3 -m http.server 8765` in this folder, then open
http://localhost:8765 (and `/az/`, `/ru/`).
