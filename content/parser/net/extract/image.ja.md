---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: ".NET 経由で Excel、Word、PDF およびその他のドキュメントまたはページから画像を抽出します"
head_description: "GroupDocs.Parser .NET API を使用すると、ソフトウェア プログラマは、.NET アプリ内で MS Excel、Word、PowerPoint、PDF などのさまざまなドキュメントから画像を抽出できます。"

############################# Header ############################
title: "C#.NET API 経由で PDF、DOCX、PPTX、MSG、XLSX ドキュメントとページから画像を抽出します"
description: "GroupDocs.Parser .NET API を使用すると、プログラマーは PDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV から画像を抽出できます、ODT、RTF、および EPUB ドキュメントまたはドキュメントのページ。"
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
    title: ".NET 経由でドキュメントから画像を抽出するにはどうすればよいですか?"
    content: |
        画像を使用すると、言葉では表現できない情報を伝えることができます。画像はユーザーの注意を引き、難しい概念を簡単に説明するのに役立ちます。文書や雑誌を読んだり、プレゼンテーションから恩恵を受けたりしているときに、魅力的な画像を見つけてダウンロードしたくなることがあります。 GroupDocs.Parser for .NET は、ユーザーがさまざまな種類のドキュメントから画像を抽出し、PNG、JPEG、WebP、GIF、BMP などの形式で保存するための便利なアプリケーションを開発するのに役立つ強力な API です。 API には、PDF、電子メール、電子書籍、Microsoft Office 形式などの最も一般的に使用されるファイル形式のいくつかからのテキストだけでなく画像抽出のサポートが含まれています: Word (DOC、DOCX)、{ 284} (PPT、PPTX)、Excel (XLS、XLSX)、LibreOffice 形式など。この API は、ドキュメントの解析、プレーン テキストと構造化テキストの抽出、キーワードによるテキスト検索、メタデータや画像、コンテナや添付ファイルの抽出なども完全にサポートしています。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: ".NET のドキュメントから画像を抽出します"
    content_left: |
        [GroupDocs.Parser for .NET](/ja/parser/net/) を使用すると、C# 開発者はいくつかの簡単な手順を実装することで、ドキュメントから画像を簡単に抽出できます。
        
        * 最初のドキュメントの [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) オブジェクトをインスタンス化します。
        * [GetImages](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser/methods/getimages) メソッドを呼び出して、画像オブジェクトのコレクションを取得します。
        * リーダーが *null* ではないかどうかを確認します (ドキュメントの画像抽出がサポートされています)。
        * コレクションを反復処理して、サイズ、画像タイプ、画像コンテンツを取得します。

    title_right: "画像抽出について詳しくはこちら"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document/">文書から画像を抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page/">ドキュメントページから画像を抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page-area/">文書ページ領域から画像を抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-to-files/">画像をファイルに抽出する方法</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="C# サンプルコードを使用してドキュメントから画像を抽出する方法">}}

        ```csharp    
        // GroupDocs.Parser API を使用してドキュメントから画像を抽出する
        // Parserクラスのインスタンスを作成する
        using (Parser parser = new Parser(filePath)) {
            // 画像の抽出
            IEnumerable<PageImageArea> images = parser.GetImages();
            // 画像抽出がサポートされているかどうかを確認する
            if (images == null) {
                Console.WriteLine("画像の抽出はサポートされていません");
                return;
            }
            // 画像を反復処理する
            foreach (PageImageArea image in images) {
                // ページインデックス、四角形、および画像タイプを印刷します。
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", image.Page.Index, image.Rectangle, image.FileType));
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
        .NET ファイル形式と画像のドキュメント解析と画像抽出 API。以下に示すように、いくつかの一般的なファイル形式のデータを抽出します。

############################# Back to top ###############################
back_to_top:
    enable: true
---