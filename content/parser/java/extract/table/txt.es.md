---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:12
draft: false
otherformats: 

############################# Head ############################
head_title: "Extraiga tablas de PDF, DOCX, PPTX, XLSX, EPUB y más a través de Java API"
head_description: "GroupDocs.Parser Java API permite a los programadores extraer tablas de PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV , ODT, RTF y muchos otros tipos de documentos dentro de las aplicaciones Java."

############################# Header ############################
title: "Extraiga tablas de documentos Excel, Word, PDF y PowerPoint a través de la API Java"
description: "GroupDocs.Parser Java API permite a los programadores extraer tablas de PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV , ODT, RTF y EPUB documentos o páginas."
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
    title: "¿Cómo extraer tablas de archivos TXT a través de la API Java?"
    content: |
        La tabla es la colección de celdas dispuestas en filas y columnas. Las tablas juegan un papel muy importante en el almacenamiento y la organización de datos detallados o complicados que permiten a los usuarios leerlos y verlos fácilmente. Las tablas se pueden usar de muchas maneras, como hacer listas, comparar información, alinear datos, agrupar información, resaltar tendencias o patrones en los datos y muchas más. GroupDocs.Parser for Java es una API útil que permite a los programadores de software desarrollar una solución para extraer tablas, texto e imágenes de varios tipos de formatos de documentos admitidos, como PDF, correos electrónicos, libros electrónicos, Word (DOC, { 318}), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), formatos de correo electrónico (EML, MSG) y muchos más. La API Java ha incluido varias funciones importantes para trabajar con tablas, como extraer todas las tablas de un documento, extraer una tabla de una página en particular, obtener datos de celdas de tabla, obtener el número total de filas y columnas de una tabla, obtener altura de fila, imprimir datos de una tabla y más.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extraer tablas de TXT en Java"
    content_left: |
        [GroupDocs.Parser for Java](/es/parser/java/) facilita a los desarrolladores de Java extraer tablas de un archivo TXT mediante la implementación de unos sencillos pasos.
        
        * Crear una instancia del objeto [Parser](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/) para el documento inicial;
        * Compruebe si el documento admite la extracción de tablas;
        * Crea una instancia de [PageTableAreaOptions](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.options/pagetableareaoptions/) y [TemplateTableLayout](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.templates/templatetablelayout/) clases para establecer el diseño de las tablas
        * Llame al método [getTables](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getTables-com.groupdocs.parser.options.PageTableAreaOptions-) y obtenga la colección de [PageTableArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/pagetablearea/) objetos;

    title_right: "Más información sobre la extracción de tablas"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document/">Cómo extraer tablas de un documento</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document-page/">Cómo extraer tablas de la página del documento</a>
 
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Cómo extraer tablas del archivo TXT usando el código de ejemplo Java">}}

        ```java    
        // Extraiga tablas del archivo TXT usando la API GroupDocs.Parser
        // Crear una instancia de la clase Parser
        try (Parser parser = new Parser(Constants.SampleInvoicePagesPdf)) {
            // Compruebe si el documento admite la extracción de tablas
            if (!parser.getFeatures().isTables()) {
                System.out.println("El documento no admite la extracción de tablas.");
                return;
            }
            // Crear el diseño de las tablas.
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));
            // Crear las opciones para la extracción de tablas.
            PageTableAreaOptions options = new PageTableAreaOptions(layout);
            // Extraer tablas del documento.
            Iterable<PageTableArea> tables = parser.getTables(options);
            // Iterar sobre tablas
            for (PageTableArea t : tables) {
                // Iterar sobre filas
                for (int row = 0; row < t.getRowCount(); row++) {
                    // Iterar sobre columnas
                    for (int column = 0; column < t.getColumnCount(); column++) {
                        // Obtener la celda de la tabla
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null) {
                            // Imprimir el texto de la celda de la tabla
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
    title: "Extraer tablas de otros formatos de documentos"
    content: |
        Java API de análisis de documentos y extracción de tablas para formatos de archivo e imágenes. Extraiga datos para algunos de los formatos de archivo populares como se indica a continuación.

############################# Back to top ###############################
back_to_top:
    enable: true
---