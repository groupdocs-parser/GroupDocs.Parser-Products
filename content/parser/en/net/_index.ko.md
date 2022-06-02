---
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

head_title: ".NET Parsing API, PDF Word Excel에서 텍스트 이미지 메타데이터 추출"
head_description: "데이터베이스, PDF, Word, Excel, 프레젠테이션, 웹, 이메일, EPUB 및 zip 파일 형식에서 텍스트, 이미지, 메타데이터 및 인코딩을 추출하는 C# .NET 문서 구문 분석 API."

title: ".문서 데이터를 추출하는 NET API"
description: "‎.NET 앱 내에서 문서, 스프레드시트, 프레젠테이션, 이메일 및 아카이브에서 이미지, 원시 또는 형식이 지정된 텍스트 및 메타데이터를 추출합니다.‎"
button:
    enable: true

submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:
            - link: "#overview"
              text: "개요"

            - link: "#features"
              text: "특징"

            - link: "#support"
              text: "지원하다"

            - link: "https://products.groupdocs.app/parser"
              text: "라이브 데모"

            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "가격"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net/"
        link_buy: "https://purchase.groupdocs.com"

overview:
    enable: true
    content: |
      .NET용 GroupDocs.Parser는 C#, ASP.NET 및 기타 .NET 기술을 사용하여 개발된 비즈니스 응용 프로그램을 위한 텍스트, 메타데이터 및 이미지 추출기 API입니다. 지원되는 형식의 파일에서 원시, 형식 및 구조화된 텍스트와 메타데이터 추출을 지원합니다. .NET용 GroupDocs.Parser를 통해 응용 프로그램은 워드 프로세싱 문서, Excel 스프레드시트, PowerPoint 프레젠테이션, OneNote, PDF 파일 및 ZIP 아카이브와 같이 널리 사용되는 형식에 대해 암호로 보호된 문서의 구문 분석을 수행할 수도 있습니다.
    tabs:
      enable: true
      
      tab_one:
        description: |
          다음은 .NET용 GroupDocs.Parser의 개요입니다.
      
        left:
          enable: true
          icon: "fas fa-tools"
          title: "특징"
          content: |
            * 이미지 추출
            * 원시 텍스트 추출
            * 서식 있는 텍스트 추출
            * 구조화된 텍스트 추출
            * 메타데이터 추출
            * ZIP 파일 내의 파일에서 추출
            * 검색하여 추출
            * 텍스트 포맷터로 추출
            * 인코딩 표준 감지
            * 미디어 유형 감지
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "API"
          content: |
            * 입력 파일 가져오기
            * 원시 또는 서식 있는 텍스트를 가져옵니다.
            * 메타데이터 가져오기
      
      tab_two:
        description: |
          .NET용 GroupDocs.Parser는 다음 [문서 파일 형식](https://docs.groupdocs.com/parser/net/supported-document-formats/)을 지원합니다.

        left:
          enable: true
          table:
            - title: "텍스트 추출"
              content: |
                * **텍스트**: DOC, DOCX, DOT, DOTM, DOTX, DOCM, RTF, ODT, OTT, TXT, MD, WordprocessingML(XML)
                * **스프레드시트**: XLS, XLSX, CSV, XLSM, XLSB, ODS, SpreadsheetML(XML), XLT, XLTX, XLTM, OTS, XLA,, XLAM, TSV
                * **프레젠테이션**: PPT, PPTX, PPTM, PPS, PPSX, PPSM, POT, POTX, POTM, ODP, OTP
                * **원노트**: 하나
                * **이메일**: MSG, EML, EMLX, PST, OST, MS EXCHANGE SERVER, POP, IMAP
                * **전자출판**: EPUB, FB2
                * **Portable Document**: PDF, PDF 포트폴리오, 암호화된 PDF
                * **DOM 기반**: XML, HTML, XHTML, MHTML
                * **압축 및 포장**: ZIP, CHM
                * **데이터베이스**: ADO.NET

            - title: "인코딩 감지"
              content: |
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8 및 UTF7
                * **내용**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8 및 ANSI

        right:
          enable: true
          table:
            - title: "메타데이터 추출"
              content: |
                * **텍스트**: DOC, DOCX, DOT, DOTX, DOTM, OTT, ODT
                * **스프레드시트**: XLS, XLSX, XLT, XLTX, XLTM, XLA, XLAM, OTS, ODS
                * **프레젠테이션**: PPT, PPTX, POT, POTX, POTM, PPSM, PPTM, OTP, ODP
                * **이메일**: MSG, EML, EMLX
                * **전자출판**: EPUB, FB2
                * **기타**: PDF

            - title: "텍스트 및 메타데이터 추출"
              content: |
                * **템플릿**: DOTX, POTX
                * **매크로 사용 템플릿**: DOTM, POTM, PPSM, PPTM
                * **OpenDocument 템플릿**: OTT

            - title: "이미지 추출"
              content: |
                * **텍스트**: DOC, DOCX, DOCM, RTF, DOT, DOTM, DOTX, ODT
                * **스프레드시트**: XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **프레젠테이션**: PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **이동식 문서**: PDF, POT, POTM, POTX
                * **전자책**: CHM, EPUB, FB2
                * **마크업**: HTML

      tab_three:
        description: |
          .NET용 GroupDocs.Parser는 다음 운영 체제, 프레임워크 및 패키지 관리자를 지원합니다.‎
        
        left:
          enable: true
          table:
            - icon: "fab fa-windows"
              title: "운영체제"
              content: |
                * 윈도우 데스크탑
                * 윈도우 서버
                * 윈도우 애저
                * 리눅스

            - icon: "fas fa-code"
              title: "지원되는 프레임워크"
              content: |
                * .NET 프레임워크 2.0 이상
                * 모노 프레임워크 1.2 이상
                * .NET 표준 2.0
                * .NET 코어 2.0

        right:
          enable: true
          table:
            - icon: "fas fa-box"
              title: "패키지 관리자"
              content: |
                * 누겟

            - icon: "fas fa-tools"
              title: "개발 환경"
              content: |
                * 마이크로소프트 비주얼 스튜디오
                * 자마린.안드로이드
                * 자마린.IOS
                * 자마린.맥
                * 모노디벨롭

features:
    enable: true
    title: ".NET 기능을 위한 GroupDocs.Parser"

    feature:
      - icon: "fas fa-copy"
        content: "단일 또는 다중 파일에서 통계적으로 단어 발생 횟수 계산"

      - icon: "fas fa-eye"
        content: "Excel 워크시트 및 프레젠테이션 템플릿에서 텍스트 및 메타데이터 추출"

      - icon: "fas fa-bolt"
        content: "문서 판독기를 설치하지 않고 파일 또는 스트림에서 텍스트 콘텐츠 추출"
      
      - icon: "fas fa-file-powerpoint"
        content: "빠른 또는 표준 텍스트 추출 모드를 사용하여 문서에서 서식 있는 텍스트 가져오기"

      - icon: "fas fa-code"
        content: "암호로 보호된 XML 문서의 미디어 유형 감지 및 텍스트 가져오기"

      - icon: "fas fa-cloud"
        content: "이메일 및 첨부 파일 내에서 프로그래밍 방식으로 서식 있는 텍스트 가져오기"

      - icon: "fas fa-remove-format"
        content: "OneNote 문서의 단일 또는 여러 페이지에서 텍스트 그리기"

      - icon: "fas fa-comment-slash"
        content: "PDF, MS Word, Excel 및 프레젠테이션 문서에서 데이터 추출‎"

      - icon: "fas fa-location-arrow"
        content: "PDF 양식에서 데이터 추출 및 간단한 PDF 파일 또는 PDF 포트폴리오 문서에서 텍스트 가져오기"

      - icon: "fas fa-border-all"
        content: "PowerPoint 프레젠테이션에서 서식 있는 텍스트 가져오기 또는 특정 슬라이드에서 텍스트 추출"

      - icon: "fas fa-wrench"
        content: "Excel 스프레드시트의 셀, 행 및 열에서 원시 또는 서식 있는 텍스트 수집"

      - icon: "fas fa-columns"
        content: "Word 문서에서 원시 또는 HTML 형식의 텍스트 추출"

      - icon: "fas fa-file-word"
        content: "HTML 포맷터는 단락, 하이퍼링크, 글꼴, 머리글, 목록 및 표의 서식 지정을 지원합니다."

      - icon: "fas fa-envelope"
        content: "EPUB, CHM, Markdown 및 FB2 파일에서 단일 문장 또는 전체 텍스트 추출"

      - icon: "fas fa-print"
        content: "데이터베이스, PDF, EPUB, CHM 및 워드 프로세싱 문서에서 목차 발췌"

      - icon: "fas fa-file-archive"
        content: "콘텐츠 구조가 있는 텍스트를 그대로 가져오고 문서에서 강조 표시된 텍스트를 발췌합니다."

      - icon: "fas fa-lock"
        content: "분석을 위해 문서에서 텍스트 영역 가져오기 및 지원되는 문서 형식에서 메타데이터 그리기"

      - icon: "fas fa-file-code"
        content: "지원되는 형식에서 전체 또는 선택한 이미지 가져오기 및 추출된 이미지 회전"
      
      - icon: "fas fa-fill-drip"
        content: "Zip 아카이브 및 OST 컨테이너 내의 파일에서 텍스트 꺼내기 및 ZIP 컨테이너 항목의 파일 유형 감지"

      - icon: "fas fa-file-excel"
        content: "이메일 컨테이너에서 데이터 가져오기(Exchange 웹 서버, POP3, IMAP)"

      - icon: "fas fa-heading"
        content: "문서 내에서 간단한 텍스트, 전체 단어 및 정규식 검색"

      - icon: "fas fa-project-diagram"
        content: "문서 템플릿 준비, 문서에서 데이터 추출 및 데이터 필드 및 테이블 분석"

      - icon: "fas fa-cube"
        content: "문서에서 강조 표시된 표현식 검색 및 추출"

      - icon: "fab fa-uncharted"
        content: "일반 텍스트 포맷터(단순 및 ASCII) 또는 마크다운 포맷터로 텍스트 가져오기"

      - icon: "fab fa-uncharted"
        content: "Markdown Formatter는 글꼴, 하이퍼링크, 제목, 목록 및 표의 서식 지정을 지원합니다."

      - icon: "fab fa-uncharted"
        content: "모서리, 각도 및 교차로 사용자 지정 서식을 수행하여 일반 텍스트 서식 지정"

      - icon: "fab fa-uncharted"
        content: "열 구분 기호로 테이블 레이아웃 이동 및 직사각형 영역의 테이블 감지"

      - icon: "fab fa-uncharted"
        content: "Microsoft Office 파일 형식 내의 도형, WordArt 개체 및 텍스트 상자에서 텍스트 추출"

      - icon: "fab fa-uncharted"
        content: "파일로 이미지 추출 – JPG, PNG, GIF, BMP, PNG 또는 WEBP 형식으로 저장"

    more_feature:
      - title: "문서에서 텍스트 추출"
        content: |
          GroupDocs.Parser for .NET API를 사용하여 문서에서 텍스트를 추출하는 것은 간단하며 몇 줄의 코드로 달성됩니다.

          ```cs
          // Parser 클래스의 인스턴스 생성
          using(Parser parser = new Parser("sample.docx"))
          {
            // 리더로 텍스트 추출
            using(TextReader reader = parser.GetText())
            {
              // 문서에서 텍스트 인쇄
              // 텍스트 추출이 지원되지 않는 경우 판독기는 null입니다.
              Console.WriteLine(reader == null ? "Text extraction isn't supported." : reader.ReadToEnd());
            }
          }
          ```

support:
    enable: true

solutions:
    enable: true
    title: "GroupDocs.Parser는 다른 인기 있는 개발 환경을 위한 문서 보기 API를 제공합니다."

    solution:
        - img_alt: "GroupDocs.Parser for Java"
          image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-java.png"
          product: "GroupDocs.Parser"
          platform: "Java"
          link: "/parser/java/"

back_to_top:
  enable: true
---
