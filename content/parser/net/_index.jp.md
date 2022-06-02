---
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

head_title: ".NET解析API、PDFWordExcelからテキスト画像メタデータを抽出"
head_description: "データベース、PDF、Word、Excel、プレゼンテーション、Web、電子メール、EPUB、およびzipファイル形式からテキスト、画像、メタデータ、およびエンコーディングを抽出するためのC＃.NETドキュメント解析API."

title: ".ドキュメントデータを抽出するためのNETAPI"
description: ".NETアプリ内から、ドキュメント、スプレッドシート、プレゼンテーション、メール、アーカイブから画像、生またはフォーマットされたテキストとメタデータを抽出します。"
button:
    enable: true

submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:
            - link: "#overview"
              text: "概要"

            - link: "#features"
              text: "特徴"

            - link: "#support"
              text: "サポート"

            - link: "https://products.groupdocs.app/parser"
              text: "ライブデモ"

            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "価格設定"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net/"
        link_buy: "https://purchase.groupdocs.com"

overview:
    enable: true
    content: |
      GroupDocs.Parser for .NETは、C＃、ASP.NET、およびその他の.NETテクノロジを使用して開発されたビジネスアプリケーション用のテキスト、メタデータ、および画像抽出APIです。サポートされている形式のファイルからのメタデータだけでなく、生のフォーマットされた構造化テキストの抽出もサポートしています。 GroupDocs.Parser for .NETを使用すると、アプリケーションは、ワードプロセッシングドキュメント、Excelスプレッドシート、PowerPointプレゼンテーション、OneNote、PDFファイル、ZIPアーカイブなどの一般的な形式のパスワードで保護されたドキュメントの解析も実行できます。
    tabs:
      enable: true
      
      tab_one:
        description: |
          以下は、GroupDocs.Parserfor.NETの概要です。
      
        left:
          enable: true
          icon: "fas fa-tools"
          title: "特徴"
          content: |
            *画像を抽出する
            *生のテキストを抽出する
            *フォーマットされたテキストを抽出する
            *構造化テキストを抽出する
            *メタデータを抽出する
            *ZIPファイル内のファイルから抽出
            *検索して抽出
            *テキストフォーマッタで抽出
            *エンコーディング標準を検出
            *メディアタイプの検出
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "API"
          content: |
            *入力ファイルを取得します
            *生またはフォーマットされたテキストをフェッチします
            *メタデータを取得します
      
      tab_two:
        description: |
          GroupDocs.Parser for .NETは、次の[ドキュメントファイル形式]（https://docs.groupdocs.com/parser/net/supported-document-formats/）をサポートしています。

        left:
          enable: true
          table:
            - title: "テキスト抽出"
              content: |
                * **テキスト**：DOC、DOCX、DOT、DOTM、DOTX、DOCM、RTF、ODT、OTT、TXT、MD、WordprocessingML（XML）
                * **スプレッドシート**：XLS、XLSX、CSV、XLSM、XLSB、ODS、SpreadsheetML（XML）、XLT、XLTX、XLTM、OTS、XLA 、、 XLAM、TSV
                * **プレゼンテーション**：PPT、PPTX、PPTM、PPS、PPSX、PPSM、POT、POTX、POTM、ODP、OTP
                * ** OneNote **：ONE
                * **メール**：MSG、EML、EMLX、PST、OST、MS EXCHANGE SERVER、POP、IMAP
                * **電子出版**：EPUB、FB2
                * **ポータブルドキュメント**：PDF、PDFポートフォリオ、暗号化されたPDF
                * ** DOMベース**：XML、HTML、XHTML、MHTML
                * **圧縮とパッケージ化**：ZIP、CHM
                * **データベース**：ADO.NET

            - title: "エンコーディング検出"
              content: |
                * ** BOM **：UTF32 LE、UTF32 BE、UTF16 LE、UTF16 BE、UTF8、およびUTF7
                * **コンテンツ**：UTF32 LE、UTF32 BE、UTF16 LE、UTF16 BE、UTF8、およびANSI

        right:
          enable: true
          table:
            - title: "メタデータ抽出"
              content: |
                * **テキスト**：DOC、DOCX、DOT、DOTX、DOTM、OTT、ODT
                * **スプレッドシート**：XLS、XLSX、XLT、XLTX、XLTM、XLA、XLAM、OTS、ODS
                * **プレゼンテーション**：PPT、PPTX、POT、POTX、POTM、PPSM、PPTM、OTP、ODP
                * **メール**：MSG、EML、EMLX
                * **電子出版**：EPUB、FB2
                * **その他**：PDF

            - title: "テキストとメタデータの抽出"
              content: |
                * **テンプレート**：DOTX、POTX
                * **マクロ対応テンプレート**：DOTM、POTM、PPSM、PPTM
                * ** OpenDocumentテンプレート**：OTT

            - title: "画像抽出"
              content: |
                * **テキスト**：DOC、DOCX、DOCM、RTF、DOT、DOTM、DOTX、ODT
                * **スプレッドシート**：XLS、XLSX、XLSM、XLSB、ODS、XLT、XLTM、XLTX
                * **プレゼンテーション**：PPT、PPTX、PPTM、ODP、POT、POTM、POTX、PPS、PPSX、PPSM
                * **ポータブルドキュメント**：PDF、POT、POTM、POTX
                * **電子書籍**：CHM、EPUB、FB2
                * **マークアップ**：HTML

      tab_three:
        description: |
          GroupDocs.Parser for .NETは、次のオペレーティングシステム、フレームワーク、およびパッケージマネージャーをサポートしています。
        
        left:
          enable: true
          table:
            - icon: "fab fa-windows"
              title: "オペレーティングシステム"
              content: |
                *Windowsデスクトップ
                * WindowsServer
                * Windows Azure
                * Linux

            - icon: "fas fa-code"
              title: "サポートされているフレームワーク"
              content: |
                * .NETFramework2.0以降
                * MonoFramework1.2以降
                * .NET Standard 2.0
                * .NET Core 2.0

        right:
          enable: true
          table:
            - icon: "fas fa-box"
              title: "パッケージマネージャー"
              content: |
                * NuGet

            - icon: "fas fa-tools"
              title: "開発環境"
              content: |
                * Microsoft Visual Studio
                * Xamarin.Android
                * Xamarin.IOS
                * Xamarin.Mac
                * MonoDevelop

features:
    enable: true
    title: "GroupDocs.Parserfor.NET機能"

    feature:
      - icon: "fas fa-copy"
        content: "単一または複数のファイルでの単語の出現を統計的にカウント"

      - icon: "fas fa-eye"
        content: "Excelワークシートとプレゼンテーションテンプレートからテキストとメタデータを抽出する"

      - icon: "fas fa-bolt"
        content: "ドキュメントリーダーをインストールせずにファイルまたはストリームからテキストコンテンツを抽出する"
      
      - icon: "fas fa-file-powerpoint"
        content: "高速または標準のテキスト抽出モードを使用して、ドキュメントからフォーマットされたテキストを取得する"

      - icon: "fas fa-code"
        content: "パスワードで保護されたXMLドキュメントのメディアタイプを検出し、それらからテキストをプルします"

      - icon: "fas fa-cloud"
        content: "電子メールと添付ファイル内からプログラムでフォーマットされたテキストを取得する"

      - icon: "fas fa-remove-format"
        content: "OneNoteドキュメントの1ページまたは複数ページからテキストを引き出す"

      - icon: "fas fa-comment-slash"
        content: "PDF、MS Word、Excel、およびプレゼンテーションドキュメントからデータを抽出する"

      - icon: "fas fa-location-arrow"
        content: "PDFフォームからデータを抽出し、単純なPDFファイルまたはPDFポートフォリオドキュメントからテキストを取り出します"

      - icon: "fas fa-border-all"
        content: "PowerPointプレゼンテーションからフォーマットされたテキストを取得するか、特定のスライドからテキストを削除します"

      - icon: "fas fa-wrench"
        content: "Excelスプレッドシートのセル、行、列から生のテキストまたは書式設定されたテキストを収集する"

      - icon: "fas fa-columns"
        content: "Word文書から生またはHTML形式のテキストを抽出する"

      - icon: "fas fa-file-word"
        content: "HTMLフォーマッタは、段落、ハイパーリンク、フォント、見出し、リスト、および表のフォーマットをサポートします"

      - icon: "fas fa-envelope"
        content: "EPUB、CHM、Markdown、FB2ファイルから単一の文または全文を引き出す"

      - icon: "fas fa-print"
        content: "データベース、PDF、EPUB、CHM、ワードプロセッシングドキュメントからの目次の抜粋"

      - icon: "fas fa-file-archive"
        content: "コンテンツ構造を含むテキストをそのまま引き出し、ドキュメントから強調表示されたテキストを抜粋"

      - icon: "fas fa-lock"
        content: "分析用のドキュメントからテキスト領域を取得し、サポートされているドキュメント形式からメタデータを引き出します"

      - icon: "fas fa-file-code"
        content: "サポートされている形式からすべてまたは選択した画像を取得し、抽出した画像を回転します"
      
      - icon: "fas fa-fill-drip"
        content: "ZipアーカイブおよびOSTコンテナ内のファイルからテキストを取り出し、ZIPコンテナアイテムのファイルタイプを検出する"

      - icon: "fas fa-file-excel"
        content: "電子メールコンテナ（Exchange Webサーバー、POP3、IMAP）からデータを取得する"

      - icon: "fas fa-heading"
        content: "ドキュメント内の単純なテキスト、単語全体、正規表現を検索"

      - icon: "fas fa-project-diagram"
        content: "ドキュメントテンプレートを準備し、ドキュメントからデータを抽出し、データフィールドとテーブルを分析します"

      - icon: "fas fa-cube"
        content: "ドキュメント内の強調表示された式を検索して抽出する"

      - icon: "fab fa-uncharted"
        content: "プレーンテキストフォーマッター（シンプル＆ASCII）またはマークダウンフォーマッターでテキストを取得"

      - icon: "fab fa-uncharted"
        content: "Markdown Formatterは、フォント、ハイパーリンク、見出し、リスト、およびテーブルのフォーマットをサポートします"

      - icon: "fab fa-uncharted"
        content: "プレーンテキストをフォーマットするために、エッジ、角度、および交差を使用してカスタムフォーマットを実行します"

      - icon: "fab fa-uncharted"
        content: "テーブルレイアウトの移動と列セパレータによる長方形領域内のテーブルの検出"

      - icon: "fab fa-uncharted"
        content: "Microsoft Officeファイル形式内の図形、WordArtオブジェクト、およびテキストボックスからテキストを抽出する"

      - icon: "fab fa-uncharted"
        content: "画像をファイルに抽出– JPG、PNG、GIF、BMP、PNG、またはWEBP形式で保存"

    more_feature:
      - title: "ドキュメントからのテキストの抽出"
        content: |
          GroupDocs.Parser for .NET APIを使用してドキュメントからテキストを抽出するのは簡単で、数行のコードで実現できます。

          ```cs
          //パーサークラスのインスタンスを作成します
          using(Parser parser = new Parser("sample.docx"))
          {
            //テキストをリーダーに抽出します
            using(TextReader reader = parser.GetText())
            {
              //ドキュメントからテキストを印刷します
              //テキスト抽出がサポートされていない場合、リーダーはnullです
              Console.WriteLine(reader == null ? "Text extraction isn't supported." : reader.ReadToEnd());
            }
          }
          ```

support:
    enable: true

solutions:
    enable: true
    title: "GroupDocs.Parserは、他の一般的な開発環境向けのドキュメント表示APIを提供します"

    solution:
        - img_alt: "GroupDocs.Parser for Java"
          image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-java.png"
          product: "GroupDocs.Parser"
          platform: "Java"
          link: "/parser/java/"

back_to_top:
  enable: true
---
