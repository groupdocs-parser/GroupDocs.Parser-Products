---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "ja/parser/net/extract/image/odt/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: ".NETを介してExcel、Word、PDF、その他のドキュメントまたはページから画像を抽出する "
head_description: "GroupDocs.Parser .NET APIを使用すると、ソフトウェアプログラマーは、.NETアプリ内のMS Excel、Word、PowerPoint、PDFなどのさまざまなドキュメントから画像を抽出できます。"

############################# Header ############################
title: "C＃.NET APIを介してPDF、DOCX、PPTX、MSG、XLSXドキュメントおよびページから画像を抽出する"
description: "GroupDocs.Parser .NET APIを使用すると、プログラマーはPDF、DOC、DOCX、PPT、PPTX、EML、MSG、XLS、XLSX、CSV、ODT、RTF、EPUBドキュメントまたはドキュメントのページから画像を抽出できます。"

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: ".NETを介してドキュメントまたはページ領域から画像を抽出する方法は？"
    content: |
       画像は、言葉では表現できないような方法で情報を配信するために使用できます。 画像は、ユーザーの注意を引き付け、難しい概念を簡単に説明するのに役立ちます。 文書やジャーナルを読んだり、プレゼンテーションの恩恵を受けたりしているときに、魅力的な画像を見つけてダウンロードしたいと思うことがよくありました。 GroupDocs.Parser for .NETは、ユーザーがさまざまな種類のドキュメントから画像を抽出し、PNG、JPEG、WebP、GIF、BMPなどの形式で保存するための便利なアプリケーションを開発するのに役立つ強力なAPIです。 APIには、PDF、電子メール、電子ブック、Microsoft Office形式（Word（DOC、DOCX）、PowerPoint（PPT、PPTX）、Excel（XLS））など、最も一般的に使用されるファイル形式からのテキストおよび画像抽出のサポートが含まれています。 、XLSX）、LibreOffice形式など。 APIは、ドキュメントの解析、プレーンテキストと構造化テキストの抽出、キーワードによるテキスト検索、メタデータまたは画像の抽出、コンテナ、添付ファイルなどを完全にサポートします。

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "C＃を介してODTドキュメントから画像を抽出する "
      content_left: |
       GroupDocs.Parser .NET APIを使用すると、ソフトウェア開発者はODTドキュメントから画像を抽出できます。 次のC＃.NETコード例は、ODTドキュメント内の画像を抽出する方法を示しています。 

      title_right: ".NETを介して画像を抽出する方法"
      content_right: |
        * [パーサー](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) クラスのインスタンスを作成します
        * 画像抽出がサポートされているかどうかを確認します
        * ドキュメント内の画像を繰り返します
        * [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) メソッドを呼び出して、ドキュメント全体からすべての画像を抽出します。
        * すべての画像を印刷する

      gisthash: "6bc9e8fea228c9e1b99425b338bb0f00"
      gistfile: "images_extraction_form_documents.cs"

    - title_left: "ODTドキュメントのページからのC＃による画像の抽出"
      content_left: |
       GroupDocs.Parser .NETを使用すると、ソフトウェア開発者はODTドキュメントのページから画像を抽出できます。 以下のC＃.NETコードは、ODTドキュメント内で画像抽出を実現する方法を示しています。

      title_right: ".NETを介してファイルイメージを抽出する"
      content_right: |
        * [パーサー](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) クラスのインスタンスを作成します  
        * 画像抽出のサポートについてはドキュメントを確認してください
        * [GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo) を呼び出してドキュメント情報を取得します
        * 既存のページのドキュメントを確認してください
        * ページを繰り返し、ページ番号を印刷する
        * [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) メソッドを呼び出して、ドキュメント全体からすべての画像を抽出します。
        * 画像を繰り返し、画像を印刷します
     
      gisthash: "2000d476c202a688677f57a2fbd7ceab"
      gistfile: "images_extraction_form_documents_page.cs"
      
    - title_left: "ODTドキュメントページ領域から画像を抽出する方法"
      content_left: |
       GroupDocs.Parser .NET APIは、数行の.NETコードを使用して、ODTドキュメントからの画像の抽出を完全にサポートします。 次の.NETコード例は、ODTドキュメントページ領域から画像を抽出する方法を示しています。

      title_right: ".NETを介してファイルページ領域から画像を抽出する"
      content_right: |
        * [パーサー](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) クラスのインスタンスを作成します  
        * 画像抽出に使用できるオプションの作成をカスタマイズする
        * 画像抽出のサポートについてはドキュメントを確認してください
        * [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) メソッドを呼び出して、ページの左上隅から画像を抽出します。 オプション。
        * 画像を繰り返し、画像を印刷します
     
      gisthash: "ea6c6b8fa613384f1e7f637dabcb7bca"
      gistfile: "extract_images_form_documents_page_area.cs"

    - title_left: "C＃.NETを介して画像を抽出してファイルに保存する方法」"
      content_left: |
       GroupDocs.Parser .NET APIを使用すると、ソフトウェア開発者はドキュメントから画像を抽出し、わずか数行の.NETコードでファイルに保存できます。 次の例は、ODTドキュメントから画像を抽出し、画像の内容をファイルに保存する方法を示しています。

      title_right: "Save Images to a File via .NET"
      content_right: |
        * [パーサー](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) クラスのインスタンスを作成します  
        * ドキュメントから画像を抽出する
        * 画像抽出のサポートについてはドキュメントを確認してください
        * [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) メソッドを呼び出して、ページの左上隅から画像を抽出します。 オプション。
        * PNG形式で画像を保存するためのオプション作成
        * 画像を繰り返し、画像をPNGファイルに保存します
     
      gisthash: "bc242d5ff4050564fa275858ffa7d34f"
      gistfile: "images_saving_to_files.cs"

    - title_left: "システム要求"
      content_left: |
       GroupDocs.Parser for .NETは、すべての主要なプラットフォームとオペレーティングシステムで完全にサポートされています。 完全なシステム要件ガイドについては、[システム要件]（hhttps：//docs.groupdocs.com/parser/net/system-requirements/）にアクセスしてください。以下のコードを実行する前に、次の前提条件がインストールされていることを確認してください。 システム：
        * オペレーティングシステム：Microsoft Windows、Linux、MacOS
        * 開発環境：Visual Studio、Xamarin、MonoDevelopなど
        * フレームワーク：.NETフレームワーク、.NET標準、.NETコア、モノラル
        * [NuGet](https://www.nuget.org/packages/GroupDocs.parser/)から最新バージョンのGroupDocs.Parser.NETAPIを入手します。
        
      title_right: "GroupDocs.Parserを使用する理由"
      content_right: |
        * サポートされているドキュメントからのプレーンテキスト抽出のサポート
        * ユーザー定義のテンプレートを介して解析するドキュメント。
        * 構造化テキスト抽出を完全にサポート
        * キーワードおよび正規表現によるテキスト検索
        * フォーマットされたテキスト、メタデータ、画像、コンテナ、および添付ファイルを抽出します。
        * サポートされている一部のドキュメント形式の目次を抽出します。
        * PDFドキュメントからフォームデータを解析します。
        * ドキュメントからハイパーリンクを抽出します

demos:
    enable: true
        

more_formats:
    enable: true


back_to_top:
    enable: true
---