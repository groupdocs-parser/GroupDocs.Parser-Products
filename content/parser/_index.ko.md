---
############################# Static ############################
layout: "family"
date:  2024-02-13T17:01:03
draft: false

product: "Parser"
product_tag: "parser"

lang: ko

############################# Head ############################
head_title: ".NET, Java, Cloud API 및 온라인 문서 파서 앱"
head_description: ".NET, Java 및 클라우드 기반 애플리케이션을 위한 올인원 문서 구문 분석 솔루션을 받으세요. 간단한 드래그 앤 드롭 기능을 사용하여 온라인으로 문서 형식에서 데이터 추출"

############################# Header ############################
title: "문서분석 솔루션"
description: |
  다양한 파일 형식에서 데이터를 추출하기 위한 강력한 API입니다.

  최소한의 코딩 노력으로 문서를 구문 분석합니다.

  구문 분석 결과를 사용자 정의합니다.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "플랫폼을 선택하세요"
  title: "플랫폼 독립성"
  description: "GroupDocs.Parser 라이브러리는 다음 운영 체제 및 프레임워크를 지원합니다."
  details_link_title: "더 알아보기"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser ~을 위한 .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    .NET Framework 4.6.2 or higher
                    .NET Core 2.0 or higher
                    .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    Microsoft Visual Studio
                    JetBrains Rider
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser ~을 위한 Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    Java 8 or higher
                    Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    IntelliJ IDEA
                    Eclipse
                    NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser 개요"
  description: "PDF, Word, Excel 등의 데이터 구문 분석을 위한 API입니다."

  items:
    # items loop
    - icon: "text"
      title: "텍스트 추출"
      content: "다양한 파일 형식에서 텍스트 정보를 추출합니다."

    # items loop
    - icon: "image"
      title: "이미지 추출"
      content: "다양한 소스에서 시각적 콘텐츠를 검색합니다."

    # items loop
    - icon: "template"
      title: "템플릿으로 데이터 구문 분석"
      content: "사용자 정의 템플릿을 만들고 이를 활용하여 특정 정보를 구문 분석합니다."

    # items loop
    - icon: "pdf"
      title: "PDF 양식 구문 분석"
      content: "PDF 양식은 사용자 상호작용을 위해 입력 가능한 필드가 포함된 디지털 문서입니다."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser 코드 샘플"
  description: "C# 및 Java의 일반적인 GroupDocs.Parser 작업의 일부 사용 사례입니다."

  items:
    # items loop
    - title: "PDF 문서에서 텍스트를 추출하는 방법"
      content: "GroupDocs.Parser API를 사용하면 C# 개발자가 몇 가지 간단한 단계를 구현하여 문서에서 텍스트를 쉽게 추출할 수 있습니다."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              <pre>
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
              </pre>
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              <pre>
              // Create an instance of Parser class
              try (Parser parser = new Parser(fileName)) {
                  // Extract a text into the reader
                  try (TextReader reader = parser.getText()) {
                      // Print a text from the document
                      System.out.println(reader == null 
                              ? "" 
                              : reader.readToEnd());
                  }
              }
              <pre>

############################# Supported Formats ###############################
formats:
  enable: true
  title: "50개 이상의 파일 형식 지원"
  description: "GroupDocs.Parser은 다양한 형식 계열 내에서 파서 작업을 활성화합니다."

############################# Metrics ###############################
metrics:
  enable: false
  title: "자세한 지표 및 통계적 통찰력"
  description: "당사의 성과, 영향력 및 확장에 대한 포괄적인 지표와 통계적 통찰력을 제공하는 주요 수치에 대한 철저한 분석을 살펴보세요."

  items:
    # items loop
    - number: "50+"
      title: "지원되는 형식"
      content: "API는 가장 널리 사용되는 50개 이상의 파일 및 문서 형식을 수용합니다."

    # items loop
    - number: "700k"
      title: "NuGet 다운로드"
      content: "GroupDocs.Parser for .NET는 NuGet 패키지 관리자를 통해 80만 건이 넘는 다운로드를 받았습니다."

    # items loop
    - number: "15k"
      title: "메이븐 다운로드"
      content: "GroupDocs.Parser for Java는 Maven 저장소에서 15,000회가 넘는 다운로드를 누적했습니다."


############################# Customers ###############################
customers:
  enable: true
  title: "우리의 행복한 고객"
  description: "GroupDocs 라이브러리는 전 세계적으로 세계적으로 유명하고 뛰어난 브랜드에서 사용됩니다."

  items:
    # items loop
    - title: "BenQ Corporation"
      logo: "benq"
      
    # items loop
    - title: "Nasdaq Stock Market"
      logo: "nasdaq"
      
    # items loop
    - title: "AT&T Inc."
      logo: "att"
      
    # items loop
    - title: "Customer logo AstraZeneca"
      logo: "astrazeneca"
      
    # items loop
    - title: "Central Bank of Argentina"
      logo: "argentinacentralbank"
      
    # items loop
    - title: "Roche Holding AG"
      logo: "roche"
      
    # items loop
    - title: "Capita"
      logo: "capita"
      
    # items loop
    - title: "Axa S.A."
      logo: "axa"
      
    # items loop
    - title: "Instructure Inc."
      logo: "instructure"
      
    # items loop
    - title: "Wipro"
      logo: "wipro"


############################# Actions ###############################
actions:
  enable: true
  title: "시작할 준비가 되셨나요?"
  description: "귀하의 플랫폼에서 무료로 GroupDocs.Parser 기능을 사용해 보세요"

  items:
    # items loop
    - title: ".NET"
      color: "blue"
      link: "/parser/net/"

    # items loop
    - title: "Java"
      color: "red"
      link: "/parser/java/"   

############################# FAQ ###############################
faq:
  enable: true
  title: "자주 묻는 질문"
  description: "가장 자주 묻는 질문에 대한 답변입니다."

  items:
    # items loop
    - question: "문서를 조작하려면 GroupDocs.Parser 라이브러리에 다른 타사 소프트웨어가 필요합니까?"
      answer: "GroupDocs.Parser은 Adobe Acrobat, Microsoft Office 등과 같은 외부 소프트웨어를 설치할 필요가 없습니다."

    # items loop
    - question: "구매하기 전에 GroupDocs.Parser 라이브러리를 사용해 볼 수 있나요?"
      answer: "예, 라이센스를 구매하지 않고도 GroupDocs.Parser을 사용해 볼 수 있습니다. 라이센스 없이 설치하면 라이브러리는 평가판 모드에서 작동합니다. 이 모드에서는 결과 문서에 평가판 배지가 추가되고 처음 3페이지로 잘립니다. 평가판의 제한 없이 GroupDocs.Parser을 테스트하고 싶다면 30일 임시 라이센스를 요청할 수도 있습니다. 자세한 내용은 다음을 참조하세요. [purchase.groupdocs.com/temporary-license/](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "어떤 라이선스를 갖고 있나요?"
      answer: "우리는 특정 개발자나 회사의 요구에 맞게 여러 가지 라이선스 유형을 제공합니다. 라이선스 유형은 개발자 수, 개발자 사이트 위치 수, 최종 고객에게 SDK/API를 제공해야 하는지 여부에 따라 달라집니다. 또는 제품의 월별 사용량을 기준으로 측정 라이센스를 선택할 수 있습니다. 자세히 알아보기 [purchase.groupdocs.com/policies/](https://purchase.groupdocs.com/policies/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser 로우 코드 API"
  description: "클라우드 기반 REST API를 사용하여 모든 애플리케이션에 문서 파서 기능을 통합합니다."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "지원되는 광범위한 파일 형식에 걸쳐 문서를 파싱하는 전체 문서 파서 Cloud API용 cURL 명령입니다."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "이미지, 텍스트, 문서 정보를 추출하거나 Microsoft .NET 애플리케이션에서 사용자 정의 템플릿으로 모든 문서를 구문 분석할 수도 있습니다."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Java 개발자가 문서를 구문 분석하고 Java 기반 애플리케이션 내에서 문서 정보 및 데이터를 추출하기 위한 Cloud SDK입니다."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser NoCode 앱"
  description: "브라우저에서 직접 50개 이상의 널리 사용되는 파일 형식에 대한 구문 분석을 수행할 수 있는 웹 기반 애플리케이션입니다."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Word, Excel, PowerPoint, PDF 외 30개 이상의 문서 유형을 구문 분석하는 무료 온라인 앱입니다."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "웹 브라우저에서 직접 Word 문서를 구문 분석하여 이미지, 텍스트 또는 메타데이터를 추출합니다."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "모든 플랫폼이나 기기에서 제한 없이 작동하는 무료 PDF 구문 분석 앱입니다."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"     


---