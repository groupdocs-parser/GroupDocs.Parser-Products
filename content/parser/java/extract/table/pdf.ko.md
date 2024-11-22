---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:12
draft: false
otherformats: ppsx ppt pptx rtf tex vdx vsdm vsdx vssm vssx vstm vstx vsx vtx xlam xls

############################# Head ############################
head_title: "Java API를 통해 PDF, DOCX, PPTX, XLSX, EPUB 등에서 테이블 추출"
head_description: "GroupDocs.Parser Java API를 사용하면 프로그래머가 PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV에서 테이블을 추출할 수 있습니다. , ODT, RTF 및 Java 앱 내의 다른 많은 문서 유형."

############################# Header ############################
title: "Java API를 통해 Excel, Word, PDF 및 PowerPoint 문서에서 테이블 추출"
description: "GroupDocs.Parser Java API를 통해 프로그래머는 PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV에서 테이블을 추출할 수 있습니다. , ODT, RTF & EPUB 문서 또는 페이지."
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
    title: "Java API를 통해 PDF 파일에서 테이블을 추출하는 방법은 무엇입니까?"
    content: |
        표는 행과 열로 배열된 셀 모음입니다. 테이블은 상세하거나 복잡한 데이터를 사용자가 쉽게 읽고 볼 수 있도록 저장하고 정리하는 데 매우 중요한 역할을 합니다. 표는 목록 만들기, 정보 비교, 데이터 정렬, 정보 그룹화, 데이터의 추세 또는 패턴 강조 등 다양한 방법으로 사용할 수 있습니다. GroupDocs.Parser for Java는 소프트웨어 프로그래머가 PDF, 이메일, 전자책, Word(DOC, { 318}), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), 이메일(EML, MSG) 형식 등. Java API에는 문서에서 모든 테이블 추출, 특정 페이지에서 테이블 추출, 테이블 셀 데이터 가져오기, 테이블 행 및 열의 총 수 가져오기, 행 높이 가져오기, 테이블의 데이터를 인쇄하고 그 이상일 수 있습니다.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Java의 PDF에서 테이블 추출"
    content_left: |
        [GroupDocs.Parser for Java](/ko/parser/java/)를 사용하면 Java 개발자가 몇 가지 간단한 단계를 구현하여 PDF 파일에서 테이블을 쉽게 추출할 수 있습니다.
        
        * 초기 문서에 대한 [파서](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/) 개체를 인스턴스화합니다.
        * 문서가 테이블 추출을 지원하는지 확인하십시오.
        * [PageTableAreaOptions](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.options/pagetableareaoptions/) 및 인스턴스화 [TemplateTableLayout](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.templates/templatetablelayout/) 테이블 레이아웃을 설정하는 클래스
        * [getTables](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getTables-com.groupdocs.parser.options.PageTableAreaOptions-) 메서드를 호출하고 [PageTableArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/pagetablearea/) 개체;

    title_right: "테이블 추출에 대해 자세히 알아보기"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document/">문서에서 테이블을 추출하는 방법</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document-page/">문서 페이지에서 표를 추출하는 방법</a>
 
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Java 예제 코드를 사용하여 PDF 파일에서 테이블을 추출하는 방법">}}

        ```java    
        // GroupDocs.Parser API를 사용하여 PDF 파일에서 테이블 추출
        // Parser 클래스의 인스턴스 생성
        try (Parser parser = new Parser(Constants.SampleInvoicePagesPdf)) {
            // 문서가 테이블 추출을 지원하는지 확인
            if (!parser.getFeatures().isTables()) {
                System.out.println("문서는 테이블 추출을 지원하지 않습니다.");
                return;
            }
            // 테이블 레이아웃 만들기
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));
            // 테이블 추출 옵션 만들기
            PageTableAreaOptions options = new PageTableAreaOptions(layout);
            // 문서에서 테이블을 추출합니다.
            Iterable<PageTableArea> tables = parser.getTables(options);
            // 테이블 반복
            for (PageTableArea t : tables) {
                // 행 반복
                for (int row = 0; row < t.getRowCount(); row++) {
                    // 열을 반복
                    for (int column = 0; column < t.getColumnCount(); column++) {
                        // 테이블 셀 가져오기
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null) {
                            // 테이블 셀 텍스트 인쇄
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                    System.out.println();
                }
                System.out.println();
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

############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "다른 문서 형식에서 테이블 추출"
    content: |
        Java 파일 형식 및 이미지에 대한 문서 구문 분석 및 테이블 추출 API. 아래에 설명된 대로 널리 사용되는 일부 파일 형식에 대한 데이터를 추출합니다.

############################# Back to top ###############################
back_to_top:
    enable: true
---