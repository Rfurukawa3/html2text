"""Test cases for HTML text extraction functionality."""

import tempfile
from pathlib import Path

import pytest

from html2text.extractor import HtmlTextExtractor


class TestHtmlTextExtractor:
    """Test class for HtmlTextExtractor."""

    def test_extract_text_from_simple_html(self) -> None:
        """Test extracting text from simple HTML content."""
        html_content = """
        <html>
            <head><title>Test Page</title></head>
            <body>
                <h1>Main Title</h1>
                <p>This is a paragraph with some text.</p>
                <p>Another paragraph here.</p>
            </body>
        </html>
        """
        extractor = HtmlTextExtractor()
        result = extractor.extract_text(html_content)

        assert "Main Title" in result
        assert "This is a paragraph with some text." in result
        assert "Another paragraph here." in result
        assert "<html>" not in result
        assert "<p>" not in result

    def test_extract_text_with_script_and_style(self) -> None:
        """Test that script and style tags are excluded from extraction."""
        html_content = """
        <html>
            <head>
                <title>Test Page</title>
                <style>body { color: red; }</style>
            </head>
            <body>
                <h1>Main Content</h1>
                <script>alert('Hello');</script>
                <p>Visible content</p>
            </body>
        </html>
        """
        extractor = HtmlTextExtractor()
        result = extractor.extract_text(html_content)

        assert "Main Content" in result
        assert "Visible content" in result
        assert "body { color: red; }" not in result
        assert "alert('Hello');" not in result

    def test_extract_text_from_empty_html(self) -> None:
        """Test extracting text from empty HTML."""
        html_content = "<html><head></head><body></body></html>"
        extractor = HtmlTextExtractor()
        result = extractor.extract_text(html_content)

        assert result.strip() == ""

    def test_process_directory_structure(self) -> None:
        """Test processing directory with HTML files maintaining structure."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "input"
            output_dir = Path(temp_dir) / "output"

            # Create input directory structure
            (input_dir / "subdir").mkdir(parents=True)

            # Create HTML files
            html1 = input_dir / "page1.html"
            html1.write_text("<html><body><h1>Page 1</h1></body></html>")

            html2 = input_dir / "subdir" / "page2.html"
            html2.write_text("<html><body><p>Page 2 content</p></body></html>")

            # Process directory
            extractor = HtmlTextExtractor()
            extractor.process_directory(input_dir, output_dir)

            # Check output files exist
            assert (output_dir / "page1.txt").exists()
            assert (output_dir / "subdir" / "page2.txt").exists()

            # Check content
            txt1_content = (output_dir / "page1.txt").read_text()
            assert "Page 1" in txt1_content

            txt2_content = (output_dir / "subdir" / "page2.txt").read_text()
            assert "Page 2 content" in txt2_content

    def test_process_directory_ignores_non_html_files(self) -> None:
        """Test that non-HTML files are ignored during processing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "input"
            output_dir = Path(temp_dir) / "output"
            input_dir.mkdir()

            # Create HTML and non-HTML files
            (input_dir / "page.html").write_text("<html><body>HTML content</body></html>")
            (input_dir / "data.txt").write_text("Text file content")
            (input_dir / "image.jpg").write_bytes(b"fake image data")

            extractor = HtmlTextExtractor()
            extractor.process_directory(input_dir, output_dir)

            # Only HTML file should be processed
            assert (output_dir / "page.txt").exists()
            assert not (output_dir / "data.txt").exists()
            assert not (output_dir / "image.jpg").exists()

    def test_html_file_extensions(self) -> None:
        """Test that various HTML file extensions are recognized."""
        extractor = HtmlTextExtractor()

        assert extractor._is_html_file(Path("test.html"))
        assert extractor._is_html_file(Path("test.htm"))
        assert not extractor._is_html_file(Path("test.txt"))
        assert not extractor._is_html_file(Path("test.xml"))
