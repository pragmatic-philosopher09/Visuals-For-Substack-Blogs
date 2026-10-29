"""Export original panels with an existing Python Playwright/Chromium installation."""

import argparse
import re
from pathlib import Path

from playwright.sync_api import expect, sync_playwright


PANELS = (
    "scale",
    "personas",
    "journey",
    "interface",
    "retention",
    "economy",
    "metrics",
    "opportunities",
    "concept",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--pdf", type=Path, help="Optional nine-page print export")
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    article = (folder / "article.md").read_text()

    for link in re.findall(r"\]\(([^)]+)\)", article):
        if not link.startswith(("https://", "http://", "#")):
            path, _, _ = link.partition("#")
            assert (folder / path).is_file(), f"Missing article asset: {link}"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(
            viewport={"width": 1160, "height": 1000}, reduced_motion="reduce"
        )
        errors = []
        requests = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("request", lambda request: requests.append(request.url))
        page.goto((folder / "visuals.html").as_uri())
        assert page.locator("section.panel").count() == len(PANELS)
        assert page.locator(".crowd-person.kid").count() == 35
        assert page.locator(".crowd-person.teen").count() == 38
        assert page.locator(".crowd-person.adult").count() == 27
        assert not any(url.startswith("https://") for url in requests), requests
        assert page.locator("iframe").count() == 0

        ids = page.locator("[id]").evaluate_all("(nodes) => nodes.map(n => n.id)")
        assert len(ids) == len(set(ids)), "Duplicate element IDs"
        for link in page.locator('a[href^="#"]').all():
            assert link.get_attribute("href")[1:] in ids

        for width in (1440, 1160, 1024, 768, 560, 390, 320):
            page.set_viewport_size({"width": width, "height": 1000})
            assert page.evaluate(
                "document.documentElement.scrollWidth <= innerWidth"
            ), f"Horizontal overflow at {width}px"
            for name in PANELS:
                assert page.locator(f"#{name}").is_visible()

        page.set_viewport_size({"width": 1160, "height": 1000})
        for step in range(1, 7):
            page.locator("#journey-next").click()
            expected = (step % 6) + 1
            assert f"Room {expected} of 6" in page.locator(
                "#journey-status"
            ).inner_text()
            assert page.locator('.corridor [aria-current="step"]').count() == 1

        page.locator("#route-friend").click()
        assert page.locator("#route-friend").get_attribute("aria-pressed") == "true"
        assert "not a speed claim" in page.locator("#route-status").inner_text()
        page.locator("#route-browse").click()
        page.locator("#balance-toggle").click()
        assert page.locator("#balance-toggle").get_attribute("aria-pressed") == "true"
        page.locator("#balance-toggle").click()
        page.locator("#guidance-toggle").check()
        assert "Example only" in page.locator("#guidance").inner_text()
        page.locator("#guidance-toggle").uncheck()
        assert "Not provided" in page.locator("#guidance").inner_text()
        page.locator('a[href="#metric-definitions"]').click()
        expect(page.locator("#metric-definitions")).to_have_attribute("open", "")
        page.locator('a[href="#experiment-notes"]').click()
        expect(page.locator("#experiment-notes")).to_have_attribute("open", "")

        # Test consent and persistent fallback links without requiring video playback.
        page.route(
            "https://www.youtube-nocookie.com/embed/**",
            lambda route: route.fulfill(
                status=200, content_type="text/html", body="<p>Player test stub</p>"
            ),
        )
        for key, video_id in (("hunt", "I7pmbho1DUQ"), ("discovery", "K7jsk3bzmvE")):
            page.locator(f'[data-load-video="{key}"]').click()
            frame = page.locator(f'[data-video="{key}"] iframe')
            assert frame.get_attribute("src") == (
                f"https://www.youtube-nocookie.com/embed/{video_id}"
            )
            assert "autoplay" not in frame.get_attribute("allow")
            assert page.locator(
                f'a[href="https://www.youtube.com/watch?v={video_id}"]'
            ).is_visible()
        assert not errors, errors

        if not args.check_only:
            assets = folder / "assets"
            assets.mkdir(exist_ok=True)
            page.goto((folder / "visuals.html").as_uri())
            page.set_viewport_size({"width": 1160, "height": 1400})
            page.evaluate("document.documentElement.classList.add('exporting')")
            for index, name in enumerate(PANELS, 1):
                page.locator(f"#{name}").screenshot(
                    path=str(assets / f"{index:02}-{name}.png"),
                    animations="disabled",
                )
            print(f"Exported {len(PANELS)} original panels to {assets}")

        if args.pdf:
            page.pdf(
                path=str(args.pdf),
                prefer_css_page_size=True,
                print_background=True,
            )
            page_count = len(re.findall(rb"/Type\s*/Page\b", args.pdf.read_bytes()))
            assert page_count == 9, f"Expected 9 print pages; got {page_count}"
            print(f"Print export: {page_count} pages")
        browser.close()

    print("Responsive layouts, interactions, links, and click-to-load media: passed")
    print("Video playback is not asserted; tests use a local player response stub.")


if __name__ == "__main__":
    main()
