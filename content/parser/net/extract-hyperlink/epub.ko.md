


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: ko
format: Epub
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "C# 앱에서 EPUB 파일의 하이퍼링크 추출"
head_description: "GroupDocs.Parser를 사용하여 C#에서 추가 도구나 소프트웨어 없이 EPUB 파일의 하이퍼링크를 감지하고 추출하세요."

############################# Header ############################
title: "C#를 사용한 EPUB 하이퍼링크 추출" 
description: "GroupDocs.Parser를 사용하여 PDF, Word, Excel 및 기타 문서 유형에서 URL과 하이퍼링크를 감지하고 추출하세요."
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
    title: "GroupDocs.Parser for .NET API에 대하여"
    link: "/parser/net/"
    link_title: "더 알아보기"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/)는 .NET 개발자를 위한 다용도 문서 파싱 API입니다. PDF, Word, Excel, HTML 등의 다양한 파일 형식에서 하이퍼링크, 텍스트, 이미지 및 구조화된 내용을 추출하는 기능을 제공하며, 외부 소프트웨어에 의존하지 않습니다.

############################# Steps ############################
steps:
    enable: true
    title: "C#에서 Epub에서 하이퍼링크를 추출하는 단계"
    content: |
      [GroupDocs.Parser](/parser/net/)는 .NET 개발자가 다음 간단한 단계를 따르세요: EPUB 파일에서 하이퍼링크를 추출할 수 있습니다.
      
      1. Parser 인스턴스를 사용하여 EPUB 파일을 로드합니다.
      2. 문서가 하이퍼링크 추출을 지원하는지 확인합니다.
      3. 문서에서 하이퍼링크 목록을 검색합니다.
      4. 결과를 루프하여 추출된 URL을 사용합니다.
   
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
        // 하이퍼링크가 포함된 문서를 Parser 클래스를 사용하여 로드합니다.
        using (Parser parser = new Parser("input.epub")) {

            // 파일이 하이퍼링크 추출을 지원하는지 확인합니다.
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("해당 파일에서는 하이퍼링크 추출을 사용할 수 없습니다.");
                return;
            }

            // 추출된 하이퍼링크를 검색하고 처리합니다.
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "고급 문서 파싱 기능"
  description: "하이퍼링크 추출 외에도 GroupDocs.Parser는 텍스트, 메타데이터, 이미지 및 구조화된 데이터를 추출할 수 있으며, 강력한 데이터 처리 작업 흐름을 지원합니다."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "하이퍼링크 감지 및 문서 파싱"
  features:
    # feature loop
    - title: "문서에서 하이퍼링크 감지"
      content: "PDF, Word 파일, 스프레드시트 등에서 URL과 링크 주석을 신속하게 추출합니다."

    # feature loop
    - title: "웹 및 삽입 링크 지원"
      content: "다양한 형식에서 표준 웹 URL 및 삽입 문서 링크를 감지하고 추출합니다."

    # feature loop
    - title: "유연한 파싱 옵션"
      content: "성능과 정확성을 향상시키기 위해 특정 섹션이나 페이지를 스캔할 수 있도록 추출 설정을 사용자 정의합니다."
      
  code_samples:
    # code sample loop
    - title: "링크 옵션을 사용하여 PDF에서 하이퍼링크 추출하는 방법"
      content: |
        이 코드 예제에서는 사용자 지정 옵션을 사용하여 PDF 파일에서 모든 하이퍼링크를 추출하는 방법을 보여줍니다.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  PDF 문서로 Parser를 초기화합니다.
        using (Parser parser = new Parser("input.docx"))
        {
            // 하이퍼링크 추출이 지원되는지 확인합니다.
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // 결과를 좁히기 위해 링크 추출 옵션을 설정합니다.
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // 문서에서 하이퍼링크 데이터를 추출합니다.
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // 추출된 링크 목록을 처리합니다.
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    title: "하이퍼링크 추출 지원 형식"
    exclude: "EPUB"
    description: "GroupDocs.Parser는 다양한 문서 유형에서 하이퍼링크를 추출할 수 있습니다. 일반적으로 지원되는 형식은 아래를 참조하세요."
    items: 
        # format loop 1
        - name: "PDF 파싱"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(휴대 문서 형식)"
          
        # format loop 2
        - name: "DOCX 파싱"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Office 2007+ 워드 문서)"
          
        # format loop 3
        - name: "PPTX 파싱"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Open XML 프레젠테이션 형식)"
          
        # format loop 4
        - name: "XLSX 파싱"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Open XML 워크북)"
          
        # format loop 5
        - name: "TXT 파싱"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(텍스트 파일)"
          
        # format loop 6
        - name: "RTF 파싱"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(리치 텍스트 형식)"
          
        # format loop 7
        - name: "XML 파싱"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(확장 마크업 언어)"
          
        # format loop 8
        - name: "EPUB 파싱"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(오픈 전자책 파일)"
         
          

---