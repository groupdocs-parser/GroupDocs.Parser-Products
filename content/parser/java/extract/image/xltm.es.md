---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "es/parser/java/extract/image/xltm/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Extraiga imágenes de Excel, Word, PDF y otros documentos o páginas a través de .NET "
head_description: "Extraiga imágenes de Excel, Word, PDF y otros documentos o páginas a través de .NET"

############################# Header ############################
title: "Extraiga imágenes de Excel, Word, PDF y otros documentos o páginas a través de .NET"
description: "GroupDocs.Parser .NET API permite a los programadores extraer imágenes de documentos o páginas de documentos PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF y EPUB."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "¿Cómo extraer imágenes de documentos o área de página a través de .NET?"
    content: |
       Las imágenes se pueden usar para entregar información de tal manera que no se pueda expresar con palabras. Las imágenes nos ayudan a captar la atención del usuario y explican conceptos difíciles con facilidad. A veces, mientras leíamos documentos, diarios o nos beneficiábamos de presentaciones, a menudo encontrábamos algunas imágenes fascinantes y queríamos descargarlas. GroupDocs.Parser para .NET es una potente API que ayuda a los usuarios a desarrollar aplicaciones útiles para extraer imágenes de diferentes tipos de documentos y guardarlas en PNG, JPEG, WebP, GIF, BMP y otros formatos. La API ha incluido soporte para la extracción de texto e imágenes de algunos de los formatos de archivo más utilizados, como PDF, correos electrónicos, libros electrónicos, formatos de Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS , XLSX), formatos de LibreOffice y muchos más. La API también es totalmente compatible con el análisis de documentos, la extracción de texto sin formato y estructurado, la búsqueda de texto por palabras clave, la extracción de metadatos o imágenes, contenedores y archivos adjuntos y mucho más.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Extraiga imágenes de XLTM Documentos a través de C# "
      content_left: |
       GroupDocs.Parser .NET API permite a los desarrolladores de software extraer imágenes de XLTM documentos. El siguiente ejemplo de código C# .NET demuestra cómo extraer imágenes dentro de un documento XLTM.

      title_right: "Cómo extraer imágenes a través de .NET"
      content_right: |
        * Cree una instancia de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * compruebe si se admite la extracción de imágenes
        * Iterar sobre imágenes en el documento
        * Llamar al método [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) para extraer todas las imágenes de todo el documento.
        * Imprimir todas las imágenes

      gisthash: "6bc9e8fea228c9e1b99425b338bb0f00"
      gistfile: "images_extraction_form_documents.cs"

    - title_left: "Extracción de imágenes de la página del documento XLTM a través de C#"
      content_left: |
       GroupDocs.Parser .NET permite a los desarrolladores de software extraer imágenes de la página de documentos XLTM. El siguiente código C# .NET muestra cómo se puede lograr la extracción de imágenes dentro de un documento XLTM.

      title_right: "Extraer imagen de archivo a través de .NET"
      content_right: |
        * Cree una instancia de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * Verifique el documento para soporte de extracción de imágenes
        * Obtenga información del documento llamando a [GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo)
        * Consultar documento por páginas existentes
        * Iterar sobre páginas e imprimir un número de página
        * Llame al método [getImages(Int32)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/2) para extraer todas las imágenes de todo el documento.
        * Iterar sobre imágenes e imprimir las imágenes
     
      gisthash: "2000d476c202a688677f57a2fbd7ceab"
      gistfile: "images_extraction_form_documents_page.cs"
      
    - title_left: "Cómo extraer una imagen del área de la página de documentos XLTM"
      content_left: |
       GroupDocs.Parser .NET API es totalmente compatible con la extracción de imágenes de documentos XLTM usando un par de líneas de código .NET. El siguiente ejemplo de código .NET muestra cómo realizar la extracción de imágenes desde un área de página de documento XLTM.

      title_right: "Extraiga imágenes de un área de página de archivo a través de .NET"
      content_right: |
        * Cree una instancia de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * personalizar la creación de opciones que se pueden usar para la extracción de imágenes
        * Verifique el documento para soporte de extracción de imágenes
        * Extraiga imágenes de la esquina superior izquierda de una página llamando al método [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) usando personalizar Opciones.
        * Iterar sobre imágenes e imprimir las imágenes
     
      gisthash: "ea6c6b8fa613384f1e7f637dabcb7bca"
      gistfile: "extract_images_form_documents_page_area.cs"

    - title_left: "Cómo extraer y guardar una imagen en un archivo a través de C# .NET"
      content_left: |
       GroupDocs.Parser .NET API permite a los desarrolladores de software extraer imágenes de un documento y guardarlas en un archivo con solo un par de líneas de código .NET. El siguiente ejemplo demuestra cómo realizar la extracción de imágenes de un documento XLTM y guardar el contenido de la imagen en el archivo.

      title_right: "Guardar imágenes en un archivo a través de .NET"
      content_right: |
        * Crear una instancia de la clase [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * Extraer imágenes del documento
        * Llamar al método [getImages](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getimages) para extraer todas las imágenes de todo el documento.
        * Verifique el documento para soporte de extracción de imágenes
        * Extraiga imágenes de la esquina superior izquierda de una página llamando al método [getImages(options)](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/getimages/methods/3) usando personalizar Opciones.
        * opción Creación para guardar imágenes en formato PNG
        * Iterar sobre imágenes y guardar la imagen en el archivo PNG
     
      gisthash: "bc242d5ff4050564fa275858ffa7d34f"
      gistfile: "images_saving_to_files.cs"

    - title_left: "Requisitos del sistema"
      content_left: |
       GroupDocs.Parser para Java es compatible con todas las principales plataformas y sistemas operativos. Puede generar documentos en Microsoft Word, Excel, PowerPoint, Outlook, OpenOffice y más de 50 formatos. Para obtener una guía completa de requisitos del sistema, visite los requisitos del sistema antes de ejecutar el código a continuación, asegúrese de tener instalados los siguientes requisitos previos en su sistema:
         * Sistemas Operativos: Microsoft Windows, Linux, Mac OS
         * Compatibilidad con versiones de Java: J2SE 7.0 (1.7), J2SE 8.0 (1.8) o superior
         * Obtenga la última versión de GroupDocs.Parser Java API de GroupDocs [Repositorio](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)
        
      title_right: "Por qué usar GroupDocs.Parser"
      content_right: |
        * Extraiga un texto sin formato de cualquiera de los documentos admitidos.
        * Soporte de extracción de tabla de contenido
        * Extraiga texto formateado, metadatos, imágenes, contenedores y archivos adjuntos.
        * Análisis de documentos a través de plantillas definidas por el usuario.
        * Buscar texto usando palabras clave o expresiones regulares.
        * Soporte de extracción de texto estructurado
        * Extraiga la tabla de contenido para algunos formatos de documentos compatibles.
        * Analizar datos de formularios de documentos PDF.

demos:
    enable: true
        

more_formats:
    enable: true


back_to_top:
    enable: true
---