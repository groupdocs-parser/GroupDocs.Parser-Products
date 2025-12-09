---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Java Java용 문서 파서 SDK"
head_description: "Java용 고성능 문서 파서 SDK. PDF, Word, Excel, 이메일 및 50개 이상의 문서 형식에서 텍스트, 이미지, 메타데이터, 바코드, 표 및 기타 데이터를 추출합니다."

############################# Header ############################
title: "Java용 문서 파서 SDK"
description: "Java 애플리케이션에 빠르고 정확한 문서 파싱을 추가하고 문서 및 이미지에서 텍스트, 이미지, 메타데이터 및 구조화된 데이터를 추출합니다."
words:
  for: "용"

actions:
  main: "Maven 다운로드"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "라이선스"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "시작할 준비가 되셨나요?"
  description: "GroupDocs.Parser 기능을 무료로 사용해 보거나 라이선스를 요청하세요."

release:
  title: "버전 {0} 출시"
  notes: "새로운 기능 보기"
  downloads: "다운로드"

code:
  title: "SDK를 사용하여 문서 내용을 빠르게 파싱"
  more: "추가 예제"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // 소스 파일을 Parser 인스턴스에 전달합니다
    try (Parser parser = new Parser("source.pdf"))
    {
        // 문서 텍스트를 TextReader에 전달합니다
        try (TextReader reader = parser.getText())
        {
            // 문서 텍스트를 처리합니다
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 한눈에 보기"
  description: "Java 애플리케이션에서 고정밀 문서 파싱을 수행하기 위한 Document Parser SDK"
  features:
    # feature loop
    - title: "문서에서 데이터 추출"
      content: "GroupDocs.Parser for Java API를 사용하면 Office 문서, 이메일, 첨부 파일 및 아카이브와 같은 다양한 파일 형식에서 텍스트, 메타데이터 및 이미지를 검색할 수 있습니다. 이 강력한 도구는 데이터 분석, 검색 엔진 인덱싱 또는 콘텐츠 관리 시스템과 같은 다양한 애플리케이션을 위해 파일에 포함된 귀중한 정보를 효율적으로 액세스하고 처리하는 데 도움을 줍니다."

    # feature loop
    - title: "문서 구문 분석"
      content: "PDF 양식에서 하이퍼링크, 표, QR 코드, 바코드 및 데이터를 비롯한 다양한 요소를 추출합니다. 또한 사용자 정의 템플릿을 사용하여 문서에서 원하는 정보를 구문 분석합니다."

    # feature loop
    - title: "결과 사용자 지정"
      content: "Java API를 사용하면 raw, structured, HTML, Markdown과 같은 다양한 형식으로 데이터를 검색할 수 있습니다. 또한 API는 문서 텍스트 내에서 특정 단어나 구를 찾는 검색 기능을 제공합니다."

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
    GroupDocs.Parser for Java은(는) 다음 [파일 형식](https://docs.groupdocs.com/parser/java/supported-document-formats/)에 대한 작업을 지원합니다.
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
        * **전자책:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java 기능"
  description: "우리의 Java Document Parser SDK를 사용하여 PDF, Office 문서, 이미지 및 기타 형식에서 데이터를 신속하고 정확하게 추출합니다."

  items:
    # feature loop
    - icon: "text"
      title: "텍스트 추출"
      content: "Office 문서, PDF 파일 및 이미지와 같은 다양한 파일 형식에서 텍스트 정보를 추출해 가독성과 분석을 용이하게 합니다."

    # feature loop
    - icon: "image"
      title: "이미지 추출"
      content: "Office 문서, PDF 파일 등 다양한 소스에서 시각적 콘텐츠를 검색해 편리하게 액세스하고 사용할 수 있습니다."

    # feature loop
    - icon: "qr"
      title: "QR 코드 스캔"
      content: "Office 문서, PDF 파일 또는 시각적 콘텐츠에 포함된 QR 코드를 감지하고 디코딩해 효율적인 정보 검색을 지원합니다."

    # feature loop
    - icon: "email"
      title: "이메일 첨부 파일 및 아카이브에서 데이터 추출"
      content: "이메일 메시지, 파일 첨부 및 압축 데이터 소스에서 귀중한 정보를 수집하여 효과적인 분석 및 활용을 수행합니다."

    # feature loop
    - icon: "table"
      title: "테이블 추출"
      content: "PDF 문서에서 표 형식 데이터를 식별하고 추출하여 체계적인 분석 및 활용에 사용할 수 있습니다."

    # feature loop
    - icon: "hyperlink"
      title: "하이퍼링크 추출"
      content: "오피스 문서나 PDF 파일 내의 하이퍼링크 및 이메일 주소를 찾아 추출하여 효율적인 액세스를 가능하게 합니다."

    # feature loop
    - icon: "pdf"
      title: "PDF 양식 파싱"
      content: "PDF 양식은 사용자가 전자적으로 정보를 입력할 수 있는 입력 가능한 필드를 포함한 디지털 문서입니다. .NET API를 사용하여 이러한 양식에서 데이터를 추출하고 효율적으로 처리할 수 있습니다."

    # feature loop
    - icon: "template"
      title: "템플릿으로 데이터 파싱"
      content: "사용자 정의 템플릿을 생성하고 이를 .NET API와 함께 사용하여 PDF 파일에서 특정 정보를 파싱함으로써 데이터 추출 프로세스를 간소화합니다."

    # feature loop
    - icon: "search"
      title: "문서 내 텍스트 검색"
      content: "문서 내에서 특정 단어나 패턴을 신속하게 찾습니다."


############################# Code samples ############################
code_samples:
  enable: true
  title: "코드 샘플"
  description: "일반적인 GroupDocs.Parser for Java 작업의 몇 가지 사용 사례"
  items:
    # code sample loop
    - title: "PDF 문서에서 이미지 추출"
      content: |
        GroupDocs.Parser for Java는 Java 개발자가 [문서](https://docs.groupdocs.com/parser/java/extract-images-from-documents/)에서 이미지를 쉽게 추출할 수 있도록 합니다:
        {{< landing/code title="Java에서 PDF 문서에서 이미지 추출">}}
        ```java {style=abap}
        // Parser 클래스의 인스턴스를 생성합니다.
        try (Parser parser = new Parser("source.pdf"))
        {
            // 이미지 추출
            Iterable<PageImageArea> images = parser.getImages();

            // 무언가가 추출되었는지 확인합니다
            if (images == null) {
                return;
            }

            // 이미지를 반복 처리합니다
            for (PageImageArea image : images) {
                // 페이지 인덱스, 사각형 및 이미지 유형을 출력합니다
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "이미지에서 바코드 추출"
      content: |
        Java API를 사용하여 이미지에서 [바코드](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/)를 추출합니다:
        {{< landing/code title="Java에서 이미지에서 바코드 추출">}}
        ```java {style=abap}   
        // Parser에 소스 이미지를 로드합니다
        try (Parser parser = new Parser("source.jpg")){

            // 파일이 바코드 추출을 지원하는지 확인합니다
            if (!parser.getFeatures().isBarcodes()) {

                // 파일에서 바코드 추출
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // 바코드를 반복 처리합니다
                for (PageBarcodeArea barcode : barcodes) {
                    // 페이지 인덱스를 출력합니다
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // 바코드 값을 출력합니다
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
