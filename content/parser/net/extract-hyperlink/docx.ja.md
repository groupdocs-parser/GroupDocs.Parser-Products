


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: ja
format: Docx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "C#アプリでDOCXファイルからハイパーリンクを抽出"
head_description: "GroupDocs.Parserを使用して、C#におけるDOCXファイルからハイパーリンクを検出および抽出します。他のツールやソフトウェアは不要です。"

############################# Header ############################
title: "C#を使用したDOCXからのハイパーリンク抽出" 
description: "GroupDocs.Parserを使用して、PDF、Word、ExcelなどのドキュメントタイプからURLおよびハイパーリンクを検出し、抽出します。これを.NETアプリケーションで行います。"
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
    title: "GroupDocs.Parser for .NET APIについて"
    link: "/parser/net/"
    link_title: "詳細はこちら"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/)は、.NET開発者向けの多用途の文書解析APIです。PDF、Word、Excel、HTMLなどのさまざまなファイル形式からハイパーリンク、テキスト、画像、構造化されたコンテンツを抽出することができ、外部ソフトウェアには依存しません。

############################# Steps ############################
steps:
    enable: true
    title: "C#におけるDocxからハイパーリンクを抽出する手順"
    content: |
      [GroupDocs.Parser](/parser/net/)は、.NET開発者がDOCXファイルからハイパーリンクを抽出するための簡単な手順を提供します：
      
      1. Parserインスタンスを使用してDOCXファイルを読み込む。
      2. ドキュメントがハイパーリンク抽出をサポートしているか確認する。
      3. ドキュメントからハイパーリンクのリストを取得する。
      4. 結果をループ処理し、抽出したURLを扱う。
   
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
        // Parserクラスを使用してハイパーリンクを含むドキュメントを読み込む
        using (Parser parser = new Parser("input.docx")) {

            // ファイルがハイパーリンク抽出をサポートしているか確認する
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("ファイルに対してハイパーリンク抽出は利用できません");
                return;
            }

            // 抽出したハイパーリンクを取得し、処理する
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "高度な文書解析機能"
  description: "ハイパーリンク抽出に加えて、GroupDocs.Parserはテキスト、メタデータ、画像、構造化データを抽出でき、強力なデータ処理ワークフローをサポートします。"
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "ハイパーリンク検出と文書解析"
  features:
    # feature loop
    - title: "ドキュメントからのハイパーリンク検出"
      content: "PDF、Wordファイル、スプレッドシートなどのドキュメントから、URLとリンクアノテーションを迅速に抽出します。"

    # feature loop
    - title: "ウェブリンクと埋め込みリンクのサポート"
      content: "複数のフォーマットで、標準のウェブURLと埋め込みドキュメントリンクの両方を検出して抽出します。"

    # feature loop
    - title: "柔軟な解析オプション"
      content: "特定のセクションやページをスキャンするための抽出設定をカスタマイズし、パフォーマンスと精度を向上させます。"
      
  code_samples:
    # code sample loop
    - title: "リンクオプションを使用したPDFからのハイパーリンク抽出方法"
      content: |
        このコードサンプルは、カスタムオプションを使用してPDFファイルからすべてのハイパーリンクを抽出する方法を示します。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  PDFドキュメントでParserを初期化する
        using (Parser parser = new Parser("input.docx"))
        {
            // ハイパーリンク抽出がサポートされているか確認する
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // 結果を絞り込むためにリンク抽出オプションを設定する
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // ドキュメントからハイパーリンクデータを抽出する
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // 抽出したリンクのリストを処理する
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    title: "ハイパーリンク抽出に対応するフォーマット"
    exclude: "DOCX"
    description: "GroupDocs.Parserは、さまざまな文書タイプからハイパーリンクを抽出できます。以下に一般的にサポートされているフォーマットを示します。"
    items: 
        # format loop 1
        - name: "PDFを解析する"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(ポータブル文書形式)"
          
        # format loop 2
        - name: "DOCXを解析する"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Office 2007+ Word文書)"
          
        # format loop 3
        - name: "PPTXを解析する"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Open XMLプレゼンテーション形式)"
          
        # format loop 4
        - name: "XLSXを解析する"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Open XMLワークブック)"
          
        # format loop 5
        - name: "TXTを解析する"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(テキストファイル)"
          
        # format loop 6
        - name: "RTFを解析する"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(リッチテキスト形式)"
          
        # format loop 7
        - name: "XMLを解析する"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(拡張可能なマークアップ言語)"
          
        # format loop 8
        - name: "EPUBを解析する"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(オープンeBookファイル)"
         
          

---