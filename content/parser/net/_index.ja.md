---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: ja
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "GroupDocs.Parser for .NET 文書解析アプリ"
head_description: ".NET アプリケーション向けのすべてを兼ね備えた文書解析ソリューションを提供します。シンプルなドラッグ＆ドロップ機能でオンライン文書フォーマットからデータを抽出します。"

############################# Header ############################
title: ".NET APIを介して文書を解析"
description: "プログラマーやエンドユーザー向けに柔軟なAPIとアプリベースのソリューションを使用して、任意のプラットフォームで文書および画像からデータを抽出します。"
words:
  for: "のために"

actions:
  main: "Nuget ダウンロード"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "ライセンス取得"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "始める準備はできましたか？"
  description: "無料で GroupDocs.Parser の機能を試すか、ライセンスをリクエストしてください。"

release:
  title: "バージョン {0} がリリースされました"
  notes: "新機能を確認する"
  downloads: "ダウンロード"

code:
  title: "文書内容を迅速に解析"
  more: "さらに例を見る"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Parser インスタンスにソースファイルを渡します。
    using (var parser = new Parser("source.pdf"))
    {
        // TextReader に文書テキストを渡します。
        using (var textReader = parser.GetText())
        {
            // 文書テキストを処理します。
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 概要"
  description: ".NET アプリケーションで文書解析を実行するためのAPI"
  features:
    # feature loop
    - title: "文書からデータを抽出"
      content: "GroupDocs.Parser for .NET APIを活用して、Office文書、Eメール、添付ファイル、アーカイブなど、広範囲のファイル形式からテキスト、メタデータ、画像を取得します。この強力なツールは、データ分析、検索エンジンのインデックス作成、コンテンツ管理システムなど、さまざまなアプリケーション内でこれらのファイルに含まれる貴重な情報に効率的にアクセスし処理するのに役立ちます。"

    # feature loop
    - title: "文書を解析"
      content: "ハイパーリンク、表、QRコード、バーコード、PDFフォームのデータなど、さまざまな要素を抽出します。また、カスタムテンプレートを使用して任意の情報を文書から解析します。"

    # feature loop
    - title: "結果のカスタマイズ"
      content: ".NET APIでは、生データ、構造化データ、HTML、またはMarkdownなど、さまざまな形式でデータを取得できます。さらに、文書のテキスト内に特定の単語やフレーズを見つけるための検索機能も提供しています。"

############################# Platforms ############################
platforms:
  enable: true
  title: "プラットフォームの独立性"
  description: "GroupDocs.Parser for .NET は次のオペレーティングシステム、フレームワーク、パッケージマネージャーをサポートしています。"
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
    GroupDocs.Parser for .NET は次の [ファイル形式](https://docs.groupdocs.com/parser/net/supported-document-formats/)に対応しています。
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office形式
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### 画像およびその他の形式
        * **ポータブル:** PDF 
        * **画像:** JPG, BMP, PNG, TIFF, GIF
        * **その他のオフィス形式:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### その他の形式
        * **ウェブ:** HTML, MHTML 
        * **アーカイブ:** ZIP, TAR, 7Z 
        * **e-Book:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for .NET の機能"
  description: "PDF、Office文書、および画像から迅速かつ正確にデータを抽出します。"

  items:
    # feature loop
    - icon: "text"
      title: "テキストの抽出"
      content: "オフィス文書、PDFファイル、画像など、さまざまなファイル形式からテキスト情報を抽出します。"

    # feature loop
    - icon: "image"
      title: "画像の抽出"
      content: "オフィス文書やPDFファイルから視覚コンテンツを抽出し、便宜上アクセス可能にします。"

    # feature loop
    - icon: "qr"
      title: "QRコードのスキャン"
      content: "オフィス文書やPDFファイル、または視覚コンテンツに存在するQRコードを検出してデコードします。"

    # feature loop
    - icon: "email"
      title: "メール添付ファイルやアーカイブからデータを抽出"
      content: "メールメッセージ、ファイル添付、圧縮データソースから貴重な情報を取得します。"

    # feature loop
    - icon: "table"
      title: "表の抽出"
      content: "PDF文書内の表形式のデータを識別して抽出し、整理された分析と利用を行います。"

    # feature loop
    - icon: "hyperlink"
      title: "ハイパーリンクの抽出"
      content: "オフィス文書やPDFファイル内のハイパーリンクやメールアドレスを見つけて抽出します。"

    # feature loop
    - icon: "pdf"
      title: "PDFフォームを解析"
      content: "PDFフォームはユーザーが情報を電子的に入力できるようにするための入力可能なフィールドを含むデジタル文書です。 .NET APIを使用して、これらのフォームからデータを抽出し、効率的に処理します。"

    # feature loop
    - icon: "template"
      title: "テンプレートによるデータ解析"
      content: "カスタムテンプレートを作成し、.NET APIを利用してPDFファイルから特定の情報を解析します。"

    # feature loop
    - icon: "search"
      title: "文書内のテキストを検索"
      content: "文書内で特定の言葉やパターンを迅速に見つけます。"


############################# Code samples ############################
code_samples:
  enable: true
  title: "コードサンプル"
  description: "典型的な GroupDocs.Parser for .NET 操作のいくつかのユースケース"
  items:
    # code sample loop
    - title: "PDF文書から画像を抽出"
      content: |
        GroupDocs.Parser for .NET は C# 開発者が [文書](https://docs.groupdocs.com/parser/net/extract-images-from-documents/) から画像を抽出するのを簡単にします：
        {{< landing/code title="C# でPDF文書から画像を抽出">}}
        ```csharp {style=abap}
        // Parser クラスのインスタンスを作成します。
        using (var parser = new Parser("source.pptx"))
        {
            // 画像を抽出します。
            var images = parser.GetImages();

            // 何かが抽出されたか確認します。
            if (images == null)
            {
                return;
            }
            // 画像を反復処理します。
            foreach (PageImageArea image in images)
            {
                // ページインデックス、矩形、画像タイプを出力します。
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "画像からバーコードを抽出"
      content: |
        私たちの .NET APIを使用して、画像から [バーコード](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) を抽出します：
        {{< landing/code title="C# で画像からバーコードを抽出">}}
        ```csharp {style=abap}   
        // Parser にソース画像を読み込みます。
        using (var parser = new Parser("source.jpg"))
        {
            // ファイルがバーコード抽出をサポートしているか確認します。
            if (parser.Features.Barcodes)
            {
                // ファイルからバーコードを抽出します。
                var barcodes = parser.GetBarcodes();

                // バーコードを反復処理します。
                foreach (var barcode in barcodes)
                {
                    // ページインデックスを出力します。
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // バーコードの値を出力します。
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
