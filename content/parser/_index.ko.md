---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: ko

############################# Head ############################
head_title: "PDF, Word 및 Excel용 문서 파서 SDK | GroupDocs"
head_description: ".NET, Java 및 Python 앱용으로 PDF, Word, Excel, 이메일 및 50개 이상의 기타 문서 형식에서 텍스트, 이미지, 메타데이터, 바코드 및 표를 추출하는 Document Parser SDK."

############################# Header ############################
title: "문서 파서 SDK"
description:  |
  개발자 친화적인 Document Parser SDK로 50개 이상의 문서 및 이미지 형식에서 텍스트, 이미지, 바코드, 메타데이터 및 표를 추출합니다.

  .NET, Java 및 Python 애플리케이션에 최소한의 코드 작성으로 고성능 문서 파싱을 통합하세요.

  유연한 템플릿과 고급 API를 사용해 파싱 규칙을 맞춤 설정하고 정제된 구조화 데이터 출력을 제공합니다.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "플랫폼 선택"
  title: "플랫폼 독립성"
  description: "GroupDocs.Parser 라이브러리는 다음 운영 체제와 프레임워크를 지원합니다:"
  details_link_title: "자세히 보기"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser for .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    .NET Framework 4.6.2 or higher <br> .NET Core 2.0 or higher <br> .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    Microsoft Visual Studio <br> JetBrains Rider <br> Microsoft Visual Code
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser for Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Java 8 or higher <br> Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    IntelliJ IDEA <br> Eclipse <br> NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats


    # items loop
    - title: "Python"
      description: GroupDocs.Parser for Python
      color: "yellow"
      tag: "python-net"
      link: "/parser/python-net/"
      features_link: "https://docs.groupdocs.com/parser/python-net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Python 3.5+
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> macOS
      
          # features loop
          - rows: "4"
            content: |
                    PyCharm, VS Code, Jupyter Notebook
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats                    

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser 한눈에 보기"
  description: "PDF, Office 문서, 이미지, 이메일 및 아카이브에서 구조화 및 비구조화 데이터를 추출하는 강력한 Document Parser SDK."

  items:
    # items loop
    - icon: "text"
      title: "텍스트 추출"
      content: "다양한 파일 형식에서 텍스트 정보를 추출합니다"

    # items loop
    - icon: "image"
      title: "이미지 추출"
      content: "다양한 소스에서 시각적 콘텐츠를 가져옵니다"

    # items loop
    - icon: "template"
      title: "템플릿으로 데이터 파싱"
      content: "맞춤 템플릿을 생성하고 이를 사용해 특정 정보를 파싱합니다"

    # items loop
    - icon: "pdf"
      title: "PDF 양식 파싱"
      content: "PDF 양식은 사용자가 입력할 수 있는 필드를 포함한 디지털 문서입니다"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser 코드 샘플"
  description: "C#, Java 및 Python에서 일반적인 GroupDocs.Parser 작업의 몇 가지 사용 사례"

  items:
    # items loop
    - title: "PDF 문서에서 텍스트 추출 방법"
      content: "GroupDocs.Parser API는 몇 단계만 구현하면 문서에서 텍스트를 쉽게 추출할 수 있도록 합니다."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // 원하는 파일을 전달하여 Parser 클래스의 인스턴스를 생성합니다.
                using (var parser = new Parser("source.pdf"))
                {
                    // 텍스트 추출
                    using (var textReader = parser.GetText())
                    {
                        // 추출된 텍스트를 처리합니다.
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // 원하는 파일을 전달하여 Parser 클래스의 인스턴스를 생성합니다.
                try (Parser parser = new Parser("source.pdf"))
                {
                    // 텍스트 추출
                    try (TextReader reader = parser.getText())
                    {
                        // 추출된 텍스트를 처리합니다.
                        System.out.println(reader == null 
                                ? "" 
                                : reader.readToEnd());
                    }
                }  
              ```
          # samples loop
          - language: "Python"
            color: "green"
            content: |
              ```python {style=abap}
                from groupdocs.parser import Parser

                # 원하는 파일을 전달하여 Parser 클래스의 인스턴스를 생성합니다.
                with Parser("source.pdf") as parser:
                    # 텍스트 추출
                    text = parser.get_text()

                    # 추출된 텍스트를 처리합니다.
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "50개 이상의 문서 및 이미지 형식 지원"
  description: "GroupDocs.Parser Document Parser SDK는 Office 문서, PDF, 이미지, 이메일, 아카이브 등 다양한 형식에 대한 파싱 작업을 가능하게 합니다."

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser 성과"
  description: "우리 라이브러리 성과의 주요 지표를 확인하세요"

  items:
    # items loop
    - number: "50+"
      title: "지원되는 포맷"
      content: "GroupDocs.Parser는 50개 이상의 인기 파일 포맷을 지원합니다."

    # items loop
    - number: "1600k"
      title: "NuGet 다운로드"
      content: "GroupDocs.Parser .NET용 NuGet 패키지는 1,600,000회 이상 다운로드되었습니다."

    # items loop
    - number: "18k"
      title: "Maven 다운로드"
      content: "GroupDocs.Parser는 Maven에서 18,000회 다운로드되었습니다. 강력한 Java 파싱 기능."

    # items loop
    - number: "140+"
      title: "만족하는 고객"
      content: "유명 기업과 개인 개발자 모두 혁신적인 솔루션을 구축하기 위해 GroupDocs 제품을 선호합니다."


############################# Customers ###############################
customers:
  enable: true
  title: "우리의 만족하는 고객"
  description: "GroupDocs 라이브러리는 전 세계적으로 유명하고 저명한 브랜드에서 사용됩니다."

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
  description: "귀하의 플랫폼에서 GroupDocs.Parser 기능을 무료로 사용해 보세요."

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
    - question: "GroupDocs.Parser 라이브러리가 문서를 조작하기 위해 다른 타사 소프트웨어가 필요합니까?"
      answer: "GroupDocs.Parser는 Adobe Acrobat, Microsoft Office 등과 같은 외부 소프트웨어를 설치할 필요가 없습니다."

    # items loop
    - question: "GroupDocs.Parser 라이브러리를 구매하기 전에 체험할 수 있나요?"
      answer: "예, 라이선스를 구매하지 않고도 GroupDocs.Parser를 체험할 수 있습니다. 라이선스 없이 설치하면 라이브러리는 체험 모드로 작동합니다. 이 모드에서는 결과 문서에 체험 배지가 추가되고 처음 3페이지로 제한됩니다. GroupDocs.Parser를 체험 버전 제한 없이 테스트하려면 30일 임시 라이선스를 요청할 수도 있습니다. 자세한 내용은 [자세히 보기](https://purchase.groupdocs.com/temporary-license/)를 참고하십시오."

    # items loop
    - question: "어떤 라이선스를 제공하나요?"
      answer: "당사는 특정 개발자 또는 기업의 요구에 맞는 다양한 라이선스 유형을 제공합니다. 라이선스 유형은 개발자 수, 개발자 사이트 위치 수, 그리고 SDK/API를 최종 고객에게 제공해야 하는지 여부에 따라 결정됩니다. 또한 제품의 월별 사용량에 기반한 종량제 라이선스를 선택할 수도 있습니다. 자세한 내용은 [자세히 보기](https://purchase.groupdocs.com/pricing/parser/net/)에서 확인하십시오."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser 로우코드 문서 파서 API"
  description: "클라우드 기반 REST API 및 SDK를 사용하여 모든 애플리케이션에 문서 파싱 기능을 통합하십시오."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "지원되는 다양한 인기 파일 형식 전반에 걸쳐 문서를 파싱하기 위한 RESTful 문서 파서 클라우드 API용 cURL 명령."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Microsoft .NET 애플리케이션에서 사용자 정의 템플릿으로 이미지, 텍스트, 문서 정보를 추출하거나 모든 문서를 파싱할 수 있습니다."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Java 개발자를 위한 클라우드 SDK로 Java 기반 애플리케이션에서 문서를 파싱하고 문서 정보 및 데이터를 추출합니다."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser 문서 파서 노코드 앱"
  description: "웹 기반 문서 파서 앱으로 브라우저에서 직접 50개 이상의 인기 파일 형식에서 데이터를 추출할 수 있습니다."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Word, Excel, PowerPoint, PDF 및 50개 이상의 문서 형식을 파싱할 수 있는 무료 온라인 앱."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "웹 브라우저에서 직접 Word 문서를 파싱하여 이미지, 텍스트 또는 메타데이터를 추출합니다."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "제한 없이 모든 플랫폼이나 디바이스에서 작동하는 무료 PDF 파싱 앱."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---