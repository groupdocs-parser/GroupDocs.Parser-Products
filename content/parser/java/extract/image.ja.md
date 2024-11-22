---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Java 経由で Excel、Word、PDF およびその他のドキュメントから画像を抽出するにはどうすればよいですか?"
head_description: "GroupDocs.Parser for Java API を使用すると、ソフトウェア開発者は、Java アプリ内の PDF、DOC、DOCX、PPT、PPTX、XLS、XLSX のドキュメントとメールから画像を解析して抽出できます。"

############################# Header ############################
title: "Java Excel、Word、PowerPoint、PDF およびその他のドキュメントのページから画像を解析して抽出する API"
description: "GroupDocs.Parser for Java API を使用すると、プログラマーは PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV、{358) から画像を抽出できます。 }、RTF & EPUB ドキュメント、または Java アプリケーション内のドキュメントのページ。"
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "無料トライアルをダウンロード"
    link: "https://downloads.groupdocs.com/parser/java"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/java"
              text: "APIリファレンス"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "コード例"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "ライブデモ"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "価格設定"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Java API を介して {{EXT}} ドキュメントまたは特定のページから画像を抽出する方法を学ぶ"
    content: |
        画像は一千の言葉に匹敵し、今日のビジュアル世界では魅力的なコンテンツを作成する際に無視することはできません。画像は、ユーザーの注意を引くだけでなく、情報伝達の優れたソースにもなります。多くの場合、文書、雑誌、プレゼンテーションから画像を取得して、別の場所で使用する必要があります。 GroupDocs.Parser for Java は、ソフトウェア開発者やプログラマーが、さまざまな種類のドキュメントから画像やその他の情報を解析して抽出するためのソリューションを構築するのに役立つ強力な API です。また、PNG、JPEG、WebP、GIF、BMP およびその他の形式での画像の保存もサポートしています。 API には、PDF、Microsoft Office 形式などのいくつかの一般的なドキュメント形式のサポートが含まれています: Word (DOC、DOCX)、PowerPoint (PPT、PPTX)、{282 } (XLS、XLSX)、LibreOffice 形式、電子メール、電子ブックなど。また、ドキュメントの解析、プレーンテキストと構造化テキストの抽出、キーワードによるテキスト検索、メタデータや画像、コンテナや添付ファイルの抽出などに関連するいくつかの高度な機能のサポートも含まれています。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Java のドキュメントから画像を抽出します"
    content_left: |
        [GroupDocs.Parser for Java](/ja/parser/java/) を使用すると、Java 開発者はいくつかの簡単な手順を実装することで、ドキュメントから画像を簡単に抽出できます。
        
        * 最初のドキュメントの [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) オブジェクトをインスタンス化します。
        * [getImages](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getImages--) メソッドを呼び出して、画像オブジェクトのコレクションを取得します。
        * リーダーが *null* ではないかどうかを確認します (ドキュメントの画像抽出がサポートされています)。
        * コレクションを反復処理して、サイズ、画像タイプ、画像コンテンツを取得します。

    title_right: "画像抽出について詳しくはこちら"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document/">文書から画像を抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page/">ドキュメントページから画像を抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page-area/">文書ページ領域から画像を抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-to-files/">画像をファイルに抽出する方法</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Java サンプルコードを使用してドキュメントから画像を抽出する方法">}}

        ```java    
        // GroupDocs.Parser API を使用してドキュメントから画像を抽出する
        // Parserクラスのインスタンスを作成する
        try (Parser parser = new Parser(Constants.SampleImagesPdf)) {
            // 画像の抽出
            Iterable<PageImageArea> images = parser.getImages();
            // 画像抽出がサポートされているかどうかを確認する
            if (images == null) {
                System.out.println("画像の抽出はサポートされていません");
                return;
            }
            // 画像を反復処理する
            for (PageImageArea image : images) {
                // ページインデックス、四角形、および画像タイプを印刷します。
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "システム要求"
    content_left: |
        GroupDocs.Parser for Java API は、すべての主要なプラットフォームとオペレーティング システムでサポートされています。以下のコードを実行する前に、次の前提条件がシステムにインストールされていることを確認してください。
        
        * オペレーティング システム: Microsoft Windows、Linux、MacOS
        * 開発環境: NetBeans, Intellij IDEA, Eclipse, etc.
        * フレームワーク
        * GroupDocs.Parser for Java の最新バージョンを [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser) からダウンロードします

    title_right: "GroupDocs.Parser for Java を使用する理由"
    content_right: |
        * サポートされているドキュメントからのプレーン テキスト抽出のサポート    
        * ユーザー定義のテンプレートを使用したドキュメントの解析    
        * 構造化テキスト抽出を完全にサポート    
        * キーワードおよび正規表現によるテキスト検索    
        * 書式設定されたテキスト、メタデータ、画像、コンテナ、添付ファイルを抽出します    
        * サポートされている一部のドキュメント形式の目次を抽出します    
        * PDF ドキュメントからのフォーム データを解析する    
        * ドキュメントからハイパーリンクを抽出する   

############################# Demos ############################
demos:
    enable: true
    title: "ライブデモ - オンラインで文書から画像を抽出"
    content: |
       [GroupDocs.Parser ライブ デモ](https://products.groupdocs.app/parser/images/) Web サイトにアクセスして、今すぐドキュメントから画像を抽出します。
       ライブデモには次のようなメリットがあります。
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "他のドキュメント形式から画像を抽出する"
    content: |
        Java ファイル形式と画像のドキュメント解析と画像抽出 API。以下に示すように、いくつかの一般的なファイル形式のデータを抽出します。

############################# Back to top ###############################
back_to_top:
    enable: true
---