


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: ko
format: Pdf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java 앱에서 PDF 파일의 하이퍼링크 추출"
head_description: "GroupDocs.Parser를 사용하여 Java 프로젝트의 PDF 문서에서 URL 링크를 찾아 추출하세요. 추가 소프트웨어는 필요 없습니다."

############################# Header ############################
title: "Java로 PDF에서 하이퍼링크 추출" 
description: "GroupDocs.Parser를 사용하여 PDFs, Word 파일, Excel 시트 및 기타 문서에서 웹 링크와 하이퍼링크를 추출하세요. Java 환경에서 가능합니다."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "무료 체험 다운로드"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for Java API 소개"
    link: "/parser/java/"
    link_title: "더 알아보기"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/)는 Java 개발자를 위해 설계된 강력한 콘텐츠 추출 API입니다. 하이퍼링크, 구조화된 데이터, 이미지 및 텍스트를 DOCX, XLSX, PDF, HTML과 같은 인기 형식에서 추출하는 도구를 제공합니다. 외부 플러그인이 필요 없습니다.

############################# Steps ############################
steps:
    enable: true
    title: "Java에서 Pdf의 하이퍼링크를 추출하는 방법"
    content: |
      [GroupDocs.Parser](/parser/java/)는 Java 애플리케이션에서 PDF 파일의 하이퍼링크 추출을 위한 기본 단계로 다음을 제공합니다:
      
      1. Parser의 인스턴스를 사용하여 PDF 파일을 엽니다.
      2. 파일 형식에서 하이퍼링크 추출이 가능함을 확인합니다.
      3. 적절한 메서드를 사용하여 모든 하이퍼링크를 추출합니다.
      4. 결과를 반복하여 각 링크를 필요에 따라 처리합니다.
   
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
        // Parser를 사용하여 하이퍼링크가 포함될 수 있는 파일을 불러옵니다.
        try (Parser parser = new Parser("input.pdf")) {

            // 문서 형식이 하이퍼링크 파싱을 지원하는지 확인합니다.
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("파일에 대한 하이퍼링크 추출이 불가능합니다.");
                return;
            }

            // 문서에서 하이퍼링크 데이터를 추출하고 사용합니다.
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "종합적인 문서 파싱 도구"
  description: "GroupDocs.Parser는 하이퍼링크 추출 외에도, 자동화된 워크플로우에 사용될 수 있는 일반 텍스트, 임베디드 미디어 및 구조화된 데이터와 같은 유용한 콘텐츠를 수집할 수 있도록 합니다."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "하이퍼링크 추출 및 문서 분석"
  features:
    # feature loop
    - title: "정확한 링크 탐지"
      content: "클릭 가능한 텍스트와 숨겨진 URL을 포함한 다양한 문서 레이아웃에서 모든 유형의 하이퍼링크를 캡처합니다."

    # feature loop
    - title: "문서 및 웹 콘텐츠와 호환"
      content: "하이퍼링크가 포함된 PDF, DOCX, XLSX, HTML 및 이미지 파일에서 링크를 추출합니다."

    # feature loop
    - title: "사용자 정의 추출 동작"
      content: "페이지 범위, 링크 유형 또는 콘텐츠 필터와 같은 옵션을 사용하여 하이퍼링크 추출 방식을 세밀하게 조정합니다."
      
  code_samples:
    # code sample loop
    - title: "예제: 사용자 정의 옵션이 있는 PDF에서 하이퍼링크 추출"
      content: |
        이 샘플은 링크 추출 설정을 사용하여 PDF 파일에서 모든 링크를 추출하는 방법을 보여줍니다.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Parser 클래스를 사용하여 PDF를 엽니다.
        try (Parser parser = new Parser("input.docx"))
        {
            // 이 문서에 대해 하이퍼링크 지원이 활성화되어 있는지 확인합니다.
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // 링크 필터링을 위한 옵션을 적용합니다.
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // 파서를 사용하여 하이퍼링크 데이터를 가져옵니다.
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // 링크를 반복하고 적절히 처리합니다.
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    title: "하이퍼링크 추출을 지원하는 문서 형식"
    exclude: "PDF"
    description: "GroupDocs.Parser를 사용하면 일반적으로 사용되는 다양한 파일 형식에서 하이퍼링크를 추출할 수 있습니다. 일반적으로 지원되는 형식 목록은 다음과 같습니다."
    items: 
        # format loop 1
        - name: "PDF 파싱"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(휴대 문서 형식)"
          
        # format loop 2
        - name: "DOCX 파싱"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Office 2007+ 워드 문서)"
          
        # format loop 3
        - name: "PPTX 파싱"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Open XML 프레젠테이션 형식)"
          
        # format loop 4
        - name: "XLSX 파싱"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Open XML 워크북)"
          
        # format loop 5
        - name: "TXT 파싱"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(텍스트 파일)"
          
        # format loop 6
        - name: "RTF 파싱"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(리치 텍스트 형식)"
          
        # format loop 7
        - name: "XML 파싱"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(확장 마크업 언어)"
          
        # format loop 8
        - name: "EPUB 파싱"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(오픈 전자책 파일)"
         
          

---