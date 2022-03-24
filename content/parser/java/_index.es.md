---
############################# Static ############################
layout: "product"
date: 2021-04-27T09:31:06+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "API de Java para analizar texto, imágenes y metadatos de PDF Word Excel HTML"
head_description: "API de analizador de documentos Java para extraer texto, imágenes, metadatos y codificación de bases de datos, Word, Excel, presentaciones, PDF, correo electrónico, EPUB y archivos ZIP."

############################# Header ############################
title: "API de Java Parser para extraer datos"
description: "API de Java para analizar y extraer imágenes y texto con metadatos de documentos, presentaciones, archivos y correos electrónicos."
button:
    enable: true

############################# SubMenu ############################
submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "/border/groupdocs-parser-java.svg"
        product: "GroupDocs.Parser"
        platform: "Java"

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
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Precios"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java/"
        link_buy: "https://purchase.groupdocs.com"

############################# Visión de conjunto ############################
overview:
    enable: true
    content: |
      GroupDocs.Parser para Java es una API de extracción de texto, imágenes y metadatos que admite más de 50 tipos de documentos populares para ayudar a crear aplicaciones comerciales con funciones de análisis de texto sin procesar, estructurado y formateado. También admite el análisis de documentos utilizando plantillas predefinidas y permite extraer datos complejos de facturas y otros documentos típicos con rapidez y precisión. GroupDocs.Parser para Java le permite extraer texto y metadatos de archivos protegidos con contraseña de todos los formatos populares, incluidos documentos de procesamiento de texto, hojas de cálculo de Excel, presentaciones de PowerPoint, OneNote, archivos PDF y archivos ZIP.
    tabs:
      enable: true     
      
      ## TAB ONE ##
      tab_one:
        description: |
          A continuación se muestra una descripción general de GroupDocs.Parser para Java:

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
          GroupDocs.Parser para Java admite los siguientes [formatos de archivo de documento] (https://docs.groupdocs.com/parser/java/supported-document-formats/):

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
                * **Text**: DOC, DOCX, DOT, DOTX, DOTM, OTT, ODT
                * **Spreadsheets**: XLS, XLSX, XLT, XLTX, XLTM, XLA, XLAM, OTS, ODS
                * **Presentations**: PPT, PPTX, POT, POTX, POTM, PPSM, PPTM, OTP, ODP
                * **Email**: MSG, EML, EMLX
                * **Electronic Publishing**: EPUB, FB2
                * **Other**: PDF

            # table loop
            - title: "Text & Extracción de metadatos"
              content: |
                * **Template**: DOTX, POTX
                * **Macro-Enabled Template**: DOTM, POTM, PPSM, PPTM
                * **OpenDocument Template**: OTT

            # table loop
            - title: "Extracción de imagen"
              content: |
                * **Text**: DOC, DOCX, DOCM, RTF, DOT, DOTM, DOTX, ODT
                * **Spreadsheets**: XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **Presentations**: PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **Portable Document**: PDF, POT, POTM, POTX
                * **Ebook**: CHM, EPUB, FB2
                * **Markup**: HTML

      ## TAB THREE ##
      tab_three:
        description: |
          GroupDocs.Parser for Java supports following Sistemas operativos, Frameworks & Package ‎Managers:‎
        
        left:
          enable: true
          table:
            # table loop
            - icon: "fab fa-windows"
              title: "Sistemas operativos"
              content: |
                * Microsoft Windows Desktop
                * Microsoft Windows Server
                * Linux
                * MacOS

            # table loop
            - icon: "fas fa-code"
              title: "Marcos compatibles"
              content: |
                * Java 7 (1.7) y superior

        right:
          enable: true
          table:
            # table loop
            - icon: "fas fa-cogs"
              title: "Entornos de desarrollo"
              content: |
                * NetBeans
                * IntelliJ IDEA
                * Eclipse
            # table loop
            - icon: "fas fa-tools"
              title: "Herramienta de automatización de compilación"
              content: |
                * Maven

############################# Características ############################
features:
    enable: true
    title: "GroupDocs.Parser for Java Características"

    feature:
      # feature loop
      - icon: "fas fa-copy"
        content: "Contar estadísticamente la ocurrencia de palabras para documentos individuales o múltiples"

      # feature loop
      - icon: "fas fa-eye"
        content: "Extraiga texto y metadatos de hojas de cálculo de Excel y plantillas de presentación de PowerPoint"

      # feature loop
      - icon: "fas fa-bolt"
        content: "Obtener texto de un archivo o flujo, sin instalar el lector de documentos"
      
      # feature loop
      - icon: "fas fa-file-powerpoint"
        content: "Pull Out Formatted Text from a Document Using Fast or Standard Extracción de texto Mode"

      # feature loop
      - icon: "fas fa-code"
        content: "Detecte el tipo de medio de documentos XML protegidos con contraseña y extraiga texto de ellos"

      # feature loop
      - icon: "fas fa-cloud"
        content: "Obtenga texto con formato de una presentación de PowerPoint, correos electrónicos y archivos adjuntos mediante programación"

      # feature loop
      - icon: "fas fa-remove-format"
        content: "Expulsar texto de una o varias páginas del documento de OneNote"

      # feature loop
      - icon: "fas fa-comment-slash"
        content: "Saque el texto sin procesar de un archivo PDF simple o un documento de cartera PDF"

      # feature loop
      - icon: "fas fa-location-arrow"
        content: "Extraiga datos de PDF, MS Word, Excel y documentos de presentación"

      # feature loop
      - icon: "fas fa-border-all"
        content: "Extraiga texto sin procesar o formateado de celdas, filas y columnas de la hoja de cálculo de Excel"

      # feature loop
      - icon: "fas fa-wrench"
        content: "Recopile texto sin procesar o con formato HTML de un documento de Word y extraiga el texto resaltado de los documentos"

      # feature loop
      - icon: "fas fa-columns"
        content: "Obtenga datos de los formularios PDF y obtenga una tabla con formato de un documento PDF o Word"

      # feature loop
      - icon: "fas fa-file-word"
        content: "Extraiga una sola oración o texto completo de archivos EPUB, CHM, Markdown y FB2"

      # feature loop
      - icon: "fas fa-print"
        content: "Recuperar área de texto de documentos para análisis y extracción de texto con su estructura de contenido intacta"

      # feature loop
      - icon: "fas fa-file-archive"
        content: "Obtener metadatos de formatos de documentos admitidos"

      # feature loop
      - icon: "fas fa-lock"
        content: "Extraiga todas las imágenes o las seleccionadas de los formatos admitidos y gire las imágenes extraídas"

      # feature loop
      - icon: "fas fa-file-code"
        content: "Extract Text from Files within Zip Archives & OST Containers – Detectar tipo de medios for Zip Container Items"
      
      # feature loop
      - icon: "fas fa-fill-drip"
        content: "Obtener datos del contenedor de correo electrónico (Exchange Web Server, POP3, IMAP)"

      # feature loop
      - icon: "fas fa-file-excel"
        content: "Take Out Text from Base de datos Containers in Fast, Reliable and Efficient Manner"

      # feature loop
      - icon: "fas fa-heading"
        content: "Encuentre texto simple, palabra completa y expresión regular dentro de los documentos"

      # feature loop
      - icon: "fas fa-project-diagram"
        content: "Prepare la plantilla del documento, extraiga datos del documento y analice campos y tablas de datos"

      # feature loop
      - icon: "fas fa-cube"
        content: "Buscar y extraer expresiones resaltadas en documentos"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Saque el texto con formateador de texto sin formato (simple y ASCII) o formato personalizado con bordes, ángulos e intersecciones"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Obtenga y formatee texto (fuente, hipervínculos, encabezados, listas y tablas) con Markdown Formatter"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Obtenga texto con formateador HTML y aplique formateador a párrafos, hipervínculos, fuentes, encabezados, listas y tablas"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Mueva el diseño de la tabla y detecte las tablas en un área rectangular por separadores de columnas"

      # feature loop
      - icon: "fab fa-uncharted"
        content: "Extract Text from Shapes, WordArt Objects & Text Boxes within oficina de Microsoft File Formats"

    more_feature:
      # more_feature_loop
      - title: "Obtener texto con formateadores de texto sin formato o HTML"
        content: |
          Con GroupDocs.Parser para Java, puede aplicar varios formateadores al texto y HTML. Puede extraer texto con el Formateador de texto sin formato tanto para Sencillo como para ASCII. También puede obtener texto con HTML Formatter y aplicar formato a párrafos, hipervínculos, fuentes, encabezados, listas y tablas.

############################# Support ############################
support:
    enable: true

############################# Solutions ############################
solutions:
    enable: true
    title: "GroupDocs.Parser ofrece API de visualización de documentos para otros entornos de desarrollo populares"

    solution:
        # solution loop
        - img_alt: "GroupDocs.Parser for .NET"
          image: "/border/groupdocs-parser-net.svg"
          product: "GroupDocs.Parser"
          platform: ".NET"
          link: "/parser/net/"

############################# Back to top ###############################
back_to_top:
  enable: true
---