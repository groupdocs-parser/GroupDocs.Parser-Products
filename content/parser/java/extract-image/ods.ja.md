


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: ja
format: Ods
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java アプリケーションで ODS ファイルから画像を抽出"
head_description: "GroupDocs.Parser を使用すると、Java で ODS ファイルから画像を抽出できます。サードパーティ製のツールは不要です。"

############################# Header ############################
title: "Java を使用して ODS から画像を抽出" 
description: "PDF、Word、Excel などのファイルから埋め込まれた画像を、Java 開発環境で GroupDocs.Parser を使用して取得できます。"
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
    title: "GroupDocs.Parser for Java とは？"
    link: "/parser/java/"
    link_title: "詳細はこちら"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) は、Java 開発者向けに特化した機能豊富なパース API です。DOCX、XLSX、PDF、PNG、JPG など、さまざまなファイル形式から画像、テキスト、リンク、構造化された要素を抽出でき、外部ライブラリやアプリケーションは不要です。

############################# Steps ############################
steps:
    enable: true
    title: "Java で Ods から画像を抽出する方法"
    content: |
      [GroupDocs.Parser](/parser/java/) を使用して Java アプリケーション内の ODS ドキュメントから画像を抽出するための手順は次のとおりです：
      
      1. Parser インスタンスを作成し、ODS ファイルをロードします。
      2. ロードしたドキュメントから画像データを抽出します。
      3. 必要に応じて抽出した画像を使用またはエクスポートします。
   
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
        // Parser を使用してパーサーを初期化し、画像を含むドキュメントをロードします
        try (Parser parser = new Parser("input.ods"))
        {
            // ドキュメントに埋め込まれているすべての画像要素を収集します
            Iterable<PageImageArea> images = parser.getImages();

            // ドキュメントに画像がない場合は処理をスキップします
            if (images == null) {
                return;
            }

            // 必要に応じて各画像を処理します
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "その他のドキュメントパース機能"
  description: "画像抽出に加えて、GroupDocs.Parser を使用すると、生のコンテンツ（テキスト、リンク、メタデータ、構造化データ）を抽出して処理および分析することができます。"
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "ドキュメントから画像とコンテンツを抽出"
  features:
    # feature loop
    - title: "さまざまなフォーマットに対応"
      content: "PDF、DOCX、PPTX、XLSX などの異なる文書タイプ、ならびに PNG、JPEG、GIF などの画像フォーマットから画像を抽出します。"

    # feature loop
    - title: "画像の明瞭さと解像度を維持"
      content: "すべての抽出された画像は元の解像度とファイルタイプを保持し、一貫した品質と使いやすさを確保します。"

    # feature loop
    - title: "柔軟な設定オプション"
      content: "画像の種類、サイズ、ページインデックス、またはファイル形式によって画像抽出プロセスをカスタマイズできます。"
      
  code_samples:
    # code sample loop
    - title: "PDF ファイルから画像を抽出して保存"
      content: |
        この例では、PDF ドキュメントから画像を抽出し、それらを個別にデバイスに保存する方法を示します。
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Parser を使用して PDF ファイルを開きます
        try (Parser parser = new Parser("input.pdf"))
        {
            // ドキュメントコンテンツから画像を取得します
            Iterable<PageImageArea> images = parser.getImages();

            // 出力パラメータを設定します（例：JPEG または PNG など）
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // 抽出された画像をローカルディレクトリに保存します
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
                imageNumber++;
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
    title: "画像抽出に対応したファイル形式"
    exclude: "ODS"
    description: "GroupDocs.Parser は、幅広いドキュメントと画像に対応した画像抽出をサポートします。一般的にサポートされるフォーマットを以下で探求してください。"
    items: 
        # format loop 1
        - name: "PDFを解析する"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(ポータブル文書形式)"
          
        # format loop 2
        - name: "DOCXを解析する"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Office 2007+ Word文書)"
          
        # format loop 3
        - name: "PPTXを解析する"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Open XMLプレゼンテーション形式)"
          
        # format loop 4
        - name: "XLSXを解析する"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Open XMLワークブック)"
          
        # format loop 5
        - name: "ODTを解析する"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(OpenDocumentテキスト文書)"
          
        # format loop 6
        - name: "ODSを解析する"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(OpenDocumentスプレッドシート)"
          
        # format loop 7
        - name: "ODPを解析する"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(OpenDocumentプレゼンテーション)"
          
        # format loop 8
        - name: "EPUBを解析する"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(オープンeBookファイル)"
          
        # format loop 9
        - name: "FB2を解析する"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(FictionBook eBook)"
         
          

---