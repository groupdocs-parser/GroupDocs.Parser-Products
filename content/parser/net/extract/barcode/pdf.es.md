---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "es/parser/net/extract/pdf/"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF  MHTML MD XML EPUB FB2 CHM XLS XLT XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: ".NET API para analizar y extraer hipervínculos de documentos, páginas o área de página"
head_description: "GroupDocs.Parser .NET API permite a los programadores de software extraer hipervínculos de documentos, páginas o áreas de página de PDF, DOCX, XLSX, CSV, PPTX, EML, MSG, EPUB y muchos más."

############################# Header ############################
title: "Extraiga hipervínculos de documentos, páginas o áreas de páginas específicas a través de la API de C#/VB.NET"
description: "GroupDocs.Parser .NET API permite a los desarrolladores de software analizar y extraer hipervínculos de documentos, páginas o páginas Área de PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, ODT, RTF, EPUB y muchos otros documentos."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "¿Cómo analizar y extraer hipervínculos de documentos o páginas a través de .NET?"
    content: |
       Un hipervínculo es un fragmento de texto, una imagen o un icono que apunta a un documento completo o a una parte particular dentro de un documento. El uso de hipervínculos permite a los usuarios navegar a una página web o documento. A menudo se requiere extraer hipervínculos de un documento y usarlo para acceder a documentos externos o páginas web. GroupDocs.Parser .NET API es una fascinante API de extracción de texto de documentos que proporciona una funcionalidad completa para implementar soluciones de extracción de texto y metadatos. Admite la extracción de texto e hipervínculos de PDF, correos electrónicos, libros electrónicos, formatos de Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), formatos de LibreOffice y muchos más. Admite varias funciones avanzadas para el análisis de documentos, la extracción de texto sin formato y estructurado, la búsqueda de texto por palabras clave, la extracción de metadatos o imágenes, los contenedores y los archivos adjuntos, y mucho más.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Extraiga hipervínculos de PDF Documentos a través de .NET"
      content_left: |
       GroupDocs.Parser .NET brinda soporte completo para extraer hipervínculos de documentos PDF. El siguiente ejemplo de código C# .NET demuestra cómo extraer hipervínculos dentro de un documento PDF. 

      title_right: "Cómo extraer hipervínculos"
      content_right: |
        * Cree una instancia de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * Verifique el documento para soporte de extracción de hipervínculos
        * Extraer hipervínculos del documento
        * Llamar al método [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) para extraer todos los hipervínculos de todo el documento.
        * Iterar sobre hipervínculos e imprimir la URL del hipervínculo

      gisthash: "35be3a09e0135c65be790c42c5c86d37"
      gistfile: "Extract_hyperlinks_form_documents.cs"

    - title_left: "Extraer hipervínculos de la página de documentos PDF"
      content_left: |
       GroupDocs.Parser .NET permite a los desarrolladores de software extraer hipervínculos de documentos PDF con un par de líneas de código. El siguiente código C# .NET muestra la extracción de hipervínculos dentro de un documento PDF. 

      title_right: "Extraer hipervínculos a través de .NET"
      content_right: |
        * Cree una instancia de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * Verifique el documento para soporte de extracción de hipervínculos
        * Obtenga información del documento llamando a [GetDocumentInfo](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/getdocumentinfo)
        * Iterar sobre páginas e imprimir un número de página
        * Extraer hipervínculos del documento
        * Llamar al método [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) para extraer todos los hipervínculos de todo el documento.
        * Iterar sobre hipervínculos e imprimir la URL del hipervínculo
     
      gisthash: "e71f8e39ba36ebf97034dfbf6fceeec1"
      gistfile: "hyperlinks_extraction_form_documents_page.cs"
      
    - title_left: "Extraer hipervínculos del área de la página de documentos PDF"
      content_left: |
       GroupDocs.Parser .NET API es totalmente compatible con la extracción de hipervínculos de documentos PDF con facilidad. El siguiente ejemplo de código .NET demuestra cómo extraer hipervínculos de un área de página de documento PDF.

      title_right: "Cómo extraer hipervínculos usando .NET"
      content_right: |
        * Cree una instancia de [Parser](https://apireference.groupdocs.com/parser/net/groupdocs.parser/parser)
        * Verifique el documento para soporte de extracción de hipervínculos
        * Crear las opciones que se utilizan para la extracción de hipervínculos
        * Llame al método [GetHyperlinks](https://apireference.groupdocs.com/parser/net/groupdocs.parser.parser/gethyperlinks/methods/1) para extraer hipervínculos de una página de documento.
        * Iterar sobre hipervínculos e imprimir la URL del hipervínculo
     
      gisthash: "eefbede6f391ea44ddb6901edb353950"
      gistfile: "hyperlinks_extraction_from__documents_page_area.cs"

    - title_left: "Requisitos del sistema"
      content_left: |
       Las API de GroupDocs.Assembly .NET son compatibles con todas las principales plataformas y sistemas operativos. Para obtener una guía completa de requisitos del sistema, visite [requisitos del sistema] (hhttps://docs.groupdocs.com/parser/net/system-requirements/) Antes de ejecutar el código a continuación, asegúrese de tener los siguientes requisitos previos instalados en su sistema:
        * Sistemas Operativos: Microsoft Windows, Linux, Mac OS
        * Entorno de desarrollo: Visual Studio, Xamarin, MonoDevelop, etc.
        * Marcos: .NET Framework, .NET Standard, .NET Core, Mono
        * Obtenga la última versión de las API GroupDocs.Assembly .NET de [NuGet](https://www.nuget.org/packages/GroupDocs.parser/)
        
      title_right: "Por qué usar GroupDocs.Assembly"
      content_right: |
        * Compatibilidad con la extracción de texto sin formato de cualquier documento compatible
        * Análisis de documentos a través de plantillas definidas por el usuario.
        * Totalmente compatible con la extracción de texto estructurado
        * Búsqueda de texto por palabra clave y expresión regular
        * Extraiga texto formateado, metadatos, imágenes, contenedores y archivos adjuntos.
        * Extraiga la tabla de contenido para algunos formatos de documentos compatibles.
        * Analizar datos de formularios de documentos PDF.
        * Extraer hipervínculos del documento

demos:
    enable: true
        

more_formats:
    enable: true


back_to_top:
    enable: true
---