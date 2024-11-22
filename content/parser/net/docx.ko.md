---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:06
draft: false
otherformats: dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf pps ppsx
ext: docx

############################# Head ############################
head_title: ".NET 문서, 페이지 또는 페이지 영역에서 하이퍼링크를 구문 분석 및 추출하는 API"
head_description: "GroupDocs.Parser .NET API는 소프트웨어 프로그래머가 PDF, DOCX, XLSX, CSV, PPTX, EML, MSG, EPUB의 문서, 페이지 또는 페이지 영역에서 하이퍼링크를 추출할 수 있도록 합니다. 그리고 더 많은 것."

############################# Header ############################
title: "C#/VB.NET API를 통해 문서, 페이지 또는 특정 페이지 영역에서 하이퍼링크 추출"
description: "GroupDocs.Parser .NET API를 사용하면 소프트웨어 개발자가 PDF, DOC, DOCX, PPT, PPTX, EML, MSG의 문서, 페이지 또는 페이지 영역에서 하이퍼링크를 구문 분석하고 추출할 수 있습니다. , XLS, XLSX, CSV, ODT, RTF, EPUB 및 기타 많은 문서."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "무료 평가판 다운로드"
    link: "https://downloads.groupdocs.com/parser/net"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/net"
              text: "API 참조"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "코드 예제"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "라이브 데모"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "가격"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: ".NET API를 통해 DOCX 문서에서 하이퍼링크를 구문 분석하고 추출하는 방법은 무엇입니까?"
    content: |
        하이퍼링크는 전체 문서 또는 문서 내의 특정 부분을 가리키는 텍스트나 이미지 또는 아이콘입니다. 하이퍼링크를 사용하면 사용자가 웹 페이지나 문서로 이동할 수 있습니다. 문서에서 하이퍼링크를 추출하여 외부 문서나 웹 페이지에 접근하기 위해 사용하는 경우가 많습니다. GroupDocs.Parser for .NET는 텍스트 및 메타데이터 추출 솔루션을 구현하기 위한 완벽한 기능을 제공하는 매력적인 문서 텍스트 추출 API입니다. PDF, 이메일, 전자책, Microsoft Office 형식에서 텍스트 및 하이퍼링크 추출을 지원합니다: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel ( XLS, XLSX), LibreOffice 형식 등. 문서 구문 분석, 일반 및 구조화된 텍스트 추출, 키워드로 텍스트 검색, 메타데이터 또는 이미지 추출, 컨테이너 및 첨부 파일 등을 위한 몇 가지 고급 기능을 지원합니다.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: ".NET의 DOCX에서 하이퍼링크 추출"
    content_left: |
        [GroupDocs.Parser for .NET](/ko/parser/net/)를 사용하면 C# 개발자가 몇 가지 간단한 단계를 구현하여 DOCX 파일에서 하이퍼링크를 쉽게 추출할 수 있습니다.
        
        * 초기 문서에 대한 [파서](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) 개체를 인스턴스화합니다.
        * 문서가 하이퍼링크 추출을 지원하는지 확인하십시오.
        * [GetHyperlinks](https://reference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) 메서드를 호출하고 [PageHyperlinkArea](https://reference.groupdocs.com/parser/net/groupdocs.parser.data/pagehyperlinkarea) 개체;
        * 컬렉션을 반복하고 하이퍼링크 텍스트와 URL을 가져옵니다.

    title_right: "하이퍼링크 추출에 대해 자세히 알아보기"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document/">문서에서 하이퍼링크를 추출하는 방법</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page/">문서 페이지에서 하이퍼링크를 추출하는 방법</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page-area/">문서 페이지 영역에서 하이퍼링크를 추출하는 방법</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="C# 예제 코드를 사용하여 DOCX 파일에서 하이퍼링크를 추출하는 방법">}}

        ```csharp    
        // GroupDocs.Parser API를 사용하여 DOCX 파일에서 하이퍼링크 추출
        // Parser 클래스의 인스턴스 생성
        using (Parser parser = new Parser(filePath)) {
            // 문서가 하이퍼링크 추출을 지원하는지 확인
            if (!parser.Features.Hyperlinks) {
                Console.WriteLine("문서가 하이퍼링크 추출을 지원하지 않습니다.");
                return;
            }
            // 문서에서 하이퍼링크 추출
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();
            // 하이퍼링크 반복
            foreach (PageHyperlinkArea h in hyperlinks) {
                // 하이퍼링크 텍스트 인쇄
                Console.WriteLine(h.Text);
                // 하이퍼링크 URL 인쇄
                Console.WriteLine(h.Url);
                Console.WriteLine();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "시스템 요구 사항"
    content_left: |
        GroupDocs.Parser for .NET API는 모든 주요 플랫폼 및 운영 체제에서 지원됩니다. 아래 코드를 실행하기 전에 시스템에 다음 필수 구성 요소가 설치되어 있는지 확인하십시오.
        
        * 운영 체제: Microsoft Windows, Linux, MacOS
        * 개발 환경: Microsoft Visual Studio, Xamarin, MonoDevelop
        * 프레임워크
        * [Nuget](https://www.nuget.org/packages/groupdocs.parser)에서 GroupDocs.Parser for .NET의 최신 버전을 다운로드하세요.

    title_right: "GroupDocs.Parser for .NET를 사용하는 이유"
    content_right: |
        * 지원되는 모든 문서에서 일반 텍스트 추출 지원    
        * 사용자 정의 템플릿을 통한 문서 분석    
        * 구조화된 텍스트 추출을 완벽하게 지원    
        * 키워드 및 정규 표현식을 통한 텍스트 검색    
        * 형식이 지정된 텍스트, 메타데이터, 이미지, 컨테이너 및 첨부 파일 추출    
        * 지원되는 일부 문서 형식의 목차 추출    
        * PDF 문서에서 양식 데이터 구문 분석    
        * 문서에서 하이퍼링크 추출   
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "다른 문서 형식에서 하이퍼링크 추출"
    content: |
        .NET 파일 형식 및 이미지에 대한 문서 구문 분석 및 하이퍼링크 추출 API. 아래에 설명된 대로 널리 사용되는 일부 파일 형식에 대한 데이터를 추출합니다.

############################# Back to top ###############################
back_to_top:
    enable: true
---