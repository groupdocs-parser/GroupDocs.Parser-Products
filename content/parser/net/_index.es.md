---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "API de análisis de .NET, extraiga metadatos de imágenes de texto de PDF Word Excel"
head_description: "API de análisis de documentos C# .NET para extraer texto, imágenes, metadatos y codificación de bases de datos, PDF, Word, Excel, presentaciones, web, correo electrónico, EPUB y formatos de archivo zip."

############################# Header ############################
title: ".NET API para extraer datos de documentos"
description: "Extraiga imágenes, texto sin formato o formateado y metadatos de documentos, hojas de cálculo, presentaciones, correos electrónicos y archivos desde aplicaciones .NET."
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "/border/groupdocs-parser-net.svg"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:
            # button loop
            - link: "#overview"
              text: "Visión de conjunto"

            # button loop
            - link: "#features"
              text: "Características"

            # button loop
            - link: "#support"
              text: "Support"

            # button loop
            - link: "https://products.groupdocs.app/parser"
              text: "Live Demo"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Precios"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net/"
        link_buy: "https://purchase.groupdocs.com"

############################# Visión de conjunto ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser para .NET es una API de extracción de texto, metadatos e imágenes para aplicaciones comerciales desarrolladas con C#, ASP.NET y otras tecnologías .NET. Admite la extracción de texto sin procesar, formateado y estructurado, así como metadatos de los archivos de formatos admitidos. A través de GroupDocs.Parser para .NET, sus aplicaciones también pueden analizar documentos protegidos con contraseña para formatos populares, como documentos de procesamiento de Word, hojas de cálculo de Excel, presentaciones de PowerPoint, OneNote, archivos PDF y archivos ZIP.
    tabs:
      enable: true
      
      ## TAB ONE ##
      tab_one:
        description: |
          A continuación se muestra una descripción general de GroupDocs.Parser para .NET:
      
        left:
          enable: true
          icon: "fas fa-tools"
          title: "Características"
          content: |
            * Extraer imágenes
            * Extraer texto sin procesar
            * Extraer texto formateado
            * Extraer texto estructurado
            * Extraer metadatos
            * Extraer de archivos dentro del archivo ZIP
            * Extraer por búsqueda
            * Extraer con formateadores de texto
            * Estándar de codificación de detección
            * Detectar tipo de medio
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "la API"
          content: |
            * Obtiene el archivo de entrada
            * Obtiene texto sin procesar o formateado
            * Obtiene metadatos
      
      ## TAB TWO ##
      tab_two:
        description: |
          GroupDocs.Parser para .NET admite los siguientes [formatos de archivo de documento] (https://docs.groupdocs.com/parser/net/supported-document-formats/):

        left:
          enable: true
          table:
            # table loop
            - title: "Extracción de texto"
              content: |
                * **Texto**: DOC, DOCX, DOT, DOTM, DOTX, DOCM, RTF, ODT, OTT, TXT, MD, WordprocessingML (XML)
                * **Hojas de cálculo**: XLS, XLSX, CSV, XLSM, XLSB, ODS, SpreadsheetML (XML), XLT, XLTX, XLTM, OTS, XLA, XLAM, TSV
                * **Presentaciones**: PPT, PPTX, PPTM, PPS, PPSX, PPSM, POT, POTX, POTM, ODP, OTP
                * **Una Nota**: UNO
                * **Correo electrónico**: MSG, EML, EMLX, PST, OST, MS EXCHANGE SERVER, POP, IMAP
                * **Publicación electrónica**: EPUB, FB2
                * **Documento portátil**: PDF, cartera PDF, PDF encriptado
                * **Basado en DOM**: XML, HTML, XHTML, MHTML
                * **Compresión y embalaje**: ZIP, CHM
                * **Base de datos**: ADO.NET

            # table loop
            - title: "Detección de codificación"
              content: |
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and UTF7
                * **Content**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, and ANSI

        right:
          enable: true
          table:
            # table loop
            - title: "Extracción de metadatos"
              content: |
                * **Texto**: DOC, DOCX, DOT, DOTX, DOTM, OTT, ODT
                * **Hojas de cálculo**: XLS, XLSX, XLT, XLTX, XLTM, XLA, XLAM, OTS, ODS
                * **Presentaciones**: PPT, PPTX, POT, POTX, POTM, PPSM, PPTM, OTP, ODP
                * **Correo electrónico**: MSG, EML, EMLX
                * **Publicación electrónica**: EPUB, FB2
                * **Otro**: PDF

            # table loop
            - title: "Text & Extracción de metadatos"
              content: |
                * **Plantilla**: DOTX, POTX
                * **Plantilla habilitada para macros**: DOTM, POTM, PPSM, PPTM
                * **Plantilla de documento abierto**: OTT

            # table loop
            - title: "Extracción de imagen"
              content: |
                * **Texto**: DOC, DOCX, DOCM, RTF, DOT, DOTM, DOTX, ODT
                * **Hojas de cálculo**: XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **Presentaciones**: PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **Documento portátil**: PDF, POT, POTM, POTX
                * **Libro electrónico**: CHM, EPUB, FB2
                * **Marcado**: HTML

      ## TAB THREE ##
      tab_three:
        description: |
          GroupDocs.Parser for .NET apoya siguiendo Sistemas operativos, Frameworks & Gerente de empaquetacións:
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Sistemas operativos"
              content: |
                * Windows Desktop
                * Windows Server
                * Windows Azure
                * Linux

            # table loop
            - icon: "fas fa-code"
              title: "Marcos compatibles"
              content: |
                * .NET Framework 2.0 o superior
                * Mono Framework 1.2 o superior
                * .NET estándar 2.0
                * .NET Core 2.0

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-box"
              title: "Gerente de empaquetación"
              content: |
                * NuGet

            # table loop
            - icon: "fas fa-tools"
              title: "Entornos de desarrollo"
              content: |
                * Microsoft Visual Studio
                * Xamarin.Android
                * Xamarin.IOS
                * Xamarin.Mac
                * MonoDevelop

############################# Características ############################
features:
    enable: true
    title: "GroupDocs.Parser for .NET Características"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Cuente estadísticamente la ocurrencia de palabras en archivos únicos o múltiples"

      # feature loop
      - icon: "fas fa-eye"
        content: "Extraiga texto y metadatos de hojas de cálculo y plantillas de presentación de Excel"

      # feature loop
      - icon: "fas fa-bolt"
        content: "Extraiga contenido de texto de un archivo o secuencia sin instalar el lector de documentos"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "Obtenga texto formateado de un documento usando el modo de extracción de texto rápido o estándar"

      # feature loop
      - icon: "fas fa-code"
        content: "Detecte el tipo de medio de documentos XML protegidos con contraseña y extraiga texto de ellos"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Obtenga texto formateado programáticamente desde correos electrónicos y archivos adjuntos"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Sacar texto de una o varias páginas de un documento de OneNote"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Extraiga datos de PDF, MS Word, Excel y documentos de presentación"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Extraiga datos de los formularios PDF y extraiga texto de un archivo PDF simple o un documento de cartera PDF"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Obtenga texto formateado de una presentación de PowerPoint o elimine el texto de una diapositiva específica"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Reúna texto sin formato o con formato de celdas, filas y columnas de la hoja de cálculo de Excel"

      # feature loop
      - icon: "fas fa-columns"
        content: "Extraiga texto sin procesar o con formato HTML de un documento de Word"

      # feature loop
      - icon: "fas fa-file-word"
        content: "El formateador HTML admite formato de párrafo, hipervínculo, fuente, encabezados, listas y tablas"

      # feature loop
      - icon: "fas fa-envelope"
        content: "Extraiga una sola oración o texto completo de archivos EPUB, CHM, Markdown y FB2"

      # feature loop
      - icon: "fas fa-print"
        content: "Extracto del índice de la base de datos, PDF, EPUB, CHM y documentos de procesamiento de textos"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Saque el texto con su estructura de contenido intacta y extraiga el texto resaltado de los documentos"

      # feature loop
      - icon: "fas fa-lock"
        content: "Obtenga el área de texto de los documentos para el análisis y extraiga los metadatos de los formatos de documentos admitidos"

      # feature loop
      - icon: "fas fa-file-code"
        content: "Obtenga todas las imágenes o las seleccionadas de los formatos admitidos y gire las imágenes extraídas"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Extraiga texto de archivos dentro de archivos comprimidos y contenedores OST y detecte tipos de archivos de elementos de contenedores ZIP"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "Obtener datos del contenedor de correo electrónico (Exchange Web Server, POP3, IMAP)"

      # feature loop
      - icon: "fas fa-heading"
        content: "Busque texto simple, palabra completa y expresión regular dentro de los documentos"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Prepare la plantilla del documento, extraiga datos del documento y analice campos y tablas de datos"

      # feature loop
      - icon: "fas fa-cube"
        content: "Buscar y extraer expresiones resaltadas en documentos"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Obtener texto con el formateador de texto sin formato (simple y ASCII) o con el formateador Markdown"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Markdown Formatter admite formato de fuente, hipervínculos, encabezados, listas y tablas"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Aplicar formato personalizado con bordes, ángulos e intersecciones para dar formato a texto sin formato"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Mueva el diseño de la tabla y detecte las tablas en un área rectangular por separadores de columnas"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extract Text from Shapes, WordArt Objects & Text Boxes within oficina de Microsoft File Formats"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extraer imágenes to Files – Save to JPG, PNG, GIF, BMP, PNG or WEBP Formats"

    more_feature:
      # more_feature_loop
      - title: "Extraer texto de un documento"
        content: |
          Usar GroupDocs.Parser para .NET API para extraer texto de un documento es simple y se logra con solo unas pocas líneas de código:

          ```cs
          using(Parser parser = new Parser("sample.docx"))
          {
            // Extraer texto en el lector
            using(TextReader reader = parser.GetText())
            {
              // Imprimir texto del documento
              // Si no se admite la extracción de texto, el lector es nulo
              Console.WriteLine(reader == null ? "Text extraction isn't supported." : reader.ReadToEnd());
            }
          }
          ```

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser ofrece API de visualización de documentos para otros entornos de desarrollo populares"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for Java"
          image: "/border/groupdocs-parser-java.svg"
          product: "GroupDocs.Parser"
          platform: "Java"
          link: "/parser/java/"

############################# Back to top ###############################
back_to_top:
  enable: true
---