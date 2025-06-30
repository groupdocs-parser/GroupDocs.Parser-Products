


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:34
draft: false
lang: ko
format: Ods
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "C# 앱에서 ODS 파일의 이미지를 추출하기"
head_description: "GroupDocs.Parser를 사용하여 C#에서 ODS 파일의 이미지 탐지 및 추출하세요. 추가 도구는 필요하지 않습니다."

############################# Header ############################
title: "C#를 사용하여 ODS에서 이미지 추출하기" 
description: "GroupDocs.Parser를 통해 PDF, 워드 문서, 엑셀 시트 및 기타 파일 유형에서 내장 이미지를 신속하게 찾고 추출할 수 있습니다."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "무료 체험 다운로드"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for .NET API 소개"
    link: "/parser/net/"
    link_title: "더 알아보기"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/)는 .NET 개발자를 위한 강력한 문서 파싱 라이브러리입니다. PDF, DOCX, XLSX, PPTX와 같은 인기 있는 파일 형식에서 이미지, 텍스트, 하이퍼링크 및 구조화된 데이터를 추출할 수 있으며, 타사 응용 프로그램이 필요 없습니다.

############################# Steps ############################
steps:
    enable: true
    title: "C#에서 Ods의 이미지를 추출하는 단계"
    content: |
      [GroupDocs.Parser](/parser/net/)를 사용하여 .NET 프로젝트에서 ODS 문서에서 이미지를 추출하는 단계는 다음과 같습니다:
      
      1. ODS 파일로 Parser를 초기화합니다.
      2. 문서에서 이미지 요소를 가져옵니다.
      3. 필요에 따라 추출된 이미지를 워크플로에 사용합니다.
   
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
        // Parser를 사용하여 이미지를 포함한 문서를 엽니다.
        using (Parser parser = new Parser("input.ods")) {

            // 파일에서 모든 내장 이미지를 추출합니다.
            IEnumerable<PageImageArea> images = parser.GetImages();

            // 이미지가 발견되지 않은 경우를 처리합니다.
            if (images == null)
            {
                return;
            }

            // 가져온 이미지를 처리하거나 저장합니다.
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "종합 문서 내용 추출"
  description: "GroupDocs.Parser는 이미지 추출 이상의 기능을 제공합니다. 원시 텍스트, 하이퍼링크, 메타데이터 및 구조화된 콘텐츠를 추출하여 고급 자동화 시나리오에 활용할 수 있습니다."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "이미지 추출 및 문서 파싱 워크플로"
  features:
    # feature loop
    - title: "다양한 형식에서 이미지 추출"
      content: "DOCX, PDF, PPTX, XLSX 및 PNG, JPG, TIFF와 같은 이미지 파일을 포함한 다양한 파일 형식에서 내장 이미지를 추출할 수 있습니다."

    # feature loop
    - title: "원본 이미지 품질 유지"
      content: "이미지는 원래 해상도, 형식 및 색상 프로필을 유지하여 높은 충실도로 추출됩니다."

    # feature loop
    - title: "고급 추출 옵션"
      content: "페이지, 형식 또는 해상도별로 필터링하여 이미지 추출을 사용자 정의하며, 다중 페이지 문서도 지원합니다."
      
  code_samples:
    # code sample loop
    - title: "PDF 문서에서 이미지를 추출하고 저장하는 방법"
      content: |
        이 예제는 PDF 파일에서 모든 이미지 자산을 추출하고 로컬 파일 시스템에 저장하는 방법을 보여줍니다.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Parser 클래스를 사용하여 PDF를 로드합니다.
        using (Parser parser = new Parser("input.pdf"))
        {
            // 파일에서 내장 이미지를 추출합니다.
            IEnumerable<PageImageArea> images = parser.GetImages();

            // 출력 형식 및 이미지 옵션(예: PNG)을 설정합니다.
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // 추출된 이미지를 디스크에 씁니다.
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
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
    title: "이미지 추출을 위한 지원 형식"
    exclude: "ODS"
    description: "GroupDocs.Parser는 다양한 문서 및 이미지 형식에서 정확한 이미지 추출을 가능하게 합니다. 일반적으로 지원되는 유형을 아래 목록에서 확인하세요."
    items: 
        # format loop 1
        - name: "PDF 파싱"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(휴대 문서 형식)"
          
        # format loop 2
        - name: "DOCX 파싱"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Office 2007+ 워드 문서)"
          
        # format loop 3
        - name: "PPTX 파싱"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Open XML 프레젠테이션 형식)"
          
        # format loop 4
        - name: "XLSX 파싱"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Open XML 워크북)"
          
        # format loop 5
        - name: "ODT 파싱"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(OpenDocument 텍스트 문서)"
          
        # format loop 6
        - name: "ODS 파싱"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(OpenDocument 스프레드시트)"
          
        # format loop 7
        - name: "ODP 파싱"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(OpenDocument 프레젠테이션)"
          
        # format loop 8
        - name: "EPUB 파싱"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(오픈 전자책 파일)"
          
        # format loop 9
        - name: "FB2 파싱"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(픽션북 전자책)"
         
          

---