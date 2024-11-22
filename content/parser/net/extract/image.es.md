---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Extraiga imágenes de Excel, Word, PDF y otro documento o página a través de .NET"
head_description: "La API GroupDocs.Parser .NET permite a los programadores de software extraer imágenes de diferentes documentos como MS Excel, Word, PowerPoint, PDF y más dentro de sus .NET aplicaciones."

############################# Header ############################
title: "Extraiga imágenes de PDF, DOCX, PPTX, MSG, XLSX documentos y páginas a través de la API de C#.NET"
description: "GroupDocs.Parser .NET API permite a los programadores extraer imágenes de PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV , ODT, RTF y EPUB documentos o páginas de documentos."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Descargue prueba gratis"
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
              text: "Referencia de la API"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Ejemplos de código"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "demostraciones en vivo"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Precios"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "¿Cómo extraer imágenes de documentos a través de .NET?"
    content: |
        Las imágenes se pueden usar para entregar información de tal manera que no se pueda expresar con palabras. Las imágenes nos ayudan a captar la atención del usuario y explican conceptos difíciles con facilidad. A veces, mientras leíamos documentos, diarios o nos beneficiábamos de presentaciones, a menudo encontrábamos algunas imágenes fascinantes y queríamos descargarlas. GroupDocs.Parser for .NET es una potente API que ayuda a los usuarios a desarrollar aplicaciones útiles para extraer imágenes de diferentes tipos de documentos y guardarlas en PNG, JPEG, WebP, GIF, BMP y otros formatos. La API ha incluido compatibilidad con la extracción de texto e imágenes de algunos de los formatos de archivo más utilizados, como PDF, correos electrónicos, libros electrónicos, Microsoft Office formatos: Word (DOC, DOCX), { 284} (PPT, PPTX), Excel (XLS, XLSX), formatos de LibreOffice y muchos más. La API también es totalmente compatible con el análisis de documentos, la extracción de texto sin formato y estructurado, la búsqueda de texto por palabras clave, la extracción de metadatos o imágenes, contenedores y archivos adjuntos y mucho más.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extraer imágenes de documentos en .NET"
    content_left: |
        [GroupDocs.Parser for .NET](/es/parser/net/) facilita a los desarrolladores de C# la extracción de imágenes de un documento mediante la implementación de unos sencillos pasos.
        
        * Crear una instancia del objeto [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) para el documento inicial;
        * Llame al método [GetImages](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser/methods/getimages) y obtenga una colección de objetos de imagen;
        * Compruebe si el lector no es * nulo * (la extracción de imágenes es compatible con el documento);
        * Iterar a través de la colección y obtener tamaños, tipos de imágenes y contenidos de imágenes.

    title_right: "Más información sobre la extracción de imágenes"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document/">Cómo extraer imágenes de un documento</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page/">Cómo extraer imágenes de la página del documento</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page-area/">Cómo extraer imágenes del área de la página del documento</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-to-files/">Cómo extraer imágenes a archivos</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Cómo extraer imágenes de documentos usando el código de ejemplo C#">}}

        ```csharp    
        // Extrae imágenes de documentos usando la API GroupDocs.Parser
        // Crear una instancia de la clase Parser
        using (Parser parser = new Parser(filePath)) {
            // Extraer imágenes
            IEnumerable<PageImageArea> images = parser.GetImages();
            // Compruebe si se admite la extracción de imágenes
            if (images == null) {
                Console.WriteLine("La extracción de imágenes no es compatible");
                return;
            }
            // Iterar sobre imágenes
            foreach (PageImageArea image in images) {
                // Imprima un índice de página, un rectángulo y un tipo de imagen:
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "Requisitos del sistema"
    content_left: |
        GroupDocs.Parser for .NET Las API son compatibles con todas las principales plataformas y sistemas operativos. Antes de ejecutar el código a continuación, asegúrese de tener instalados los siguientes requisitos previos en su sistema.
        
        * Sistemas operativos: Microsoft Windows, Linux, MacOS
        * Entornos de desarrollo: Microsoft Visual Studio, Xamarin, MonoDevelop
        * Marcos
        * Descarga la última versión de GroupDocs.Parser for .NET desde [Nuget](https://www.nuget.org/packages/groupdocs.parser)

    title_right: "Por qué usar GroupDocs.Parser for .NET"
    content_right: |
        * Compatibilidad con la extracción de texto sin formato de cualquier documento compatible    
        * Análisis de documentos a través de plantillas definidas por el usuario    
        * Totalmente compatible con la extracción de texto estructurado    
        * Búsqueda de texto por palabra clave y expresión regular    
        * Extraiga texto formateado, metadatos, imágenes, contenedores y archivos adjuntos    
        * Extraiga la tabla de contenido para algunos formatos de documentos compatibles    
        * Analizar datos de formulario de PDF documentos    
        * Extraer hipervínculos del documento   

############################# Demos ############################
demos:
    enable: true
    title: "Demostraciones en vivo: extraiga imágenes de documentos en línea"
    content: |
       Extraiga imágenes de documentos ahora mismo visitando el sitio web [GroupDocs.Parser Live Demos](https://products.groupdocs.app/parser/images/).
       La demostración en vivo tiene los siguientes beneficios.
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extraiga imágenes de otros formatos de documentos"
    content: |
        .NET API de análisis de documentos y extracción de imágenes para formatos de archivo e imágenes. Extraiga datos para algunos de los formatos de archivo populares como se indica a continuación.

############################# Back to top ###############################
back_to_top:
    enable: true
---