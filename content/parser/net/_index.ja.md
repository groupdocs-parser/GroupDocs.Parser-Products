---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for .NET Document Parser SDK .NET 向け"
head_description: ".NET 用の高性能 Document Parser SDK。PDF、Word、Excel、メール、50 以上のドキュメント形式からテキスト、画像、メタデータ、バーコード、テーブル、その他のデータを抽出します。"

############################# Header ############################
title: "Document Parser SDK .NET 用"
description: ".NET アプリに高速かつ正確なドキュメント解析を追加し、ドキュメントや画像からテキスト、画像、メタデータ、構造化データを抽出します。"
words:
  for: "対象"

actions:
  main: "Nuget ダウンロード"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "ライセンス"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "開始する準備はできましたか？"
  description: "GroupDocs.Parserの機能を無料でお試し、またはライセンスをリクエストしてください"

release:
  title: "バージョン {0} がリリースされました"
  notes: "新機能を見る"
  downloads: "ダウンロード"

code:
  title: "SDK を使用してドキュメントコンテンツを迅速に解析する"
  more: "その他のサンプル"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // ソースファイルを Parser インスタンスに渡す
    using (var parser = new Parser("source.pdf"))
    {
        // ドキュメントテキストを TextReader に渡す
        using (var textReader = parser.GetText())
        {
            // ドキュメントテキストを処理する
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser の概要"
  description: ".NET アプリケーションで高精度のドキュメント解析を実行するための Document Parser SDK"
  features:
    # feature loop
    - title: "ドキュメントからデータを抽出する"
      content: "GroupDocs.Parser for .NET API を使用すると、Office ドキュメント、メール、添付ファイル、アーカイブなど、さまざまなファイル形式からテキスト、メタデータ、画像を取得できます。この強力なツールにより、データ分析、検索エンジンのインデックス作成、コンテンツ管理システムなどの様々なアプリケーションで、これらのファイルに含まれる貴重な情報へ効率的にアクセスし、処理できます。"

    # feature loop
    - title: "ドキュメントを解析する"
      content: "PDF フォームからハイパーリンク、テーブル、QR コード、バーコード、データなどのさまざまな要素を抽出します。また、カスタムテンプレートを使用してドキュメントから任意の情報を解析できます。"

    # feature loop
    - title: "結果のカスタマイズ"
      content: ".NET API を使用すると、RAW、構造化、HTML、Markdown などのさまざまな形式でデータを取得できます。また、API はドキュメントテキスト内の特定の単語やフレーズを検索する機能も提供します。"

############################# Platforms ############################
platforms:
  enable: true
  title: "プラットフォームに依存しない"
  description: "GroupDocs.Parser for .NET は以下のオペレーティングシステム、フレームワーク、パッケージマネージャーをサポートします"
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
    GroupDocs.Parser for .NET は以下の [ファイル形式](https://docs.groupdocs.com/parser/net/supported-document-formats/) の操作をサポートします。
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
  title: "GroupDocs.Parser for .NET の機能"
  description: "弊社の .NET Document Parser SDK を使用して、PDF、Office ドキュメント、画像、その他の形式からデータを迅速かつ正確に抽出します。"

  items:
    # feature loop
    - icon: "text"
      title: "テキストを抽出する"
      content: "Office ドキュメント、PDF ファイル、画像などのさまざまなファイル形式からテキスト情報を抽出し、読みやすさと分析のしやすさを高めます。"

    # feature loop
    - icon: "image"
      title: "画像を抽出する"
      content: "Office ドキュメントや PDF ファイルなど、さまざまなソースから視覚コンテンツを取得し、便利にアクセス・活用できます。"

    # feature loop
    - icon: "qr"
      title: "QR コードをスキャンする"
      content: "Office ドキュメント、PDF ファイル、またはビジュアルコンテンツ内にある QR コードを検出・デコードし、効率的に情報を取得します。"

    # feature loop
    - icon: "email"
      title: "メール添付ファイルおよびアーカイブからデータを抽出する"
      content: "メールメッセージ、ファイル添付、および圧縮データソースから貴重な情報を収集し、効果的な分析と活用を実現します。"

    # feature loop
    - icon: "table"
      title: "テーブルを抽出"
      content: "PDFドキュメントから表形式データを識別・抽出し、整理された分析と利用を可能にします。"

    # feature loop
    - icon: "hyperlink"
      title: "ハイパーリンクを抽出"
      content: "オフィス文書やPDFファイル内のハイパーリンクとメールアドレスを検索し抽出して、効率的にアクセスできるようにします。"

    # feature loop
    - icon: "pdf"
      title: "PDFフォームを解析"
      content: "PDFフォームは、ユーザーが入力できるフィールドを備えたデジタル文書で、情報を電子的に入力できます。.NET APIを使用してこれらのフォームからデータを抽出し、効率的に処理できます。"

    # feature loop
    - icon: "template"
      title: "テンプレートでデータを解析"
      content: "カスタムテンプレートを作成し、.NET APIと組み合わせてPDFファイルから特定の情報を解析することで、データ抽出プロセスを簡素化します。"

    # feature loop
    - icon: "search"
      title: "ドキュメント内のテキストを検索"
      content: "ドキュメント内の特定の単語やパターンを迅速に検索します。"


############################# Code samples ############################
code_samples:
  enable: true
  title: "コードサンプル"
  description: "典型的な GroupDocs.Parser for .NET の操作例の一部"
  items:
    # code sample loop
    - title: "PDFドキュメントから画像を抽出"
      content: |
        GroupDocs.Parser for .NET は C# 開発者が [ドキュメント](https://docs.groupdocs.com/parser/net/extract-images-from-documents/) から画像を簡単に抽出できるようにします：
        {{< landing/code title="C# で PDF ドキュメントから画像を抽出する">}}
        ```csharp {style=abap}
        // Parser クラスのインスタンスを作成する
        using (var parser = new Parser("source.pptx"))
        {
            // 画像を抽出する
            var images = parser.GetImages();

            // 何かが抽出されたか確認する
            if (images == null)
            {
                return;
            }
            // 画像を反復処理する
            foreach (PageImageArea image in images)
            {
                // ページインデックス、矩形、画像タイプを出力する
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "画像からバーコードを抽出"
      content: |
        当社の .NET API を使用して画像から [バーコード](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) を抽出します：
        {{< landing/code title="C# で画像からバーコードを抽出する">}}
        ```csharp {style=abap}   
        // ソース画像を Parser にロードする
        using (var parser = new Parser("source.jpg"))
        {
            // ファイルがバーコード抽出に対応しているか確認する
            if (parser.Features.Barcodes)
            {
                // ファイルからバーコードを抽出する
                var barcodes = parser.GetBarcodes();

                // バーコードを反復処理する
                foreach (var barcode in barcodes)
                {
                    // ページインデックスを出力する
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // バーコードの値を出力する
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
