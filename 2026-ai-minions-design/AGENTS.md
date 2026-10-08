# AGENTS.md — Instructions for AI Agents Working on This Project

This document outlines the project architecture, file organization, presentation template rules, and required automated validation workflows.

---

## 1. Project Structure and File Organization

All agents modifying content in this repository must understand the file layout:

```text
./
├── AGENTS.md               # Operating instructions and SOPs for AI agents (this file)
├── lint_slides.py          # Python linter and validator for slide JSON definitions
└── slides/                 # Presentation assets and configuration
    ├── slides.json         # Primary slide deck JSON configuration file
    ├── theme.json          # Theme, styling, and footer configuration
    └── *.png, *.webp       # Media assets and images referenced by slides
```

### Key Files:
- **Slide Deck** ([`slides/slides.json`](slides/slides.json)): Defines presentation metadata and the array of slide objects.
- **Theme Configuration** ([`slides/theme.json`](slides/theme.json)): Defines fonts, colors, and global footer text.
- **Validator** ([`lint_slides.py`](lint_slides.py)): Automated linter ensuring schema compliance and local asset presence.

---

## 2. Slide Template Specifications

To determine the schema, supported layout options, and formatting rules for slides, agents **MUST** refer to the upstream documentation:
> **Official Template Reference**:  
> [https://raw.githubusercontent.com/rainbowbreeze/slide-presenter/refs/heads/main/README.md](https://raw.githubusercontent.com/rainbowbreeze/slide-presenter/refs/heads/main/README.md)

> [!IMPORTANT]
> **Template Specification Synchronization**:  
> The first time a project is scaffolded, or whenever the user requests an update to the slide template specifications, agents **MUST** re-read the upstream **Official Template Reference** URL and update **both** this `AGENTS.md` file and the [`lint_slides.py`](lint_slides.py) validator to reflect any new, modified, or deprecated templates and validation rules.

### Universal Slide Fields (Inside `data`)
Every slide template supports these optional properties inside its `data` dictionary:
- `speaker_notes` (*string, optional*): Markdown text for speaker notes.  
  **CRITICAL**: Must always be placed inside `data` (e.g. `slide["data"]["speaker_notes"]`), **never** at the root level of the slide object.
- `image_uri` (*string, optional*): Path to a local image in `slides/` or external URL.

### The 7 Approved Slide Templates
Every slide in `slides.json` must strictly use one of the following templates:

1. **`section_title`**: Centered section title slide.
   - `title` (*string, required*): Main heading.
   - `sentence` (*string, optional*): Subtitle or catchy section summary.

2. **`quote_slide`**: Large centered quote slide.
   - `quote` (*string, required*): Full quote text.
   - `attribution` (*string, required*): Author or source name.

3. **`content_simple`**: Title with an optional introductory sentence and a single bullet list.
   - `title` (*string, required*): Slide heading.
   - `sentence` (*string, optional*): Introductory sentence displayed above the bullet points.
   - `bullets` (*list of strings, required*): Bullet points.

4. **`content_double`**: Two-column content slide, each column supporting an optional sub-heading and introductory sentence.
   - `title` (*string, required*): Slide heading.
   - `column_left` (*object, required*): Contains `sub_heading` (*string, optional*), `sentence` (*string, optional*), and `bullets` (*list of strings, required*).
   - `column_right` (*object, required*): Contains `sub_heading` (*string, optional*), `sentence` (*string, optional*), and `bullets` (*list of strings, required*).

5. **`content_and_image`**: Split slide with bullets on one side and an image on the other.
   - `title` (*string, required*): Slide heading.
   - `bullets` (*list of strings, required*): Bullet points.
   - `image_uri` (*string, required*): Path to image in `slides/` or external URL.
   - `image_position` (*string, optional*): `"left"` or `"right"` (defaults to `"right"`).

6. **`title_and_image`**: Title with a centered image beneath.
   - `title` (*string, required*): Slide heading.
   - `image_uri` (*string, required*): Path to image in `slides/` or external URL.

7. **`image_full_screen`**: Full-bleed image without text or footer.
   - `image_uri` (*string, required*): Path to image in `slides/` or external URL.

---

## 3. General Formatting Rules

1. **Local Image References**:
   - When referencing local images, provide the relative file name located within the `slides/` directory (e.g., `"image_uri": "rainbowbreeze_full.png"`).

---

## 4. Mandatory Agent Verification Workflow: Running the Linter

> **MANDATORY FOR ALL AGENTS:**  
> Whenever you add, update, rearrange, or delete slides in [`slides/slides.json`](slides/slides.json), you **MUST** run the slide linter before reporting back to the user.

### Execution Command:
```bash
# From project root:
python3 lint_slides.py

# Or from within slides/ directory:
python3 ../lint_slides.py
```

### Verification Criteria:
- The command must terminate with exit code `0` and print `Result: PASSED`.
- If any `[X] ERRORS` or `[!] WARNINGS` are displayed, you must address and resolve them immediately before finishing the task.

---

## 5. Scaffolding a New Slide Deck

When tasked with creating a new slide deck or scaffolding a presentation project, agents must follow this procedure:

1. **Sync Template Specifications & Validator**:  
   Follow the synchronization rule in **Section 2**: re-read the upstream Official Template Reference and ensure `AGENTS.md` and `lint_slides.py` are up to date.

2. **Create the Directory**:  
   Create the `slides/` folder in the project root.

3. **Generate `slides/theme.json`**:  
   Define the theme file **without any background image** (do not include `"background-image"`):
   ```json
   {
     "font-main": "'Helvetica', sans-serif",
     "text-color": "#000000",
     "footer-text": "Presentation Title"
   }
   ```

4. **Generate `slides/slides.json`**:  
   Create the initial slide deck with the presentation title in metadata and a single sample `section_title` slide:
   ```json
   {
     "presentation_metadata": {
       "title": "Presentation Title",
       "version": "1.0"
     },
     "slides": [
       {
         "template": "section_title",
         "data": {
           "title": "Sample Section Title"
         }
       }
     ]
   }
   ```

5. **Verify the Scaffold**:  
   Always run the linter following the workflow in **Section 4** to guarantee the initial deck passes all validation checks.
