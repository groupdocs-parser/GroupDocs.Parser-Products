---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "ko/parser/net/extract/image/ods/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: ".NET을 통해 Excel, Word, PDF 및 기타 문서 또는 페이지에서 이미지 추출 "
head_description: "GroupDocs.Parser .NET API를 사용하면 소프트웨어 프로그래머가 .NET 앱 내에서 MS Excel, Word, PowerPoint, PDF 등과 같은 다양한 문서에서 이미지를 추출할 수 있습니다."

############################# Header ############################
title: "C#.NET API를 통해 PDF, DOCX, PPTX, MSG, XLSX 문서 및 페이지에서 이미지 추출"
description: "GroupDocs.Parser .NET API를 사용하면 프로그래머가 PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF 및 EPUB 문서 또는 문서의 페이지에서 이미지를 추출할 수 있습니다."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: ".NET을 통해 문서 또는 페이지 영역에서 이미지를 추출하는 방법은 무엇입니까?"
    content: |
       이미지는 말로 표현할 수 없는 방식으로 정보를 전달하는 데 사용될 수 있습니다. 이미지는 사용자의 관심을 끌고 어려운 개념을 쉽게 설명하는 데 도움이 됩니다. 때때로 문서, 저널을 읽거나 프리젠테이션에서 혜택을 보는 동안 우리는 종종 매혹적인 이미지를 발견하고 그것을 다운로드하고 싶었습니다. .NET용 GroupDocs.Parser는 사용자가 다양한 유형의 문서에서 이미지를 추출하고 PNG, JPEG, WebP, GIF, BMP 및 기타 형식으로 저장하는 유용한 응용 프로그램을 개발하는 데 도움이 되는 강력한 API입니다. API에는 PDF, 이메일, 전자책, Microsoft Office 형식과 같이 가장 일반적으로 사용되는 일부 파일 형식에서 텍스트 및 이미지 추출에 대한 지원이 포함되어 있습니다. Word(DOC, DOCX), PowerPoint(PPT, PPTX), Excel(XLS) , XLSX), LibreOffice 형식 등. API는 또한 문서 구문 분석, 일반 및 구조화된 텍스트 추출, 키워드로 텍스트 검색, 메타데이터 또는 이미지 추출, 컨테이너 및 첨부 파일 등을 완벽하게 지원합니다.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "C#을 통해 ODS 문서에서 이미지 추출 "
      content_left: |
       GroupDocs.Parser .NET API를 사용하면 소프트웨어 개발자가 ODS 문서에서 이미지를 추출할 수 있습니다. 다음 C# .NET 코드 예제는 ODS 문서 내에서 이미지를 추출하는 방법을 보여줍니다. 

      title_right: ".NET을 통해 이미지를 추출하는 방법"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 인스턴스 생성
        * 이미지 추출이 지원되는지 확인
        * 문서의 이미지 반복
        * [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) 메소드를 호출하여 전체 문서에서 모든 이미지를 추출합니다.
        * 모든 이미지 인쇄

      gisthash: "6bc9e8fea228c9e1b99425b338bb0f00"
      gistfile: "images_extraction_form_documents.cs"

    - title_left: "C#을 통해 ODS 문서 페이지에서 이미지 추출"
      content_left: |
       GroupDocs.Parser .NET을 사용하면 소프트웨어 개발자가 ODS 문서 페이지에서 이미지를 추출할 수 있습니다. 아래 C# .NET 코드는 ODS 문서 내에서 이미지 추출을 달성하는 방법을 보여줍니다.

      title_right: ".NET을 통해 파일 이미지 추출"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 인스턴스 생성
        * 이미지 추출 지원 문서 확인
        * [GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo)를 호출하여 문서 정보 가져오기
        * 존재하는 페이지에 대한 문서 확인
        * 페이지를 반복하고 페이지 번호 인쇄
        * [getImages(Int32)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/2) 메서드를 호출하여 전체 문서에서 모든 이미지를 추출합니다.
        * 이미지 반복 및 이미지 인쇄
     
      gisthash: "2000d476c202a688677f57a2fbd7ceab"
      gistfile: "images_extraction_form_documents_page.cs"
      
    - title_left: "ODS 문서 페이지 영역에서 이미지를 추출하는 방법"
      content_left: |
       GroupDocs.Parser .NET API는 몇 줄의 .NET 코드를 사용하여 ODS 문서에서 이미지 추출을 완벽하게 지원합니다. 다음 .NET 코드 예제는 ODS 문서 페이지 영역에서 이미지 추출을 수행하는 방법을 보여줍니다.

      title_right: ".NET을 통해 파일 페이지 영역에서 이미지 추출"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 인스턴스 생성
        * 이미지 추출에 사용할 수 있는 옵션 생성 사용자 지정
        * 이미지 추출 지원 문서 확인
        * 사용자 정의를 사용하여 [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) 메소드를 호출하여 페이지의 왼쪽 상단 모서리에서 이미지 추출 옵션.
        * 이미지 반복 및 이미지 인쇄
     
      gisthash: "ea6c6b8fa613384f1e7f637dabcb7bca"
      gistfile: "extract_images_form_documents_page_area.cs"

    - title_left: "C# .NET을 통해 이미지를 추출하고 파일로 저장하는 방법"
      content_left: |
       GroupDocs.Parser .NET API를 사용하면 소프트웨어 개발자가 문서에서 이미지를 추출하고 몇 줄의 .NET 코드로 파일에 저장할 수 있습니다. 다음 예는 ODS 문서에서 이미지 추출을 수행하고 이미지 내용을 파일에 저장하는 방법을 보여줍니다.

      title_right: ".NET을 통해 파일에 이미지 저장"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 클래스의 인스턴스 생성
        * 문서에서 이미지 추출
        * [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) 메소드를 호출하여 전체 문서에서 모든 이미지를 추출합니다.
        * 이미지 추출 지원 문서 확인
        * 사용자 정의를 사용하여 [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) 메소드를 호출하여 페이지의 왼쪽 상단 모서리에서 이미지 추출 옵션.
        * PNG 형식으로 이미지를 저장하기 위한 옵션 생성
        * 이미지를 반복하고 이미지를 PNG 파일로 저장
     
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