---
############################# Static ############################
layout: "landing"
date: 2024-02-13T17:01:03
draft: false
#operation: 
#parsertype: 
#fileformat: 
#productName: Java
lang: "es"
#productCode: java
#otherformats: 
#breadcrumb: Put  parser on  for Java
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: ".NET, Java, API en la nube y aplicaciones de análisis de documentos en línea"
head_description: "Obtenga una solución de análisis de documentos todo en uno para .NET, Java y aplicaciones basadas en la nube. Extraiga datos de formatos de documentos en línea usando la función simple de arrastrar y soltar"

############################# Header ############################
title: "Analizar documentos<br>a través de Java API"
description: "Extraiga datos de documentos e imágenes en cualquier plataforma utilizando nuestras API flexibles y soluciones basadas en aplicaciones para programadores y usuarios finales."
words:
  for: "para"

actions:
  main: "Descarga gratuita de Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licencia"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java"
  title: "¿Listo para comenzar?"
  description: "Pruebe GroupDocs.Parser funciones gratis o solicite una licencia"

release:
  title: "Versión {0} lanzada"
  notes: "Ver qué hay de nuevo"
  downloads: "Descargas"

code:
  title: "Extraiga texto de PDF archivos en Java"
  more: "Más ejemplos"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Create an instance of Parser class
    try (Parser parser = new Parser(fileName)) {
        // Extract a text into the reader
        try (TextReader reader = parser.getText()) {
            // Print a text from the document
            System.out.println(reader == null 
                    ? "" 
                    : reader.readToEnd());
        }
    } 
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser Descripción general"
  description: "API para realizar análisis de documentos en Java aplicaciones"
  features:
    # feature loop
    - title: "Extraer datos de documentos"
      content: "Java API le permite recuperar texto, metadatos e imágenes de una amplia gama de formatos de archivo, como documentos de Office, correos electrónicos, archivos adjuntos y archivos. Esta poderosa herramienta lo ayuda a acceder y procesar de manera eficiente información valiosa contenida en estos archivos para diversas aplicaciones como análisis de datos, indexación de motores de búsqueda o sistemas de administración de contenido."

    # feature loop
    - title: "Analizar documentos"
      content: "Extraiga varios elementos como hipervínculos, tablas, códigos QR, códigos de barras y datos de PDF formularios. Analice también cualquier información deseada de los documentos utilizando plantillas personalizadas."

    # feature loop
    - title: "Personalización de resultados"
      content: "Java API le permite recuperar datos en varios formatos, como sin formato, estructurado, HTML o Markdown. Además, API ofrece una función de búsqueda para localizar palabras o frases específicas dentro del texto de los documentos."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independencia de plataforma"
  description: "GroupDocs.Parser for Java es compatible con los siguientes sistemas operativos, marcos y administradores de paquetes"
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
  title: "Formatos de archivo admitidos"
  description: |
    GroupDocs.Parser for Java admite operaciones con los siguientes [formatos de archivo](https://docs.groupdocs.com/parser/java/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office formatos
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Imágenes y otros formatos
        * **Portable:** PDF
        * **Imágenes:** JPG, BMP, PNG, TIFF, GIF, DICOM, WEBP
        * **Otros formatos de oficina:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Otros formatos
        * **Web:** HTML, MHTML
        * **Archivo:** ZIP, TAR, 7Z
        * **Libros electrónicos:** CHM, EPUB, FB2, MOBI

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser características"
  description: "Extraiga datos de PDFs, documentos de Office e imágenes de forma rápida y precisa."

  items:
    # feature loop
    - icon: "text"
      title: "Extraer texto"
      content: "Extraiga información textual de varios formatos de archivo, como documentos de Office, PDF archivos e imágenes para facilitar la lectura y el análisis."

    # feature loop
    - icon: "image"
      title: "Extraer imágenes"
      content: "Recupere contenido visual de diversas fuentes, como documentos de Office y archivos PDF para acceder y utilizar cómodamente."

    # feature loop
    - icon: "qr"
      title: "Escanear códigos QR"
      content: "Detecte y decodifique códigos QR presentes en documentos de Office, PDF archivos o contenido visual para una recuperación eficiente de la información."

    # feature loop
    - icon: "email"
      title: "Extraiga datos de archivos adjuntos y archivos de correo electrónico"
      content: "Recopile información valiosa de mensajes de correo electrónico, archivos adjuntos y fuentes de datos comprimidos para un análisis y utilización eficaces."

    # feature loop
    - icon: "table"
      title: "Extraer tablas"
      content: "Identifique y extraiga datos tabulares de PDF documentos para su análisis y uso organizados."

    # feature loop
    - icon: "hyperlink"
      title: "Extraer hipervínculos"
      content: "Localice y extraiga hipervínculos y direcciones de correo electrónico dentro de documentos de Office o archivos PDF para un acceso eficiente."

    # feature loop
    - icon: "pdf"
      title: "Analizar PDF formularios"
      content: "PDF Los formularios son documentos digitales que presentan campos que se pueden completar para la interacción del usuario, lo que les permite ingresar información electrónicamente. Java Se puede utilizar API para extraer datos de estos formularios para un procesamiento eficiente."

    # feature loop
    - icon: "template"
      title: "Analizar datos por plantillas"
      content: "Cree plantillas personalizadas y utilícelas con Java API para analizar información específica de PDF archivos, simplificando los procesos de extracción de datos."

    # feature loop
    - icon: "search"
      title: "Buscar un texto en documentos"
      content: "Localice rápidamente palabras o patrones específicos dentro de los documentos."

############################# Code samples ############################
code_samples:
  enable: true
  title: "Ejemplo de código"
  description: "Algunos casos de uso de operaciones GroupDocs.Parser for Java típicas"
  items:
    # code sample loop
    - title: "Extraer imágenes de PDF documentos"
      content: |
        La API Java facilita a los desarrolladores Java la extracción de imágenes de documentos mediante la implementación de unos sencillos pasos.
        {{< landing/code title="Extraiga imágenes de PDF documentos en Java">}}
        ```java {style=abap}
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // Extract images
            Iterable<PageImageArea> images = parser.getImages();
            // Check if images extraction is supported
            if (images != null) {
                int imageIndex = 0;
                // Iterate over images
                for (PageImageArea image : images) {
                    // Save the image to the file
                    image.save(String.format("%s%s", imageIndex, image.getFileType().getExtension()));
                }
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraer códigos de barras de imágenes"
      content: |
        La API Java facilita a los desarrolladores Java extraer códigos de barras de documentos implementando unos sencillos pasos.
        {{< landing/code title="Extraer códigos de barras de imágenes">}}
        ```java {style=abap}   
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // // Check if the file supports barcode extracting
            if (!parser.getFeatures().isBarcodes()) {
                // Extract barcodes from the file.
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
                // Iterate over barcodes
                for (PageBarcodeArea barcode : barcodes) {
                    // Print the page index
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Print the barcode value
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
