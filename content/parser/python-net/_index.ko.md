---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: ko
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

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
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK for Python"
head_description: "고성능 Python용 Document Parser SDK. PDF, Word, Excel, 이메일 및 50개 이상의 문서 형식에서 텍스트, 이미지, 메타데이터, 바코드, 표 및 기타 데이터를 추출합니다."

############################# Header ############################
title: "Python용 Document Parser SDK"
description: "Python 앱에 빠르고 정확한 문서 파싱을 추가하고 문서와 이미지에서 텍스트, 이미지, 메타데이터 및 구조화된 데이터를 추출합니다."
words:
  for: "용"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI 다운로드"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "라이선스"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "시작할 준비가 되셨나요?"
  description: "GroupDocs.Parser 기능을 무료로 사용해 보거나 라이선스를 요청하세요."

release:
  enable: false
  title: "버전 {0} 출시"
  notes: "새로운 기능 보기"
  downloads: "다운로드"

code:
  title: "Python을 사용하여 텍스트 추출"
  more: "추가 예제"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # 문서 로드
    with Parser("sample.pdf") as parser:
        # 문서에서 텍스트 추출
        text = parser.GetText()

        # 추출된 모든 텍스트 출력
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser 한눈에 보기"
  description: "Python 애플리케이션에서 고정밀 문서 파싱을 수행하기 위한 Document Parser SDK"
  features:
    # feature loop
    - title: "문서에서 데이터 추출"
      content: "GroupDocs.Parser for Python via .NET API를 사용하면 Office 문서, 이메일, 첨부 파일 및 압축 파일과 같은 다양한 파일 형식에서 텍스트, 메타데이터 및 이미지를 가져올 수 있습니다. 이 강력한 도구는 데이터 분석, 검색 엔진 인덱싱 또는 콘텐츠 관리 시스템과 같은 다양한 애플리케이션에서 이러한 파일에 포함된 중요한 정보를 효율적으로 액세스하고 처리하는 데 도움이 됩니다."

    # feature loop
    - title: "문서 파싱"
      content: "PDF 양식에서 하이퍼링크, 표, QR 코드, 바코드 및 데이터를 포함한 다양한 요소를 추출합니다. 또한 사용자 정의 템플릿을 사용하여 문서에서 원하는 정보를 파싱할 수 있습니다."

    # feature loop
    - title: "결과 맞춤화"
      content: "Python API를 사용하면 원시, 구조화, HTML 또는 Markdown과 같은 다양한 형식으로 데이터를 가져올 수 있습니다. 또한 API는 문서 텍스트 내에서 특정 단어나 구문을 찾을 수 있는 검색 기능을 제공합니다."

############################# Platforms ############################
platforms:
  enable: true
  title: "플랫폼 독립성"
  description: "GroupDocs.Parser for Python via .NET는 다음 운영 체제, 프레임워크 및 패키지 관리자를 지원합니다."
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
    GroupDocs.Parser for Python via .NET는 다음 [파일 형식](https://docs.groupdocs.com/parser/python-net/supported-document-formats/)과 함께 작업을 지원합니다.
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
  title: "GroupDocs.Parser for Python via .NET 기능"
  description: "우리의 Python Document Parser SDK로 PDF, Office 문서, 이미지 및 기타 형식에서 데이터를 빠르고 정확하게 추출합니다."

  items:
    # feature loop
    - icon: "text"
      title: "텍스트 추출"
      content: "Office 문서, PDF 파일 및 이미지와 같은 다양한 파일 형식에서 텍스트 정보를 추출하여 손쉽게 읽고 분석할 수 있습니다."

    # feature loop
    - icon: "image"
      title: "이미지 추출"
      content: "Office 문서, PDF 파일 등 다양한 소스에서 시각적 콘텐츠를 가져와 편리하게 접근하고 사용할 수 있습니다."

    # feature loop
    - icon: "qr"
      title: "QR 코드 스캔"
      content: "Office 문서, PDF 파일 또는 시각적 콘텐츠에 포함된 QR 코드를 감지하고 디코딩하여 효율적인 정보 검색을 가능하게 합니다."

    # feature loop
    - icon: "email"
      title: "이메일 첨부 파일 및 압축 파일에서 데이터 추출"
      content: "이메일 메시지, 파일 첨부 및 압축 데이터 소스에서 유용한 정보를 수집하여 효과적인 분석 및 활용이 가능합니다."

    # feature loop
    - icon: "table"
      title: "표 추출"
      content: "PDF 문서에서 표 형태의 데이터를 식별하고 추출하여 체계적인 분석 및 활용이 가능합니다."

    # feature loop
    - icon: "hyperlink"
      title: "하이퍼링크 추출"
      content: "오피스 문서 또는 PDF 파일 내에서 하이퍼링크와 이메일 주소를 찾아 추출하여 효율적으로 액세스합니다."

    # feature loop
    - icon: "pdf"
      title: "PDF 양식 파싱"
      content: "PDF 양식은 사용자가 상호 작용할 수 있는 입력 가능한 필드를 포함한 디지털 문서로, 전자적으로 정보를 입력할 수 있습니다. Python API를 사용하여 이러한 양식에서 데이터를 추출하고 효율적으로 처리할 수 있습니다."

    # feature loop
    - icon: "template"
      title: "템플릿을 사용한 데이터 파싱"
      content: "맞춤 템플릿을 생성하고 Python API와 함께 사용하여 PDF 파일에서 특정 정보를 파싱함으로써 데이터 추출 프로세스를 간소화합니다."

    # feature loop
    - icon: "search"
      title: "문서에서 텍스트 검색"
      content: "문서 내에서 특정 단어나 패턴을 빠르게 찾습니다."


############################# Code samples ############################
code_samples:
  enable: true
  title: "코드 샘플"
  description: "기본 텍스트 추출을 넘어, 빠른 텍스트, 이미지 및 메타데이터 추출을 위한 가장 일반적인 사용 사례는 다음과 같습니다."
  items:
    # code sample loop
    - title: "문서에서 텍스트 검색"
      content: |
        이 예제는 PDF 문서에서 특정 구문을 검색하고 해당 위치를 출력하는 방법을 보여줍니다.
        {{< landing/code title="Python에서 문서 텍스트 검색">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # 문서 로드
        with Parser("sample.pdf") as parser:
            # 구문이 발견된 페이지 인덱스와 사각형 영역을 출력
            for area in parser.Search("Total Amount"):
                # 구문이 발견된 페이지 인덱스와 사각형 영역을 출력
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "문서에서 이미지 추출"
      content: |
        이 예제는 PDF 문서에서 이미지를 추출하고 파일에 저장하는 방법을 보여줍니다.
        {{< landing/code title="Python에서 문서 이미지 추출">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # 문서 로드
        with Parser("sample.docx") as parser:
            # 문서에서 이미지 추출
            images = parser.GetImages()

            # 이미지를 파일에 저장
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "문서에서 메타데이터 추출"
      content: |
        이 예제는 PDF 문서에서 메타데이터를 추출하고 출력하는 방법을 보여줍니다.
        {{< landing/code title="Python에서 문서 메타데이터 추출">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # 문서 로드
        with Parser("sample.pdf") as parser:
            # 문서에서 메타데이터 추출
            metadata = parser.GetMetadata()

            # 메타데이터 출력
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
