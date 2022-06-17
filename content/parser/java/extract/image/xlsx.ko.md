---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "ko/parser/java/extract/image/xlsx/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Java를 통해 Excel, Word, PDF 및 기타 문서에서 이미지를 추출하는 방법은 무엇입니까?"
head_description: "GroupDocs.Parser Java API를 사용하면 소프트웨어 개발자가 Java 앱 내부의 PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX 문서 및 이메일에서 이미지를 구문 분석하고 추출할 수 있습니다."

############################# Header ############################
title: "Excel, Word, PowerPoint, PDF 및 기타 문서 페이지에서 이미지를 구문 분석하고 추출하는 Java API"
description: "GroupDocs.Parser Java API를 사용하면 프로그래머가 PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF 및 EPUB 문서 또는 Java 응용 프로그램 내의 문서 페이지에서 이미지를 추출할 수 있습니다."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "Java API를 통해 문서 또는 특정 페이지에서 이미지를 추출하는 방법을 배우십니까?"
    content: |
       이미지는 수천 단어의 가치가 있으며 매력적인 콘텐츠를 만드는 동안 오늘날의 시각적 세계에서 무시할 수 없습니다. 이미지는 사용자의 관심을 끌 뿐만 아니라 정보 커뮤니케이션의 훌륭한 소스가 될 수 있습니다. 문서, 저널 또는 프리젠테이션에서 이미지를 가져와 다른 곳에서 사용하는 데 종종 필요합니다. Java용 GroupDocs.Parser는 소프트웨어 개발자와 프로그래머가 다양한 문서 유형에서 이미지 또는 기타 정보를 구문 분석하고 추출하기 위한 솔루션을 구축하는 데 도움이 되는 강력한 API입니다. 또한 PNG, JPEG, WebP, GIF, BMP 및 기타 형식으로 이미지 저장을 지원합니다. API에는 PDF, Microsoft Office 형식(Word(DOC, DOCX), PowerPoint(PPT, PPTX), Excel(XLS, XLSX), LibreOffice 형식, 이메일, 전자책 등)과 같은 일부 인기 있는 문서 형식에 대한 지원이 포함되어 있습니다. . 또한 문서 구문 분석, 일반 및 구조화된 텍스트 추출, 키워드로 텍스트 검색, 메타데이터 또는 이미지 추출, 컨테이너 및 첨부 파일 등과 관련된 일부 고급 기능에 대한 지원도 포함되어 있습니다.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "XLSX 문서에서 이미지를 추출하는 방법"
      content_left: |
       GroupDocs.Parser Java에는 XLSX 문서에서 이미지를 추출하는 기능이 포함되어 있습니다. 다음 Java 코드 예제는 XLSX 문서에서 이미지를 쉽게 추출하는 방법을 보여줍니다. 

      title_right: "Java를 통해 문서에서 이미지 가져오기"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)의 인스턴스 생성
        * 문서가 이미지 추출을 지원하는지 확인
        * [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) 메서드를 호출하여 전체 문서에서 모든 이미지를 추출합니다.
        * 문서에서 모든 이미지 추출
        * 이미지를 반복하고 이미지 유형 인쇄

      gisthash: "b13e690d2593f92081abd99948363e06"
      gistfile: "extract_images_form_documents.java"

    - title_left: "XLSX 문서 페이지에서 이미지 추출"
      content_left: |
       GroupDocs.Parser Java API를 사용하면 소프트웨어 개발자가 몇 줄의 코드로 XLSX 문서에서 이미지를 추출할 수 있습니다. 아래 Java 코드는 XLSX 문서에서 이미지 추출을 보여줍니다.

      title_right: "Java를 통해 파일 이미지를 추출하는 방법"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)의 인스턴스 생성
        * 문서가 이미지 추출을 지원하는지 확인
        * [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()) 메서드를 호출하여 문서 정보를 가져옵니다.
        * 문서에 페이지가 있는지 확인
        * 페이지를 반복하고 페이지 번호 인쇄
        * [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) 메서드를 호출하여 전체 문서에서 모든 이미지를 추출합니다.
        * 이미지 반복 및 이미지 유형 인쇄
     
      gisthash: "68450336a57c5d8df06b4ef1ea69b29f"
      gistfile: "extract_images_form_documents_page.java"
      
    - title_left: "XLSX 문서 페이지 영역에서 이미지를 추출하는 방법"
      content_left: |
       GroupDocs.Parser Java API는 XLSX 문서의 페이지 용이성에서 추출을 위한 완벽한 지원을 제공했습니다. 다음 Java 코드는 프로그래머가 자체 Java 앱 내부의 XLSX 문서 페이지 영역에서 이미지를 추출하는 방법을 보여줍니다.

      title_right: "Java 를 사용하여 이미지를 추출하시겠습니까?"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)의 인스턴스 생성
        * 이미지 추출에 사용되는 옵션 생성
        * 이미지 추출 지원 문서 확인
        * [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) 메서드를 호출하여 페이지의 왼쪽 상단 모서리에서 이미지를 추출합니다.
        * 이미지를 반복하고 이미지 URL 인쇄
     
      gisthash: "40143a56569ae88e7e7c972ccca041b5"
      gistfile: "extract_images_form_documents_page_area.java"

    - title_left: "Java API를 통해 이미지를 파일로 추출하는 방법"
      content_left: |
       GroupDocs.Parser Java API를 사용하면 XLSX 문서에서 이미지를 추출하고 이미지 내용을 파일에 저장할 수 있습니다. 다음 Java 코드는 프로그래머가 자신의 Java 앱 내에서 선택한 파일로 이미지를 추출하는 방법을 보여줍니다.

      title_right: "문서에서 파일로 이미지 추출"
      content_right: |
        * [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)의 인스턴스 생성
        * 이미지 추출 지원 문서 확인
        * [getImages()](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getImages()) 메서드를 호출하여 페이지의 왼쪽 상단 모서리에서 이미지를 추출합니다.
        * 지원되는 파일 형식으로 이미지를 저장하는 옵션 생성
        * 이미지를 반복하고 이미지 URL 인쇄
     
      gisthash: "6faeafc93e4412265b7439209828950b"
      gistfile: "images_saving_to_files.java"

    - title_left: "시스템 요구 사항"
      content_left: |
        Java용 GroupDocs.Parser는 모든 주요 플랫폼 및 운영 체제에서 지원됩니다. Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice 및 50개 이상의 기타 형식으로 문서를 생성할 수 있습니다. 전체 시스템 요구 사항 가이드를 보려면 아래 코드를 실행하기 전에 시스템 요구 사항을 방문하십시오. 시스템에 다음 전제 조건이 설치되어 있는지 확인하십시오.
         * 운영 체제: 마이크로소프트 윈도우, 리눅스, 맥OS
         * 자바 버전 지원: J2SE 7.0(1.7), J2SE 8.0(1.8) 이상
         * GroupDocs[Repository](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)에서 최신 버전의 GroupDocs.Assembly Java API 다운로드
        
      title_right: "GroupDocs.Parser를 사용하는 이유"
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