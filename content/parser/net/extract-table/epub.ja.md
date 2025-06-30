


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:40
draft: false
lang: ja
format: Epub
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "C#アプリからEPUBファイルのテーブルを抽出"
head_description: "GroupDocs.Parserを使用して、C#アプリケーション内のEPUBファイルから構造化されたテーブルデータを特別な依存関係なしに位置特定し、抽出します。"

############################# Header ############################
title: "C#を使用してEPUBからテーブルを抽出" 
description: "GroupDocs.Parserを使用して、PDF、Word、Excelその他のファイル形式からテーブル構造を迅速に特定し、抽出します。あなたの.NETプロジェクトにおいて。"
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
       [GroupDocs.Parser](/parser/net/)は、.NET開発者向けに構築された包括的な文書解析APIです。PDF、DOCX、XLSX、PPTXなどの形式から、テキスト、テーブル、画像、ハイパーリンク、およびその他の構造化要素を正確に抽出できるように設計されています。サードパーティソフトウェアは必要ありません。

############################# Steps ############################
steps:
    enable: true
    title: "C#におけるEpubからテーブルを抽出する手順"
    content: |
      [GroupDocs.Parser](/parser/net/)を使用して、あなたの.NET環境内でEPUBファイルからテーブルを抽出するための手順を次の通りに従ってください：
      
      1. Parserインスタンスを初期化し、EPUB文書をロードします。
      2. 入力フォーマットがテーブル抽出をサポートしているか確認します。
      3. ファイルからテーブルコンテンツを抽出します。
      4. 出力のために構造化されたテーブルデータを使用します。
   
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
        // Parserを使用してテーブルデータを含む文書を開く
        using (Parser parser = new Parser("input.epub")) {

            // フォーマットがテーブル認識をサポートしているか確認する
            if (!parser.Features.Tables) {
                Console.WriteLine("テーブル解析をサポートしない文書を処理する");
                return;
            }

            // テーブル構造をどのように認識するかを定義する
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // テーブルデータの抽出パラメータを指定する
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  ファイルコンテンツからテーブルを抽出する
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  検出された各テーブルをループする
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "強力なデータ抽出機能"
  description: "テーブル解析に加え、GroupDocs.Parserは、文書自動化を促進するために、テキストブロック、画像、メタデータ、およびその他の構造化データを抽出できます。"
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "テーブル認識とコンテンツ抽出"
  features:
    # feature loop
    - title: "正確なマルチフォーマットテーブル検出"
      content: "DOCX、XLSX、PDF、HTMLなどのフォーマットから高精度でタブラー・データを抽出します。"

    # feature loop
    - title: "ファイルからテーブル構造を解析"
      content: "ドキュメントやスプレッドシートからフォーマットの損失なしに効率的にテーブルデータを取得します。"

    # feature loop
    - title: "柔軟なテーブル抽出設定"
      content: "レイアウト検出、列の整列、ヘッダー/フッターオプションを調整して出力を正確に制御します。"
      
  code_samples:
    # code sample loop
    - title: "Excelスプレッドシートからテーブルを抽出する方法"
      content: |
        このコードサンプルは、GroupDocs.Parserを使用してXLSXファイル内のテーブルデータを読み取り、イテレートする方法を示しています。
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Parser APIを使用してExcelファイルを開く
        using (Parser parser = new Parser("input.xlsx"))
        {
            // テーブルをファイルから抽出できない場合は終了する
            if (!parser.Features.Tables)
            {
                return;
            }

            // レイアウトルールを使用してタブラーコンテンツを特定する
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // テーブルの抽出パラメータを設定する
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // テーブル抽出操作を実行する
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // 検出された各テーブル構造をループする
            foreach (PageTableArea t in tables)
            {
                // テーブル内の各行をイテレートする
                for (int row = 0; row < t.RowCount; row++)
                {
                    // 各行のセルをループする
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // 現在のテーブルセルにアクセスする
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // 各セルのテキストコンテンツを表示する
                            Console.Write(cell.Text);
                            Console.Write(" | ");
                        }
                    }
                }
            }
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
    title: "テーブル抽出に対応したフォーマット"
    exclude: "EPUB"
    description: "GroupDocs.Parserは、さまざまな文書タイプからテーブルデータを抽出できます。以下は、構造化されたテーブル解析に最も頻繁に使用されるフォーマットです。"
    items: 
        # format loop 1
        - name: "PDFを解析する"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(ポータブル文書形式)"
          
        # format loop 2
        - name: "DOCXを解析する"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Office 2007+ Word文書)"
          
        # format loop 3
        - name: "PPTXを解析する"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Open XMLプレゼンテーション形式)"
          
        # format loop 4
        - name: "XLSXを解析する"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Open XMLワークブック)"
          
        # format loop 5
        - name: "TXTを解析する"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(テキストファイル)"
          
        # format loop 6
        - name: "RTFを解析する"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(リッチテキスト形式)"
          
        # format loop 7
        - name: "XMLを解析する"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(拡張可能なマークアップ言語)"
          
        # format loop 8
        - name: "EPUBを解析する"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(オープンeBookファイル)"
         
          

---