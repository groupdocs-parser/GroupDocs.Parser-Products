---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:12
draft: false
otherformats: 

############################# Head ############################
head_title: "Java API を介して PDF、DOCX、PPTX、XLSX、EPUB などからテーブルを抽出します"
head_description: "GroupDocs.Parser Java API を使用すると、プログラマーは PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV からテーブルを抽出できます、ODT、RTF、および Java アプリ内のその他の多くのドキュメント タイプ。"

############################# Header ############################
title: "Java API を介して Excel、Word、PDF、および PowerPoint ドキュメントからテーブルを抽出します"
description: "GroupDocs.Parser Java API を使用すると、プログラマーは PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV からテーブルを抽出できます、ODT、RTF、および EPUB のドキュメントまたはページ。"
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
    title: "Java API 経由で EML ファイルからテーブルを抽出するにはどうすればよいですか?"
    content: |
        テーブルは行と列に配置されたセルの集合です。テーブルは、詳細または複雑なデータを保存および整理して、ユーザーが簡単に読み取ったり表示できるようにする上で非常に重要な役割を果たします。テーブルは、リストの作成、情報の比較、データの整列、情報のグループ化、データの傾向やパターンの強調表示など、さまざまな方法で使用できます。 GroupDocs.Parser for Java は、ソフトウェア プログラマが、PDF、電子メール、電子ブック、Word (DOC、{ 318})、PowerPoint (PPT、PPTX)、Excel (XLS、XLSX)、メール (EML、MSG) 形式など。 Java API には、ドキュメントからすべての表を抽出する、特定のページから表を抽出する、表のセル データを取得する、表の行と列の合計数を取得する、行の高さを取得するなど、表を操作するための重要な機能がいくつか含まれています。テーブルなどのデータを印刷します。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Java の EML からテーブルを抽出します"
    content_left: |
        [GroupDocs.Parser for Java](/ja/parser/java/) を使用すると、Java 開発者は、いくつかの簡単な手順を実装することで、EML ファイルからテーブルを簡単に抽出できます。
        
        * 最初のドキュメントの [Parser](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/) オブジェクトをインスタンス化します。
        * ドキュメントがテーブル抽出をサポートしているかどうかを確認します。
        * [PageTableAreaOptions](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.options/pagetableareaoptions/) および  をインスタンス化します。 [TemplateTableLayout](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.templates/templatetablelayout/) テーブルのレイアウトを設定するクラス
        * [getTables](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getTables-com.groupdocs.parser.options.PageTableAreaOptions-) メソッドを呼び出し、のコレクションを取得します。[PageTableArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/pagetablearea/) オブジェクト。

    title_right: "テーブル抽出の詳細"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document/">文書から表を抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document-page/">ドキュメントページから表を抽出する方法</a>
 
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Java サンプルコードを使用して EML ファイルからテーブルを抽出する方法">}}

        ```java    
        // GroupDocs.Parser API を使用して EML ファイルからテーブルを抽出する
        // Parserクラスのインスタンスを作成する
        try (Parser parser = new Parser(Constants.SampleInvoicePagesPdf)) {
            // ドキュメントがテーブル抽出をサポートしているかどうかを確認する
            if (!parser.getFeatures().isTables()) {
                System.out.println("ドキュメントはテーブル抽出をサポートしていません。");
                return;
            }
            // テーブルのレイアウトを作成する
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));
            // テーブル抽出のオプションを作成する
            PageTableAreaOptions options = new PageTableAreaOptions(layout);
            // ドキュメントから表を抽出します。
            Iterable<PageTableArea> tables = parser.getTables(options);
            // テーブルを反復処理する
            for (PageTableArea t : tables) {
                // 行を反復処理する
                for (int row = 0; row < t.getRowCount(); row++) {
                    // 列を反復処理する
                    for (int column = 0; column < t.getColumnCount(); column++) {
                        // 表のセルを取得する
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null) {
                            // 表のセルのテキストを印刷します
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                    System.out.println();
                }
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
    title: "他のドキュメント形式からのテーブルの抽出"
    content: |
        Java ファイル形式と画像のドキュメント解析とテーブル抽出 API。以下に示すように、いくつかの一般的なファイル形式のデータを抽出します。

############################# Back to top ###############################
back_to_top:
    enable: true
---