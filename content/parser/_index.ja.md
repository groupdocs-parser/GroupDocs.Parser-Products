---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: ja

############################# Head ############################
head_title: "PDF、Word、Excel 用 Document Parser SDK | GroupDocs"
head_description: "PDF、Word、Excel、メール および 50 以上のその他のドキュメント形式からテキスト、画像、メタデータ、バーコード、テーブルを抽出する Document Parser SDK（.NET、Java、Python アプリ向け）。"

############################# Header ############################
title: "Document Parser SDK"
description:  |
  開発者に優しい Document Parser SDKで、50 以上のドキュメントと画像形式からテキスト、画像、バーコード、メタデータ、テーブルを抽出します。

  最小限のコードで、.NET、Java、Python アプリケーションに高性能なドキュメント解析を統合できます。

  柔軟なテンプレートと高度な API を使用して、解析ルールをカスタマイズし、クリーンで構造化されたデータ出力を提供します。

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "プラットフォームを選択"
  title: "プラットフォームに依存しない"
  description: "GroupDocs.Parser ライブラリは以下の OS とフレームワークをサポートしています："
  details_link_title: "詳しく見る"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser for .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    .NET Framework 4.6.2 or higher <br> .NET Core 2.0 or higher <br> .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    Microsoft Visual Studio <br> JetBrains Rider <br> Microsoft Visual Code
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser for Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Java 8 or higher <br> Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    IntelliJ IDEA <br> Eclipse <br> NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats


    # items loop
    - title: "Python"
      description: GroupDocs.Parser for Python
      color: "yellow"
      tag: "python-net"
      link: "/parser/python-net/"
      features_link: "https://docs.groupdocs.com/parser/python-net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Python 3.5+
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> macOS
      
          # features loop
          - rows: "4"
            content: |
                    PyCharm, VS Code, Jupyter Notebook
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats                    

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser の概要"
  description: "PDF、Office ドキュメント、画像、メール、アーカイブから構造化データと非構造化データを抽出する強力な Document Parser SDK。"

  items:
    # items loop
    - icon: "text"
      title: "テキスト抽出"
      content: "さまざまなファイル形式からテキスト情報を抽出します"

    # items loop
    - icon: "image"
      title: "画像抽出"
      content: "多様なソースからビジュアルコンテンツを取得します"

    # items loop
    - icon: "template"
      title: "テンプレートによるデータ解析"
      content: "カスタムテンプレートを作成し、特定情報の解析に利用します"

    # items loop
    - icon: "pdf"
      title: "PDF フォーム解析"
      content: "PDF フォームは、ユーザーが入力できるフィールドを備えたデジタル文書です"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser コードサンプル"
  description: "C#, Java および Python における典型的な GroupDocs.Parser 操作のユースケース"

  items:
    # items loop
    - title: "PDF ドキュメントからテキストを抽出する方法"
      content: "GroupDocs.Parser API は、数ステップの実装でドキュメントからテキストを簡単に抽出できます。"
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // 目的のファイルを渡して Parser クラスのインスタンスを作成する
                using (var parser = new Parser("source.pdf"))
                {
                    // テキストを抽出する
                    using (var textReader = parser.GetText())
                    {
                        // 抽出したテキストを処理する
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // 目的のファイルを渡して Parser クラスのインスタンスを作成する
                try (Parser parser = new Parser("source.pdf"))
                {
                    // テキストを抽出する
                    try (TextReader reader = parser.getText())
                    {
                        // 抽出したテキストを処理する
                        System.out.println(reader == null 
                                ? "" 
                                : reader.readToEnd());
                    }
                }  
              ```
          # samples loop
          - language: "Python"
            color: "green"
            content: |
              ```python {style=abap}
                from groupdocs.parser import Parser

                # 目的のファイルを渡して Parser クラスのインスタンスを作成する
                with Parser("source.pdf") as parser:
                    # テキストを抽出する
                    text = parser.get_text()

                    # 抽出したテキストを処理する
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "50 以上のドキュメントと画像形式をサポート"
  description: "GroupDocs.Parser Document Parser SDK は、Office ドキュメント、PDF、画像、メール、アーカイブなどの解析操作を可能にします。"

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser の実績"
  description: "当ライブラリの成果に関する主要指標を確認してください"

  items:
    # items loop
    - number: "50+"
      title: "対応フォーマット"
      content: "GroupDocs.Parser は、50 以上の主要ファイル形式での操作をサポートしています。"

    # items loop
    - number: "1600k"
      title: "NuGet ダウンロード数"
      content: ".NET 用 GroupDocs.Parser NuGet パッケージは 1,600,000 回以上ダウンロードされています。"

    # items loop
    - number: "18k"
      title: "Maven ダウンロード数"
      content: "GroupDocs.Parser は Maven で 18,000 回ダウンロードされました。強力な Java パーシング機能を提供します。"

    # items loop
    - number: "140+"
      title: "満足したお客様"
      content: "有名企業や個人開発者も、革新的なソリューションを構築するためにGroupDocsの製品を選んでいます。"


############################# Customers ###############################
customers:
  enable: true
  title: "当社の満足したお客様"
  description: "GroupDocsのライブラリは、世界中で高く評価されている著名なブランドによって使用されています。"

  items:
    # items loop
    - title: "BenQ Corporation"
      logo: "benq"
      
    # items loop
    - title: "Nasdaq Stock Market"
      logo: "nasdaq"
      
    # items loop
    - title: "AT&T Inc."
      logo: "att"
      
    # items loop
    - title: "Customer logo AstraZeneca"
      logo: "astrazeneca"
      
    # items loop
    - title: "Central Bank of Argentina"
      logo: "argentinacentralbank"
      
    # items loop
    - title: "Roche Holding AG"
      logo: "roche"
      
    # items loop
    - title: "Capita"
      logo: "capita"
      
    # items loop
    - title: "Axa S.A."
      logo: "axa"
      
    # items loop
    - title: "Instructure Inc."
      logo: "instructure"
      
    # items loop
    - title: "Wipro"
      logo: "wipro"


############################# Actions ###############################
actions:
  enable: true
  title: "開始する準備はできましたか？"
  description: "ご使用のプラットフォームでGroupDocs.Parserの機能を無料でお試しください"

  items:
    # items loop
    - title: ".NET"
      color: "blue"
      link: "/parser/net/"

    # items loop
    - title: "Java"
      color: "red"
      link: "/parser/java/"

############################# FAQ ###############################
faq:
  enable: true
  title: "よくある質問"
  description: "最もよく寄せられる質問への回答です。"

  items:
    # items loop
    - question: "GroupDocs.Parser ライブラリは、ドキュメント操作に他のサードパーティ製ソフトウェアを必要としますか？"
      answer: "GroupDocs.Parser は、Adobe Acrobat や Microsoft Office などの外部ソフトウェアのインストールを必要としません。"

    # items loop
    - question: "購入前に GroupDocs.Parser ライブラリを試用できますか？"
      answer: "はい、ライセンスを購入せずに GroupDocs.Parser を試すことができます。ライセンスなしでインストールすると、ライブラリはトライアルモードで動作します。このモードでは、結果のドキュメントにトライアルバッジが付加され、最初の3ページに切り詰められます。GroupDocs.Parser をトライアル版の制限なくテストしたい場合は、30日間の一時ライセンスをリクエストすることも可能です。詳細については、[参照](https://purchase.groupdocs.com/temporary-license/)。"

    # items loop
    - question: "どのようなライセンスがありますか？"
      answer: "特定の開発者や企業のニーズに合わせた複数のライセンス形態をご用意しています。ライセンス形態は、開発者数、開発拠点数、エンドユーザーへの SDK/API の提供有無に応じて決定されます。また、製品の月間使用量に基づく従量課金型ライセンスも選択可能です。詳細は[こちら](https://purchase.groupdocs.com/pricing/parser/net/)をご覧ください。"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser ローコード ドキュメント パーサ API"
  description: "クラウドベースの REST API と SDK を使用して、任意のアプリケーションにドキュメント解析機能を組み込むことができます。"
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "cURL コマンドを使用した RESTful ドキュメント パーサ クラウド API で、幅広いサポート対象の一般的なファイル形式のドキュメントを解析します。"
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Microsoft .NET アプリケーションで、画像、テキスト、ドキュメント情報を抽出したり、ユーザー定義テンプレートで任意のドキュメントを解析したりできます。"
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Java 開発者向けのクラウド SDK で、ドキュメントを解析し、Java ベースのアプリケーション内でドキュメント情報とデータを抽出できます。"
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser ドキュメント パーサ ノーコード アプリ"
  description: "Web ベースのドキュメント パーサ アプリで、ブラウザー上で 50 以上の一般的なファイル形式からデータを直接抽出できます。"

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Word、Excel、PowerPoint、PDF など 50 以上のドキュメントタイプを解析できる無料のオンラインアプリ。"
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Web ブラウザーから直接 Word 文書を解析し、画像、テキスト、メタデータを抽出します。"
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "制限なく、あらゆるプラットフォームやデバイスで動作する無料の PDF 解析アプリ。"
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---