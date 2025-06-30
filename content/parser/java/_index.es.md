---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: es
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "Aplicaciones de análisis de documentos GroupDocs.Parser for Java"
head_description: "Obtenga una solución integral para el análisis de documentos para aplicaciones Java. Extraiga datos de formatos de documentos en línea utilizando una sencilla función de arrastrar y soltar."

############################# Header ############################
title: "Analizar documentos a través de la API Java"
description: "Extraiga datos de documentos e imágenes en cualquier plataforma utilizando nuestras APIs flexibles y soluciones basadas en aplicaciones para programadores y usuarios finales."
words:
  for: "para"

actions:
  main: "Descarga de Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licencias"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "¿Listo para comenzar?"
  description: "Pruebe las funciones de GroupDocs.Parser de forma gratuita o solicite una licencia."

release:
  title: "Versión {0} lanzada"
  notes: "Vea las novedades"
  downloads: "Descargas"

code:
  title: "Obtener rápidamente el contenido del documento"
  more: "Más ejemplos"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Pase el archivo fuente a la instancia de Parser.
    try (Parser parser = new Parser("source.pdf"))
    {
        // Pase el texto del documento a TextReader.
        try (TextReader reader = parser.getText())
        {
            // Procese el texto del documento.
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser en un vistazo"
  description: "API para realizar análisis de documentos en aplicaciones Java."
  features:
    # feature loop
    - title: "Extraer datos de documentos"
      content: "La API GroupDocs.Parser for Java permite recuperar texto, metadatos e imágenes de una amplia gama de formatos de archivo, como documentos de Office, correos electrónicos, archivos adjuntos y archivos comprimidos. Esta herramienta potente le ayuda a acceder y procesar eficientemente la información valiosa contenida dentro de estos archivos para varias aplicaciones, como análisis de datos, indexación de motores de búsqueda o sistemas de gestión de contenido."

    # feature loop
    - title: "Analizar documentos"
      content: "Extraiga varios elementos como hipervínculos, tablas, códigos QR, códigos de barras y datos de formularios PDF. También analice cualquier información deseada de documentos utilizando plantillas personalizadas."

    # feature loop
    - title: "Personalización de resultados"
      content: "La API Java le permite recuperar datos en varios formatos, como bruto, estructurado, HTML o Markdown. Además, la API ofrece una funcionalidad de búsqueda para localizar palabras o frases específicas dentro del texto de los documentos."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independencia de la plataforma"
  description: "La API GroupDocs.Parser for Java es compatible con los siguientes sistemas operativos, marcos de trabajo y gerentes de paquetes."
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
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "Formatos de archivo compatibles"
  description: |
    GroupDocs.Parser for Java admite operaciones con los siguientes [formatos de archivo](https://docs.groupdocs.com/parser/java/supported-document-formats/).
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
        * **Portátiles:** PDF 
        * **Imágenes:** JPG, BMP, PNG, TIFF, GIF
        * **Otros formatos de oficina:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Otros formatos
        * **Web:** HTML, MHTML 
        * **Archivos:** ZIP, TAR, 7Z 
        * **e-Libros:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "Características de GroupDocs.Parser for Java"
  description: "Extraiga datos de PDF, documentos de Office e imágenes de manera rápida y precisa."

  items:
    # feature loop
    - icon: "text"
      title: "Extraer texto"
      content: "Extraiga información textual de varios formatos de archivo como documentos de oficina, archivos PDF e imágenes para una fácil legibilidad y análisis."

    # feature loop
    - icon: "image"
      title: "Extraer imágenes"
      content: "Recupere contenido visual de diversas fuentes, como documentos de oficina y archivos PDF, para un acceso y uso conveniente."

    # feature loop
    - icon: "qr"
      title: "Escanear códigos QR"
      content: "Detecte y decodifique códigos QR presentes en documentos de oficina, archivos PDF o contenido visual para una eficiente recuperación de información."

    # feature loop
    - icon: "email"
      title: "Extraer datos de archivos adjuntos de correo electrónico y archivos comprimidos"
      content: "Reúna información valiosa de mensajes de correo electrónico, archivos adjuntos y fuentes de datos comprimidos para un análisis y utilización efectiva."

    # feature loop
    - icon: "table"
      title: "Extraer tablas"
      content: "Identifique y extraiga datos tabulares de documentos PDF para un análisis y uso organizado."

    # feature loop
    - icon: "hyperlink"
      title: "Extraer hipervínculos"
      content: "Ubique y extraiga hipervínculos y direcciones de correo electrónico dentro de documentos de oficina o archivos PDF para un acceso eficiente."

    # feature loop
    - icon: "pdf"
      title: "Analizar formularios PDF"
      content: "Los formularios PDF son documentos digitales con campos rellenables para la interacción del usuario, permitiendo ingresar información electrónicamente. La API .NET puede ser utilizada para extraer datos de estos formularios para un procesamiento eficiente."

    # feature loop
    - icon: "template"
      title: "Analizar datos por plantillas"
      content: "Cree plantillas personalizadas y utilícelas con la API .NET para analizar información específica de archivos PDF, simplificando los procesos de extracción de datos."

    # feature loop
    - icon: "search"
      title: "Buscar un texto en documentos"
      content: "Localice rápidamente palabras o patrones específicos dentro de los documentos."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Ejemplos de código"
  description: "Algunos casos de uso de operaciones típicas de GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Extraer imágenes de documentos PDF"
      content: |
        GroupDocs.Parser for Java facilita a los desarrolladores Java extraer imágenes de [documentos](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Extraer imágenes de documentos PDF en Java">}}
        ```java {style=abap}
        // Cree una instancia de la clase Parser.
        try (Parser parser = new Parser("source.pdf"))
        {
            // Extraiga imágenes.
            Iterable<PageImageArea> images = parser.getImages();

            // Verifique si se extrajo algo.
            if (images == null) {
                return;
            }

            // Itere sobre las imágenes.
            for (PageImageArea image : images) {
                // Imprima el índice de la página, rectángulo y tipo de imagen.
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraer códigos de barras de imágenes"
      content: |
        Utilice nuestra API Java para extraer [códigos de barras](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) de imágenes:
        {{< landing/code title="Extraer códigos de barras de imágenes en Java">}}
        ```java {style=abap}   
        // Cargue la imagen fuente en Parser.
        try (Parser parser = new Parser("source.jpg")){

            // Verifique si el archivo es compatible con la extracción de códigos de barras.
            if (!parser.getFeatures().isBarcodes()) {

                // Extraiga códigos de barras del archivo.
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Itere sobre los códigos de barras.
                for (PageBarcodeArea barcode : barcodes) {
                    // Imprima el índice de la página.
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Imprima el valor del código de barras.
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
