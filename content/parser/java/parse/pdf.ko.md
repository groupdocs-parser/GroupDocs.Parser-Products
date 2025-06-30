


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:50
draft: false
lang: ko
format: Pdf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java 애플리케이션에서 PDF 파일의 콘텐츠 추출"
head_description: "GroupDocs.Parser를 활용하여 Java에서 PDF 파일의 구조화된 데이터, 텍스트, 테이블 및 이미지를 파싱하고 검색할 수 있습니다. 외부 도구가 필요하지 않습니다."

############################# Header ############################
title: "Java에서 PDF 문서의 데이터 추출" 
description: "GroupDocs.Parser를 사용하여 PDFs, Word, Excel 및 이미지 기반 문서에서 텍스트, 메타데이터, 테이블 및 그래픽과 같은 구조화된 콘텐츠를 원활하게 추출해 보세요. Java 앱에서 가능합니다."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "무료 평가판 다운로드"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for Java란 무엇인가요?"
    link: "/parser/java/"
    link_title: "더 알아보기"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/)는 Java 개발자를 위해 구축된 강력한 API로, 고급 문서 파싱 기능을 제공합니다. PDF, DOCX, XLSX, PPTX 등 다양한 형식의 텍스트 데이터, 이미지, 테이블, 구조화된 필드 및 바코드를 추출하고 처리할 수 있으며, 추가 라이브러리 설치 없이 가능합니다.

############################# Steps ############################
steps:
    enable: true
    title: "Java를 사용하여 Pdf에서 데이터 추출 방법"
    content: |
      [GroupDocs.Parser](/parser/java/)를 사용하여 Java 프로젝트에서 PDF 문서에서 유용한 정보를 추출하려면 다음 지침을 따르세요:
      
      1. Parser 객체로 PDF 파일 열기.
      2. 파서를 사용하여 필요한 데이터(텍스트, 테이블, 메타데이터 등)를 검색합니다.
      3. 출력이 정확하고 완전한지 확인합니다.
      4. 파싱된 콘텐츠를 데이터 흐름, 비즈니스 프로세스 또는 애플리케이션에 통합합니다.
   
    code:
      platform: "net"
      copy_title: "복사"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "클릭하여 복사"
        copy_done: "복사되었습니다"
      links:
        #  loop
        - title: "더 많은 예시"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "문서화"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // 입력 문서로 Parser 초기화
        try (Parser parser = new Parser("input.pdf"))
        {
            // 문서에서 사용 가능한 모든 텍스트 콘텐츠 검색
            try (TextReader reader = parser.getText())
            {
                // 텍스트가 발견되지 않으면 반환 값이 null이 됩니다.
                // 추출된 콘텐츠를 솔루션에 통합
                System.out.println(reader == null ? 
                    "이 형식은 텍스트 추출을 지원하지 않을 수 있습니다." : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "다재다능한 문서 파싱 기능"
  description: "GroupDocs.Parser는 단순한 텍스트 추출을 넘어서 바코드, 메타데이터, 이미지, 테이블 및 기타 데이터를 전체적으로 파싱하여 지능형 자동화 및 데이터 기반 애플리케이션을 지원합니다."
  image: "/img/parser/features_parse.webp" # 500x500 px
  image_description: "문서 데이터 파싱 및 추출에 대한 시각적 개요"
  features:
    # feature loop
    - title: "여러 파일 형식에서 추출"
      content: "PDF, Word, Excel, PowerPoint, HTML 등 널리 사용되는 파일 유형에서 텍스트, 테이블 및 미디어와 같은 데이터에 접근할 수 있습니다."

    # feature loop
    - title: "디지털 및 스캔된 소스에서 콘텐츠 파싱"
      content: "원본 디지털 파일과 스캔된 이미지 모두에서 콘텐츠를 처리하며, 필요한 경우 OCR을 사용하여 내장된 텍스트를 해석합니다."

    # feature loop
    - title: "유연한 구성 옵션"
      content: "페이지 선택, 레이아웃 영역 및 특정 추출 요구 사항에 맞는 사용자 정의 필드 템플릿 설정으로 파싱을 조정하세요."
      
  code_samples:
    # code sample loop
    - title: "데이터 추출 템플릿을 사용한 PDF 파싱"
      content: |
        이 샘플은 GroupDocs.Parser를 통해 사용자 정의 템플릿을 사용하여 PDF에서 구조화된 필드를 추출하는 방법을 보여줍니다.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Parser 클래스를 사용하여 PDF를 엽니다.
        try (Parser parser = new Parser("input.pdf"))
        {
            // 정의된 데이터를 추출하기 위해 파싱 템플릿을 적용합니다.
            DocumentData data = parser.parseByTemplate(GetTemplate());

            // 템플릿 기반 추출이 가능한지 확인합니다.
            if (data == null) {
                return;
            }

            // 추출된 데이터 필드와 작업합니다.
            for (int i = 0; i < data.getCount(); i++) {
                System.out.print(data.get(i).getName() + ": ");
                PageTextArea area = data.get(i).getPageArea() instanceof PageTextArea
                        ? (PageTextArea) data.get(i).getPageArea() : null;
                System.out.println(area == null ? "Not a template field" : area.getText());
            }
        }

        private static Template GetTemplate()
        {
            // '세부정보' 섹션을 추출하기 위한 감지기 설정 정의
            TemplateTableParameters detailsTableParameters = 
                new TemplateTableParameters(new Rectangle(new Point(35, 320), new Size(530, 55)), null);

            TemplateItem[] templateItems = new TemplateItem[]
            {
                new TemplateTable(detailsTableParameters, "details", null)
            };

            Template template = new Template(java.util.Arrays.asList(templateItems));
            return template;
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "시작할 준비가 되셨나요?"
  description: "GroupDocs.Parser 기능을 무료로 사용해 보거나 라이센스를 요청하세요"
  items:
    #  loop
    - title: "Maven 다운로드"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "라이선스"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "내용 추출 지원 파일 형식"
    exclude: "PDF"
    description: "GroupDocs.Parser는 다양한 문서 및 이미지 파일 형식과 호환되며, 파싱 및 데이터 자동화 시나리오에서 일반적으로 사용되는 형식의 정보를 쉽게 추출할 수 있습니다."
    items: 
        # format loop 1
        - name: "PDF 파싱"
          format: "PDF"
          link: "/parser/java/parse/pdf/"
          description: "(휴대 문서 형식)"
          
        # format loop 2
        - name: "DOCX 파싱"
          format: "DOCX"
          link: "/parser/java/parse/docx/"
          description: "(Office 2007+ 워드 문서)"
          
        # format loop 3
        - name: "PPTX 파싱"
          format: "PPTX"
          link: "/parser/java/parse/pptx/"
          description: "(Open XML 프레젠테이션 형식)"
          
        # format loop 4
        - name: "XLSX 파싱"
          format: "XLSX"
          link: "/parser/java/parse/xlsx/"
          description: "(Open XML 워크북)"
          
        # format loop 5
        - name: "TXT 파싱"
          format: "TXT"
          link: "/parser/java/parse/txt/"
          description: "(텍스트 파일)"
          
        # format loop 6
        - name: "RTF 파싱"
          format: "RTF"
          link: "/parser/java/parse/rtf/"
          description: "(리치 텍스트 형식)"
          
        # format loop 7
        - name: "XML 파싱"
          format: "XML"
          link: "/parser/java/parse/xml/"
          description: "(확장 마크업 언어)"
          
        # format loop 8
        - name: "EPUB 파싱"
          format: "EPUB"
          link: "/parser/java/parse/epub/"
          description: "(오픈 전자책 파일)"
         
          

---