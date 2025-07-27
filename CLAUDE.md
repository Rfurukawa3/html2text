# html2text

## Project Overview

htmlファイルを読み込み、そのhtmlの本文部分のみを抽出してテキストファイルとして保存するツール。

引数には入力ディレクトリと出力ディレクトリを受け付けます。

入力ディレクトリ内を再帰的に探索してhtmlファイルを探し、そこから本文を抽出したテキストファイルを出力ディレクトリに保存します。

出力ディレクトリは入力ディレクトリと同じ構造になるように作成します。

## Requirements

### 1. Python Project with Ruff Coding Standards

- This is a Python project
- Follow Ruff linting rules as specified in pyproject.toml
- Compliant rules and ignored rules are defined in the configuration
- **Type hints are mandatory** for all functions and methods
- **Docstrings are mandatory** for all functions, classes, and methods
- Docstrings must follow **Google Style** format

### 2. Markdown Documentation Standards

- All documentation and markdown files should follow markdownlint rules
- Ensure proper formatting and consistency across all .md files
- You can use `markdownlint-cli2` in CLI

### 3. Test-Driven Development

- Follow Test-Driven Development (TDD) methodology
- Use pytest for all testing
- Write tests before implementing functionality
- Ensure comprehensive test coverage

### 4. Package Management with uv

- Use uv for package management
- Runtime dependencies: `uv add <package>`
- Development-only dependencies: `uv add --dev <package>`
