"""HTML to text extraction tool."""

import argparse
import sys
from pathlib import Path

from .extractor import HtmlTextExtractor


def main() -> None:
    """Main entry point for the html2text CLI tool."""
    parser = argparse.ArgumentParser(
        description="Extract text content from HTML files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  html2text input_dir output_dir
  html2text /path/to/html/files /path/to/text/output
        """,
    )

    parser.add_argument(
        "input_dir",
        type=Path,
        help="Input directory containing HTML files",
    )

    parser.add_argument(
        "output_dir",
        type=Path,
        help="Output directory for extracted text files",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    try:
        extractor = HtmlTextExtractor()

        if args.verbose:
            print(f"Processing HTML files from: {args.input_dir}")  # noqa: T201
            print(f"Saving text files to: {args.output_dir}")  # noqa: T201

        extractor.process_directory(args.input_dir, args.output_dir)

        if args.verbose:
            print("Processing completed successfully!")  # noqa: T201

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)  # noqa: T201
        sys.exit(1)
    except (OSError, KeyboardInterrupt) as e:
        print(f"Unexpected error: {e}", file=sys.stderr)  # noqa: T201
        sys.exit(1)
