


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: ko
format: Odp
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java 애플리케이션에서 ODP 파일의 이미지를 추출합니다"
head_description: "GroupDocs.Parser를 사용하면 Java에서 ODP 파일의 이미지를 외부 도구 없이 쉽게 추출할 수 있습니다."

############################# Header ############################
title: "Java를 사용하여 ODP에서 이미지를 추출합니다" 
description: "GroupDocs.Parser를 사용하여 PDF, Word, Excel 등 다양한 파일에서 임베드된 이미지를 Java 개발 환경에서 검색할 수 있습니다."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "무료 체험판 다운로드"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for Java란 무엇인가요?"
    link: "/parser/java/"
    link_title: "더 알아보기"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/)는 Java 개발자를 위해 설계된 기능이 풍부한 파싱 API입니다. 이 API는 다양한 파일 형식(DOCX, XLSX, PDF, PNG, JPG 등)에서 이미지, 텍스트, 링크 및 구조화된 요소를 추출할 수 있도록 합니다. 외부 라이브러리나 응용 프로그램 없이도 가능합니다.

############################# Steps ############################
steps:
    enable: true
    title: "Java에서 Odp의 이미지를 추출하는 방법"
    content: |
      [GroupDocs.Parser](/parser/java/)를 사용하여 Java 애플리케이션에서 ODP 문서에서 이미지를 추출하는 방법은 다음과 같습니다:
      
      1. Parser 인스턴스를 생성하고 ODP 파일을 로드합니다.
      2. 로드된 문서에서 이미지 데이터를 추출합니다.
      3. 필요에 따라 추출된 이미지를 사용하거나 내보냅니다.
   
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
        // Parser를 사용하여 파서를 초기화하고 이미지를 포함한 문서를 로드합니다.
        try (Parser parser = new Parser("input.odp"))
        {
            // 문서에 포함된 모든 이미지 요소를 수집합니다.
            Iterable<PageImageArea> images = parser.getImages();

            // 문서에 이미지가 없으면 처리를 건너뜁니다.
            if (images == null) {
                return;
            }

            // 필요한 대로 각 이미지를 처리합니다.
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "문서 파싱을 위한 추가 기능"
  description: "이미지 추출 외에도 GroupDocs.Parser를 사용하면 텍스트, 링크, 메타데이터 및 구조화된 데이터를 추출하여 처리 및 분석할 수 있습니다."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "문서에서 이미지 및 콘텐츠를 추출합니다."
  features:
    # feature loop
    - title: "다양한 형식 지원"
      content: "PDF, DOCX, PPTX, XLSX와 같은 다양한 문서 유형과 PNG, JPEG, GIF와 같은 이미지 형식에서 이미지를 추출합니다."

    # feature loop
    - title: "이미지 선명도 및 해상도 유지"
      content: "모든 추출된 이미지는 원래 해상도와 파일 형식을 유지하여 일관된 품질과 사용성을 보장합니다."

    # feature loop
    - title: "유연한 구성 옵션"
      content: "형식, 크기, 페이지 인덱스 또는 파일 형식별로 이미지를 필터링하여 이미지 추출 프로세스를 사용자 지정할 수 있습니다."
      
  code_samples:
    # code sample loop
    - title: "PDF 파일에서 이미지 추출 및 저장"
      content: |
        이 예제에서는 PDF 문서에서 이미지를 추출하고 이를 개별적으로 장치에 저장하는 방법을 보여줍니다.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Parser를 사용하여 PDF 파일을 엽니다.
        try (Parser parser = new Parser("input.pdf"))
        {
            // 문서 콘텐츠에서 이미지를 가져옵니다.
            Iterable<PageImageArea> images = parser.getImages();

            // 형식(예: JPEG 또는 PNG)과 같은 출력 매개변수를 설정합니다.
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // 추출된 이미지를 로컬 디렉터리에 저장합니다.
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
                imageNumber++;
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
    title: "이미지 추출을 위한 지원 파일 형식"
    exclude: "ODP"
    description: "GroupDocs.Parser는 다양한 문서 및 이미지에서 이미지 추출을 지원합니다. 아래에서 일반적으로 지원되는 형식을 탐색해 보세요."
    items: 
        # format loop 1
        - name: "PDF 파싱"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(휴대 문서 형식)"
          
        # format loop 2
        - name: "DOCX 파싱"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Office 2007+ 워드 문서)"
          
        # format loop 3
        - name: "PPTX 파싱"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Open XML 프레젠테이션 형식)"
          
        # format loop 4
        - name: "XLSX 파싱"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Open XML 워크북)"
          
        # format loop 5
        - name: "ODT 파싱"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(OpenDocument 텍스트 문서)"
          
        # format loop 6
        - name: "ODS 파싱"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(OpenDocument 스프레드시트)"
          
        # format loop 7
        - name: "ODP 파싱"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(OpenDocument 프레젠테이션)"
          
        # format loop 8
        - name: "EPUB 파싱"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(오픈 전자책 파일)"
          
        # format loop 9
        - name: "FB2 파싱"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(픽션북 전자책)"
         
          

---