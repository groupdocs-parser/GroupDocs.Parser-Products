---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:12
draft: false
otherformats: html mht mhtml odp ods odt one otp ott pdf pps ppsx ppt pptx rtf tex

############################# Head ############################
head_title: "C#.NET API 経由で PDF、DOCX、PPTX、XLSX、EPUB などからテーブルを抽出します"
head_description: "GroupDocs.Parser .NET API を使用すると、プログラマーは PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV からテーブルを抽出できます、ODT、RTF、および .NET アプリ内のその他の多くのドキュメント タイプ。"

############################# Header ############################
title: "C#.NET API 経由で Excel、Word、PDF、PowerPoint ドキュメントからテーブルを抽出します"
description: "GroupDocs.Parser .NET API を使用すると、プログラマは PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV からテーブルを抽出できます。 、ODT、RTF、および EPUB のドキュメントまたはページ。"
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "無料トライアルをダウンロード"
    link: "https://downloads.groupdocs.com/parser/net"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/net"
              text: "APIリファレンス"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "コード例"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "ライブデモ"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "価格設定"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: ".NET API 経由で EPUB ファイルからテーブルを抽出するにはどうすればよいですか?"
    content: |
        テーブルは行と列に配置されたセルの集合です。テーブルは、詳細または複雑なデータを保存および整理して、ユーザーが簡単に読み取ったり表示できるようにする上で非常に重要な役割を果たします。テーブルは、リストの作成、情報の比較、データの整列、情報のグループ化、データの傾向やパターンの強調表示など、さまざまな方法で使用できます。 GroupDocs.Parser for .NET は、ソフトウェア プログラマが、PDF、電子メール、電子ブック、Word (DOC、{ 318})、PowerPoint (PPT、PPTX)、Excel (XLS、XLSX)、メール (EML、MSG) 形式など。 .NET API には、ドキュメントからすべての表を抽出する、特定のページから表を抽出する、表のセル データを取得する、表の行と列の合計数を取得する、行の高さを取得するなど、表を操作するための重要な機能がいくつか含まれています。テーブルなどのデータを印刷します。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: ".NET の EPUB からテーブルを抽出します"
    content_left: |
        [GroupDocs.Parser for .NET](/ja/parser/net/) を使用すると、C# 開発者は、いくつかの簡単な手順を実装することで、EPUB ファイルからテーブルを簡単に抽出できます。
        
        * 最初のドキュメントの [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) オブジェクトをインスタンス化します。
        * ドキュメントがテーブル抽出をサポートしているかどうかを確認します。
        * [PageTableAreaOptions](https://reference.groupdocs.com/parser/net/groupdocs.parser.options/pagetableareaoptions/) および  をインスタンス化します。 [TemplateTableLayout](https://reference.groupdocs.com/parser/net/groupdocs.parser.templates/templatetablelayout/) テーブルのレイアウトを設定するクラス
        * [GetTables](https://reference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gettables) メソッドを呼び出し、のコレクションを取得します。[PageTableArea](https://reference.groupdocs.com/parser/net/groupdocs.parser.data/pagetablearea) オブジェクト。

    title_right: "テーブル抽出の詳細"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-tables-from-document/">文書から表を抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-tables-from-document-page/">ドキュメントページから表を抽出する方法</a>
 
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="C# サンプルコードを使用して EPUB ファイルからテーブルを抽出する方法">}}

        ```csharp    
        // GroupDocs.Parser API を使用して EPUB ファイルからテーブルを抽出する
        // Parserクラスのインスタンスを作成する
        using (Parser parser = new Parser(filePath)) {
            // ドキュメントがテーブル抽出をサポートしているかどうかを確認する
            if (!parser.Features.Tables) {
                Console.WriteLine("ドキュメントはテーブル抽出をサポートしていません。");
                return;
            }
            // テーブルのレイアウトを作成する
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });
            // テーブル抽出のオプションを作成する
            PageTableAreaOptions options = new PageTableAreaOptions(layout);
            // ドキュメントから表を抽出します。
            IEnumerable<PageTableArea> tables = parser.GetTables(options);
            // テーブルを反復処理する
            foreach (PageTableArea t in tables) {
                // 行を反復処理する
                for (int row = 0; row < t.RowCount; row++) {
                    // 列を反復処理する
                    for (int column = 0; column < t.ColumnCount; column++) {
                        // 表のセルを取得する
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null) {
                            // 表のセルのテキストを印刷します
                            Console.Write(cell.Text);
                            Console.Write(" | ");
                        }
                    }
                    Console.WriteLine();
                }
                Console.WriteLine();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "システム要求"
    content_left: |
        GroupDocs.Parser for .NET API は、すべての主要なプラットフォームとオペレーティング システムでサポートされています。以下のコードを実行する前に、次の前提条件がシステムにインストールされていることを確認してください。
        
        * オペレーティング システム: Microsoft Windows、Linux、MacOS
        * 開発環境: Microsoft Visual Studio, Xamarin, MonoDevelop
        * フレームワーク
        * GroupDocs.Parser for .NET の最新バージョンを [Nuget](https://www.nuget.org/packages/groupdocs.parser) からダウンロードします

    title_right: "GroupDocs.Parser for .NET を使用する理由"
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
        .NET ファイル形式と画像のドキュメント解析とテーブル スキャン API。以下に示すように、いくつかの一般的なファイル形式のデータを抽出します。

############################# Back to top ###############################
back_to_top:
    enable: true
---