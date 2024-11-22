---
############################# Static ############################
layout: "family"
date:  2024-02-13T17:01:03
draft: false

product: "Parser"
product_tag: "parser"

lang: ja

############################# Head ############################
head_title: ".NET、Java、クラウド API およびオンライン ドキュメント パーサー アプリ"
head_description: ".NET、Java、およびクラウドベースのアプリケーション向けのオールインワンの文書解析ソリューションを入手します。シンプルなドラッグ アンド ドロップ機能を使用してオンラインでドキュメント形式からデータを抽出します"

############################# Header ############################
title: "文書解析ソリューション"
description: |
  さまざまなファイル形式からデータを抽出するための堅牢な API。

  最小限のコーディング作業でドキュメントを解析します。

  解析結果をカスタマイズします。

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "プラットフォームを選択してください"
  title: "プラットフォームの独立性"
  description: "GroupDocs.Parser ライブラリは、次のオペレーティング システムとフレームワークをサポートしています。"
  details_link_title: "もっと詳しく知る"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser のために .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    .NET Framework 4.6.2 or higher
                    .NET Core 2.0 or higher
                    .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    Microsoft Visual Studio
                    JetBrains Rider
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser のために Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    Java 8 or higher
                    Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    IntelliJ IDEA
                    Eclipse
                    NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser の概要"
  description: "PDF、Word、Excel などのデータ解析用の API。"

  items:
    # items loop
    - icon: "text"
      title: "テキストを抽出する"
      content: "さまざまなファイル形式からテキスト情報を抽出します。"

    # items loop
    - icon: "image"
      title: "画像の抽出"
      content: "さまざまなソースからビジュアル コンテンツを取得します。"

    # items loop
    - icon: "template"
      title: "テンプレートによるデータの解析"
      content: "カスタム テンプレートを作成し、それを利用して特定の情報を解析します。"

    # items loop
    - icon: "pdf"
      title: "PDF フォームを解析する"
      content: "PDF フォームは、ユーザー操作のための入力可能なフィールドを備えたデジタル ドキュメントです。"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser コードサンプル"
  description: "C# および Java での典型的な GroupDocs.Parser 操作のいくつかの使用例。"

  items:
    # items loop
    - title: "PDF ドキュメントからテキストを抽出する方法"
      content: "GroupDocs.Parser API を使用すると、C# 開発者はいくつかの簡単な手順を実装することで、ドキュメントからテキストを簡単に抽出できます。"
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              <pre>
              // Create an instance of Parser class
              using (var parser = new Parser(fileName))
              {
                  // Extract a text into the reader
                  using (var textReader = parser.GetText())
                  {
                      // Print a text from the document
                      Console.WriteLine(textReader?.ReadToEnd());
                  }
              }
              </pre>
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              <pre>
              // Create an instance of Parser class
              try (Parser parser = new Parser(fileName)) {
                  // Extract a text into the reader
                  try (TextReader reader = parser.getText()) {
                      // Print a text from the document
                      System.out.println(reader == null 
                              ? "" 
                              : reader.readToEnd());
                  }
              }
              <pre>

############################# Supported Formats ###############################
formats:
  enable: true
  title: "50以上のファイル形式をサポート"
  description: "GroupDocs.Parser により、さまざまな形式ファミリー内でのパーサー操作が可能になります。"

############################# Metrics ###############################
metrics:
  enable: false
  title: "詳細な指標と統計的洞察"
  description: "当社の主要な数値を徹底的に分析し、当社の業績、影響力、拡大に関する包括的な指標と統計的洞察を提供します。"

  items:
    # items loop
    - number: "50+"
      title: "サポートされている形式"
      content: "API は、最も広く使用されている 50 以上のファイルおよびドキュメント形式に対応しています。"

    # items loop
    - number: "700k"
      title: "NuGet ダウンロード"
      content: "GroupDocs.Parser for .NET は、NuGet パッケージ マネージャーを通じて 80 万件を超えるダウンロードを受け取りました。"

    # items loop
    - number: "15k"
      title: "Mavenのダウンロード"
      content: "GroupDocs.Parser for Java は、Maven リポジトリからの累計ダウンロード数が 15,000 を超えています。"


############################# Customers ###############################
customers:
  enable: true
  title: "幸せなお客様"
  description: "GroupDocs ライブラリは、世界中の世界的に有名な著名なブランドによって採用されています。"

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
  title: "始める準備はできていますか?"
  description: "お使いのプラットフォームで GroupDocs.Parser 機能を無料でお試しください"

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
    - question: "GroupDocs.Parser ライブラリでは、ドキュメントを操作するために他のサードパーティ ソフトウェアが必要ですか?"
      answer: "GroupDocs.Parser では、Adobe Acrobat、Microsoft Office などの外部ソフトウェアをインストールする必要はありません。"

    # items loop
    - question: "GroupDocs.Parser ライブラリを購入する前に試すことはできますか?"
      answer: "はい、ライセンスを購入せずに GroupDocs.Parser を試すことができます。ライセンスなしでインストールすると、ライブラリは試用モードで動作します。このモードでは、結果のドキュメントにトライアルバッジが追加され、最初の 3 ページがトリミングされます。試用版の制限なしで GroupDocs.Parser をテストしたい場合は、30 日間の一時ライセンスをリクエストすることもできます。詳細については、を参照してください。 [purchase.groupdocs.com/temporary-license/](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "どのようなライセンスを持っていますか?"
      answer: "特定の開発者や企業のニーズに合わせて、いくつかのライセンス タイプを提供しています。ライセンスの種類は、開発者の数、開発者サイトの場所の数、および SDK/API をエンド顧客に提供する必要があるかどうかによって異なります。あるいは、製品の毎月の使用量に基づいて従量制ライセンスを選択することもできます。詳細については、こちらをご覧ください [purchase.groupdocs.com/policies/](https://purchase.groupdocs.com/policies/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser ローコード API"
  description: "クラウドベースの REST API を使用して、ドキュメント パーサー機能を任意のアプリケーションに組み込みます。"
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "RESTサポートされている一般的なファイル形式の幅広いドキュメントを解析するためのフル ドキュメント パーサー Cloud API 用の cURL コマンド。"
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Microsoft .NET アプリケーションのユーザー定義テンプレートによって、画像、テキスト、ドキュメント情報を抽出したり、ドキュメントを解析したりすることもできます。"
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Java 開発者がドキュメントを解析し、Java ベースのアプリケーション内のドキュメント情報とデータを抽出するための Cloud SDK。"
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser NoCode アプリ"
  description: "50 を超える一般的なファイル形式の解析をブラウザで直接実行できる Web ベースのアプリケーション。"

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Word、Excel、PowerPoint、PDF など 30 種類以上のドキュメント タイプを解析する無料のオンライン アプリ。"
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Web ブラウザから直接 Word ドキュメントを解析して、画像、テキスト、またはメタデータを抽出します。"
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "無料の PDF 解析アプリは、あらゆるプラットフォームやデバイスで制限なく動作します。"
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"     


---