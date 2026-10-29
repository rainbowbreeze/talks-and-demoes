# Gemini Project Overview: talks-and-demoes

This document provides an overview of the `talks-and-demoes` repository architecture, presentation conventions, and automated workflows.

## Repository Structure

Each talk or workshop lives in its own top-level directory prefixed by the year (e.g., `2026-ai-minions-design`, `2026-build_your_agent`, `2026-hermes_workshop`, `2026-openclaw`):

- **`<talk-folder>/slides/slides.json`**: Structured slide deck definition (metadata + array of slides following the 8 templates supported by [SelfHosted Slide Presenter](https://github.com/rainbowbreeze/slide-presenter)).
- **`<talk-folder>/slides/theme.json`**: Visual theme configuration (fonts, colors, background image, and footer text).
- **`<talk-folder>/slides/*.{png,jpg,webp}`**: Local media assets referenced by `slides.json` and `theme.json`.
- **`.github/workflows/export-slides-pdf.yml`**: GitHub Actions workflow that automatically generates 16:9 widescreen PDFs and publishes them to rolling GitHub Releases.

## Automated PDF Generation & GitHub Releases

- **Workflow File:** [`.github/workflows/export-slides-pdf.yml`](.github/workflows/export-slides-pdf.yml)
- **Triggers:**
  - `push` to `main` modifying any file matching `**/slides/**`.
  - `workflow_dispatch` with an optional `presentation` input (`all` by default, or a specific talk folder name such as `2026-ai-minions-design`).
- **Execution Pipeline:**
  1. Detects which `<talk-folder>` directories have modified `slides/` (and contain both `slides/slides.json` and `slides/theme.json`).
  2. Installs Linux font packages (`fonts-inter`, `fonts-noto-color-emoji`, `fonts-liberation`) so typography and emojis match local macOS rendering.
  3. Clones `https://github.com/rainbowbreeze/slide-presenter.git`, creates a Python virtual environment (`python3 -m venv /tmp/slide-presenter/venv`), installs its Python dependencies (`pip install -r requirements.txt`), and installs headless Chromium (`playwright install --with-deps chromium`).
  4. Runs `python src/app.py --slides-dir <talk-folder>/slides --export-pdf <talk-folder>/<talk-folder>.pdf` to generate a 16:9 (`1920x1080`) PDF.
  5. Moves the rolling git tag `<talk-folder>` to the current commit SHA and creates or updates the corresponding GitHub Release (`<talk-folder>`), uploading `<talk-folder>.pdf` with `--clobber`.
