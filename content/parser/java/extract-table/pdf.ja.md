


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: ja
format: Pdf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java アプリケーションで PDF ドキュメントからテーブルを取得する"
head_description: "GroupDocs.Parser を使用して Java アプリケーション内の PDF ファイルから構造化された表形式データを抽出します—外部ツールは不要です。"

############################# Header ############################
title: "Java を使用して PDF からテーブルデータを取得する" 
description: "GroupDocs.Parser を使用して、PDF、DOCX、XLSXなどの形式からテーブルをシームレスに検出して抽出します。"
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
    title: "GroupDocs.Parser for Java API の紹介"
    link: "/parser/java/"
    link_title: "詳細はこちら"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) は、Java プラットフォーム向けの多機能なコンテンツ抽出 API です。PDF、Word 文書、Excel シート、PowerPoint プレゼンテーションなどからテーブル、テキスト、グラフィック、リンク、構造化データを正確に解析することが可能で、サードパーティプラグインは必要ありません。

############################# Steps ############################
steps:
    enable: true
    title: "Java で Pdf からテーブルを取得する方法"
    content: |
      [GroupDocs.Parser](/parser/java/) を使用して PDF ドキュメントからテーブルを解析するには、Java 環境で以下の手順に従ってください。
      
      1. Parser のインスタンスを作成し、対象の PDF ファイルを読み込む。
      2. ファイルが構造化されたテーブル抽出をサポートしていることを確認する。
      3. API を使用してドキュメントからテーブル要素を取得する。
      4. 抽出されたデータを分析、レポート、または自動化システムで活用する。
   
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
        // Parser を使用してテーブル要素を含む入力ドキュメントを読み込む
        try (Parser parser = new Parser("input.pdf"))
        {
            // ドキュメントタイプがテーブル認識を許可していることを確認する
            if (!parser.getFeatures().isTables()) {
                System.out.println("テーブルをサポートしていないファイルに対するロジックを追加する");
                return;
            }

            // テーブル構造を解釈するルールを定義する
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // テーブルを抽出するためのパラメータを設定する
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  読み込んだドキュメントでテーブル抽出を実行する
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  結果から抽出された各テーブルを処理する
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "高度なコンテンツ抽出ツール"
  description: "テーブルの読み取りにとどまらず、GroupDocs.Parser はプレーンテキスト、視覚要素、埋め込まれたメタデータ、および構造化オブジェクトのキャプチャをサポートし、ドキュメント処理タスクを強化します。"
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "構造化されたコンテンツと表形式データの抽出"
  features:
    # feature loop
    - title: "形式を超えた正確なテーブル解析"
      content: "PDF、Word、Excel、HTMLなどの標準ドキュメントタイプからのテーブル抽出を高い精度でサポートします。"

    # feature loop
    - title: "多様なソースからの表形式構造の読み取り"
      content: "スプレッドシート、文書、レポートからテーブルデータを取得し、構造と配置を保持します。"

    # feature loop
    - title: "カスタマイズ可能なテーブル抽出設定"
      content: "レイアウト検出を制御し、ヘッダーとフッターを管理し、柔軟な設定オプションで抽出を微調整します。"
      
  code_samples:
    # code sample loop
    - title: "サンプル: Excel ドキュメントからテーブルを抽出"
      content: |
        この例では、GroupDocs.Parser を使用して Excel (XLSX) ファイルのテーブルコンテンツを抽出しループする方法を示します。
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Parser を Excel ファイルで初期化する
        try (Parser parser = new Parser("input.pdf"))
        {
            // このドキュメントのテーブル抽出がサポートされていない場合は終了する
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // テーブルレイアウトを見つけるためのルールを適用する
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // テーブル抽出の設定を構成する
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // 抽出プロセスを呼び出す
            Iterable<PageTableArea> tables = parser.getTables(options);

            // 解析された全てのテーブル構造をループする
            for (PageTableArea t : tables)
            {
                // テーブルの各行を反復処理する
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // 現在の行内の各セルを処理する
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // 現在のセルの内容にアクセスして読み取る
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // 各テーブルセルのテキスト値を出力する
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                }
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
    title: "テーブル抽出に対応するドキュメントタイプ"
    exclude: "PDF"
    description: "GroupDocs.Parser は、複数のファイルタイプで信頼できるテーブル検出を提供します。以下は、テーブル抽出に最も広くサポートされているドキュメント形式のリストです。"
    items: 
        # format loop 1
        - name: "PDFを解析する"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(ポータブル文書形式)"
          
        # format loop 2
        - name: "DOCXを解析する"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(Office 2007+ Word文書)"
          
        # format loop 3
        - name: "PPTXを解析する"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(Open XMLプレゼンテーション形式)"
          
        # format loop 4
        - name: "XLSXを解析する"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(Open XMLワークブック)"
          
        # format loop 5
        - name: "TXTを解析する"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(テキストファイル)"
          
        # format loop 6
        - name: "RTFを解析する"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(リッチテキスト形式)"
          
        # format loop 7
        - name: "XMLを解析する"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(拡張可能なマークアップ言語)"
          
        # format loop 8
        - name: "EPUBを解析する"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(オープンeBookファイル)"
         
          

---