---
############################# Static ############################
layout: "landing"
date: 2024-02-13T17:01:03
draft: false
#operation: 
#parsertype: 
#fileformat: 
#productName: Java
lang: ko
#productCode: java
#otherformats: 
#breadcrumb: Put  parser on  for Java
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: ".NET, Java, Cloud API 및 온라인 문서 파서 앱"
head_description: ".NET, Java 및 클라우드 기반 애플리케이션을 위한 올인원 문서 구문 분석 솔루션을 받으세요. 간단한 드래그 앤 드롭 기능을 사용하여 온라인으로 문서 형식에서 데이터 추출"

############################# Header ############################
title: "문서 분석<br>.NET API를 통해"
description: "프로그래머와 최종 사용자를 위한 유연한 API와 앱 기반 솔루션을 사용하여 모든 플랫폼의 문서와 이미지에서 데이터를 추출합니다."
words:
  for: "~을 위한"

actions:
  main: "무료 NuGet 다운로드"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "라이선스"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net"
  title: "시작할 준비가 되셨나요?"
  description: "무료로 GroupDocs.Parser 기능을 사용해 보거나 라이선스를 요청하세요"

release:
  title: "버전 {0} 출시"
  notes: "새로운 소식 보기"
  downloads: "다운로드"

code:
  title: "C#의 PDF 파일에서 텍스트 추출"
  more: "더 많은 예"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Create an instance of Parser class
    using (var parser = new Parser(fileName))
    {
        // Extract a text into the reader
        using (var textReader = parser.GetText())
        {
            // Print a text from the document
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 개요"
  description: ".NET 애플리케이션에서 문서 구문 분석을 수행하기 위한 API"
  features:
    # feature loop
    - title: "문서에서 데이터 추출"
      content: "API를 사용하면 Office 문서, 이메일, 첨부 파일, 아카이브 등 다양한 파일 형식에서 텍스트, 메타데이터, 이미지를 검색할 수 있습니다. 이 강력한 도구는 데이터 분석, 검색 엔진 색인화 또는 콘텐츠 관리 시스템과 같은 다양한 응용 프로그램을 위해 이러한 파일에 포함된 중요한 정보에 효율적으로 액세스하고 처리하는 데 도움이 됩니다."

    # feature loop
    - title: "문서 분석"
      content: "PDF 양식에서 하이퍼링크, 표, QR 코드, 바코드 및 데이터와 같은 다양한 요소를 추출합니다. 또한 사용자 정의 템플릿을 사용하여 문서에서 원하는 정보를 구문 분석합니다."

    # feature loop
    - title: "결과 맞춤설정"
      content: ".NET API를 사용하면 원시, 구조화, HTML 또는 마크다운과 같은 다양한 형식의 데이터를 검색할 수 있습니다. 또한 API는 문서 텍스트 내에서 특정 단어나 문구를 찾는 검색 기능을 제공합니다."

############################# Platforms ############################
platforms:
  enable: true
  title: "플랫폼 독립성"
  description: "다음 운영체제, 프레임워크, 패키지 관리자를 지원합니다."
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
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "지원되는 파일 형식"
  description: |
    다음 [파일 형식](https://docs.groupdocs.com/parser/net/supported-document-formats/)을 사용한 작업을 지원합니다.
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office 형식
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### 이미지 및 기타 형식
        * **Portable:** PDF
        * **이미지:** JPG, BMP, PNG, TIFF, GIF
        * **기타 사무실 형식:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### 기타 형식
        * **편물:** HTML, MHTML
        * **아카이브:** ZIP, TAR, 7Z
        * **전자책:** CHM, EPUB, FB2, MOBI

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser 기능"
  description: "PDF, Office 문서 및 이미지에서 데이터를 신속하고 정확하게 추출합니다."

  items:
    # feature loop
    - icon: "text"
      title: "텍스트 추출"
      content: "쉽게 읽고 분석할 수 있도록 사무용 문서, PDF 파일, 이미지 등 다양한 파일 형식에서 텍스트 정보를 추출합니다."

    # feature loop
    - icon: "image"
      title: "이미지 추출"
      content: "편리한 액세스 및 사용을 위해 사무실 문서, PDF 파일과 같은 다양한 소스에서 시각적 콘텐츠를 검색합니다."

    # feature loop
    - icon: "qr"
      title: "QR 코드 스캔"
      content: "효율적인 정보 검색을 위해 사무실 문서, PDF 파일 또는 시각적 콘텐츠 내에 있는 QR 코드를 감지하고 디코딩합니다."

    # feature loop
    - icon: "email"
      title: "이메일 첨부 파일 및 아카이브에서 데이터 추출"
      content: "효과적인 분석과 활용을 위해 이메일 메시지, 첨부 파일, 압축 데이터 소스에서 귀중한 정보를 수집하세요."

    # feature loop
    - icon: "table"
      title: "테이블 추출"
      content: "체계적인 분석 및 사용을 위해 PDF 문서에서 표 형식 데이터를 식별하고 추출합니다."

    # feature loop
    - icon: "hyperlink"
      title: "하이퍼링크 추출"
      content: "효율적인 액세스를 위해 사무실 문서 또는 PDF 파일 내에서 하이퍼링크와 이메일 주소를 찾아 추출합니다."

    # feature loop
    - icon: "pdf"
      title: "PDF 양식 구문 분석"
      content: "PDF 양식은 사용자 상호작용을 위해 입력 가능한 필드가 포함된 디지털 문서로, 정보를 전자적으로 입력할 수 있습니다. 효율적인 처리를 위해 API를 활용하여 이러한 양식에서 데이터를 추출할 수 있습니다."

    # feature loop
    - icon: "template"
      title: "템플릿으로 데이터 구문 분석"
      content: "맞춤 템플릿을 만들고 이를 .NET API로 활용하여 PDF 파일의 특정 정보를 구문 분석하여 데이터 추출 프로세스를 단순화합니다."

    # feature loop
    - icon: "search"
      title: "문서에서 텍스트 검색"
      content: "문서 내에서 특정 단어나 패턴을 빠르게 찾습니다."

############################# Code samples ############################
code_samples:
  enable: true
  title: "코드 샘플"
  description: "일반적인 작업의 일부 사용 사례"
  items:
    # code sample loop
    - title: "PDF 문서에서 이미지 추출"
      content: |
        API를 사용하면 C# 개발자가 몇 가지 간단한 단계를 구현하여 문서에서 이미지를 쉽게 추출할 수 있습니다.
        {{< landing/code title="C#의 PDF 문서에서 이미지 추출">}}
        ```csharp {style=abap}
        // Create an instance of Parser class
        using (var parser = new Parser(fileName))
        {
            // Extract images
            var images = parser.GetImages();

            // Check if images extraction is supported
            if (images != null)
            {
                var imageIndex = 0;

                // Iterate over images
                foreach (var image in images)
                {
                    // Save the image to the file
                    image.Save($"{++imageIndex}{image.FileType.Extension}");
                }
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "이미지에서 바코드 추출"
      content: |
        API를 사용하면 C# 개발자가 몇 가지 간단한 단계를 구현하여 문서에서 바코드를 쉽게 추출할 수 있습니다.
        {{< landing/code title="이미지에서 바코드 추출">}}
        ```csharp {style=abap}   
        // Create an instance of Parser class
        using (var parser = new Parser(fileName))
        {
            // Check if the file supports barcode extracting
            if (parser.Features.Barcodes)
            {
                // Extract barcodes from the file.
                var barcodes = parser.GetBarcodes();

                // Iterate over barcodes
                foreach (var barcode in barcodes)
                {
                    // Print the page index
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Print the barcode value
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
