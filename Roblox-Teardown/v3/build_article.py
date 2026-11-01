"""Build article_v3.html and Roblox_Teardown_v3.pdf from article_v3.md (same packaging as the Jio case study)."""
import pathlib
import re

import markdown
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
TITLE = "Roblox Product Teardown (v3)"
PDF_NAME = "Roblox_Teardown_v3.pdf"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap');
@page { size: A4; margin: 16mm 14mm 18mm 14mm; }
body { font-family: 'Source Serif 4', Georgia, serif; color: #1e293b; font-size: 11.2pt; line-height: 1.6; max-width: 760px; margin: 0 auto; }
h1, h2, h3 { font-family: 'Outfit', sans-serif; color: #0f172a; line-height: 1.2; page-break-after: avoid; }
h1 { font-size: 28pt; font-weight: 800; margin: 0 0 8px; letter-spacing: -0.5px; }
h1 + p em { font-family: 'Outfit', sans-serif; font-style: normal; color: #475569; font-size: 13pt; }
h2 { font-size: 18pt; font-weight: 800; margin-top: 28px; }
h3 { font-size: 13pt; font-weight: 700; margin-top: 20px; }
p, li { orphans: 3; widows: 3; }
strong { color: #0f172a; }
blockquote { border-left: 4px solid #2563eb; background: #eff6ff; margin: 18px 0; padding: 10px 16px; font-family: 'Outfit', sans-serif; font-size: 12pt; page-break-inside: avoid; }
blockquote p { margin: 0; }
figure { margin: 18px 0; page-break-inside: avoid; break-inside: avoid; }
img { width: 100%; display: block; border-radius: 6px; }
table { border-collapse: collapse; width: 100%; font-size: 10pt; page-break-inside: avoid; }
th, td { border: 1px solid #e2e8f0; padding: 6px 8px; text-align: left; vertical-align: top; }
th { font-family: 'Outfit', sans-serif; background: #f8fafc; }
hr { border: 0; border-top: 1px solid #e2e8f0; margin: 26px 0; }
em { color: #475569; }
a { color: #1d4ed8; }
"""


def main() -> None:
    md = (HERE / "article_v3.md").read_text()
    body = markdown.markdown(md, extensions=["extra", "sane_lists"])
    body = re.sub(r"<p>(<img [^>]+>)</p>", r"<figure>\1</figure>", body)
    html = (
        f"<!doctype html><html><head><meta charset='utf-8'><title>{TITLE}</title>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )
    out = HERE / "article_v3.html"
    out.write_text(html)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto(out.resolve().as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        broken = page.evaluate("[...document.images].filter(i => !i.naturalWidth).map(i => i.src)")
        if broken:
            raise SystemExit(f"Broken images: {broken}")
        page.pdf(path=str(HERE / PDF_NAME), format="A4", print_background=True, prefer_css_page_size=True)
        browser.close()
    print(f"Wrote {out.name} and {PDF_NAME}")


if __name__ == "__main__":
    main()
