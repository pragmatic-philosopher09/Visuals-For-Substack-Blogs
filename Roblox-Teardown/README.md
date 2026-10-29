# Roblox teardown versions

| Version | Contents | Open |
|---|---|---|
| **v1 — reconstructed** | Earlier card-based visuals, source HTML/CSS, and nine PNG exports. Recreated from the conversation after the original uncommitted files were overwritten; not an exact backup. | [Visuals](v1/visuals.html) |
| **v2 — current** | Revised conversational article, bespoke illustrated visuals, official video embeds, source files, and nine PNG exports. | [Article](v2/article.md) · [Visuals](v2/visuals.html) |

Each version is self-contained; `assets/` inside each version contains its own PNGs. V1 contains the visual reconstruction only, not a reconstructed article.

Work is stored in this session's isolated worktree. The main checkout at `/Users/priyanshu._.mohanty/Visuals-For-Substack-Blogs/Roblox-Teardown` has not been read or modified.

To re-export v2 with an existing Python Playwright/Chromium installation:

```sh
python3 Roblox-Teardown/v2/export_visuals.py
```

Use `--check-only` to validate without rewriting images, or `--pdf /absolute/path/to/panels.pdf` for a print export. No dependencies are installed by the script.
