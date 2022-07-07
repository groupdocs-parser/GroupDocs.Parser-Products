---
############################# Static ############################
layout: "auto-gen-gist"
draft: false
path: "es/parser/java/extract"
otherformats: DOC DOT DOCX DOCM DOTX DOTM TXT ODT OTT RTF PDF XHTML MHTML MD XML EPUB FB2 CHM XLS XLSX XLSM XLSB XLTX XLTM ODS CSV OTS XLA XLAM PPT PPTX  PPS POT PPSX PPTM POTX PPSM ODP OTP PST OST EML EMLX MSG ONE 

############################# Head ############################
head_title: "Extracción de hipervínculos de documentos, páginas o área de página a través de la API de Java"
head_description: "GroupDocs.Parser Java API permite a los desarrolladores extraer hipervínculos de documentos, páginas de documentos o áreas de páginas específicas de Excel, PowerPoint, PDF, Outlook y más."

############################# Header ############################
title: "API de Java para extraer hipervínculos de documentos, páginas o áreas de páginas particulares"
description: "GroupDocs.Parser Java API facilita el trabajo de los desarrolladores al permitirles extraer hipervínculos de documentos, páginas de documentos o páginas específicas Área de PDF, DOCX, PPTX, EML, MSG, XLS, XLSX, CSV, RTF, EPUB y muchos más."

######################### Download Button #######################
button:
    enable: true

############################# About ############################
about:
    enable: true
    title: "¿Cómo realizar la extracción de hipervínculos de varios documentos a través de Java?"
    content: |
       Esta página web explica cómo analizar y extraer hipervínculos de diferentes tipos de documentos, páginas de documentos o un área particular de una página utilizando solo un par de líneas de código Java. El hipervínculo puede ser muy útil para navegar entre páginas o sitios web y puede apuntar a un documento completo oa una parte particular dentro de un documento, gráficos, sonidos, direcciones de correo electrónico y más. GroupDocs.Parser para Java es una API muy potente que permite a los desarrolladores de software analizar documentos y extraer texto y metadatos de varios documentos populares dentro de sus propias aplicaciones Java. Ha incluido varias funciones avanzadas para extraer texto e hipervínculos de varios tipos de documentos, como PDF, correos electrónicos, libros electrónicos, formatos de Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), formatos de LibreOffice y muchos más.

############################# content ############################
steps:
    enable: true
    block:
    - title_left: "Cómo extraer hipervínculos de documentos XLT"
      content_left: |
       GroupDocs.Parser Java ha incluido la funcionalidad para extraer hipervínculos de documentos XLT. El siguiente ejemplo de código Java muestra cómo se pueden extraer los hipervínculos del documento XLT. 

      title_right: "Extraer hipervínculos a través de Java"
      content_right: |
        * Cree una instancia de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Compruebe si el documento admite la extracción de hipervínculos
        * Extraer hipervínculos del documento
        * Llame al método [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) para extraer todos los hipervínculos de todo el documento.
        * Iterar sobre hipervínculos e imprimir la URL del hipervínculo

      gisthash: "036de701f5f17a02dd2353ee547afd5b"
      gistfile: "extract_hyperlinks_form_documents.java"

    - title_left: "Cómo extraer hipervínculos de la página de documentos XLT"
      content_left: |
       GroupDocs.Parser .NET permite a los desarrolladores de software extraer hipervínculos de documentos XLT con un par de líneas de código. El siguiente código C# .NET muestra la extracción de hipervínculos dentro de un documento XLT.

      title_right: "Extraer hipervínculos a través de Java"
      content_right: |
        * Cree una instancia de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Compruebe si el documento admite la extracción de hipervínculos
        * Obtenga información del documento llamando al método [getDocumentInfo](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getDocumentInfo()).
        * Iterar sobre páginas e imprimir un número de página
        * Extraer hipervínculos del documento
        * Llame al método [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) para extraer todos los hipervínculos de todo el documento.
        * Iterar sobre hipervínculos e imprimir la URL del hipervínculo
     
      gisthash: "bcca6319f2287edb7295443c1def46ee"
      gistfile: "extract_hyperlinks_form_documents_page.java"
      
    - title_left: "Extraer hipervínculos del área de la página de documentos XLT"
      content_left: |
       GroupDocs.Parser Java API ha brindado soporte completo para extraer hipervínculos de la página del documento XLT con facilidad. El siguiente código Java muestra cómo los programadores pueden extraer hipervínculos de un área de página de documento XLT dentro de sus propias aplicaciones Java.

      title_right: "¿Cómo extraer hipervínculos usando Java?"
      content_right: |
        * Cree una instancia de [Parser](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser)
        * Verifique el documento para soporte de extracción de hipervínculos
        * Crear las opciones que se utilizan para la extracción de hipervínculos
        * Llame al método [GetHyperlinks](https://apireference.groupdocs.com/parser/java/com.groupdocs.parser/Parser#getHyperlinks()) para extraer todos los hipervínculos de todo el documento.
        * Iterar sobre hipervínculos e imprimir la URL del hipervínculo
     
      gisthash: "4aefff1fcc6733c0fc12b736d7e36711"
      gistfile: "hyperlinks_extraction_from_document_page_area.java"

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