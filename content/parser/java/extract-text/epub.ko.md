


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:45
draft: false
lang: ko
format: Epub
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java 애플리케이션에서 EPUB 파일의 텍스트 추출하기"
head_description: "GroupDocs.Parser를 활용하여 Java에서 EPUB 문서의 비정형 또는 구조화된 텍스트 콘텐츠를 외부 의존성 없이 추출하세요."

############################# Header ############################
title: "Java를 사용하여 EPUB의 텍스트를 추출하세요" 
description: "GroupDocs.Parser를 사용하여 PDF, Word, Excel 등과 같은 파일에서 읽을 수 있는 텍스트 또는 구조화된 텍스트를 원활하게 추출하세요. 이를 통해 Java 개발 프로젝트를 더욱 발전시킬 수 있습니다."
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
    title: "GroupDocs.Parser for Java API 소개"
    link: "/parser/java/"
    link_title: "더 알아보기"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/)는 Java 개발자를 위해 설계된 강력하고 확장 가능한 문서 파서입니다. PDF, DOCX, XLSX, PPTX 등 다양한 형식에서 텍스트, 테이블, 이미지 및 구조화된 구성 요소를 정확하게 추출할 수 있는 기능을 제공합니다—외부 유틸리티에 의존하지 않고.

############################# Steps ############################
steps:
    enable: true
    title: "Java를 사용하여 Epub에서 텍스트를 추출하는 방법"
    content: |
      [GroupDocs.Parser](/parser/java/)를 사용하여 Java 프로젝트 내에서 EPUB 파일에서 텍스트를 추출하려면 아래 단계를 따르세요:
      
      1. Parser 클래스를 사용하여 EPUB 문서 로드.
      2. 파일 콘텐츠에서 텍스트 추출 수행.
      3. 텍스트가 성공적으로 검색되었는지 확인.
      4. 검색, 분석 또는 자동화 시스템에서 텍스트 데이터를 사용.
   
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
        // 문서로 Parser 초기화
        try (Parser parser = new Parser("input.epub"))
        {
            // 모든 텍스트 데이터 읽고 추출
            try (TextReader reader = parser.getText())
            {
                // 텍스트 콘텐츠가 없는 경우 null 반환
                // 추출된 텍스트를 워크플로우에 통합
                System.out.println(reader == null ? 
                    "지원되지 않는 텍스트 추출 형식은 건너뛰기" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "풍부한 텍스트 추출 기능"
  description: "GroupDocs.Parser는 단순한 텍스트 추출을 넘어 이미지, 메타데이터 및 구조화된 데이터의 검색을 지원하여 콘텐츠 처리 작업을 향상시킵니다."
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "문서에서 텍스트 콘텐츠 추출 및 구조화"
  features:
    # feature loop
    - title: "다양한 문서 형식에서 작동"
      content: "DOCX, XLSX, PPTX, PDF, HTML 등 여러 형식에서 원시 및 구조화된 텍스트를 캡처."

    # feature loop
    - title: "시각적 및 텍스트 콘텐츠에서 텍스트 추출"
      content: "논리 구조를 유지하면서 스캔된 문서, 슬라이드, 스프레드시트 및 기타 파일 유형에서 텍스트 파싱."

    # feature loop
    - title: "추출 프로세스에 대한 세부 제어"
      content: "정밀한 텍스트 파싱을 위해 페이지 범위, 레이아웃 영역 및 정확도 매개변수를 구성."
      
  code_samples:
    # code sample loop
    - title: "샘플: PPTX 문서에서 텍스트 영역 추출"
      content: |
        이 샘플은 GroupDocs.Parser를 사용하여 PowerPoint 프레젠테이션에서 텍스트 블록과 그 공간 좌표를 추출하는 방법을 보여줍니다.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Parser API로 PPTX 파일 로드
        try (Parser parser = new Parser("input.pptx"))
        {
            // 모든 직사각형 텍스트존 가져오기
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // 이 기능이 지원되지 않으면 종료
            if (areas == null)
            {
                return;
            }

            // 페이지별로 텍스트 영역 반복
            for (PageTextArea a : areas)
            {
                // 각 텍스트 블록을 페이지 번호와 경계 사각형으로 처리
                System.out.println(String.format("Page: %d, R: %s, Text: %s", a.getPage().getIndex(), a.getRectangle(), a.getText()));
            }
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
    title: "텍스트 추출을 지원하는 파일 유형"
    exclude: "EPUB"
    description: "GroupDocs.Parser는 수많은 파일 및 이미지 형식에서 텍스트 콘텐츠를 추출할 수 있습니다. 아래는 지원되는 가장 일반적인 유형입니다."
    items: 
        # format loop 1
        - name: "PDF 파싱"
          format: "PDF"
          link: "/parser/java/extract-text/pdf/"
          description: "(휴대 문서 형식)"
          
        # format loop 2
        - name: "DOCX 파싱"
          format: "DOCX"
          link: "/parser/java/extract-text/docx/"
          description: "(Office 2007+ 워드 문서)"
          
        # format loop 3
        - name: "PPTX 파싱"
          format: "PPTX"
          link: "/parser/java/extract-text/pptx/"
          description: "(Open XML 프레젠테이션 형식)"
          
        # format loop 4
        - name: "XLSX 파싱"
          format: "XLSX"
          link: "/parser/java/extract-text/xlsx/"
          description: "(Open XML 워크북)"
          
        # format loop 5
        - name: "TXT 파싱"
          format: "TXT"
          link: "/parser/java/extract-text/txt/"
          description: "(텍스트 파일)"
          
        # format loop 6
        - name: "RTF 파싱"
          format: "RTF"
          link: "/parser/java/extract-text/rtf/"
          description: "(리치 텍스트 형식)"
          
        # format loop 7
        - name: "XML 파싱"
          format: "XML"
          link: "/parser/java/extract-text/xml/"
          description: "(확장 마크업 언어)"
          
        # format loop 8
        - name: "EPUB 파싱"
          format: "EPUB"
          link: "/parser/java/extract-text/epub/"
          description: "(오픈 전자책 파일)"
         
          

---