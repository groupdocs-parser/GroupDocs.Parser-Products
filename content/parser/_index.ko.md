---
############################# Static ############################
layout: "family"
date:  2025-06-30T10:26:00
draft: false

product: "Parser"
product_tag: "parser"

lang: ko

############################# Head ############################
head_title: ".NET, Java, 클라우드 API 및 온라인 문서 파서 앱"
head_description: ".NET, Java 및 클라우드 기반 애플리케이션을 위한 올인원 문서 파싱 솔루션을 얻으십시오. 간단한 드래그 앤 드롭 기능으로 온라인에서 문서 형식의 데이터를 추출하세요."

############################# Header ############################
title: "문서 파싱 솔루션"
description:  |
  다양한 파일 형식에서 데이터 추출을 위한 강력한 API입니다.

  최소한의 코딩으로 문서를 파싱하세요.

  파싱 결과를 사용자 맞춤화하세요.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "플랫폼 선택하기"
  title: "플랫폼 독립성"
  description: "GroupDocs.Parser 라이브러리는 다음 운영 체제와 프레임워크를 지원합니다:"
  details_link_title: "자세히 알아보기"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser .NET 
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
      description: GroupDocs.Parser Java
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

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser 개요"
  description: "PDF, Word, Excel 등 다양한 문서에서 데이터를 파싱하기 위한 API입니다."

  items:
    # items loop
    - icon: "text"
      title: "텍스트 추출"
      content: "다양한 파일 형식에서 텍스트 정보를 추출합니다."

    # items loop
    - icon: "image"
      title: "이미지 추출"
      content: "다양한 소스에서 비주얼 콘텐츠를 가져옵니다."

    # items loop
    - icon: "template"
      title: "템플릿에 따른 데이터 파싱"
      content: "사용자 정의 템플릿을 생성하고 이를 활용하여 특정 정보를 파싱합니다."

    # items loop
    - icon: "pdf"
      title: "PDF 양식 파싱"
      content: "PDF 양식은 사용자 상호작용을 위한 작성 가능한 필드가 포함된 디지털 문서입니다."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser 코드 샘플"
  description: "C# 및 Java에서의 전형적인 GroupDocs.Parser 작업 사례 몇 가지"

  items:
    # items loop
    - title: "PDF 문서에서 텍스트 추출하기"
      content: "GroupDocs.Parser API는 몇 가지 단계를 구현하여 문서에서 텍스트를 추출하는 것을 돕습니다."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
                    <code class="language-csharp" data-lang="csharp">

                        // Parser 클래스의 인스턴스를 생성하고 원하는 파일을 전달하세요.
                        using (var parser = new Parser("source.pdf"))
                        {
                            // 텍스트 추출하기
                            using (var textReader = parser.GetText())
                            {
                                // 추출된 텍스트를 처리하기
                                Console.WriteLine(textReader?.ReadToEnd());
                            }
                        }     
                        
                    </code>

          # samples loop
          - language: "Java"
            color: "red"
            content: |
                    <code class="language-java" data-lang="java">

                        // Parser 클래스의 인스턴스를 생성하고 원하는 파일을 전달하세요.
                        try (Parser parser = new Parser("source.pdf"))
                        {
                            // 텍스트 추출하기
                            try (TextReader reader = parser.getText())
                            {
                                // 추출된 텍스트를 처리하기
                                System.out.println(reader == null 
                                        ? "" 
                                        : reader.readToEnd());
                            }
                        }  

                    </code>


############################# Supported Formats ###############################
formats:
  enable: true
  title: "50개 이상의 지원 파일 형식"
  description: "GroupDocs.Parser는 다양한 형식 가족 내에서 파서 작업을 지원합니다."

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser 업적"
  description: "우리 라이브러리의 주요 성과 지표를 확인하세요."

  items:
    # items loop
    - number: "50+"
      title: "지원되는 형식"
      content: "GroupDocs.Parser는 50개 이상의 인기 파일 형식과의 작업을 지원합니다."

    # items loop
    - number: "1600k"
      title: "NuGet 다운로드"
      content: "GroupDocs.Parser .NET NuGet 패키지는 1,600,000회 이상 다운로드되었습니다."

    # items loop
    - number: "18k"
      title: "Maven 다운로드"
      content: "GroupDocs.Parser는 Maven에서 18,000회 다운로드되었습니다. 강력한 Java 파싱 기능."

    # items loop
    - number: "140+"
      title: "만족한 고객"
      content: "유명한 기업과 개인 개발자들이 혁신적인 솔루션 구축을 위해 GroupDocs 제품을 선호합니다."


############################# Customers ###############################
customers:
  enable: true
  title: "우리의 만족한 고객들"
  description: "GroupDocs 라이브러리는 전세계적으로 저명한 브랜드에 의해 사용되고 있습니다."

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
  description: "GroupDocs.Parser 기능을 귀하의 플랫폼에서 무료로 체험하세요."

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
  description: "가장 많이 묻는 질문에 대한 답변입니다."

  items:
    # items loop
    - question: "GroupDocs.Parser 라이브러리는 문서 작업을 위해 다른 서드파티 소프트웨어가 필요합니까?"
      answer: "GroupDocs.Parser는 Adobe Acrobat, Microsoft Office 또는 기타 외부 소프트웨어가 설치될 필요가 없습니다."

    # items loop
    - question: "GroupDocs.Parser 라이브러리를 구매 전에 시험해볼 수 있습니까?"
      answer: "예, 라이선스 없이 GroupDocs.Parser를 시험해볼 수 있습니다. 라이선스 없이 설치하면 라이브러리는 시험 모드로 작동합니다. 이 모드에서는 결과 문서에 시험 배지가 추가되고 첫 3페이지로 제한됩니다. 시험 버전의 제한 없이 GroupDocs.Parser를 테스트하고 싶다면, 30일 임시 라이선스를 요청할 수도 있습니다. 자세한 내용은 [여기](https://purchase.groupdocs.com/temporary-license/)에서 확인하세요."

    # items loop
    - question: "어떤 라이선스가 있습니까?"
      answer: "특정 개발자나 회사의 요구에 맞는 여러 라이선스 유형을 제공합니다. 라이선스 유형은 개발자 수, 개발자 사이트 위치 수 및 최종 고객에게 SDK/API를 전달할 필요성에 따라 다릅니다. 또는 제품의 월별 사용량에 따라 미터링 라이선스를 선택할 수 있습니다. 자세한 내용은 [여기](https://purchase.groupdocs.com/pricing/parser/net/)에서 확인하세요."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser 저코드 API"
  description: "클라우드 기반 REST API를 사용하여 모든 애플리케이션에 문서 파서 기능을 통합하세요."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "지원되는 인기 파일 형식 전반에서 문서를 파싱하기 위한 RESTful 문서 파서 클라우드 API의 cURL 명령입니다."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Microsoft .NET 애플리케이션에서 이미지, 텍스트, 문서 정보를 추출하거나 사용자 정의 템플릿으로 문서를 파싱하세요."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Java 기반 애플리케이션에서 문서를 파싱하고 문서 정보 및 데이터를 추출할 수 있는 Java 개발자를 위한 클라우드 SDK입니다."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser 노코드 앱"
  description: "브라우저에서 직접 50개 이상의 인기 파일 형식에 대해 파싱을 수행할 수 있는 웹 기반 애플리케이션입니다."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Word, Excel, PowerPoint, PDF 및 50개 이상의 문서 형식을 파싱할 수 있는 무료 온라인 앱입니다."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "웹 브라우저에서 Word 문서를 직접 파싱하여 이미지, 텍스트 또는 메타데이터를 추출하세요."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "모든 플랫폼 또는 장치에서 제한 없이 작동하는 무료 PDF 파싱 앱입니다."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---