---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "ko/parser/java/extract/chm/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Java API를 통해 문서, 페이지 또는 페이지 영역에서 하이퍼링크 추출"
head_description: "GroupDocs.Parser Java API를 사용하면 개발자가 문서, 문서의 페이지 또는 Excel, PowerPoint, PDF, Outlook 등의 특정 페이지 영역에서 하이퍼링크를 추출할 수 있습니다."

############################# Header ############################
title: "문서, 페이지 또는 특정 페이지 영역에서 하이퍼링크를 추출하는 Java API "
description: "GroupDocs.Parser Java API를 사용하면 문서, 문서 페이지 또는 PDF, DOCX, PPTX, EML, MSG, XLS, XLSX, CSV, RTF, EPUB 등의 특정 페이지 영역에서 하이퍼링크를 추출할 수 있으므로 개발자가 작업을 쉽게 수행할 수 있습니다."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Java를 통해 다양한 문서에서 하이퍼링크 추출을 수행하는 방법은 무엇입니까?"
    content: |
       이 웹 페이지는 몇 줄의 Java 코드를 사용하여 다양한 유형의 문서, 문서 페이지 또는 페이지의 특정 영역에서 하이퍼링크를 구문 분석하고 추출하는 방법을 설명합니다. 하이퍼링크는 페이지나 웹 사이트 사이를 탐색하는 데 매우 유용할 수 있으며 전체 문서 또는 문서 내의 특정 부분, 그래픽, 사운드, 전자 메일 주소 등을 가리킬 수 있습니다. Java용 GroupDocs.Parser는 소프트웨어 개발자가 문서를 구문 분석하고 자체 Java 응용 프로그램 내에서 널리 사용되는 다양한 문서에서 메타데이터와 텍스트를 추출할 수 있도록 하는 매우 강력한 API입니다. Word(DOC, DOCX), PowerPoint(PPT, PPTX), Excel(XLS, XLSX), LibreOffice 형식과 같은 PDF, 이메일, 전자책, Microsoft Office 형식과 같은 다양한 문서 유형에서 텍스트 및 하이퍼링크를 추출하기 위한 몇 가지 고급 기능이 포함되어 있습니다. 그리고 더 많은.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "CHM 문서에서 하이퍼링크를 추출하는 방법"
      content_left: |
       GroupDocs.Parser Java에는 CHM 문서에서 하이퍼링크를 추출하는 기능이 포함되어 있습니다. 다음 Java 코드 예제는 CHM 문서에서 하이퍼링크를 추출하는 방법을 보여줍니다. 

      title_right: "Java를 통해 하이퍼링크 추출"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)의 인스턴스 생성
        * 문서가 하이퍼링크 추출을 지원하는지 확인
        * 문서에서 하이퍼링크 추출
        * [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) 메서드를 호출하여 전체 문서에서 모든 하이퍼링크를 추출합니다.
        * 하이퍼링크를 반복하고 하이퍼링크 URL 인쇄

      gisthash: "036de701f5f17a02dd2353ee547afd5b"
      gistfile: "extract_hyperlinks_form_documents.java"

    - title_left: "CHM 문서 페이지에서 하이퍼링크를 추출하는 방법"
      content_left: |
       GroupDocs.Parser .NET을 사용하면 소프트웨어 개발자가 몇 줄의 코드로 CHM 문서에서 하이퍼링크를 추출할 수 있습니다. 아래 C# .NET 코드는 CHM 문서 내 하이퍼링크 추출을 보여줍니다. 

      title_right: "Java를 통해 하이퍼링크 추출"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)의 인스턴스 생성
        * 문서가 하이퍼링크 추출을 지원하는지 확인
        * [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) 메서드를 호출하여 문서 정보를 가져옵니다.
        * 페이지를 반복하고 페이지 번호 인쇄
        * 문서에서 하이퍼링크 추출
        * [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) 메서드를 호출하여 전체 문서에서 모든 하이퍼링크를 추출합니다.
        * 하이퍼링크를 반복하고 하이퍼링크 URL 인쇄
     
      gisthash: "bcca6319f2287edb7295443c1def46ee"
      gistfile: "extract_hyperlinks_form_documents_page.java"
      
    - title_left: "CHM 문서 페이지 영역에서 하이퍼링크 추출"
      content_left: |
       GroupDocs.Parser Java API는 CHM 문서의 페이지 용이성에서 하이퍼링크를 추출하기 위한 완전한 지원을 제공했습니다. 다음 Java 코드는 프로그래머가 자체 Java 애플리케이션 내부의 CHM 문서 페이지 영역에서 하이퍼링크를 추출하는 방법을 보여줍니다.

      title_right: "Java를 사용하여 하이퍼링크를 추출하는 방법은 무엇입니까?"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)의 인스턴스 생성
        * 하이퍼링크 추출 지원 문서 확인
        * 하이퍼링크 추출에 사용되는 옵션 생성
        * [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) 메서드를 호출하여 전체 문서에서 모든 하이퍼링크를 추출합니다.
        * 하이퍼링크를 반복하고 하이퍼링크 URL 인쇄
     
      gisthash: "4aefff1fcc6733c0fc12b736d7e36711"
      gistfile: "hyperlinks_extraction_from_document_page_area.java"

    - title_left: "시스템 요구 사항"
      content_left: |
       Java용 GroupDocs.Parser는 모든 주요 플랫폼 및 운영 체제에서 지원됩니다. Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice 및 50개 이상의 기타 형식으로 문서를 생성할 수 있습니다. 전체 시스템 요구 사항 가이드를 보려면 아래 코드를 실행하기 전에 시스템 요구 사항을 방문하십시오. 시스템에 다음 전제 조건이 설치되어 있는지 확인하십시오.
         * 운영 체제: 마이크로소프트 윈도우, 리눅스, 맥OS
         * 자바 버전 지원: J2SE 7.0(1.7), J2SE 8.0(1.8) 이상
         * GroupDocs[Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)에서 최신 버전의 GroupDocs.Assembly Java API 다운로드
        
      title_right: "GroupDocs.Assembly를 사용하는 이유"
      content_right: |
        * 지원되는 문서에서 일반 텍스트를 추출합니다.
        * 목차 추출 지원
        * 형식이 지정된 텍스트, 메타데이터, 이미지, 컨테이너 및 첨부 파일을 추출합니다.
        * 사용자 정의 템플릿을 통한 문서 구문 분석.
        * 키워드 또는 정규식을 사용하여 텍스트를 검색합니다.
        * 구조화된 텍스트 추출 지원
        * 지원되는 일부 문서 형식의 목차를 추출합니다.
        * PDF 문서에서 양식 데이터를 구문 분석합니다.

demos:
    enable: true
        

more_formats:
    enable: true


back_to_top:
    enable: true
---