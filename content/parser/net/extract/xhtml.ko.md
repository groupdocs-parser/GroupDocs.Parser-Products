---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "ko/parser/net/extract/xhtml/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "문서, 페이지 또는 페이지 영역에서 하이퍼링크를 구문 분석하고 추출하는 .NET API"
head_description: "GroupDocs.Parser .NET API를 사용하면 소프트웨어 프로그래머가 문서, 페이지 또는 PDF, DOCX, XLSX, CSV, PPTX, EML, MSG, EPUB 등의 페이지 영역에서 하이퍼링크를 추출할 수 있습니다."

############################# Header ############################
title: "C#/VB.NET API를 통해 문서, 페이지 또는 특정 페이지 영역에서 하이퍼링크 추출"
description: "GroupDocs.Parser .NET API를 사용하면 소프트웨어 개발자가 문서, 페이지 또는 PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF, EPUB 및 기타 여러 페이지 영역에서 하이퍼링크를 구문 분석 및 추출할 수 있습니다. 서류."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: ".NET을 통해 문서 또는 페이지에서 하이퍼링크를 구문 분석하고 추출하는 방법은 무엇입니까?"
    content: |
       하이퍼링크는 전체 문서 또는 문서 내의 특정 부분을 가리키는 텍스트 또는 이미지 또는 아이콘입니다. 하이퍼링크를 사용하면 사용자가 웹 페이지나 문서로 이동할 수 있습니다. 문서에서 하이퍼링크를 추출하여 외부 문서나 웹 페이지에 액세스하는 데 사용하는 경우가 많습니다. GroupDocs.Parser .NET API는 텍스트 및 메타데이터 추출 솔루션을 구현하기 위한 완전한 기능을 제공하는 매력적인 문서 텍스트 추출 API입니다. PDF, 이메일, 전자책, Microsoft Office 형식(Word(DOC, DOCX), PowerPoint(PPT, PPTX), Excel(XLS, XLSX), LibreOffice 형식 등)에서 텍스트 및 하이퍼링크 추출을 지원합니다. 문서 구문 분석, 일반 및 구조화된 텍스트 추출, 키워드로 텍스트 검색, 메타데이터 또는 이미지 추출, 컨테이너 및 첨부 파일 등을 위한 여러 고급 기능을 지원합니다.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: ".NET을 통해 XHTML 문서에서 하이퍼링크 추출"
      content_left: |
       GroupDocs.Parser .NET은 XHTML 문서에서 하이퍼링크 추출을 완벽하게 지원합니다. 다음 C# .NET 코드 예제는 XHTML 문서 내에서 하이퍼링크를 추출하는 방법을 보여줍니다.

      title_right: "하이퍼링크를 추출하는 방법"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 인스턴스 생성
        * 하이퍼링크 추출 지원 문서 확인
        * 문서에서 하이퍼링크 추출
        * [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) 메서드를 호출하여 전체 문서에서 모든 하이퍼링크를 추출합니다.
        * 하이퍼링크를 반복하고 하이퍼링크 URL 인쇄

      gisthash: "35be3a09e0135c65be790c42c5c86d37"
      gistfile: "Extract_hyperlinks_form_documents.cs"

    - title_left: "XHTML 문서 페이지에서 하이퍼링크 추출"
      content_left: |
       GroupDocs.Parser .NET을 사용하면 소프트웨어 개발자가 몇 줄의 코드로 XHTML 문서에서 하이퍼링크를 추출할 수 있습니다. 아래 C# .NET 코드는 XHTML 문서 내 하이퍼링크 추출을 보여줍니다.

      title_right: ".NET을 통해 하이퍼링크 추출"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 인스턴스 생성
        * 하이퍼링크 추출 지원 문서 확인
        * [GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo)를 호출하여 문서 정보 가져오기
        * 페이지를 반복하고 페이지 번호 인쇄
        * 문서에서 하이퍼링크 추출
        * [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) 메서드를 호출하여 전체 문서에서 모든 하이퍼링크를 추출합니다.
        * 하이퍼링크를 반복하고 하이퍼링크 URL 인쇄
     
      gisthash: "e71f8e39ba36ebf97034dfbf6fceeec1"
      gistfile: "hyperlinks_extraction_form_documents_page.cs"
      
    - title_left: "XHTML 문서 페이지 영역에서 하이퍼링크 추출"
      content_left: |
       GroupDocs.Parser .NET API는 XHTML 문서에서 쉽게 하이퍼링크 추출을 완벽하게 지원합니다. 다음 .NET 코드 예제는 XHTML 문서 페이지 영역에서 하이퍼링크를 추출하는 방법을 보여줍니다.

      title_right: ".NET을 사용하여 하이퍼링크를 추출하는 방법"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser) 인스턴스 생성
        * 하이퍼링크 추출 지원 문서 확인
        * 하이퍼링크 추출에 사용되는 옵션 생성
        * [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/gethyperlinks/methods/1) 메서드를 호출하여 문서 페이지에서 하이퍼링크를 추출합니다.
        * 하이퍼링크를 반복하고 하이퍼링크 URL 인쇄
     
      gisthash: "eefbede6f391ea44ddb6901edb353950"
      gistfile: "hyperlinks_extraction_from__documents_page_area.cs"

    - title_left: "시스템 요구 사항"
      content_left: |
       GroupDocs.Assembly .NET API는 모든 주요 플랫폼 및 운영 체제에서 지원됩니다. 전체 시스템 요구 사항 가이드를 보려면 [시스템 요구 사항](hhttps://docs.groupdocs.com/parser/net/system-requirements/)을 방문하십시오. 아래 코드를 실행하기 전에 다음 전제 조건이 컴퓨터에 설치되어 있는지 확인하십시오. 체계:
        * 운영 체제: 마이크로소프트 윈도우, 리눅스, 맥OS
        * 개발 환경: Visual Studio, Xamarin, MonoDevelop 등
        * 프레임워크: .NET Framework, .NET Standard, .NET Core, Mono
        * [NuGet](https://www.nuget.org/packages/GroupDocs.parser/)에서 최신 버전의 GroupDocs.Assembly .NET API 가져오기
        
      title_right: "GroupDocs.Assembly를 사용하는 이유"
      content_right: |
        * 지원되는 모든 문서에서 일반 텍스트 추출 지원
        * 사용자 정의 템플릿을 통한 문서 구문 분석.
        * 구조화된 텍스트 추출을 완벽하게 지원
        * 키워드 및 정규식을 통한 텍스트 검색
        * 형식이 지정된 텍스트, 메타데이터, 이미지, 컨테이너 및 첨부 파일을 추출합니다.
        * 지원되는 일부 문서 형식의 목차를 추출합니다.
        * PDF 문서에서 양식 데이터를 구문 분석합니다.
        * 문서에서 하이퍼링크 추출

demos:
    enable: true
        

more_formats:
    enable: true


back_to_top:
    enable: true
---