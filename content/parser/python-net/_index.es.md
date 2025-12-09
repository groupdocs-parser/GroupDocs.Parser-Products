---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: es
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK para Python"
head_description: "SDK de análisis de documentos de alto rendimiento para Python. Extraiga texto, imágenes, metadatos, códigos de barras, tablas y otros datos de PDF, Word, Excel, correos electrónicos y más de 50 formatos de documentos."

############################# Header ############################
title: "SDK de análisis de documentos para Python"
description: "Añada un análisis de documentos rápido y preciso a sus aplicaciones Python y extraiga texto, imágenes, metadatos y datos estructurados de documentos e imágenes."
words:
  for: "para"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI Descargar"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Licencias"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "¿Listo para comenzar?"
  description: "Pruebe las funciones de GroupDocs.Parser de forma gratuita o solicite una licencia."

release:
  enable: false
  title: "Versión {0} lanzada"
  notes: "Ver qué hay de nuevo"
  downloads: "Descargas"

code:
  title: "Extraer texto usando Python"
  more: "Más ejemplos"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Cargar el documento
    with Parser("sample.pdf") as parser:
        # Extraer texto del documento
        text = parser.GetText()

        # Imprimir todo el texto extraído
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser en un vistazo"
  description: "SDK de análisis de documentos para realizar análisis de documentos de alta precisión en aplicaciones Python"
  features:
    # feature loop
    - title: "Extraer datos de documentos"
      content: "GroupDocs.Parser for Python via .NET API le permite recuperar texto, metadatos e imágenes de una amplia variedad de formatos de archivo, como documentos de Office, correos electrónicos, archivos adjuntos y archivos comprimidos. Esta herramienta potente le ayuda a acceder y procesar de manera eficiente la información valiosa contenida en estos archivos para diversas aplicaciones, como análisis de datos, indexación en motores de búsqueda o sistemas de gestión de contenidos."

    # feature loop
    - title: "Analizar documentos"
      content: "Extraiga diversos elementos como hipervínculos, tablas, códigos QR, códigos de barras y datos de formularios PDF. También analice cualquier información deseada de los documentos utilizando plantillas personalizadas."

    # feature loop
    - title: "Personalizar resultados"
      content: "Python API le permite recuperar datos en varios formatos, como crudo, estructurado, HTML o Markdown. Además, la API ofrece una funcionalidad de búsqueda para localizar palabras o frases específicas dentro del texto de los documentos."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independencia de plataforma"
  description: "GroupDocs.Parser for Python via .NET admite los siguientes sistemas operativos, frameworks y gestores de paquetes"
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "Formatos de archivo compatibles"
  description: |
    GroupDocs.Parser for Python via .NET admite operaciones con los siguientes [formatos de archivo](https://docs.groupdocs.com/parser/python-net/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Formatos de Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Imágenes y otros formatos
        * **Portátil:** PDF 
        * **Imágenes:** JPG, BMP, PNG, TIFF, GIF
        * **Otros formatos de oficina:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Otros formatos
        * **Web:** HTML, MHTML 
        * **Archivos:** ZIP, TAR, 7Z 
        * **eBooks:** CHM, EPUB, FB2, MOBI 

############################# Features ############################
features:
  enable: true
  title: "Funciones de GroupDocs.Parser for Python via .NET"
  description: "Extraiga datos de PDFs, documentos de Office, imágenes y otros formatos de manera rápida y precisa con nuestro SDK de análisis de documentos Python"

  items:
    # feature loop
    - icon: "text"
      title: "Extraer texto"
      content: "Extraiga información textual de varios formatos de archivo, como documentos de Office, archivos PDF e imágenes, para una fácil legibilidad y análisis."

    # feature loop
    - icon: "image"
      title: "Extraer imágenes"
      content: "Recupere contenido visual de diversas fuentes, como documentos de Office y archivos PDF, para un acceso y uso conveniente."

    # feature loop
    - icon: "qr"
      title: "Escanear códigos QR"
      content: "Detecte y decodifique códigos QR presentes en documentos de Office, archivos PDF o contenido visual, para una recuperación de información eficiente."

    # feature loop
    - icon: "email"
      title: "Extraer datos de archivos adjuntos de correo electrónico y archivos comprimidos"
      content: "Recopile información valiosa de mensajes de correo electrónico, archivos adjuntos y fuentes de datos comprimidos para un análisis y utilización efectivos."

    # feature loop
    - icon: "table"
      title: "Extraer tablas"
      content: "Identifique y extraiga datos tabulares de documentos PDF para un análisis y uso organizados."

    # feature loop
    - icon: "hyperlink"
      title: "Extraer hipervínculos"
      content: "Localice y extraiga hipervínculos y direcciones de correo electrónico dentro de documentos de Office o archivos PDF para un acceso eficiente."

    # feature loop
    - icon: "pdf"
      title: "Analizar formularios PDF"
      content: "Los formularios PDF son documentos digitales que presentan campos rellenables para la interacción del usuario, permitiendo que introduzcan información electrónicamente. La API Python puede utilizarse para extraer datos de estos formularios y procesarlos de manera eficiente."

    # feature loop
    - icon: "template"
      title: "Analizar datos mediante plantillas"
      content: "Cree plantillas personalizadas y utilícelas con la API Python para analizar información específica de archivos PDF, simplificando los procesos de extracción de datos."

    # feature loop
    - icon: "search"
      title: "Buscar texto en documentos"
      content: "Localice rápidamente palabras o patrones específicos dentro de los documentos."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Ejemplos de código"
  description: "Más allá de la extracción básica de texto, aquí están los casos de uso más comunes para la extracción rápida de texto, imágenes y metadatos."
  items:
    # code sample loop
    - title: "Buscar texto en un documento"
      content: |
        Este ejemplo muestra cómo buscar una frase específica en un documento PDF y mostrar dónde se encontró.
        {{< landing/code title="Buscar texto en un documento en Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Cargar el documento
        with Parser("sample.pdf") as parser:
            # Imprimir el índice de página y el rectángulo donde se encontró la frase
            for area in parser.Search("Total Amount"):
                # Imprimir el índice de página y el rectángulo donde se encontró la frase
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraer imágenes de un documento"
      content: |
        Este ejemplo muestra cómo extraer imágenes de un documento PDF y guardarlas en un archivo.
        {{< landing/code title="Extraer imágenes de un documento en Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Cargar el documento
        with Parser("sample.docx") as parser:
            # Extraer imágenes del documento
            images = parser.GetImages()

            # Guardar las imágenes en un archivo
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraer metadatos de un documento"
      content: |
        Este ejemplo muestra cómo extraer metadatos de un documento PDF y mostrarlos.
        {{< landing/code title="Extraer metadatos de un documento en Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Cargar el documento
        with Parser("sample.pdf") as parser:
            # Extraer metadatos del documento
            metadata = parser.GetMetadata()

            # Imprimir los metadatos
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
