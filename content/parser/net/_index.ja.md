---
############################# Static ############################
layout: "landing"
date: 2024-02-13T17:01:03
draft: false
#operation: 
#parsertype: 
#fileformat: 
#productName: Java
lang: ja
#productCode: java
#otherformats: 
#breadcrumb: Put  parser on  for Java
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: ".NET、Java、クラウド API およびオンライン ドキュメント パーサー アプリ"
head_description: ".NET、Java、およびクラウドベースのアプリケーション向けのオールインワンの文書解析ソリューションを入手します。シンプルなドラッグ アンド ドロップ機能を使用してオンラインでドキュメント形式からデータを抽出します"

############################# Header ############################
title: "文書を解析する<br>.NET API 経由"
description: "プログラマーとエンドユーザー向けの柔軟な API とアプリベースのソリューションを使用して、あらゆるプラットフォーム上のドキュメントや画像からデータを抽出します。"
words:
  for: "のために"

actions:
  main: "無料の NuGet ダウンロード"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "ライセンス"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net"
  title: "始める準備はできていますか?"
  description: "GroupDocs.Parser の機能を無料で試すか、ライセンスをリクエストしてください"

release:
  title: "バージョン {0} がリリースされました"
  notes: "新機能を見る"
  downloads: "ダウンロード"

code:
  title: "C# で PDF ファイルからテキストを抽出する"
  more: "他の例"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Create an instance of Parser class
    using (var parser = new Parser(fileName))
    {
        // Extract a text into the reader
        using (var textReader = parser.GetText())
        {
            // Print a text from the document
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 概要"
  description: ".NET アプリケーションでドキュメント解析を実行するための API"
  features:
    # feature loop
    - title: "ドキュメントからデータを抽出する"
      content: ".NET API を使用すると、Office ドキュメント、電子メール、添付ファイル、アーカイブなどの幅広いファイル形式からテキスト、メタデータ、画像を取得できます。この強力なツールは、データ分析、検索エンジンのインデックス作成、コンテンツ管理システムなどのさまざまなアプリケーションで、これらのファイルに含まれる貴重な情報に効率的にアクセスして処理するのに役立ちます。"

    # feature loop
    - title: "文書を解析する"
      content: "PDF フォームからハイパーリンク、表、QR コード、バーコード、データなどのさまざまな要素を抽出します。また、カスタム テンプレートを使用してドキュメントから必要な情報を解析します。"

    # feature loop
    - title: "結果のカスタマイズ"
      content: ".NET API を使用すると、生、構造化、HTML、マークダウンなどのさまざまな形式でデータを取得できます。さらに、API は、ドキュメントのテキスト内の特定の単語や語句を見つけるための検索機能を提供します。"

############################# Platforms ############################
platforms:
  enable: true
  title: "プラットフォームの独立性"
  description: "GroupDocs.Parser for .NET 次のオペレーティング システム、フレームワーク、パッケージ マネージャーをサポートしています"
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
    GroupDocs.Parser for .NET は、次の [ファイル形式](https://docs.groupdocs.com/parser/net/supported-document-formats/) での操作をサポートしています。
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office 形式
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### 画像とその他の形式
        * **Portable:** PDF
        * **画像:** JPG, BMP, PNG, TIFF, GIF
        * **その他のオフィス形式:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### その他の形式
        * **ウェブ:** HTML, MHTML
        * **アーカイブ:** ZIP, TAR, 7Z
        * **電子書籍:** CHM, EPUB, FB2, MOBI

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser の機能"
  description: "PDF、Office ドキュメント、画像からデータを迅速かつ正確に抽出します。"

  items:
    # feature loop
    - icon: "text"
      title: "テキストを抽出する"
      content: "オフィス文書、PDF ファイル、画像などのさまざまなファイル形式からテキスト情報を抽出し、読みやすく分析しやすくします。"

    # feature loop
    - icon: "image"
      title: "画像の抽出"
      content: "オフィス文書や PDF ファイルなどのさまざまなソースからビジュアル コンテンツを取得して、アクセスして使用するのが便利です。"

    # feature loop
    - icon: "qr"
      title: "QRコードをスキャンする"
      content: "オフィス文書、PDF ファイル、またはビジュアル コンテンツ内に存在する QR コードを検出してデコードし、効率的な情報検索を実現します。"

    # feature loop
    - icon: "email"
      title: "電子メールの添付ファイルとアーカイブからデータを抽出する"
      content: "電子メール メッセージ、添付ファイル、圧縮データ ソースから貴重な情報を収集し、効果的に分析して利用します。"

    # feature loop
    - icon: "table"
      title: "テーブルの抽出"
      content: "組織的な分析と使用のために、PDF ドキュメントから表形式のデータを特定して抽出します。"

    # feature loop
    - icon: "hyperlink"
      title: "ハイパーリンクの抽出"
      content: "オフィス文書または PDF ファイル内のハイパーリンクと電子メール アドレスを見つけて抽出し、効率的にアクセスできるようにします。"

    # feature loop
    - icon: "pdf"
      title: "PDF フォームを解析する"
      content: "PDF フォームは、ユーザーが情報を電子的に入力できるようにするための入力可能なフィールドを備えたデジタル ドキュメントです。 .NET API を利用してこれらのフォームからデータを抽出し、効率的に処理できます。"

    # feature loop
    - icon: "template"
      title: "テンプレートによるデータの解析"
      content: "カスタム テンプレートを作成し、それを .NET API で利用して、PDF ファイルからの特定の情報を解析し、データ抽出プロセスを簡素化します。"

    # feature loop
    - icon: "search"
      title: "ドキュメント内のテキストを検索する"
      content: "文書内の特定の単語やパターンをすばやく見つけます。"

############################# Code samples ############################
code_samples:
  enable: true
  title: "コードサンプル"
  description: "典型的なオペレーションのいくつかのユースケース"
  items:
    # code sample loop
    - title: "PDF ドキュメントから画像を抽出する"
      content: |
        .NET API を使用すると、C# 開発者はいくつかの簡単な手順を実装することで、ドキュメントから画像を簡単に抽出できます。
        {{< landing/code title="C# で PDF ドキュメントから画像を抽出する">}}
        ```csharp {style=abap}
        // Create an instance of Parser class
        using (var parser = new Parser(fileName))
        {
            // Extract images
            var images = parser.GetImages();

            // Check if images extraction is supported
            if (images != null)
            {
                var imageIndex = 0;

                // Iterate over images
                foreach (var image in images)
                {
                    // Save the image to the file
                    image.Save($"{++imageIndex}{image.FileType.Extension}");
                }
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "画像からバーコードを抽出する"
      content: |
        .NET API を使用すると、C# 開発者はいくつかの簡単な手順を実装することで、ドキュメントからバーコードを簡単に抽出できます。
        {{< landing/code title="画像からバーコードを抽出する">}}
        ```csharp {style=abap}   
        // Create an instance of Parser class
        using (var parser = new Parser(fileName))
        {
            // Check if the file supports barcode extracting
            if (parser.Features.Barcodes)
            {
                // Extract barcodes from the file.
                var barcodes = parser.GetBarcodes();

                // Iterate over barcodes
                foreach (var barcode in barcodes)
                {
                    // Print the page index
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Print the barcode value
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
