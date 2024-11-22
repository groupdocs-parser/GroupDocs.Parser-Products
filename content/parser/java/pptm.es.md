---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:06
draft: false
otherformats: 
ext: pptm

############################# Head ############################
head_title: "Extraer hipervínculos de documentos en Java"
head_description: "GroupDocs.Parser for Java API permite a los desarrolladores extraer hipervínculos de documentos, páginas de documentos o áreas de páginas específicas de Excel, PowerPoint, PDF, Outlook y más."

############################# Header ############################
title: "Java API para extraer hipervínculos de documentos, páginas o áreas de páginas particulares"
description: "La API GroupDocs.Parser for Java facilita el trabajo de los desarrolladores al permitirles extraer hipervínculos de documentos, páginas de documentos o páginas específicas Área de PDF, DOCX, PPTX, EML, MSG, XLS, {322 }, CSV, RTF, EPUB y muchos más."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Descargue prueba gratis"
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
              text: "Referencia de la API"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Ejemplos de código"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "demostraciones en vivo"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Precios"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "¿Cómo analizar y extraer hipervínculos de documentos PPTM a través de la API Java?"
    content: |
        Un hipervínculo es un fragmento de texto, una imagen o un icono que apunta a un documento completo o a una parte particular dentro de un documento. El uso de hipervínculos permite a los usuarios navegar a una página web o documento. A menudo se requiere extraer hipervínculos de un documento y usarlo para acceder a documentos externos o páginas web. GroupDocs.Parser for Java es una fascinante API de extracción de texto de documentos que proporciona una funcionalidad completa para implementar soluciones de extracción de texto y metadatos. Admite la extracción de texto e hipervínculos de PDF, correos electrónicos, libros electrónicos, Microsoft Office formatos: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel ( XLS, XLSX), formatos de LibreOffice y muchos más. Admite varias funciones avanzadas para el análisis de documentos, la extracción de texto sin formato y estructurado, la búsqueda de texto por palabras clave, la extracción de metadatos o imágenes, los contenedores y los archivos adjuntos, y mucho más.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extraer hipervínculos de PPTM en Java"
    content_left: |
        [GroupDocs.Parser for Java](/es/parser/java/) facilita a los desarrolladores de Java extraer hipervínculos de un archivo PPTM mediante la implementación de unos sencillos pasos.
        
        * Crear una instancia del objeto [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) para el documento inicial;
        * Compruebe si el documento admite la extracción de hipervínculos;
        * Llame al método [getHyperlinks](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getHyperlinks--) y obtenga la colección de [PageHyperlinkArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/PageHyperlinkArea) objetos;
        * Recorra la colección y obtenga un texto de hipervínculo y una URL.

    title_right: "Más información sobre la extracción de hipervínculos"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document/">Cómo extraer hipervínculos del documento</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page/">Cómo extraer hipervínculos de la página del documento</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page-area/">Cómo extraer hipervínculos del área de la página del documento</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Cómo extraer hipervínculos del archivo PPTM usando el código de ejemplo Java">}}

        ```java    
        // Extraiga hipervínculos del archivo PPTM usando la API GroupDocs.Parser
        // Crear una instancia de la clase Parser
        try (Parser parser = new Parser(Constants.HyperlinksPdf)) {
            // Compruebe si el documento admite la extracción de hipervínculos
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("El documento no admite la extracción de hipervínculos.");
                return;
            }
            // Extraer hipervínculos del documento
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();
            // Iterar sobre hipervínculos
            for (PageHyperlinkArea h : hyperlinks) {
                // Imprimir el texto del hipervínculo
                System.out.println(h.getText());
                // Imprima la URL del hipervínculo
                System.out.println(h.getUrl());
                System.out.println();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "Requisitos del sistema"
    content_left: |
        GroupDocs.Parser for Java Las API son compatibles con todas las principales plataformas y sistemas operativos. Antes de ejecutar el código a continuación, asegúrese de tener instalados los siguientes requisitos previos en su sistema.
        
        * Sistemas operativos: Microsoft Windows, Linux, MacOS
        * Entornos de desarrollo: NetBeans, Intellij IDEA, Eclipse, etc.
        * Marcos
        * Descarga la última versión de GroupDocs.Parser for Java desde [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)

    title_right: "Por qué usar GroupDocs.Parser for Java"
    content_right: |
        * Compatibilidad con la extracción de texto sin formato de cualquier documento compatible    
        * Análisis de documentos a través de plantillas definidas por el usuario    
        * Totalmente compatible con la extracción de texto estructurado    
        * Búsqueda de texto por palabra clave y expresión regular    
        * Extraiga texto formateado, metadatos, imágenes, contenedores y archivos adjuntos    
        * Extraiga la tabla de contenido para algunos formatos de documentos compatibles    
        * Analizar datos de formulario de PDF documentos    
        * Extraer hipervínculos del documento   
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extraer hipervínculos de otros formatos de documentos"
    content: |
        Java API de extracción de hipervínculos y análisis de documentos para formatos de archivo e imágenes. Extraiga datos para algunos de los formatos de archivo populares como se indica a continuación.

############################# Back to top ###############################
back_to_top:
    enable: true
---