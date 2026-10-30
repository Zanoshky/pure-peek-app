#!/usr/bin/env python3
"""Builds the guide pages in docs/ from the bodies below. Run after any edit and commit docs/. Fails on any dash."""
from pathlib import Path

D = Path(__file__).parent / "docs"
REPO = "https://github.com/Zanoshky/pure-peek-app"
PLAY = "https://play.google.com/store/apps/details?id=com.zanoshky.purepeek"
SITE = "https://purepeek.zanoski.com"
NAV = [("index.html", "Home"), ("guide.html", "Guide"), ("faq.html", "Questions"), ("report.html", "Report a bug")]


def page(name, title, desc, body):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == name else ""}>{t}</a>' for h, t in NAV)
    for bad in ("—", "–", " - "):
        if bad in body:
            raise SystemExit(f"{name}: dash {bad!r} in copy")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Pure Peek user guide</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#000000">
<meta property="og:title" content="{title} · Pure Peek user guide">
<meta property="og:description" content="{desc}">
<link rel="icon" href="img/icon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/inter-semibold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/icon.svg" alt="" width="34" height="34"><span>Pure Peek</span></a>
    <nav aria-label="Guide pages">{nav}</nav>
  </div>
</header>
<main id="main" class="page">
  <div class="wrap">
{body}
  </div>
</main>
<footer>
  <div class="wrap">
    <span>Guide text and images are shared under CC BY 4.0. The Pure Peek app itself is proprietary. Made by Marko Zanoski.</span>
    <nav aria-label="Footer"><a href="{PLAY}">Google Play</a><a href="{SITE}">purepeek.zanoski.com</a><a href="{REPO}/issues">Issues</a><a href="{SITE}/privacy">Privacy</a></nav>
  </div>
</footer>
</body>
</html>
"""
    (D / name).write_text(html)
    print(name)


page("index.html", "Home", "The user guide for Pure Peek, the offline file viewer for Android.", f"""
    <p class="kicker">User guide</p>
    <h1>Pure Peek</h1>
    <p class="lede">Open any file and see it properly: photos at full quality, PDF, CSV and Excel tables, code, logs, Markdown, Word, web pages, zip and more. Pay once, no ads, no internet permission.</p>
    <div class="shots">
      <figure><img src="img/photo.webp" alt="A photo of Lake Bled open in Pure Peek." width="540" height="1200" fetchpriority="high"><figcaption>A photo</figcaption></figure>
      <figure><img src="img/table.webp" alt="A CSV of expenses as a table with the header row and row numbers pinned." width="540" height="1200" loading="lazy"><figcaption>A CSV as a table</figcaption></figure>
      <figure><img src="img/pdf.webp" alt="A trip plan PDF with a photo and a route table." width="540" height="1200" loading="lazy"><figcaption>A PDF</figcaption></figure>
      <figure><img src="img/details.webp" alt="The details sheet of a photo: pixels, colour, camera and exposure." width="540" height="1200" loading="lazy"><figcaption>About this file</figcaption></figure>
    </div>
    <div class="cta">
      <a class="btn main" href="guide.html">Read the guide</a>
      <a class="btn ghost" href="report.html">Report a bug or ask for a feature</a>
    </div>
""")

page("guide.html", "Guide", "How to use Pure Peek: opening files, photos, PDF, tables, text and code, web pages, zip, audio, video, fonts and settings.", """
    <p class="kicker">Guide</p>
    <h1>How Pure Peek works</h1>

    <h2>Open a file</h2>
    <p>Pure Peek has no file browser of its own and needs no storage permission. Files reach it the ways Android offers:</p>
    <dl>
      <dt>Open with</dt><dd>Tap a file in Files, Gmail, Drive or Downloads. When Android asks which app to use, pick Pure Peek, then Always, so that kind of file opens straight away next time.</dd>
      <dt>Share</dt><dd>Share any file, or several, to Pure Peek from another app.</dd>
      <dt>Open files</dt><dd>On home, opens Android's file picker. Pick one file or many.</dd>
      <dt>Open a folder</dt><dd>Pick a folder once and see its files as a grid or a list, newest first or by name. Open one and step through the rest with Previous file and Next file.</dd>
      <dt>Photos</dt><dd>Opens Android's photo picker.</dd>
      <dt>Recent files</dt><dd>Home lists what you opened lately. Turn this off in Settings, Privacy.</dd>
    </dl>
    <p>If another app always opens a kind of file, Settings, Opening files names it and takes you to its info page, where Open by default, Clear defaults hands the choice back.</p>

    <h2>The viewer bar</h2>
    <p>Every file opens with its name, kind and size at the top. The buttons there: Back, Find in this file (where the file has text), About this file, and More. More holds Share, Open with another app and the actions for that kind of file.</p>
    <p>About this file shows the size in bytes, the kind, everything the file says about itself, and a SHA-256 checksum on request.</p>

    <h2>Photos</h2>
    <p>Photos open at full resolution, drawn in tiles, so zooming into a big photo stays sharp. Pinch to zoom, double tap for actual pixels, double tap again to fit. JPEG, PNG, WebP, HEIC, AVIF, GIF, DNG, BMP and more. Ultra HDR and wide colour photos show in full on screens that can.</p>
    <p>About this file lists pixels, megapixels, colour space, camera, lens, exposure, ISO and when it was taken. More has Turn a quarter, Use as wallpaper or contact photo, and Share without location and camera details, which sends a copy with the GPS taken out and leaves the original alone.</p>

    <h2>PDF</h2>
    <p>Pages render again at every zoom, so small print stays crisp. More has Go to page, First page, Last page, Copy the text of this page, Print, and on dark looks, Night pages, which shows PDFs as light text on dark. A PDF opens on the page you left it. A locked PDF asks for its password. On a tablet or a wide screen, a page strip sits beside the document.</p>

    <h2>Tables</h2>
    <p>CSV, TSV and Excel files open as tables with the header row and the row numbers pinned while you scroll. Tap a column name for Sort smallest to largest, Sort largest to smallest, Column stats (sum, average, smallest, largest, most common values) and Copy the column. Excel files with several sheets show a tab for each sheet. More has Copy as CSV for the whole table, and a switch for files whose first row is data, not names; Settings sets the default.</p>

    <h2>Text, code and documents</h2>
    <p>Text, logs and code open with line numbers and wrap; both can be turned off in Settings. JSON has As saved and Tidy tabs, Markdown has Formatted and Source, and Word documents open as clean text. Bigger text and Smaller text are in More. Big files open fast: only the lines on screen are drawn, and a 52 MB log searches in a moment.</p>
    <p>A file with the wrong name, like a picture saved as .bin, opens as what it really is, with a note. Anything Pure Peek cannot show opens as bytes.</p>

    <h2>Find</h2>
    <p>Find in this file works in text, code, tables and PDFs. Matches are marked, the current one stands out, and Previous match and Next match step through them. The count stops at 20,000 and shows 20,000+.</p>

    <h2>Web pages and SVG</h2>
    <p>HTML files and SVG drawings show inside the app with scripts off. Nothing outside the file is loaded, so a page cannot call home. Copy the source is in More.</p>

    <h2>Zip, audio, video and fonts</h2>
    <dl>
      <dt>Zip</dt><dd>Walk the folders inside a zip and tap any file to open it, without unpacking the rest.</dd>
      <dt>Audio and video</dt><dd>Play and pause, a seek bar, Back 10 seconds and On 10 seconds, speed, and Repeat. Audio shows its cover art and tags.</dd>
      <dt>Fonts</dt><dd>A sample at every size and a box to try your own words.</dd>
    </dl>

    <h2>Settings</h2>
    <dl>
      <dt>Look</dt><dd>Follow the phone, Light, Graphite or True black. Follow the phone uses Light by day and True black at night.</dd>
      <dt>Text and tables</dt><dd>Text size, wrap long lines, line numbers, and whether a table's first row holds the column names.</dd>
      <dt>Privacy</dt><dd>Remember recent files. Turning it off forgets the list at once.</dd>
      <dt>Opening files</dt><dd>Which app opens PDFs now, and how to make Pure Peek the one.</dd>
      <dt>Widget</dt><dd>Open files, Open a folder and Photos in one tap on the home screen.</dd>
      <dt>Help</dt><dd>This guide, the report page and the privacy policy.</dd>
    </dl>

    <h2>Accessibility</h2>
    <p>Every control has a TalkBack label, touch targets are at least 48 dp, text grows with the phone's text size up to 200 percent, and text keeps a 7 to 1 contrast in every look.</p>
""")

page("faq.html", "Questions", "Answers to common questions about Pure Peek, and what to try when something does not work.", f"""
    <p class="kicker">Questions</p>
    <h1>Questions and fixes</h1>

    <h2>Pure Peek is not in the Open with list</h2>
    <p>Another app may be set to always open that kind of file. Open Android settings, Apps, that app, Open by default, and tap Clear defaults. Next time you tap a file, Android asks again. Settings, Opening files in Pure Peek names the app that opens PDFs now.</p>

    <h2>Can it edit files?</h2>
    <p>No. Pure Peek only shows files and never changes or resaves them.</p>

    <h2>Why can I not see where a photo was taken?</h2>
    <p>Android hides the place in a shared photo from apps that do not ask for the media location permission, and Pure Peek asks for no permissions. About this file says when a photo has a place that Android hid. Share without location still takes it out of the copy you send.</p>

    <h2>How big a file can it open?</h2>
    <p>We tested a CSV of 500,000 rows (20 MB) and a 52 MB log. Both open, scroll and search.</p>

    <h2>A file opens as bytes</h2>
    <p>Pure Peek shows anything it cannot read as bytes, with its size and checksum. If you think it should open, report it with the kind of file, and attach a sample if it holds nothing private.</p>

    <h2>Does it use the internet?</h2>
    <p>No. It has no internet permission, so Android itself stops it from going online. Web pages it shows load nothing from outside. See the <a href="{SITE}/privacy">privacy policy</a>.</p>
""")

page("report.html", "Report a bug", "How to report a Pure Peek bug or ask for a feature on GitHub.", f"""
    <p class="kicker">Report</p>
    <h1>Report a bug or ask for a feature</h1>
    <p>Found something broken, or have an idea? Tell us on GitHub. A free GitHub account is all you need.</p>
    <div class="grid">
      <div class="card"><h2>Bug report</h2><p>A file opens wrong, looks wrong, or the app crashes.</p><p style="margin-top:16px"><a class="btn main" href="{REPO}/issues/new?template=bug_report.yml">Report a bug</a></p></div>
      <div class="card"><h2>Feature request</h2><p>A kind of file or something you would like Pure Peek to do.</p><p style="margin-top:16px"><a class="btn ghost" href="{REPO}/issues/new?template=feature_request.yml">Ask for a feature</a></p></div>
    </div>

    <h2>Before you write</h2>
    <ul>
      <li>Search the <a href="{REPO}/issues">open issues</a> first. If yours is there, add a thumbs up or a comment.</li>
      <li>Check the <a href="faq.html">questions and fixes</a> page.</li>
      <li>One problem per report makes it faster to fix.</li>
    </ul>

    <h2>What helps</h2>
    <dl>
      <dt>App version</dt><dd>Settings in Pure Peek, at the bottom.</dd>
      <dt>Phone model and Android version</dt><dd>Android settings, About phone.</dd>
      <dt>The kind of file</dt><dd>Its name ending, like .pdf or .csv, and its size.</dd>
      <dt>Steps</dt><dd>What you did, one step per line, so we can do the same.</dd>
      <dt>Expected and actual</dt><dd>What you thought would happen, and what happened.</dd>
      <dt>A picture or a sample</dt><dd>A screenshot, a short screen recording, or the file itself if it holds nothing private.</dd>
    </dl>
    <p>Issues on GitHub are public. Before you attach a screenshot or a file, make sure it shows nothing private.</p>

    <h2>Other ways</h2>
    <p>Prefer not to use GitHub? Write to <span class="mail">marko@zanoski.com</span> (<a href="mailto:marko@zanoski.com">write an email</a>).</p>
""")
