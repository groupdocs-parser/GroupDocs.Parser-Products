---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Java를 통해 Excel, Word, PDF 및 기타 문서에서 이미지를 추출하는 방법은 무엇입니까?"
head_description: "GroupDocs.Parser for Java API를 사용하면 소프트웨어 개발자가 Java 앱 내의 PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX 문서 및 이메일에서 이미지를 구문 분석하고 추출할 수 있습니다."

############################# Header ############################
title: "Excel, Word, PowerPoint, PDF 및 기타 문서 페이지에서 이미지를 구문 분석하고 추출하는 Java API"
description: "GroupDocs.Parser for Java API를 통해 프로그래머는 PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, {358에서 이미지를 추출할 수 있습니다. }, RTF 및 EPUB 문서 또는 Java 애플리케이션 내의 문서 페이지."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "무료 평가판 다운로드"
    link: "https://downloads.groupdocs.com/parser/java"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/java"
              text: "API 참조"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "코드 예제"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "라이브 데모"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "가격"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Java API를 통해 {{EXT}} 문서 또는 특정 페이지에서 이미지를 추출하는 방법 알아보기"
    content: |
        이미지는 수천 단어의 가치가 있으며 매력적인 콘텐츠를 만드는 동안 오늘날의 시각적 세계에서 무시할 수 없습니다. 이미지는 사용자의 관심을 끌 뿐만 아니라 정보 전달의 훌륭한 소스가 될 수 있습니다. 문서, 저널 또는 프리젠테이션에서 이미지를 가져와 다른 곳에서 사용하는 데 종종 필요합니다. GroupDocs.Parser for Java는 소프트웨어 개발자와 프로그래머가 수많은 문서 유형에서 이미지 또는 기타 정보를 구문 분석하고 추출하기 위한 솔루션을 구축하는 데 도움이 되는 강력한 API입니다. 또한 PNG, JPEG, WebP, GIF, BMP 및 기타 형식으로 이미지 저장을 지원합니다. API에는 PDF, Microsoft Office 형식과 같은 일부 널리 사용되는 문서 형식에 대한 지원이 포함되어 있습니다. } (XLS, XLSX), LibreOffice 형식, 이메일, 전자책 등. 또한 문서 구문 분석, 일반 및 구조화된 텍스트 추출, 키워드로 텍스트 검색, 메타데이터 또는 이미지 추출, 컨테이너 및 첨부 파일 등과 관련된 일부 고급 기능에 대한 지원도 포함되어 있습니다.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Java의 문서에서 이미지 추출"
    content_left: |
        [GroupDocs.Parser for Java](/ko/parser/java/)를 사용하면 Java 개발자가 몇 가지 간단한 단계를 구현하여 문서에서 이미지를 쉽게 추출할 수 있습니다.
        
        * 초기 문서에 대한 [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) 개체를 인스턴스화합니다.
        * [getImages](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getImages--) 메서드를 호출하고 이미지 개체 모음을 가져옵니다.
        * 판독기가 *null*이 아닌지 확인합니다(문서에 대해 이미지 추출이 지원됨).
        * 컬렉션을 반복하고 크기, 이미지 유형 및 이미지 콘텐츠를 가져옵니다.

    title_right: "이미지 추출에 대해 자세히 알아보기"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document/">문서에서 이미지를 추출하는 방법</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page/">문서 페이지에서 이미지를 추출하는 방법</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page-area/">문서 페이지 영역에서 이미지를 추출하는 방법</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-to-files/">이미지를 파일로 추출하는 방법</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Java 예제 코드를 사용하여 문서에서 이미지를 추출하는 방법">}}

        ```java    
        // GroupDocs.Parser API를 사용하여 문서에서 이미지 추출
        // Parser 클래스의 인스턴스 생성
        try (Parser parser = new Parser(Constants.SampleImagesPdf)) {
            // 이미지 추출
            Iterable<PageImageArea> images = parser.getImages();
            // 이미지 추출이 지원되는지 확인
            if (images == null) {
                System.out.println("이미지 추출은 지원되지 않습니다.");
                return;
            }
            // 이미지 반복
            for (PageImageArea image : images) {
                // 페이지 인덱스, 사각형 및 이미지 유형 인쇄:
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "시스템 요구 사항"
    content_left: |
        GroupDocs.Parser for Java API는 모든 주요 플랫폼 및 운영 체제에서 지원됩니다. 아래 코드를 실행하기 전에 시스템에 다음 필수 구성 요소가 설치되어 있는지 확인하십시오.
        
        * 운영 체제: Microsoft Windows, Linux, MacOS
        * 개발 환경: NetBeans, Intellij IDEA, Eclipse, etc.
        * 프레임워크
        * [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)에서 GroupDocs.Parser for Java의 최신 버전을 다운로드하세요.

    title_right: "GroupDocs.Parser for Java를 사용하는 이유"
    content_right: |
        * 지원되는 모든 문서에서 일반 텍스트 추출 지원    
        * 사용자 정의 템플릿을 통한 문서 분석    
        * 구조화된 텍스트 추출을 완벽하게 지원    
        * 키워드 및 정규 표현식을 통한 텍스트 검색    
        * 형식이 지정된 텍스트, 메타데이터, 이미지, 컨테이너 및 첨부 파일 추출    
        * 지원되는 일부 문서 형식의 목차 추출    
        * PDF 문서에서 양식 데이터 구문 분석    
        * 문서에서 하이퍼링크 추출   

############################# Demos ############################
demos:
    enable: true
    title: "라이브 데모 - 온라인 문서에서 이미지 추출"
    content: |
       지금 바로 [GroupDocs.Parser Live Demos](https://products.groupdocs.app/parser/images/) 웹사이트를 방문하여 문서에서 이미지를 추출하세요.
       라이브 데모에는 다음과 같은 이점이 있습니다.
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "다른 문서 형식에서 이미지 추출"
    content: |
        Java 파일 형식 및 이미지에 대한 문서 구문 분석 및 이미지 추출 API. 아래에 설명된 대로 널리 사용되는 일부 파일 형식에 대한 데이터를 추출합니다.

############################# Back to top ###############################
back_to_top:
    enable: true
---