


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:34
draft: false
lang: ja
format: Odt
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "C# アプリで ODT ファイルから画像を抽出"
head_description: "GroupDocs.Parser を使用して、C# で ODT ファイルから画像を検出し抽出します。追加のツールは不要です。"

############################# Header ############################
title: "C# を使用して ODT から画像を抽出" 
description: "GroupDocs.Parser を使用して、PDF、Word 文書、Excel シート、その他のファイルタイプから埋め込まれた画像を見つけて抽出します。"
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
       [GroupDocs.Parser](/parser/net/) は、.NET 開発者向けの堅牢なドキュメント解析ライブラリです。PDF、DOCX、XLSX、PPTX などの一般的なファイル形式から、画像、テキスト、ハイパーリンク、および構造化データを抽出することができます。すべての操作はサードパーティのアプリケーションを必要としません。

############################# Steps ############################
steps:
    enable: true
    title: "C# で Odt から画像を抽出する手順"
    content: |
      [GroupDocs.Parser](/parser/net/) を使用すると、あなたの .NET プロジェクトで ODT ドキュメントから画像をわずか数ステップで抽出できます：
      
      1. ODT ファイルを使用して Parser を初期化します。
      2. ドキュメントから画像要素を取得します。
      3. 抽出した画像を必要に応じてワークフローで使用します。
   
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
        // Parser を使用して画像を含むドキュメントを開く
        using (Parser parser = new Parser("input.odt")) {

            // ファイルからすべての埋め込まれた画像を抽出
            IEnumerable<PageImageArea> images = parser.GetImages();

            // 画像が見つからないケースを処理
            if (images == null)
            {
                return;
            }

            // 取得した画像を処理または保存
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "包括的なドキュメント内容の抽出"
  description: "GroupDocs.Parser は画像抽出だけでなく、生のテキスト、ハイパーリンク、メタデータ、構造化されたコンテンツを抽出することも可能で、高度な自動化シナリオに対応します。"
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "画像抽出とドキュメント解析のワークフロー"
  features:
    # feature loop
    - title: "複数形式からの画像抽出"
      content: "DOCX、PDF、PPTX、XLSX、PNG、JPG、TIFF など、さまざまなファイル形式から埋め込まれた画像を抽出します。"

    # feature loop
    - title: "元の画像品質を保持"
      content: "画像は高忠実度で抽出され、その元の解像度、形式、およびカラープロファイルを維持します。"

    # feature loop
    - title: "高度な抽出オプション"
      content: "ページ、形式、または解像度でのフィルタリングによる画像抽出のカスタマイズができ、マルチページドキュメントにも対応します。"
      
  code_samples:
    # code sample loop
    - title: "PDF ドキュメントから画像を抽出して保存する方法"
      content: |
        この例では、PDF ファイルからすべての画像アセットを抽出し、ローカルファイルシステムに保存する方法を示します。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Parser クラスを使用して PDF を読み込みます。
        using (Parser parser = new Parser("input.pdf"))
        {
            // ファイルから埋め込まれた画像を抽出します。
            IEnumerable<PageImageArea> images = parser.GetImages();

            // 出力形式と画像オプションを設定します（例：PNG）。
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // 抽出した画像をディスクに書き込みます。
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
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
    title: "画像抽出に対応する形式"
    exclude: "ODT"
    description: "GroupDocs.Parser は、幅広いドキュメントおよび画像形式から正確に画像を抽出します。一般的にサポートされている形式のリストを以下で確認してください。"
    items: 
        # format loop 1
        - name: "PDFを解析する"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(ポータブル文書形式)"
          
        # format loop 2
        - name: "DOCXを解析する"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Office 2007+ Word文書)"
          
        # format loop 3
        - name: "PPTXを解析する"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Open XMLプレゼンテーション形式)"
          
        # format loop 4
        - name: "XLSXを解析する"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Open XMLワークブック)"
          
        # format loop 5
        - name: "ODTを解析する"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(OpenDocumentテキスト文書)"
          
        # format loop 6
        - name: "ODSを解析する"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(OpenDocumentスプレッドシート)"
          
        # format loop 7
        - name: "ODPを解析する"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(OpenDocumentプレゼンテーション)"
          
        # format loop 8
        - name: "EPUBを解析する"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(オープンeBookファイル)"
          
        # format loop 9
        - name: "FB2を解析する"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(FictionBook eBook)"
         
          

---