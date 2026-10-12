# talks-and-demoes

Repository of slide decks, workshop materials, and demo code for my talks and sessions.

## Viewing Presentations Locally

Slide decks from 2026 onward are stored in JSON format (`<talk-folder>/slides/slides.json` and `<talk-folder>/slides/theme.json`) and rendered using **[SelfHosted Slide Presenter](https://github.com/rainbowbreeze/slide-presenter)**.

```bash
git clone https://github.com/rainbowbreeze/slide-presenter.git
cd slide-presenter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Launch a presentation in your browser at http://127.0.0.1:5000
python src/app.py --slides-dir ../talks-and-demoes/2026-ai-minions-design/slides
```

## Exporting Slides to PDF

### 1. Automated GitHub Releases (GitHub Actions)

Whenever changes are pushed to `main` inside any `<talk-folder>/slides/**` directory, the [Export Presentation Slides to PDF](.github/workflows/export-slides-pdf.yml) GitHub Actions workflow automatically:
1. Renders a 16:9 (`1920x1080`) widescreen PDF using `slide-presenter --export-pdf`.
2. Creates or updates a rolling **GitHub Release** tagged `<talk-folder>` (for example, `2026-ai-minions-design`).
3. Attaches `<talk-folder>.pdf` to that release so the latest PDF is always available at:
   `https://github.com/rainbowbreeze/talks-and-demoes/releases/download/<talk-folder>/<talk-folder>.pdf`

You can also trigger the workflow manually from the **Actions** tab (**Export Presentation Slides to PDF** → **Run workflow**), passing either a specific presentation directory name (e.g., `2026-ai-minions-design`) or `all` to regenerate PDFs for all presentations.

### 2. Local CLI PDF Export

To export a presentation to PDF locally from the command line:

```bash
cd slide-presenter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium

python src/app.py \
  --slides-dir ../talks-and-demoes/2026-ai-minions-design/slides \
  --export-pdf ../talks-and-demoes/2026-ai-minions-design/2026-ai-minions-design.pdf
```
