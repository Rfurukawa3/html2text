# html2text

HTMLファイルから本文部分のみを抽出してテキストファイルとして保存するツール

## 概要

html2textは、HTMLファイルのディレクトリを再帰的に探索し、各HTMLファイルから本文部分のみを抽出してテキストファイルとして保存するPythonツールです。

## 特徴

- HTMLファイルから本文のみを抽出（scriptタグやstyleタグを除去）
- ディレクトリ構造を保持した出力
- HTML（.html）およびHTM（.htm）ファイル形式に対応
- 再帰的なディレクトリ探索
- コマンドライン引数による入力・出力ディレクトリ指定

## インストール

このプロジェクトは[uv](https://docs.astral.sh/uv/)を使用して管理されています。

```bash
# プロジェクトの依存関係をインストール
uv sync
```

## 使用方法

### コマンドライン使用

```bash
# 基本的な使用方法
html2text input_directory output_directory

# 詳細な処理情報を表示
html2text -v input_directory output_directory

# ヘルプの表示
html2text --help
```

### 例

```bash
# htmlディレクトリ内のHTMLファイルをtextディレクトリに変換
html2text ./html_files ./text_output

# 詳細モードで実行
html2text -v ./html_files ./text_output
```

### 入力例

ディレクトリ構造:

```text
html_files/
├── index.html
├── about.html
└── blog/
    ├── post1.html
    └── post2.html
```

### 出力例

変換後の構造:

```text
text_output/
├── index.txt
├── about.txt
└── blog/
    ├── post1.txt
    └── post2.txt
```

### webページのhtmlを取得するコマンド例

```bash
wget --mirror --adjust-extension --recursive -l 8 --convert-links --quiet --show-progress \
--accept '*.html,*.htm' --wait=5 --random-wait \
https://www.example.com
```

## 開発

### テストの実行

```bash
# テストの実行
uv run pytest

# カバレッジ付きでテストを実行
uv run pytest --cov=html2text

# 詳細モードでテストを実行
uv run pytest -v
```

### コードフォーマットとリンティング

```bash
# コードフォーマット
uv run ruff format .

# リンティングチェック
uv run ruff check .

# 自動修正可能な問題を修正
uv run ruff check --fix .
```

## 技術仕様

- **Python バージョン**: 3.13以上
- **HTML解析**: BeautifulSoup4を使用
- **テストフレームワーク**: pytest
- **コードフォーマット**: Ruff
- **パッケージ管理**: uv
