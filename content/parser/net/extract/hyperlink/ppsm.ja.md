---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:06
draft: false
otherformats: 
ext: ppsm

############################# Head ############################
head_title: ".NET ドキュメント、ページ、またはページ領域からハイパーリンクを解析して抽出する API"
head_description: "GroupDocs.Parser .NET API を使用すると、ソフトウェア プログラマはドキュメント、ページ、またはページ領域 PDF、DOCX、XLSX、CSV、PPTX、EML、MSG、EPUB からハイパーリンクを抽出できます。などなど。"

############################# Header ############################
title: "C#/VB API 経由でドキュメント、ページ、または特定のページ領域からハイパーリンクを抽出します。"
description: "GroupDocs.Parser .NET API を使用すると、ソフトウェア開発者はドキュメント、ページ、またはページ領域 PDF、DOC、DOCX、PPT、PPTX、EML、MSG からハイパーリンクを解析して抽出できます。 、XLS、XLSX、CSV、ODT、RTF、EPUB、その他多くのドキュメント。"
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
    title: ".NET API 経由で PPSM ドキュメントからハイパーリンクを解析して抽出するにはどうすればよいですか?"
    content: |
        ハイパーリンクは、文書全体または文書内の特定の部分を指すテキスト、画像、またはアイコンです。ハイパーリンクを使用すると、ユーザーは Web ページまたはドキュメントに移動できます。多くの場合、ドキュメントからハイパーリンクを抽出し、それを使用して外部ドキュメントまたは Web ページにアクセスすることが必要になります。 GroupDocs.Parser for .NET は、テキストおよびメタデータ抽出ソリューションを実装するための完全な機能を提供する魅力的なドキュメント テキスト抽出 API です。 PDF、メール、電子書籍、Microsoft Office 形式からのテキストとハイパーリンクの抽出をサポートしています: Word (DOC、DOCX)、PowerPoint (PPT、PPTX)、Excel ( XLS、XLSX)、LibreOffice 形式など。ドキュメントの解析、プレーンテキストと構造化テキストの抽出、キーワードによるテキスト検索、メタデータや画像、コンテナや添付ファイルの抽出など、いくつかの高度な機能をサポートしています。
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: ".NET の PPSM からハイパーリンクを抽出します"
    content_left: |
        [GroupDocs.Parser for .NET](/ja/parser/net/) を使用すると、C# 開発者は、いくつかの簡単な手順を実装することで、PPSM ファイルからハイパーリンクを簡単に抽出できます。
        
        * 最初のドキュメントの [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) オブジェクトをインスタンス化します。
        * ドキュメントがハイパーリンク抽出をサポートしているかどうかを確認します。
        * [GetHyperlinks](https://reference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) メソッドを呼び出し、[PageHyperlinkArea](https://reference.groupdocs.com/parser/net/groupdocs.parser.data/pagehyperlinkarea) オブジェクト。
        * コレクションを反復処理して、ハイパーリンクのテキストと URL を取得します。

    title_right: "ハイパーリンク抽出の詳細"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document/">ドキュメントからハイパーリンクを抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page/">ドキュメントページからハイパーリンクを抽出する方法</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page-area/">ドキュメントのページ領域からハイパーリンクを抽出する方法</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="C# サンプルコードを使用して PPSM ファイルからハイパーリンクを抽出する方法">}}

        ```csharp    
        // GroupDocs.Parser API を使用して PPSM ファイルからハイパーリンクを抽出します
        // Parserクラスのインスタンスを作成する
        using (Parser parser = new Parser(filePath)) {
            // ドキュメントがハイパーリンク抽出をサポートしているかどうかを確認する
            if (!parser.Features.Hyperlinks) {
                Console.WriteLine("ドキュメントはハイパーリンク抽出をサポートしていません。");
                return;
            }
            // ドキュメントからハイパーリンクを抽出する
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();
            // ハイパーリンクを反復処理する
            foreach (PageHyperlinkArea h in hyperlinks) {
                // ハイパーリンクのテキストを印刷する
                Console.WriteLine(h.Text);
                // ハイパーリンクの URL を出力する
                Console.WriteLine(h.Url);
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
    title: "他のドキュメント形式からハイパーリンクを抽出する"
    content: |
        .NET ドキュメントは、ファイル形式と画像の解析とハイパーリンク抽出 API を使用します。以下に示すように、いくつかの一般的なファイル形式のデータを抽出します。

############################# Back to top ###############################
back_to_top:
    enable: true
---