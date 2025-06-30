


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:40
draft: false
lang: ko
format: Epub
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "C# 앱에서 EPUB 파일의 테이블 추출"
head_description: "GroupDocs.Parser을 사용하여 C# 애플리케이션에서 EPUB 파일의 구조화된 테이블 데이터를 찾고 추출할 수 있습니다. 추가 종속성 없이 가능합니다."

############################# Header ############################
title: "C#를 사용한 EPUB의 테이블 추출" 
description: "GroupDocs.Parser을 사용하여 PDF, Word, Excel 및 기타 파일 형식에서 테이블 구조를 신속하게 식별하고 추출하십시오. .NET 프로젝트에서 가능합니다."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "무료 평가판 다운로드"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for .NET API 소개"
    link: "/parser/net/"
    link_title: "더 알아보기"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/)는 .NET 개발자를 위해 구축된 포괄적인 문서 파싱 API입니다. PDF, DOCX, XLSX, PPTX 등과 같은 다양한 형식에서 텍스트, 테이블, 이미지, 하이퍼링크 및 기타 구조화된 요소를 정확하게 추출할 수 있으며, 제3자 소프트웨어가 필요하지 않습니다.

############################# Steps ############################
steps:
    enable: true
    title: "C#에서 Epub의 테이블을 추출하는 단계"
    content: |
      [GroupDocs.Parser](/parser/net/)를 사용하여 .NET 환경 내에서 EPUB 파일에서 테이블을 추출하기 위한 지침을 따라 주십시오:
      
      1. Parser 인스턴스를 초기화하고 EPUB 문서를 로드합니다.
      2. 입력 형식에 대한 테이블 추출 지원 여부를 확인합니다.
      3. 파일에서 테이블 내용을 추출합니다.
      4. 보고서 작성, 자동화 또는 분석을 위해 구조화된 테이블 데이터를 사용합니다.
   
    code:
      platform: "net"
      copy_title: "복사"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "클릭하여 복사"
        copy_done: "복사되었습니다"
      links:
        #  loop
        - title: "더 많은 예시"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "문서화"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Parser를 사용하여 테이블 데이터가 포함된 문서를 엽니다.
        using (Parser parser = new Parser("input.epub")) {

            // 해당 형식이 테이블 인식을 지원하는지 확인합니다.
            if (!parser.Features.Tables) {
                Console.WriteLine("테이블 파싱을 지원하지 않는 문서를 처리합니다.");
                return;
            }

            // 테이블 구조가 어떻게 인식되어야 하는지 정의합니다.
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // 테이블 데이터에 대한 추출 매개변수를 지정합니다.
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  파일 내용에서 테이블을 추출합니다.
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  감지된 각 테이블을 반복합니다.
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "강력한 데이터 추출 기능"
  description: "테이블 파싱 외에도 GroupDocs.Parser은 문서 자동화를 위한 텍스트 블록, 이미지, 메타데이터 및 기타 구조화된 데이터를 추출할 수 있습니다."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "테이블 인식 및 콘텐츠 추출"
  features:
    # feature loop
    - title: "정확한 다중 형식 테이블 감지"
      content: "DOCX, XLSX, PDF, HTML 및 유사한 형식에서 높은 정밀도로 표 형식 데이터를 추출합니다."

    # feature loop
    - title: "파일에서 테이블 구조 파싱"
      content: "형식 손실 없이 문서 및 스프레드시트에서 테이블 데이터를 효율적으로 검색합니다."

    # feature loop
    - title: "유연한 테이블 추출 구성"
      content: "출력을 위한 레이아웃 감지, 열 정렬, 머리말/바닥글 옵션을 조정하여 정확한 제어를 제공합니다."
      
  code_samples:
    # code sample loop
    - title: "Excel 스프레드시트에서 테이블 추출하는 방법"
      content: |
        이 코드 샘플은 GroupDocs.Parser을 사용하여 XLSX 파일에서 테이블 데이터를 읽고 반복하는 방법을 보여줍니다.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Parser API를 사용하여 Excel 파일을 엽니다.
        using (Parser parser = new Parser("input.xlsx"))
        {
            // 파일에서 테이블을 추출할 수 없으면 종료합니다.
            if (!parser.Features.Tables)
            {
                return;
            }

            // 레이아웃 규칙을 사용하여 표 형식 콘텐츠의 위치를 찾습니다.
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // 테이블에 대한 추출 매개변수를 설정합니다.
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // 테이블 추출 작업을 수행합니다.
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // 감지된 각 테이블 구조를 살펴봅니다.
            foreach (PageTableArea t in tables)
            {
                // 테이블의 각 행을 반복합니다.
                for (int row = 0; row < t.RowCount; row++)
                {
                    // 각 행의 셀을 반복합니다.
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // 현재 테이블 셀에 액세스합니다.
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // 각 셀의 텍스트 내용을 표시합니다.
                            Console.Write(cell.Text);
                            Console.Write(" | ");
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
    - title: "Nuget 다운로드"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "라이선스"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "테이블 추출을 위한 지원 형식"
    exclude: "EPUB"
    description: "GroupDocs.Parser은 다양한 문서 유형에서 테이블 데이터를 추출할 수 있습니다. 아래는 구조화된 테이블 파싱에 주로 사용되는 형식입니다."
    items: 
        # format loop 1
        - name: "PDF 파싱"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(휴대 문서 형식)"
          
        # format loop 2
        - name: "DOCX 파싱"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Office 2007+ 워드 문서)"
          
        # format loop 3
        - name: "PPTX 파싱"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Open XML 프레젠테이션 형식)"
          
        # format loop 4
        - name: "XLSX 파싱"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Open XML 워크북)"
          
        # format loop 5
        - name: "TXT 파싱"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(텍스트 파일)"
          
        # format loop 6
        - name: "RTF 파싱"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(리치 텍스트 형식)"
          
        # format loop 7
        - name: "XML 파싱"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(확장 마크업 언어)"
          
        # format loop 8
        - name: "EPUB 파싱"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(오픈 전자책 파일)"
         
          

---