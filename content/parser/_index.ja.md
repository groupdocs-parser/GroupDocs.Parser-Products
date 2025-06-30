---
############################# Static ############################
layout: "family"
date:  2025-06-30T10:26:00
draft: false

product: "Parser"
product_tag: "parser"

lang: ja

############################# Head ############################
head_title: ".NET、Java、クラウドAPIとオンライン文書パーサーアプリ"
head_description: "すべてを兼ね備えた文書解析ソリューションを、.NET、Java、そしてクラウドベースのアプリケーション用に提供します。シンプルなドラッグ＆ドロップ機能でオンライン文書フォーマットからデータを抽出します。"

############################# Header ############################
title: "文書解析ソリューション"
description:  |
  様々なファイル形式からデータを抽出するための堅牢なAPI。

  最小限のコーディングで文書を解析します。

  解析結果をカスタマイズします。

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "プラットフォームを選択してください"
  title: "プラットフォームの独立性"
  description: "GroupDocs.Parser ライブラリは、次のオペレーティングシステムとフレームワークをサポートしています："
  details_link_title: "詳細を学ぶ"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser .NET 
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
      description: GroupDocs.Parser Java
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

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser 概要"
  description: "PDF、Word、Excel などのデータ解析用API"

  items:
    # items loop
    - icon: "text"
      title: "テキストの抽出"
      content: "様々なファイル形式からテキスト情報を抽出します"

    # items loop
    - icon: "image"
      title: "画像の抽出"
      content: "多様なソースから視覚コンテンツを取り出します"

    # items loop
    - icon: "template"
      title: "テンプレートによるデータ解析"
      content: "カスタムテンプレートを作成し、特定の情報を解析するために利用します"

    # items loop
    - icon: "pdf"
      title: "PDFフォームの解析"
      content: "PDFフォームはユーザーとの対話のために入力可能なフィールドを含むデジタル文書です"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser コードサンプル"
  description: "C# と Java における典型的な GroupDocs.Parser 操作のいくつかのユースケース"

  items:
    # items loop
    - title: "PDF文書からテキストを抽出する方法"
      content: "GroupDocs.Parser APIを使用すると、いくつかのステップを実装することで文書からテキストを抽出できます。"
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
                    <code class="language-csharp" data-lang="csharp">

                        // 希望するファイルを渡して Parser クラスのインスタンスを作成します。
                        using (var parser = new Parser("source.pdf"))
                        {
                            // テキストを抽出します。
                            using (var textReader = parser.GetText())
                            {
                                // 抽出したテキストを処理します。
                                Console.WriteLine(textReader?.ReadToEnd());
                            }
                        }     
                        
                    </code>

          # samples loop
          - language: "Java"
            color: "red"
            content: |
                    <code class="language-java" data-lang="java">

                        // 希望するファイルを渡して Parser クラスのインスタンスを作成します。
                        try (Parser parser = new Parser("source.pdf"))
                        {
                            // テキストを抽出します。
                            try (TextReader reader = parser.getText())
                            {
                                // 抽出したテキストを処理します。
                                System.out.println(reader == null 
                                        ? "" 
                                        : reader.readToEnd());
                            }
                        }  

                    </code>


############################# Supported Formats ###############################
formats:
  enable: true
  title: "50以上のファイル形式をサポート"
  description: "GroupDocs.Parser は様々な形式ファミリー内でのパーサー操作が可能です"

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser での成果"
  description: "ライブラリの業績に関する重要な指標を発見します"

  items:
    # items loop
    - number: "50+"
      title: "サポートされている形式"
      content: "GroupDocs.Parser は50以上の人気ファイル形式で操作をサポートします。"

    # items loop
    - number: "1600k"
      title: "NuGetダウンロード"
      content: "GroupDocs.Parser の .NET NuGet パッケージは1,600,000回以上ダウンロードされました。"

    # items loop
    - number: "18k"
      title: "Mavenダウンロード"
      content: "GroupDocs.Parser はMavenで18,000回ダウンロードされています。強力なJava解析機能。"

    # items loop
    - number: "140+"
      title: "満足している顧客"
      content: "有名企業や個別開発者が革新的なソリューションを構築するために GroupDocs の製品を選択しています。"


############################# Customers ###############################
customers:
  enable: true
  title: "私たちの満足している顧客"
  description: "GroupDocs のライブラリは、世界中の著名なブランドに利用されています。"

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
  title: "始める準備はできましたか？"
  description: "お使いのプラットフォームで GroupDocs.Parser の機能を無料で試してみてください。"

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
  description: "よくある質問への回答。"

  items:
    # items loop
    - question: "GroupDocs.Parser ライブラリは文書を操作するために他のサードパーティソフトウェアを必要としますか？"
      answer: "GroupDocs.Parser はAdobe Acrobat、Microsoft Office、または他の外部ソフトウェアのインストールを必要としません。"

    # items loop
    - question: "GroupDocs.Parser ライブラリを購入前に試すことはできますか？"
      answer: "はい、ライセンスを購入せずに GroupDocs.Parser を試すことができます。ライセンスなしでインストールされた場合、ライブラリは試用モードで動作します。このモードでは、試用バッジが生成された文書に追加され、最初の3ページに制限されます。試用版の制限なしで GroupDocs.Parser をテストしたい場合は、30日間の一時ライセンスをリクエストすることもできます。詳細については、[こちらをご覧ください](https://purchase.groupdocs.com/temporary-license/)。"

    # items loop
    - question: "どのようなライセンスがありますか？"
      answer: "特定の開発者や企業のニーズに合った複数のライセンスタイプを提供しています。ライセンスタイプは、開発者の数、開発者のサイトの数、エンド顧客へのSDK/APIの提供の必要性によって異なります。あるいは、製品の月次使用に基づく測定ライセンスを選択することもできます。詳細については、[こちら](https://purchase.groupdocs.com/pricing/parser/net/)をご覧ください。"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser 低コードAPI"
  description: "クラウドベースのREST APIを使用して、任意のアプリケーションに文書パーサー機能を組み込みます。"
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "広範囲にわたる人気ファイル形式に対応した文書パーサーのクラウドAPI用のcURLコマンド。"
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Microsoft .NETアプリケーション内で、画像、テキスト、文書情報を抽出したり、ユーザー定義テンプレートで任意の文書を解析します。"
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Javaデベロッパー向けのクラウドSDKを使用して、文書の解析、文書情報とデータを抽出します。"
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser ノーコードアプリ"
  description: "50以上の人気ファイル形式を直接ブラウザで解析できるウェブベースのアプリケーションです。"

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Word、Excel、PowerPoint、PDF、50以上の文書タイプを解析するための無料オンラインアプリ。"
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "ブラウザから直接Word文書を解析し、画像、テキスト、メタデータを抽出します。"
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "プラットフォームやデバイスに関係なく動作する無料のPDFパースアプリ。"
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---