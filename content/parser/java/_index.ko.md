---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: ko
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "GroupDocs.Parser for Java 문서 파싱 앱"
head_description: "Java 애플리케이션을 위한 올인원 문서 파싱 솔루션을 얻으십시오. 간단한 드래그 앤 드롭 기능으로 온라인에서 문서 형식의 데이터를 추출하세요."

############################# Header ############################
title: "Java API를 통한 문서 파싱"
description: "프로그래머 및 최종 사용자를 위한 유연한 API와 앱 기반 솔루션을 사용하여 모든 플랫폼에서 문서와 이미지의 데이터를 추출합니다."
words:
  for: "을 위한"

actions:
  main: "Maven 다운로드"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "라이선스"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "시작할 준비가 되셨나요?"
  description: "GroupDocs.Parser 기능을 무료로 체험하거나 라이선스를 요청하세요."

release:
  title: "버전 {0} 출시"
  notes: "새로운 기능 보기"
  downloads: "다운로드"

code:
  title: "문서 콘텐츠를 빠르게 가져오기"
  more: "더 많은 예제"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // 소스 파일을 Parser 인스턴스에 전달하세요.
    try (Parser parser = new Parser("source.pdf"))
    {
        // 문서 텍스트를 TextReader에 전달하세요.
        try (TextReader reader = parser.getText())
        {
            // 문서 텍스트 처리하기
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 개요"
  description: "Java 애플리케이션에서 문서 파싱을 수행하기 위한 API"
  features:
    # feature loop
    - title: "문서에서 데이터 추출"
      content: "GroupDocs.Parser for Java API는 Office 문서, 이메일, 첨부 파일 및 아카이브와 같은 다양한 파일 형식에서 텍스트, 메타데이터 및 이미지를 검색할 수 있게 해줍니다. 이 강력한 도구는 데이터 분석, 검색 엔진 인덱싱 또는 콘텐츠 관리 시스템과 같은 다양한 애플리케이션에서 파일에 포함된 소중한 정보에 효율적으로 접근하고 처리하는 데 도움을 줍니다."

    # feature loop
    - title: "문서 파싱"
      content: "하이퍼링크, 테이블, QR 코드, 바코드 및 PDF 양식에서 데이터를 추출합니다. 또한 사용자 정의 템플릿을 사용하여 문서에서 원하는 정보를 파싱합니다."

    # feature loop
    - title: "결과 사용자 정의"
      content: "Java API는 원시, 구조화된, HTML 또는 Markdown과 같은 다양한 형식으로 데이터를 검색할 수 있게 해줍니다. 추가로, API는 문서 텍스트 내에서 특정 단어 또는 구문을 찾기 위한 검색 기능을 제공합니다."

############################# Platforms ############################
platforms:
  enable: true
  title: "플랫폼 독립성"
  description: "GroupDocs.Parser for Java는 다음 운영 체제, 프레임워크 및 패키지 관리자를 지원합니다."
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "지원되는 파일 형식"
  description: |
    GroupDocs.Parser for Java는 다음 [파일 형식](https://docs.groupdocs.com/parser/java/supported-document-formats/)으로 작업을 지원합니다.
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office 형식
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### 이미지 및 기타 형식
        * **휴대용:** PDF 
        * **이미지:** JPG, BMP, PNG, TIFF, GIF
        * **기타 오피스 형식:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### 기타 형식
        * **웹:** HTML, MHTML 
        * **아카이브:** ZIP, TAR, 7Z 
        * **e-북:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java 기능"
  description: "PDF, Office 문서 및 이미지를 신속하고 정확하게 데이터 추출"

  items:
    # feature loop
    - icon: "text"
      title: "텍스트 추출"
      content: "Office 문서, PDF 파일 및 이미지와 같은 다양한 파일 형식에서 텍스트 정보를 추출하여 가독성과 분석을 용이하게 합니다."

    # feature loop
    - icon: "image"
      title: "이미지 추출"
      content: "Office 문서, PDF 파일 등 다양한 출처에서 비주얼 콘텐츠를 리트리브하여 편리하게 사용할 수 있게 합니다."

    # feature loop
    - icon: "qr"
      title: "QR 코드 스캔"
      content: "Office 문서, PDF 파일 또는 비주얼 콘텐츠에 존재하는 QR 코드를 감지하고 해독하여 정보를 효율적으로 리트리브합니다."

    # feature loop
    - icon: "email"
      title: "이메일 첨부文件 및 압축 파일에서 데이터 추출"
      content: "이메일 메시지, 파일 첨부 파일 및 압축 데이터 소스에서 귀중한 정보를 수집하여 효과적으로 분석하고 활용합니다."

    # feature loop
    - icon: "table"
      title: "테이블 추출"
      content: "PDF 문서에서 테이블 데이터를 확인하고 추출하여 체계적인 분석 및 사용을 지원합니다."

    # feature loop
    - icon: "hyperlink"
      title: "하이퍼링크 추출"
      content: "Office 문서 또는 PDF 파일 내에 있는 하이퍼링크 및 이메일 주소를 찾아서 효율적으로 접근합니다."

    # feature loop
    - icon: "pdf"
      title: "PDF 양식 파싱"
      content: "PDF 양식은 사용자 상호작용을 위한 작성 가능한 필드가 포함된 디지털 문서입니다. .NET API를 사용하여 이러한 양식에서 데이터를 효율적으로 추출할 수 있습니다."

    # feature loop
    - icon: "template"
      title: "템플릿으로 데이터 파싱"
      content: ".NET API와 함께 사용할 사용자 정의 템플릿을 생성하고 PDF 파일에서 특정 정보를 파싱하여 데이터 추출 프로세스를 간소화합니다."

    # feature loop
    - icon: "search"
      title: "문서에서 텍스트 검색"
      content: "문서 내에서 특정 단어 또는 패턴을 신속하게 찾습니다."


############################# Code samples ############################
code_samples:
  enable: true
  title: "코드 샘플"
  description: "전형적인 GroupDocs.Parser for Java 작업 사례 몇 가지"
  items:
    # code sample loop
    - title: "PDF 문서에서 이미지 추출"
      content: |
        GroupDocs.Parser for Java은 Java 개발자가 [문서](https://docs.groupdocs.com/parser/java/extract-images-from-documents/)에서 이미지를 추출할 수 있도록 쉽게 만들어줍니다:
        {{< landing/code title="Java에서 PDF 문서의 이미지 추출">}}
        ```java {style=abap}
        // Parser 클래스의 인스턴스를 생성하세요.
        try (Parser parser = new Parser("source.pdf"))
        {
            // 이미지를 추출하세요.
            Iterable<PageImageArea> images = parser.getImages();

            // 추출된 여부 확인하기
            if (images == null) {
                return;
            }

            // 이미지를 순회하기
            for (PageImageArea image : images) {
                // 페이지 인덱스, 사각형 및 이미지 유형을 출력하기
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "이미지에서 바코드 추출"
      content: |
        우리의 Java API를 사용하여 이미지에서 [바코드](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/)를 추출하세요:
        {{< landing/code title="Java에서 이미지의 바코드 추출">}}
        ```java {style=abap}   
        // Parser에 소스 이미지를 로드하세요.
        try (Parser parser = new Parser("source.jpg")){

            // 파일이 바코드 추출을 지원하는지 확인하세요.
            if (!parser.getFeatures().isBarcodes()) {

                // 파일에서 바코드를 추출하세요.
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // 바코드를 순회하기
                for (PageBarcodeArea barcode : barcodes) {
                    // 페이지 인덱스를 출력하기
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // 바코드 값을 출력하기
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
