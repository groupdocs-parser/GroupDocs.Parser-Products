---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: ja
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

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
head_title: "GroupDocs.Parser for Java ドキュメントパーサ SDK for Java"
head_description: "高速パフォーマンスを誇る Java 用ドキュメントパーサ SDK。PDF、Word、Excel、メール、および 50 以上のドキュメント形式からテキスト、画像、メタデータ、バーコード、テーブルなどのデータを抽出します。"

############################# Header ############################
title: "ドキュメントパーサ SDK for Java"
description: "Java アプリに高速で高精度な文書解析を追加し、文書や画像からテキスト、画像、メタデータ、構造化データを抽出します。"
words:
  for: "対象"

actions:
  main: "Maven ダウンロード"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "ライセンス"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "開始する準備はできましたか？"
  description: "GroupDocs.Parserの機能を無料でお試し、またはライセンスをリクエストしてください"

release:
  title: "バージョン {0} がリリースされました"
  notes: "新機能を見る"
  downloads: "ダウンロード"

code:
  title: "SDK を使用して文書コンテンツを迅速に解析"
  more: "その他のサンプル"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // ソースファイルを Parser インスタンスに渡す
    try (Parser parser = new Parser("source.pdf"))
    {
        // 文書テキストを TextReader に渡す
        try (TextReader reader = parser.getText())
        {
            // 文書テキストを処理する
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser の概要"
  description: "Java アプリケーションで高精度な文書解析を実行するための Document Parser SDK"
  features:
    # feature loop
    - title: "文書からデータを抽出"
      content: "GroupDocs.Parser for Java API を使用すると、Office 文書、メール、添付ファイル、アーカイブなど、幅広いファイル形式からテキスト、メタデータ、画像を取得できます。この強力なツールは、データ分析、検索エンジンのインデックス作成、コンテンツ管理システムなど、さまざまなアプリケーション向けに、これらのファイルに含まれる貴重な情報へ効率的にアクセスし、処理するのに役立ちます。"

    # feature loop
    - title: "ドキュメントを解析する"
      content: "PDF フォームからハイパーリンク、表、QR コード、バーコード、データなどのさまざまな要素を抽出します。また、カスタムテンプレートを使用してドキュメントから任意の情報を解析します。"

    # feature loop
    - title: "結果のカスタマイズ"
      content: "Java API を使用すると、生データ、構造化データ、HTML、Markdown などのさまざまな形式でデータを取得できます。また、API はドキュメントテキスト内の特定の単語やフレーズを検索する機能も提供します。"

############################# Platforms ############################
platforms:
  enable: true
  title: "プラットフォームに依存しない"
  description: "GroupDocs.Parser for Java は以下のオペレーティングシステム、フレームワーク、パッケージマネージャーをサポートします。"
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
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "サポートされているファイル形式"
  description: |
    GroupDocs.Parser for Java は以下の [ファイル形式](https://docs.groupdocs.com/parser/java/supported-document-formats/) の操作をサポートします。
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
  title: "GroupDocs.Parser for Java の機能"
  description: "Java Document Parser SDK を使用して、PDF、Office ドキュメント、画像、その他の形式からデータを迅速かつ正確に抽出します。"

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
  description: "典型的な GroupDocs.Parser for Java の操作例"
  items:
    # code sample loop
    - title: "PDF ドキュメントから画像を抽出"
      content: |
        GroupDocs.Parser for Java は、Java 開発者が [ドキュメント](https://docs.groupdocs.com/parser/java/extract-images-from-documents/) から画像を抽出しやすくします。
        {{< landing/code title="Java で PDF ドキュメントから画像を抽出する">}}
        ```java {style=abap}
        // Parser クラスのインスタンスを作成する
        try (Parser parser = new Parser("source.pdf"))
        {
            // 画像を抽出する
            Iterable<PageImageArea> images = parser.getImages();

            // 何かが抽出されたか確認する
            if (images == null) {
                return;
            }

            // 画像を反復処理する
            for (PageImageArea image : images) {
                // ページインデックス、矩形、画像タイプを出力する
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "画像からバーコードを抽出"
      content: |
        当社のJava API を使用して画像から[バーコード](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/)を抽出します:
        {{< landing/code title="Java で画像からバーコードを抽出する">}}
        ```java {style=abap}   
        // ソース画像を Parser にロードする
        try (Parser parser = new Parser("source.jpg")){

            // ファイルがバーコード抽出に対応しているか確認する
            if (!parser.getFeatures().isBarcodes()) {

                // ファイルからバーコードを抽出する
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // バーコードを反復処理する
                for (PageBarcodeArea barcode : barcodes) {
                    // ページインデックスを出力する
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // バーコードの値を出力する
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
