---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: ja
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK（Python 用）"
head_description: "高速な Document Parser SDK（Python 用）。PDF、Word、Excel、メール、および50以上のドキュメント形式からテキスト、画像、メタデータ、バーコード、テーブルなどのデータを抽出します。"

############################# Header ############################
title: "Document Parser SDK（Python 用）"
description: "Python アプリに高速かつ正確な文書解析を追加し、ドキュメントや画像からテキスト、画像、メタデータ、構造化データを抽出します。"
words:
  for: "対象"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI ダウンロード"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "ライセンス"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "開始する準備はできましたか？"
  description: "GroupDocs.Parserの機能を無料でお試し、またはライセンスをリクエストしてください"

release:
  enable: false
  title: "バージョン {0} がリリースされました"
  notes: "新機能を見る"
  downloads: "ダウンロード"

code:
  title: "Python を使用してテキストを抽出"
  more: "その他のサンプル"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # ドキュメントを読み込む
    with Parser("sample.pdf") as parser:
        # ドキュメントからテキストを抽出する
        text = parser.GetText()

        # 抽出したすべてのテキストを出力する
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser の概要"
  description: "Python アプリケーションで高精度な文書解析を実行するための Document Parser SDK"
  features:
    # feature loop
    - title: "ドキュメントからデータを抽出"
      content: "GroupDocs.Parser for Python via .NET API を使用すると、Office ドキュメント、メール、添付ファイル、アーカイブなど、さまざまなファイル形式からテキスト、メタデータ、画像を取得できます。この強力なツールにより、データ分析、検索エンジンのインデックス作成、コンテンツ管理システムなど、様々なアプリケーションで必要となる情報を効率的にアクセス・処理できます。"

    # feature loop
    - title: "ドキュメントを解析"
      content: "PDF フォームからハイパーリンク、テーブル、QR コード、バーコード、およびデータなどのさまざまな要素を抽出します。また、カスタムテンプレートを使用してドキュメントから任意の情報を解析できます。"

    # feature loop
    - title: "結果のカスタマイズ"
      content: "Python API を使用すると、RAW、構造化、HTML、Markdown など、さまざまな形式でデータを取得できます。さらに、ドキュメントテキスト内の特定の単語やフレーズを検索する機能も提供します。"

############################# Platforms ############################
platforms:
  enable: true
  title: "プラットフォームに依存しない"
  description: "GroupDocs.Parser for Python via .NET は以下のオペレーティングシステム、フレームワーク、パッケージマネージャをサポートします"
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "サポートされているファイル形式"
  description: |
    GroupDocs.Parser for Python via .NET は以下の [ファイル形式](https://docs.groupdocs.com/parser/python-net/supported-document-formats/) に対応しています。
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office 形式
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### 画像 & その他の形式
        * **ポータブル:** PDF 
        * **画像:** JPG, BMP, PNG, TIFF, GIF
        * **その他のオフィス形式:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### その他の形式
        * **Web:** HTML, MHTML 
        * **アーカイブ:** ZIP, TAR, 7Z 
        * **電子書籍:** CHM, EPUB, FB2, MOBI 

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Python via .NET の機能"
  description: "当社の Python Document Parser SDK を使用して、PDF、Office ドキュメント、画像、その他の形式からデータを迅速かつ正確に抽出します。"

  items:
    # feature loop
    - icon: "text"
      title: "テキストを抽出"
      content: "Office ドキュメント、PDF ファイル、画像などさまざまなファイル形式からテキスト情報を抽出し、読みやすさと分析を容易にします。"

    # feature loop
    - icon: "image"
      title: "画像を抽出"
      content: "Office ドキュメントや PDF ファイルなど多様なソースからビジュアルコンテンツを取得し、便利にアクセス・利用できます。"

    # feature loop
    - icon: "qr"
      title: "QR コードをスキャン"
      content: "Office ドキュメント、PDF ファイル、またはビジュアルコンテンツ内にある QR コードを検出し、デコードして情報を効率的に取得します。"

    # feature loop
    - icon: "email"
      title: "メール添付ファイルやアーカイブからデータを抽出"
      content: "メールメッセージ、ファイル添付、圧縮データソースから有用な情報を収集し、効果的に分析・活用できます。"

    # feature loop
    - icon: "table"
      title: "テーブルを抽出"
      content: "PDF ドキュメントから表形式データを識別・抽出し、体系的な分析と活用が可能です。"

    # feature loop
    - icon: "hyperlink"
      title: "ハイパーリンクを抽出"
      content: "オフィス文書または PDF ファイル内のハイパーリンクとメールアドレスを検索して抽出し、効率的にアクセスできるようにします。"

    # feature loop
    - icon: "pdf"
      title: "PDF フォームの解析"
      content: "PDF フォームは、ユーザーが電子的に情報を入力できる入力可能なフィールドを備えたデジタル文書です。Python API を使用して、これらのフォームからデータを抽出し、効率的に処理できます。"

    # feature loop
    - icon: "template"
      title: "テンプレートによるデータ解析"
      content: "カスタムテンプレートを作成し、Python API と組み合わせて PDF ファイルから特定の情報を解析し、データ抽出プロセスを簡素化します。"

    # feature loop
    - icon: "search"
      title: "文書内のテキスト検索"
      content: "文書内の特定の単語やパターンを迅速に検索します。"


############################# Code samples ############################
code_samples:
  enable: true
  title: "コードサンプル"
  description: "基本的なテキスト抽出に加えて、テキスト、画像、メタデータの迅速な抽出に最も一般的なユースケースをご紹介します。"
  items:
    # code sample loop
    - title: "文書内のテキスト検索"
      content: |
        この例では、PDF 文書内で特定のフレーズを検索し、見つかった位置を出力する方法を示します。
        {{< landing/code title="Python で文書内のテキスト検索">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # 文書をロードする
        with Parser("sample.pdf") as parser:
            # フレーズが見つかったページインデックスと矩形を出力する
            for area in parser.Search("Total Amount"):
                # フレーズが見つかったページインデックスと矩形を出力する
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "文書から画像を抽出"
      content: |
        この例では、PDF 文書から画像を抽出し、ファイルに保存する方法を示します。
        {{< landing/code title="Python で文書から画像を抽出">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # 文書をロードする
        with Parser("sample.docx") as parser:
            # 文書から画像を抽出する
            images = parser.GetImages()

            # 画像をファイルに保存する
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "文書からメタデータを抽出"
      content: |
        この例では、PDF 文書からメタデータを抽出し、出力する方法を示します。
        {{< landing/code title="Python で文書からメタデータを抽出">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # 文書をロードする
        with Parser("sample.pdf") as parser:
            # 文書からメタデータを抽出する
            metadata = parser.GetMetadata()

            # メタデータを出力する
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
