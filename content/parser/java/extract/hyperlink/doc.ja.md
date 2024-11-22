---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:06
draft: false
otherformats: docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf
ext: doc

############################# Head ############################
head_title: "Java のドキュメントからハイパーリンクを抽出します"
head_description: "GroupDocs.Parser for Java API を使用すると、開発者はドキュメント、ドキュメントのページ、または Excel、PowerPoint、PDF、Outlook などの特定のページ領域からハイパーリンクを抽出できます。"

############################# Header ############################
title: "Java ドキュメント、ページ、または特定のページ領域からハイパーリンクを抽出する API"
description: "GroupDocs.Parser for Java API を使用すると、ドキュメント、ドキュメントのページ、または特定のページからハイパーリンクを抽出できるため、開発者の作業が容易になります。PDF、DOCX、PPTX、EML、MSG、XLS、{322 の領域}、CSV、RTF、EPUB など。"
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
    title: "Java API 経由で DOC ドキュメントからハイパーリンクを解析して抽出するにはどうすればよいですか?"
    content: |
        ハイパーリンクは、文書全体または文書内の特定の部分を指すテキスト、画像、またはアイコンです。ハイパーリンクを使用すると、ユーザーは Web ページまたはドキュメントに移動できます。多くの場合、ドキュメントからハイパーリンクを抽出し、それを使用して外部ドキュメントまたは Web ページにアクセスすることが必要になります。 GroupDocs.Parser for Java は、テキストおよびメタデータ抽出ソリューションを実装するための完全な機能を提供する魅力的なドキュメント テキスト抽出 API です。 PDF、メール、電子書籍、Microsoft Office 形式からのテキストとハイパーリンクの抽出をサポートしています: Word (DOC、DOCX)、PowerPoint (PPT、PPTX)、Excel ( XLS、XLSX)、LibreOffice 形式など。ドキュメントの解析、プレーンテキストと構造化テキストの抽出、キーワードによるテキスト検索、メタデータや画像、コンテナや添付ファイルの抽出など、いくつかの高度な機能をサポートしています。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Java の DOC からハイパーリンクを抽出します"
    content_left: |
        [GroupDocs.Parser for Java](/ja/parser/java/) を使用すると、Java 開発者は、いくつかの簡単な手順を実装することで、DOC ファイルからハイパーリンクを簡単に抽出できます。
        
        * 最初のドキュメントの [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) オブジェクトをインスタンス化します。
        * ドキュメントがハイパーリンク抽出をサポートしているかどうかを確認します。
        * [getHyperlinks](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getHyperlinks--) メソッドを呼び出し、[PageHyperlinkArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/PageHyperlinkArea) オブジェクト。
        * コレクションを反復処理して、ハイパーリンクのテキストと URL を取得します。

    title_right: "ハイパーリンク抽出の詳細"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document/">ドキュメントからハイパーリンクを抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page/">ドキュメントページからハイパーリンクを抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page-area/">ドキュメントのページ領域からハイパーリンクを抽出する方法</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Java サンプルコードを使用して DOC ファイルからハイパーリンクを抽出する方法">}}

        ```java    
        // GroupDocs.Parser API を使用して DOC ファイルからハイパーリンクを抽出します
        // Parserクラスのインスタンスを作成する
        try (Parser parser = new Parser(Constants.HyperlinksPdf)) {
            // ドキュメントがハイパーリンク抽出をサポートしているかどうかを確認する
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("ドキュメントはハイパーリンク抽出をサポートしていません。");
                return;
            }
            // ドキュメントからハイパーリンクを抽出する
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();
            // ハイパーリンクを反復処理する
            for (PageHyperlinkArea h : hyperlinks) {
                // ハイパーリンクのテキストを印刷する
                System.out.println(h.getText());
                // ハイパーリンクの URL を出力する
                System.out.println(h.getUrl());
                System.out.println();
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
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "他のドキュメント形式からハイパーリンクを抽出する"
    content: |
        Java ドキュメントは、ファイル形式と画像の解析とハイパーリンク抽出 API を使用します。以下に示すように、いくつかの一般的なファイル形式のデータを抽出します。

############################# Back to top ###############################
back_to_top:
    enable: true
---