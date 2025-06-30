


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:53
draft: false
lang: ja
format: Pdf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "C#アプリでPDFファイルからデータを解析する"
head_description: "GroupDocs.Parserを使用して、C#でPDFファイルからテキスト、画像、テーブル、その他のデータを抽出します。サードパーティ製ツールに依存することなく。"

############################# Header ############################
title: "C#を使用してPDF文書を解析する" 
description: "GroupDocs.Parserを使用して、PDF、Word、Excel、および画像ファイルからテキスト、メタデータ、テーブル、画像を効率的に抽出します。.NETプロジェクトで実施できます。"
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "無料トライアルをダウンロード"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for .NET APIについて"
    link: "/parser/net/"
    link_title: "詳細はこちら"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/)は、.NET開発者向けに設計された機能豊富な文書解析APIです。PDF、DOCX、XLSX、PPTXなどのポピュラーなフォーマットから、プレーンおよび構造化テキスト、メタデータ、画像、テーブル、バーコードを抽出することができます。すべて追加のソフトウェア依存関係なしで行えます。

############################# Steps ############################
steps:
    enable: true
    title: "C#でPdfからデータを抽出する手順"
    content: |
      [GroupDocs.Parser](/parser/net/)を使用して、.NETアプリでPDF文書からコンテンツを解析する手順は次のとおりです：
      
      1. Parserインスタンスを使用してPDF文書を読み込む。
      2. テキスト、テーブル、メタデータなどの必要なコンテンツを抽出する。
      3. 抽出したデータが有効であることを確認する。
      4. 解析された出力を下流処理、自動化、またはビジネスシステムで使用する。
   
    code:
      platform: "net"
      copy_title: "コピー"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "クリックしてコピー"
        copy_done: "コピーしました"
      links:
        #  loop
        - title: "さらなる例"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "ドキュメンテーション"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Parserを使って文書を読み込む
        using (Parser parser = new Parser("input.pdf")) {

            // ファイルからすべてのテキストコンテンツを抽出する
            using (TextReader reader = parser.GetText()) 
            {
                // テキストが利用できない場合、結果はnullになります
                // 抽出したテキストをアプリケーションで使用する
                Console.WriteLine(reader == null ? 
                    "このフォーマットではテキスト抽出がサポートされていません" : reader.ReadToEnd());
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "包括的な文書解析機能"
  description: "GroupDocs.Parserは、単なるテキスト読み込み以上のことができます—バーコード抽出、画像解析、メタデータアクセス、構造化データ処理をサポートし、高度な自動化とデータ分析を実現します。"
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "文書コンテンツ抽出と解析機能"
  features:
    # feature loop
    - title: "多様なファイルコンテンツタイプのサポート"
      content: "PDF、Word、Excel、HTMLなどの文書フォーマットからテキスト、画像、テーブル、フィールドを抽出します。"

    # feature loop
    - title: "スキャンされたファイルとデジタルファイルの両方に対応"
      content: "スキャンされた文書とデジタルファイルの両方からデータを解析し、OCRおよびレイアウトに配慮した抽出をサポートします。"

    # feature loop
    - title: "柔軟な抽出パラメータ"
      content: "ページ範囲の選択、領域ターゲティング、フィールド検出テンプレートなど、柔軟なオプションで解析ロジックを調整します。"
      
  code_samples:
    # code sample loop
    - title: "テンプレートを使用してPDFを解析する方法"
      content: |
        この例では、GroupDocs.Parserを使用して、定義済みの解析テンプレートからPDFから構造化データを抽出する方法を示します。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Parserクラスを使用してPDFファイルを読み込む
        using (Parser parser = new Parser("input.pdf"))
        {
            // テンプレートごとに文書を解析する
            DocumentData data = parser.ParseByTemplate(GetTemplate());

            // フォーム抽出がサポートされているか確認する
            if (data == null)
            {
                return;
            }

            // 取得したフィールドを処理する
            for (int i = 0; i < data.Count; i++)
            {
                Console.Write(data[i].Name + ": ");
                PageTextArea area = data[i].PageArea as PageTextArea;
                Console.WriteLine(area == null ? "Not a template field" : area.Text);
            }
        }

        private static Template GetTemplate()
        {
            // '詳細'テーブルの検出パラメータを作成する
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(templateItems);
            return template;
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "始める準備はできましたか？"
  description: "GroupDocs.Parserの機能を無料で試すか、ライセンスをリクエストしてください"
  items:
    #  loop
    - title: "Nugetのダウンロード"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "ライセンス情報"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "データ抽出のためにサポートされているフォーマット"
    exclude: "PDF"
    description: "GroupDocs.Parserは、広範な文書および画像フォーマットでの解析を可能にします。データ抽出ワークフローに一般的に使用されるサポートされるファイルタイプを確認してください。"
    items: 
        # format loop 1
        - name: "PDFを解析する"
          format: "PDF"
          link: "/parser/net/parse/pdf/"
          description: "(ポータブル文書形式)"
          
        # format loop 2
        - name: "DOCXを解析する"
          format: "DOCX"
          link: "/parser/net/parse/docx/"
          description: "(Office 2007+ Word文書)"
          
        # format loop 3
        - name: "PPTXを解析する"
          format: "PPTX"
          link: "/parser/net/parse/pptx/"
          description: "(Open XMLプレゼンテーション形式)"
          
        # format loop 4
        - name: "XLSXを解析する"
          format: "XLSX"
          link: "/parser/net/parse/xlsx/"
          description: "(Open XMLワークブック)"
          
        # format loop 5
        - name: "TXTを解析する"
          format: "TXT"
          link: "/parser/net/parse/txt/"
          description: "(テキストファイル)"
          
        # format loop 6
        - name: "RTFを解析する"
          format: "RTF"
          link: "/parser/net/parse/rtf/"
          description: "(リッチテキスト形式)"
          
        # format loop 7
        - name: "XMLを解析する"
          format: "XML"
          link: "/parser/net/parse/xml/"
          description: "(拡張可能なマークアップ言語)"
          
        # format loop 8
        - name: "EPUBを解析する"
          format: "EPUB"
          link: "/parser/net/parse/epub/"
          description: "(オープンeBookファイル)"
         
          

---