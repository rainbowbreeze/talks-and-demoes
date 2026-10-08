#!/usr/bin/env python3
"""
Lint and Validation Script for Slide Presenter JSON Files.

This script verifies that a slides JSON file strictly complies with the schema
and formatting rules defined in the slide-presenter specifications:
- Validates the top-level structure (presentation_metadata, slides array).
- Enforces approved template IDs (section_title, quote_slide, content_simple,
  content_double, content_and_image, title_and_image, image_full_screen).
- Checks required and optional data attributes for each slide template.
- Detects misplaced keys (such as speaker_notes located outside the data object).
- Validates data types (lists, strings, dicts).
- Optionally verifies whether referenced local images exist on disk.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple


# Set of approved template IDs according to slide_template_definition.md
VALID_TEMPLATES = {
    "section_title",
    "quote_slide",
    "content_simple",
    "content_double",
    "content_and_image",
    "title_and_image",
    "image_full_screen",
}


def validate_metadata(metadata: Any) -> List[str]:
    """
    Validate the presentation_metadata block.

    Args:
        metadata: The value associated with presentation_metadata key.

    Returns:
        A list of error message strings, if any.
    """
    errors: List[str] = []

    # Ensure metadata is a dictionary object
    if not isinstance(metadata, dict):
        errors.append("Top-level 'presentation_metadata' must be a dictionary/object.")
        return errors

    # Check for presence and type of title
    if "title" not in metadata:
        errors.append("Missing required field 'title' in 'presentation_metadata'.")
    elif not isinstance(metadata["title"], str):
        errors.append("Field 'title' in 'presentation_metadata' must be a string.")

    # Check for presence and type of version
    if "version" not in metadata:
        errors.append("Missing required field 'version' in 'presentation_metadata'.")
    elif not isinstance(metadata["version"], str):
        errors.append("Field 'version' in 'presentation_metadata' must be a string.")

    return errors


def validate_column(col_data: Any, col_name: str) -> List[str]:
    """
    Validate a column structure for the content_double template.

    Args:
        col_data: The data dictionary for the column (column_left or column_right).
        col_name: Name identifier for reporting purposes.

    Returns:
        A list of error message strings, if any.
    """
    errors: List[str] = []

    # Confirm column data is an object
    if not isinstance(col_data, dict):
        errors.append(f"Field '{col_name}' must be an object/dict.")
        return errors

    # sub_heading is required by the schema specification
    if "sub_heading" not in col_data:
        errors.append(f"Missing required field 'sub_heading' in '{col_name}'.")
    elif not isinstance(col_data["sub_heading"], str):
        errors.append(f"Field 'sub_heading' in '{col_name}' must be a string.")

    # bullets array is required
    if "bullets" not in col_data:
        errors.append(f"Missing required field 'bullets' in '{col_name}'.")
    elif not isinstance(col_data["bullets"], list):
        errors.append(f"Field 'bullets' in '{col_name}' must be a list of strings.")
    else:
        # Check that all elements inside bullets are strings
        for idx, bullet in enumerate(col_data["bullets"]):
            if not isinstance(bullet, str):
                errors.append(f"Item {idx} in '{col_name}.bullets' must be a string.")

    return errors


def validate_image_path(image_uri: Any, slides_dir: Path) -> List[str]:
    """
    Validate an image URI field and check for file existence if it is local.

    Args:
        image_uri: The URI or relative path string.
        slides_dir: The directory where the slides JSON resides.

    Returns:
        A list of warning/error messages.
    """
    issues: List[str] = []

    # Must be a non-empty string
    if not isinstance(image_uri, str) or not image_uri.strip():
        issues.append("Field 'image_uri' must be a non-empty string.")
        return issues

    # Skip remote HTTP/HTTPS images
    if image_uri.startswith("http://") or image_uri.startswith("https://"):
        return issues

    # Check local image file existence with error handling
    try:
        local_path = slides_dir / image_uri
        if not local_path.is_file():
            issues.append(f"Referenced local image file does not exist: '{image_uri}' (looked in {slides_dir})")
    except Exception as err:
        issues.append(f"Failed to check local image path '{image_uri}': {err}")

    return issues


def validate_slide(
    slide: Any,
    slide_index: int,
    slides_dir: Path,
    check_images: bool = True
) -> Tuple[List[str], List[str]]:
    """
    Validate an individual slide item according to its template rules.

    Args:
        slide: The dictionary representing a slide.
        slide_index: 1-based index of the slide.
        slides_dir: Directory of the slides file.
        check_images: Whether to verify local image file existence.

    Returns:
        A tuple of (errors, warnings).
    """
    errors: List[str] = []
    warnings: List[str] = []

    # A slide item must be a JSON dictionary
    if not isinstance(slide, dict):
        errors.append(f"Slide {slide_index}: Item must be a dictionary object.")
        return errors, warnings

    # Check for common mistake: placing speaker_notes at root level instead of data
    if "speaker_notes" in slide:
        errors.append(
            f"Slide {slide_index}: 'speaker_notes' must be placed inside the 'data' object, not at slide root."
        )

    # Validate template existence and validity
    template = slide.get("template")
    if not template:
        errors.append(f"Slide {slide_index}: Missing required field 'template'.")
        return errors, warnings

    if template not in VALID_TEMPLATES:
        errors.append(
            f"Slide {slide_index}: Unknown template '{template}'. Approved templates are: {sorted(VALID_TEMPLATES)}"
        )
        return errors, warnings

    # Validate data payload
    data = slide.get("data")
    if data is None:
        errors.append(f"Slide {slide_index}: Missing required field 'data'.")
        return errors, warnings

    if not isinstance(data, dict):
        errors.append(f"Slide {slide_index}: 'data' must be an object/dict.")
        return errors, warnings

    # Validate speaker_notes if present in data (supported by all templates)
    if "speaker_notes" in data and not isinstance(data["speaker_notes"], str):
        errors.append(f"Slide {slide_index}: 'speaker_notes' inside 'data' must be a string.")

    # All slide templates support an optional image_uri field per upstream specifications
    if "image_uri" in data:
        if not isinstance(data["image_uri"], str):
            errors.append(f"Slide {slide_index}: 'image_uri' inside 'data' must be a string.")
        elif check_images:
            img_issues = validate_image_path(data["image_uri"], slides_dir)
            for issue in img_issues:
                warnings.append(f"Slide {slide_index} ({template}): {issue}")

    # Specific template validations
    try:
        if template == "section_title":
            # title is required
            if "title" not in data or not isinstance(data["title"], str):
                errors.append(f"Slide {slide_index} (section_title): Missing or invalid string field 'title'.")
            # sentence is optional, but must be string if present
            if "sentence" in data and not isinstance(data["sentence"], str):
                errors.append(f"Slide {slide_index} (section_title): Field 'sentence' must be a string.")

        elif template == "quote_slide":
            # quote is required
            if "quote" not in data or not isinstance(data["quote"], str):
                errors.append(f"Slide {slide_index} (quote_slide): Missing or invalid string field 'quote'.")
            # attribution is required
            if "attribution" not in data or not isinstance(data["attribution"], str):
                errors.append(f"Slide {slide_index} (quote_slide): Missing or invalid string field 'attribution'.")

        elif template == "content_simple":
            # title is required
            if "title" not in data or not isinstance(data["title"], str):
                errors.append(f"Slide {slide_index} (content_simple): Missing or invalid string field 'title'.")
            # bullets is required and must be a list
            if "bullets" not in data or not isinstance(data["bullets"], list):
                errors.append(f"Slide {slide_index} (content_simple): Missing or invalid list field 'bullets'.")
            else:
                for idx, b in enumerate(data["bullets"]):
                    if not isinstance(b, str):
                        errors.append(f"Slide {slide_index} (content_simple): Bullet #{idx+1} must be a string.")

        elif template == "content_double":
            # title is required
            if "title" not in data or not isinstance(data["title"], str):
                errors.append(f"Slide {slide_index} (content_double): Missing or invalid string field 'title'.")
            # column_left and column_right are both required
            for col_key in ["column_left", "column_right"]:
                if col_key not in data:
                    errors.append(f"Slide {slide_index} (content_double): Missing required object '{col_key}'.")
                else:
                    col_errors = validate_column(data[col_key], col_key)
                    for ce in col_errors:
                        errors.append(f"Slide {slide_index} (content_double): {ce}")

        elif template == "content_and_image":
            # title is required
            if "title" not in data or not isinstance(data["title"], str):
                errors.append(f"Slide {slide_index} (content_and_image): Missing or invalid string field 'title'.")
            # bullets is required
            if "bullets" not in data or not isinstance(data["bullets"], list):
                errors.append(f"Slide {slide_index} (content_and_image): Missing or invalid list field 'bullets'.")
            else:
                for idx, b in enumerate(data["bullets"]):
                    if not isinstance(b, str):
                        errors.append(f"Slide {slide_index} (content_and_image): Bullet #{idx+1} must be a string.")
            # image_position optional ("left" or "right")
            if "image_position" in data and data["image_position"] not in {"left", "right"}:
                errors.append(
                    f"Slide {slide_index} (content_and_image): 'image_position' must be 'left' or 'right'."
                )
            # image_uri is required for content_and_image
            if "image_uri" not in data:
                errors.append(f"Slide {slide_index} (content_and_image): Missing required field 'image_uri'.")

        elif template == "title_and_image":
            # title is required
            if "title" not in data or not isinstance(data["title"], str):
                errors.append(f"Slide {slide_index} (title_and_image): Missing or invalid string field 'title'.")
            # image_uri is required for title_and_image
            if "image_uri" not in data:
                errors.append(f"Slide {slide_index} (title_and_image): Missing required field 'image_uri'.")

        elif template == "image_full_screen":
            # image_uri is required for image_full_screen
            if "image_uri" not in data:
                errors.append(f"Slide {slide_index} (image_full_screen): Missing required field 'image_uri'.")

    except Exception as err:
        # Catch unexpected validation exceptions to prevent script crash
        errors.append(f"Slide {slide_index}: Unexpected error during template validation: {err}")

    return errors, warnings


def lint_slides(file_path: Path, check_images: bool = True) -> bool:
    """
    Main linting procedure for a slides JSON file.

    Args:
        file_path: Path to the JSON file to validate.
        check_images: Flag to enable/disable image path checking.

    Returns:
        True if all checks pass without errors, False otherwise.
    """
    print(f"\n==========================================")
    print(f"Linting Slides File: {file_path}")
    print(f"==========================================\n")

    # Step 1: Check file existence and readability
    try:
        if not file_path.is_file():
            print(f"[ERROR] Target file does not exist: {file_path}", file=sys.stderr)
            return False
    except OSError as err:
        print(f"[ERROR] Cannot access target file '{file_path}': {err}", file=sys.stderr)
        return False

    # Step 2: Parse JSON structure
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            deck = json.load(f)
    except json.JSONDecodeError as err:
        print(f"[ERROR] JSON syntax error in '{file_path}':", file=sys.stderr)
        print(f"        Line {err.lineno}, Column {err.colno}: {err.msg}", file=sys.stderr)
        return False
    except Exception as err:
        print(f"[ERROR] Failed to read '{file_path}': {err}", file=sys.stderr)
        return False

    # Top-level dictionary check
    if not isinstance(deck, dict):
        print(f"[ERROR] Root JSON structure must be an object/dict.", file=sys.stderr)
        return False

    all_errors: List[str] = []
    all_warnings: List[str] = []

    # Step 3: Validate presentation_metadata
    metadata = deck.get("presentation_metadata")
    if metadata is None:
        all_errors.append("Missing top-level 'presentation_metadata' object.")
    else:
        all_errors.extend(validate_metadata(metadata))

    # Step 4: Validate slides array
    slides = deck.get("slides")
    if slides is None:
        all_errors.append("Missing top-level 'slides' array.")
    elif not isinstance(slides, list):
        all_errors.append("Top-level 'slides' must be a JSON array/list.")
    else:
        slides_dir = file_path.parent
        print(f"Found {len(slides)} slides to validate...")

        for idx, slide in enumerate(slides, start=1):
            slide_errors, slide_warnings = validate_slide(
                slide=slide,
                slide_index=idx,
                slides_dir=slides_dir,
                check_images=check_images,
            )
            all_errors.extend(slide_errors)
            all_warnings.extend(slide_warnings)

    # Step 5: Report findings
    if all_warnings:
        print(f"\n[!] WARNINGS ({len(all_warnings)}):")
        for warn in all_warnings:
            print(f"  - {warn}")

    if all_errors:
        print(f"\n[X] ERRORS FOUND ({len(all_errors)}):", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        print("\nResult: FAILED - Please fix the errors listed above.\n")
        return False

    print("\nResult: PASSED - All slides strictly conform to the template schema!\n")
    return True


def main() -> None:
    """CLI entrypoint with argument parsing and top-level error handling."""
    parser = argparse.ArgumentParser(
        description="Lint and validate Slide Presenter JSON files against template schemas."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="slides.json",
        help="Path to slides JSON file (default: slides.json)",
    )
    parser.add_argument(
        "--no-image-check",
        action="store_true",
        help="Skip checking if local images referenced in slides exist on disk.",
    )

    try:
        args = parser.parse_args()
        target = Path(args.file)
        # If target doesn't exist directly, check under slides/ subdirectory (e.g. slides/slides.json)
        if not target.exists() and (target.parent / "slides" / target.name).is_file():
            target = target.parent / "slides" / target.name
        file_path = target.resolve()
        success = lint_slides(file_path=file_path, check_images=not args.no_image_check)
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as err:
        print(f"\nUnexpected fatal error: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
