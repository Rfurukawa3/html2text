"""HTML text extraction functionality."""

import sys
from pathlib import Path

from bs4 import BeautifulSoup


class HtmlTextExtractor:
    """Extract text content from HTML files."""

    def extract_text(self, html_content: str) -> str:
        """Extract readable text from HTML content.

        Args:
            html_content: Raw HTML content as string

        Returns:
            Extracted text content without HTML tags
        """
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Get text and clean up whitespace
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        return "\n".join(chunk for chunk in chunks if chunk)

    def process_directory(self, input_dir: Path, output_dir: Path) -> None:
        """Process all HTML files in input directory and save as text files.

        Args:
            input_dir: Directory containing HTML files to process
            output_dir: Directory to save extracted text files
        """
        input_dir = Path(input_dir)
        output_dir = Path(output_dir)

        if not input_dir.exists():
            msg = f"Input directory not found: {input_dir}"
            raise FileNotFoundError(msg)

        # Create output directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)

        # Process all HTML files recursively
        for html_file in input_dir.rglob("*"):
            if self._is_html_file(html_file) and html_file.is_file():
                self._process_single_file(html_file, input_dir, output_dir)

    def _process_single_file(self, html_file: Path, input_dir: Path, output_dir: Path) -> None:
        """Process a single HTML file and save as text.

        Args:
            html_file: Path to HTML file to process
            input_dir: Base input directory
            output_dir: Base output directory
        """
        try:
            # Read HTML content
            html_content = html_file.read_text(encoding="utf-8")

            # Extract text
            text_content = self.extract_text(html_content)

            # Calculate relative path and create output file path
            relative_path = html_file.relative_to(input_dir)
            output_file = output_dir / relative_path.with_suffix(".txt")

            # Create parent directories if needed
            output_file.parent.mkdir(parents=True, exist_ok=True)

            # Write text content
            output_file.write_text(text_content, encoding="utf-8")

        except (OSError, UnicodeDecodeError) as e:
            print(f"Error processing {html_file}: {e}", file=sys.stderr)  # noqa: T201

    def _is_html_file(self, file_path: Path) -> bool:
        """Check if file is an HTML file based on extension.

        Args:
            file_path: Path to check

        Returns:
            True if file has HTML extension, False otherwise
        """
        return file_path.suffix.lower() in {".html", ".htm"}
