


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: ja
format: Txt
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "JavaアプリでTXTファイルからハイパーリンクを抽出"
head_description: "GroupDocs.Parserを使って、Javaプロジェクト内のTXTドキュメントからURLリンクを見つけて抽出します—追加のソフトウェアは不要です。"

############################# Header ############################
title: "Javaを使ったTXTからのハイパーリンク抽出" 
description: "GroupDocs.Parserを使用して、PDF、Wordファイル、Excelシート、及び他のドキュメントからウェブリンクやハイパーリンクを抽出します。環境はJavaです。"
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "無料トライアルをダウンロード"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for Java APIについて"
    link: "/parser/java/"
    link_title: "詳細はこちら"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/)は、Java開発者向けに設計された強力なコンテンツ抽出APIです。DOCX、XLSX、PDF、HTMLなどの一般的なフォーマットからハイパーリンク、構造化データ、画像、テキストを抽出するツールを提供します—外部プラグインは必要ありません。

############################# Steps ############################
steps:
    enable: true
    title: "JavaでTxtからハイパーリンクを抽出する方法"
    content: |
      [GroupDocs.Parser](/parser/java/)は、Javaアプリケーション内のTXTファイルからのハイパーリンク抽出を以下の基本ステップで簡素化します：
      
      1. Parserのインスタンスを使用して、TXTファイルを開きます。
      2. ファイルフォーマットに対してハイパーリンク抽出が可能であることを確認します。
      3. 適切なメソッドを使用してすべてのハイパーリンクを抽出します。
      4. 結果をループ処理し、各リンクを必要に応じて処理します。
   
    code:
      platform: "net"
      copy_title: "コピー"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "クリックしてコピー"
        copy_done: "コピーしました"
      links:
        #  loop
        - title: "さらなる例"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "ドキュメンテーション"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Parserを使用して、ハイパーリンクを含む可能性のあるファイルをロードします
        try (Parser parser = new Parser("input.txt")) {

            // ドキュメントフォーマットがハイパーリンク解析をサポートしているか確認します
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("そのファイルではハイパーリンクの抽出は利用できません");
                return;
            }

            // ドキュメントからハイパーリンクデータを抽出し、使用します
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "包括的なドキュメント解析ツール"
  description: "ハイパーリンクを抽出するだけでなく、GroupDocs.Parserを使用することで、プレーンテキスト、埋め込まれたメディア、及び自動化されたワークフローで使用するための構造化データなど、他の有用なコンテンツを収集できます。"
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "ハイパーリンク抽出とドキュメント分析"
  features:
    # feature loop
    - title: "正確なリンク検出"
      content: "クリック可能なテキストや隠れたURLを含む、さまざまなドキュメントレイアウトからすべてのタイプのハイパーリンクをキャッチします。"

    # feature loop
    - title: "ドキュメントとウェブコンテンツに対応"
      content: "埋め込まれたハイパーリンクを含むPDF、DOCX、XLSX、HTML、及び画像ファイルからリンクを抽出します。"

    # feature loop
    - title: "カスタム抽出動作"
      content: "ページ範囲、リンクタイプ、またはコンテンツフィルターのようなオプションを使用して、ハイパーリンクの抽出方法を調整します。"
      
  code_samples:
    # code sample loop
    - title: "例：カスタムオプションを使ったPDFからのハイパーリンク抽出"
      content: |
        このサンプルは、リンク抽出設定を使用して、PDFファイルからすべてのリンクを抽出する方法を示しています。
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Parserクラスを使用してPDFを開きます
        try (Parser parser = new Parser("input.docx"))
        {
            // このドキュメントのハイパーリンクサポートが有効になっていることを確認します
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // リンクをフィルタリングするためのオプションを適用します
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // パーサーを使用してハイパーリンクデータを取得します
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // リンクを反復処理し、適切に処理します
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    - title: "Mavenのダウンロード"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "ライセンス情報"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "ハイパーリンク抽出をサポートするドキュメントフォーマット"
    exclude: "TXT"
    description: "GroupDocs.Parserを使用すると、多くの一般的なファイルフォーマットからハイパーリンクを抽出できます。以下は通常サポートされるフォーマットのリストです。"
    items: 
        # format loop 1
        - name: "PDFを解析する"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(ポータブル文書形式)"
          
        # format loop 2
        - name: "DOCXを解析する"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Office 2007+ Word文書)"
          
        # format loop 3
        - name: "PPTXを解析する"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Open XMLプレゼンテーション形式)"
          
        # format loop 4
        - name: "XLSXを解析する"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Open XMLワークブック)"
          
        # format loop 5
        - name: "TXTを解析する"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(テキストファイル)"
          
        # format loop 6
        - name: "RTFを解析する"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(リッチテキスト形式)"
          
        # format loop 7
        - name: "XMLを解析する"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(拡張可能なマークアップ言語)"
          
        # format loop 8
        - name: "EPUBを解析する"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(オープンeBookファイル)"
         
          

---