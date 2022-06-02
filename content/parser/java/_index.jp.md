---
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

head_title: "PDF Word Excel HTMLからテキスト、画像、メタデータを解析するJava API"
head_description: "データベース、Word、Excel、プレゼンテーション、PDF、電子メール、EPUB、ZIPファイルからテキスト、画像、メタデータ、エンコーディングを抽出するJavaドキュメントパーサーAPI."

title: "データを抽出するJavaパーサーAPI"
description: "ドキュメント、プレゼンテーション、アーカイブ、メールからメタデータを使用して画像やテキストを解析および抽出するJavaAPI。"
button:
    enable: true

submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

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

            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "価格設定"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java/"
        link_buy: "https://purchase.groupdocs.com"

overview:
    enable: true
    content: |
      GroupDocs.Parser for Javaは、テキスト、画像、メタデータの抽出APIであり、生の構造化されフォーマットされたテキストを解析する機能を備えたビジネスアプリケーションの構築を支援する50以上の一般的なドキュメントタイプをサポートします。また、事前定義されたテンプレートを使用したドキュメントの解析をサポートし、請求書やその他の一般的なドキュメントから複雑なデータを迅速かつ正確に抽出できます。 GroupDocs.Parser for Javaを使用すると、ワードプロセッシングドキュメント、Excelスプレッドシート、PowerPointプレゼンテーション、OneNote、PDFファイル、ZIPアーカイブなど、すべての一般的な形式のパスワードで保護されたファイルからテキストとメタデータを抽出できます。
    tabs:
      enable: true     
      
      tab_one:
        description: |
          以下は、Java用のGroupDocs.Parserの概要です。

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
          GroupDocs.Parser for Javaは、次の[ドキュメントファイル形式]（https://docs.groupdocs.com/parser/java/supported-document-formats/）をサポートしています。

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
          GroupDocs.Parser for Javaは、次のオペレーティングシステム、フレームワーク、パッケージマネージャーをサポートしています。
        
        left:
          enable: true
          table:
            - icon: "fab fa-windows"
              title: "オペレーティングシステム"
              content: |
                *MicrosoftWindowsデスクトップ
                * Microsoft Windows Server
                * Linux
                * マックOS

            - icon: "fas fa-code"
              title: "サポートされているフレームワーク"
              content: |
                * Java 7（1.7）以降

        right:
          enable: true
          table:
            - icon: "fas fa-cogs"
              title: "開発環境"
              content: |
                * NetBeans
                * IntelliJ IDEA
                *Eclipse
            - icon: "fas fa-tools"
              title: "ビルド自動化ツール"
              content: |
                * Maven

features:
    enable: true
    title: "GroupDocs.Parser for Java Features"

    feature:
      - icon: "fas fa-copy"
        content: "単一または複数のドキュメントの単語の出現を統計的にカウントする"

      - icon: "fas fa-eye"
        content: "ExcelスプレッドシートとPowerPointプレゼンテーションテンプレートからテキストとメタデータを抽出する"

      - icon: "fas fa-bolt"
        content: "ドキュメントリーダーをインストールせずに、ファイルまたはストリームからテキストをフェッチする"
      
      - icon: "fas fa-file-powerpoint"
        content: "高速または標準のテキスト抽出モードを使用して、フォーマットされたテキストをドキュメントから引き出す"

      - icon: "fas fa-code"
        content: "パスワードで保護されたXMLドキュメントのメディアタイプを検出し、それらからテキストを抽出します"

      - icon: "fas fa-cloud"
        content: "プログラムでPowerPointプレゼンテーション、電子メール、添付ファイルからフォーマットされたテキストを取得する"

      - icon: "fas fa-remove-format"
        content: "OneNoteドキュメントの1ページまたは複数ページからテキストを削除します"

      - icon: "fas fa-comment-slash"
        content: "単純なPDFファイルまたはPDFポートフォリオドキュメントから生のテキストを引き出す"

      - icon: "fas fa-location-arrow"
        content: "PDF、MS Word、Excel、およびプレゼンテーションドキュメントからデータを抽出します"

      - icon: "fas fa-border-all"
        content: "Excelスプレッドシートのセル、行、列から生またはフォーマットされたテキストを抽出する"

      - icon: "fas fa-wrench"
        content: "Word文書から生またはHTML形式のテキストを収集し、文書から強調表示されたテキストを抜粋します"

      - icon: "fas fa-columns"
        content: "PDFフォームからデータを取得し、PDFまたはWord文書からフォーマットされたテーブルを取得する"

      - icon: "fas fa-file-word"
        content: "EPUB、CHM、Markdown、FB2ファイルから単一の文または全文を引き出す"

      - icon: "fas fa-envelope"
        content: "データベース、PDF、EPUB、CHM、ワードプロセッシングドキュメントからの目次の抜粋"

      - icon: "fas fa-print"
        content: "分析のためにドキュメントからテキスト領域を取得し、コンテンツ構造がそのままの状態でテキストを引き出します"

      - icon: "fas fa-file-archive"
        content: "サポートされているドキュメント形式からメタデータを取得する"

      - icon: "fas fa-lock"
        content: "サポートされている形式からすべてまたは選択した画像を引き出し、抽出した画像を回転します"

      - icon: "fas fa-file-code"
        content: "ZipアーカイブおよびOSTコンテナ内のファイルからテキストを抽出–Zipコンテナアイテムのメディアタイプを検出"
      
      - icon: "fas fa-fill-drip"
        content: "メールコンテナ（Exchange Webサーバー、POP3、IMAP）からデータを取得する"

      - icon: "fas fa-file-excel"
        content: "高速で信頼性が高く効率的な方法でデータベースコンテナからテキストを取り出す"

      - icon: "fas fa-heading"
        content: "ドキュメント内の単純なテキスト、単語全体、正規表現を検索する"

      - icon: "fas fa-project-diagram"
        content: "ドキュメントテンプレートを準備し、ドキュメントからデータを抽出し、データフィールドとテーブルを分析します"

      - icon: "fas fa-cube"
        content: "ドキュメント内の強調表示された式を検索して抽出する"

      - icon: "fab fa-uncharted"
        content: "プレーンテキストフォーマッタ（シンプルおよびASCII）を使用してテキストを引き出すか、エッジ、角度、および交差を使用してカスタムフォーマットを行う"

      - icon: "fab fa-uncharted"
        content: "Markdown Formatterを使用したテキスト（フォント、ハイパーリンク、見出し、リスト、表）のフェッチとフォーマット"

      - icon: "fab fa-uncharted"
        content: "HTMLフォーマッターでテキストを取得し、段落、ハイパーリンク、フォント、見出し、リスト、表にフォーマッターを適用します"

      - icon: "fab fa-uncharted"
        content: "テーブルレイアウトの移動と列セパレータによる長方形領域内のテーブルの検出"

      - icon: "fab fa-uncharted"
        content: "Microsoft Officeファイル形式内の図形、WordArtオブジェクト、およびテキストボックスからテキストを抽出する"

      - icon: "fab fa-uncharted"
        content: "画像をファイルに抽出– JPG、PNG、GIF、BMP、PNG、またはWEBP形式で保存"

      - icon: "fab fa-uncharted"
        content: "JDBCを介して電子メールサーバーおよびデータベースからテキストを抽出する"

    more_feature:
      - title: "プレーンテキストまたはHTMLフォーマッタでテキストを取得する"
        content: |
          GroupDocs.Parser for Javaを使用すると、さまざまなフォーマッタをテキストとHTMLに適用できます。 SimpleとASCIIの両方でPlainTextFormatterを使用してテキストをプルできます。 HTML Formatterを使用してテキストを取得し、段落、ハイパーリンク、フォント、見出し、リスト、および表に書式を適用することもできます。

support:
    enable: true

solutions:
    enable: true
    title: "GroupDocs.Parserは、他の一般的な開発環境向けのドキュメント表示APIを提供します"

    solution:
        - img_alt: "GroupDocs.Parser for .NET"
          image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-net.png"
          product: "GroupDocs.Parser"
          platform: ".NET"
          link: "/parser/net/"

back_to_top:
  enable: true
---
