


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: ko
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Java 앱에서 DOCX 문서의 테이블을 가져오기"
head_description: "GroupDocs.Parser를 사용하여 Java 애플리케이션에서 DOCX 파일의 구조화된 표 데이터를 추출합니다. 외부 도구는 필요하지 않습니다."

############################# Header ############################
title: "Java를 사용하여 DOCX에서 테이블 데이터 가져오기" 
description: "Java 워크플로우에서 GroupDocs.Parser를 사용하여 PDF, DOCX, XLSX와 같은 형식에서 테이블을 원활하게 감지하고 추출합니다."
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
    title: "GroupDocs.Parser for Java API 소개"
    link: "/parser/java/"
    link_title: "더 알아보기"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/)는 Java 플랫폼을 위한 기능이 풍부한 콘텐츠 추출 API입니다. 개발자는 PDF, Word 문서, Excel 시트, PowerPoint 프레젠테이션 등에서 테이블, 텍스트, 그래픽, 링크 및 구조화된 데이터를 정확하게 구문 분석할 수 있으며, 제3자 플러그인이 필요하지 않습니다.

############################# Steps ############################
steps:
    enable: true
    title: "Java에서 Docx 문서의 테이블을 가져오는 방법"
    content: |
      [GroupDocs.Parser](/parser/java/)를 사용하여 DOCX 문서에서 테이블을 구문 분석하려면 Java 환경에서 다음 단계를 따르십시오:
      
      1. Parser 인스턴스를 생성하고 대상 DOCX 파일을 로드합니다.
      2. 파일이 구조화된 테이블 추출을 지원하는지 확인합니다.
      3. API를 사용하여 문서에서 테이블 요소를 가져옵니다.
      4. 분석, 보고서 또는 자동화 시스템에서 추출된 데이터를 활용합니다.
   
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
        // 테이블 요소를 포함하는 Parser가 있는 입력 문서를 로드합니다.
        try (Parser parser = new Parser("input.docx"))
        {
            // 문서 유형이 테이블 인식을 허용하는지 확인합니다.
            if (!parser.getFeatures().isTables()) {
                System.out.println("테이블을 지원하지 않는 파일에 대한 논리를 추가합니다.");
                return;
            }

            // 테이블 구조 해석 규칙을 정의합니다.
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // 테이블 추출 파라미터를 설정합니다.
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  로드된 문서에서 테이블 추출을 실행합니다.
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  결과에서 추출된 각 테이블을 처리합니다.
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "고급 콘텐츠 추출 도구"
  description: "테이블을 읽는 것을 넘어 GroupDocs.Parser는 문서를 처리하는 작업을 향상시키기 위해 일반 텍스트, 시각적 요소, 임베디드 메타데이터 및 구조화된 객체를 캡처하는 기능을 지원합니다."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "구조화된 콘텐츠 및 표 데이터를 추출하는 모습"
  features:
    # feature loop
    - title: "형식에 따른 정확한 테이블 파싱"
      content: "PDF, Word, Excel, HTML과 같은 표준 문서 유형에서 테이블을 높은 정확도로 추출하는 것을 지원합니다."

    # feature loop
    - title: "다양한 소스에서 표 구조 읽기"
      content: "스프레드시트, 문서 및 보고서에서 테이블 데이터를 가져오면서 구조와 정렬을 유지합니다."

    # feature loop
    - title: "사용자 정의 가능한 테이블 추출 설정"
      content: "레이아웃 감지를 제어하고, 헤더 및 푸터를 관리하며, 유연한 구성 옵션으로 추출을 세부 조정할 수 있습니다."
      
  code_samples:
    # code sample loop
    - title: "샘플: Excel 문서에서 테이블 추출"
      content: |
        이 예제는 GroupDocs.Parser를 사용하여 Excel (XLSX) 파일에서 테이블 내용을 추출하고 반복하는 방법을 보여줍니다.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Parser를 Excel 파일로 초기화합니다.
        try (Parser parser = new Parser("input.pdf"))
        {
            // 이 문서에 대해 테이블 추출이 지원되지 않으면 종료합니다.
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // 테이블 레이아웃을 찾기 위한 규칙을 적용합니다.
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // 테이블 추출 설정을 구성합니다.
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // 추출 프로세스를 호출합니다.
            Iterable<PageTableArea> tables = parser.getTables(options);

            // 모든 파싱된 테이블 구조를 반복합니다.
            for (PageTableArea t : tables)
            {
                // 테이블 내의 각 행을 반복합니다.
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // 현재 행 내의 각 셀을 처리합니다.
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // 현재 셀의 내용을 접근하고 읽습니다.
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // 각 테이블 셀의 텍스트 값을 출력합니다.
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                }
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
    title: "테이블 추출을 지원하는 문서 유형"
    exclude: "DOCX"
    description: "GroupDocs.Parser는 여러 파일 유형에 걸쳐 신뢰할 수 있는 테이블 감지를 제공합니다. 다음은 테이블을 추출하는 데 가장 많이 지원되는 문서 형식의 목록입니다."
    items: 
        # format loop 1
        - name: "PDF 파싱"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(휴대 문서 형식)"
          
        # format loop 2
        - name: "DOCX 파싱"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(Office 2007+ 워드 문서)"
          
        # format loop 3
        - name: "PPTX 파싱"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(Open XML 프레젠테이션 형식)"
          
        # format loop 4
        - name: "XLSX 파싱"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(Open XML 워크북)"
          
        # format loop 5
        - name: "TXT 파싱"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(텍스트 파일)"
          
        # format loop 6
        - name: "RTF 파싱"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(리치 텍스트 형식)"
          
        # format loop 7
        - name: "XML 파싱"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(확장 마크업 언어)"
          
        # format loop 8
        - name: "EPUB 파싱"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(오픈 전자책 파일)"
         
          

---