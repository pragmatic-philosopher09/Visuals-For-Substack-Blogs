# Roblox teardown versions

| Version | Contents | Open |
|---|---|---|
| **v1 — reconstructed** | Earlier card-based visuals, source HTML/CSS, and nine PNG exports. Recreated from the conversation after the original uncommitted files were overwritten; not an exact backup. | [Visuals](v1/visuals.html) |
| **v2 — previous** | Revised conversational article, bespoke illustrated visuals, official video embeds, source files, and nine PNG exports. | [Article](v2/article.md) · [HTML](v2/article.html) · [PDF](v2/Roblox_Teardown.pdf) · [References](v2/references.md) · [Visuals](v2/visuals.html) |
| **v3 — current** | Revised after ChatGPT and Claude reviews: Q3 2026 figures, a sharper retention-vs-monetization thesis, economics, safety, defensibility, a live game-page audit, and redrawn visuals. Files carry a `_v3` suffix. | [Article](v3/article_v3.md) · [HTML](v3/article_v3.html) · [PDF](v3/Roblox_Teardown_v3.pdf) · [References](v3/references_v3.md) · [Visuals](v3/visuals_v3.html) |

Each version is self-contained; `assets/` inside each version contains its own PNGs. V1 contains the visual reconstruction only, not a reconstructed article. Earlier versions are never edited in place; each revision gets a new folder and versioned filenames.

To rebuild the v3 article HTML and PDF after editing `article_v3.md`:

```sh
python3 Roblox-Teardown/v3/build_article.py
```

To re-export v3 with an existing Python Playwright/Chromium installation:

```sh
python3 Roblox-Teardown/v3/export_visuals.py
```

Use `--check-only` to validate without rewriting images, or `--pdf /absolute/path/to/panels.pdf` for a print export. No dependencies are installed by the script.
