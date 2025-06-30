


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:47
draft: false
lang: ja
format: Epub
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "EPUB ファイルから C# アプリでテキストを抽出する"
head_description: "GroupDocs.Parser を使用して、C# アプリケーション内の EPUB ファイルからプレーンまたは構造化テキストを抽出します。このために外部ツールは必要ありません。"

############################# Header ############################
title: "C# を使用して EPUB からテキストを抽出する" 
description: "GroupDocs.Parser を使って、PDF、Word、Excel、およびその他のファイルタイプから読みやすく構造化されたテキストを迅速に抽出します。.NET ソリューション内での利用が可能です。"
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "無料トライアルをダウンロード"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for .NET API について"
    link: "/parser/net/"
    link_title: "詳細はこちら"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) は、.NET 開発者向けの高性能なドキュメント解析 API です。PDF、DOCX、XLSX、PPTX など、多数のファイル形式からテキスト、画像、テーブル、および構造化コンテンツを抽出することを容易にし、サードパーティライブラリに依存することなく利用できます。

############################# Steps ############################
steps:
    enable: true
    title: "C# で Epub からテキストを抽出する手順"
    content: |
      [GroupDocs.Parser](/parser/net/) を使用して .NET アプリ内の EPUB ドキュメントからクリーンで構造化されたテキストを抽出するための手順は次のとおりです:
      
      1. Parser インスタンスを使用して EPUB ドキュメントを開きます。
      2. ファイルコンテンツからテキストを抽出します。
      3. 結果を確認してテキスト抽出が成功したことを確認します。
      4. 抽出されたテキストをビジネスロジック、インデクシング、またはデータパイプラインで利用します。
   
    code:
      platform: "net"
      copy_title: "コピー"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "クリックしてコピー"
        copy_done: "コピーしました"
      links:
        #  loop
        - title: "さらなる例"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "ドキュメンテーション"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Parser にドキュメントを読み込む
        using (Parser parser = new Parser("input.epub")) {

            // ファイルからすべてのテキストコンテンツを抽出する
            using (TextReader reader = parser.GetText()) 
            {
                // テキストが取得できない場合、結果は null になります
                // 抽出されたテキストをアプリケーションで使用する
                Console.WriteLine(reader == null ? 
                    "この形式ではテキスト抽出はサポートされていません" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "包括的なコンテンツ抽出機能"
  description: "プレーンテキストに加えて、GroupDocs.Parser は、内容分析、変換、自動化をサポートするために、画像、構造化要素、およびメタデータを抽出することができます。"
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "テキスト認識と構造化ドキュメント解析"
  features:
    # feature loop
    - title: "さまざまなファイルタイプからのテキスト抽出"
      content: "PDF、DOCX、XLSX、PPTX、HTML などの形式からプレーンまたは構造化テキストを取得できます。"

    # feature loop
    - title: "ドキュメントとビジュアルからのテキスト処理"
      content: "スキャンした画像、プレゼンテーション、スプレッドシート、デジタルドキュメントからテキストを抽出し、構造を保持します。"

    # feature loop
    - title: "高度なテキスト抽出設定"
      content: "テキストの検出方法をカスタマイズします—ページ範囲、レイアウト領域を定義し、最大精度に向けて出力を調整します。"
      
  code_samples:
    # code sample loop
    - title: "PPTX ファイルからテキストエリアを抽出する方法"
      content: |
        このコードサンプルでは、GroupDocs.Parser を使用して PowerPoint ファイルからテキストコンテンツとエリア座標を取得する方法を示します。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Parser で PowerPoint プレゼンテーションを読み込みます。
        using (Parser parser = new Parser("input.pptx"))
        {
            // ドキュメントからすべてのテキストエリアの矩形を抽出します。
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // テキストエリア抽出ができない場合は終了します。
            if (areas == null)
            {
                return;
            }

            // 各ページのテキストエリアをループ処理します。
            foreach (PageTextArea a in areas)
            {
                // ページインデックス、エリア矩形、およびテキスト値にアクセスします。
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Text: {2}", a.Page.Index, a.Rectangle, a.Text));
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "始める準備はできましたか？"
  description: "GroupDocs.Parserの機能を無料で試すか、ライセンスをリクエストしてください"
  items:
    #  loop
    - title: "Nugetのダウンロード"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "ライセンス情報"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "テキスト抽出に対応している形式"
    exclude: "EPUB"
    description: "GroupDocs.Parser は幅広いドキュメントおよび画像タイプからのテキスト抽出を可能にします。以下に一般的にサポートされている形式を示します。"
    items: 
        # format loop 1
        - name: "PDFを解析する"
          format: "PDF"
          link: "/parser/net/extract-text/pdf/"
          description: "(ポータブル文書形式)"
          
        # format loop 2
        - name: "DOCXを解析する"
          format: "DOCX"
          link: "/parser/net/extract-text/docx/"
          description: "(Office 2007+ Word文書)"
          
        # format loop 3
        - name: "PPTXを解析する"
          format: "PPTX"
          link: "/parser/net/extract-text/pptx/"
          description: "(Open XMLプレゼンテーション形式)"
          
        # format loop 4
        - name: "XLSXを解析する"
          format: "XLSX"
          link: "/parser/net/extract-text/xlsx/"
          description: "(Open XMLワークブック)"
          
        # format loop 5
        - name: "TXTを解析する"
          format: "TXT"
          link: "/parser/net/extract-text/txt/"
          description: "(テキストファイル)"
          
        # format loop 6
        - name: "RTFを解析する"
          format: "RTF"
          link: "/parser/net/extract-text/rtf/"
          description: "(リッチテキスト形式)"
          
        # format loop 7
        - name: "XMLを解析する"
          format: "XML"
          link: "/parser/net/extract-text/xml/"
          description: "(拡張可能なマークアップ言語)"
          
        # format loop 8
        - name: "EPUBを解析する"
          format: "EPUB"
          link: "/parser/net/extract-text/epub/"
          description: "(オープンeBookファイル)"
         
          

---