---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Java Document Parser SDK para Java"
head_description: "SDK de análisis de documentos de alto rendimiento para Java. Extraiga texto, imágenes, metadatos, códigos de barras, tablas y otros datos de PDF, Word, Excel, correos electrónicos y más de 50 formatos de documento."

############################# Header ############################
title: "Document Parser SDK para Java"
description: "Añada análisis de documentos rápido y preciso a sus aplicaciones Java y extraiga texto, imágenes, metadatos y datos estructurados de documentos e imágenes."
words:
  for: "para"

actions:
  main: "Maven Descargar"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licencias"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "¿Listo para comenzar?"
  description: "Pruebe las funciones de GroupDocs.Parser de forma gratuita o solicite una licencia."

release:
  title: "Versión {0} lanzada"
  notes: "Ver qué hay de nuevo"
  downloads: "Descargas"

code:
  title: "Analice rápidamente el contenido del documento con el SDK"
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
    // Pase el archivo fuente a la instancia de Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Pase el texto del documento a TextReader
        try (TextReader reader = parser.getText())
        {
            // Procese el texto del documento
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
  description: "Document Parser SDK para realizar análisis de documentos de alta precisión en aplicaciones Java"
  features:
    # feature loop
    - title: "Extraer datos de documentos"
      content: "La API GroupDocs.Parser for Java le permite obtener texto, metadatos e imágenes de una amplia gama de formatos de archivo, como documentos de Office, correos electrónicos, adjuntos y archivos. Esta poderosa herramienta le ayuda a acceder y procesar eficientemente la información valiosa contenida en estos archivos para diversas aplicaciones, como análisis de datos, indexación de motores de búsqueda o sistemas de gestión de contenido."

    # feature loop
    - title: "Analizar documentos"
      content: "Extraiga varios elementos como hipervínculos, tablas, códigos QR, códigos de barras y datos de formularios PDF. También analice cualquier información deseada de los documentos mediante plantillas personalizadas."

    # feature loop
    - title: "Personalizar resultados"
      content: "Java API le permite obtener datos en varios formatos como sin procesar, estructurado, HTML o Markdown. Además, la API ofrece una funcionalidad de búsqueda para localizar palabras o frases específicas dentro del texto de los documentos."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independencia de plataforma"
  description: "GroupDocs.Parser for Java admite los siguientes sistemas operativos, frameworks y gestores de paquetes"
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
  title: "Funciones de GroupDocs.Parser for Java"
  description: "Extraiga datos de PDFs, documentos de Office, imágenes y otros formatos de forma rápida y precisa con nuestro SDK Java Document Parser."

  items:
    # feature loop
    - icon: "text"
      title: "Extraer texto"
      content: "Extrae información textual de varios formatos de archivo, como documentos de oficina, archivos PDF e imágenes, para una fácil lectura y análisis."

    # feature loop
    - icon: "image"
      title: "Extraer imágenes"
      content: "Recupera contenido visual de diversas fuentes, como documentos de oficina y archivos PDF, para un acceso y uso convenientes."

    # feature loop
    - icon: "qr"
      title: "Escanear códigos QR"
      content: "Detecta y decodifica códigos QR presentes en documentos de oficina, archivos PDF o contenido visual para una recuperación de información eficiente."

    # feature loop
    - icon: "email"
      title: "Extraer datos de adjuntos de correo electrónico y archivos"
      content: "Recopile información valiosa de mensajes de correo electrónico, archivos adjuntos y fuentes de datos comprimidos para un análisis y utilización eficaces."

    # feature loop
    - icon: "table"
      title: "Extraer tablas"
      content: "Identifique y extraiga datos tabulares de documentos PDF para un análisis y uso organizados."

    # feature loop
    - icon: "hyperlink"
      title: "Extraer hipervínculos"
      content: "Ubique y extraiga hipervínculos y direcciones de correo electrónico dentro de documentos de oficina o archivos PDF para un acceso eficiente."

    # feature loop
    - icon: "pdf"
      title: "Analizar formularios PDF"
      content: "Los formularios PDF son documentos digitales con campos rellenables para la interacción del usuario, que permiten introducir información electrónicamente. La API .NET puede utilizarse para extraer datos de estos formularios para un procesamiento eficiente."

    # feature loop
    - icon: "template"
      title: "Analizar datos mediante plantillas"
      content: "Cree plantillas personalizadas y utilícelas con la API .NET para analizar información específica de archivos PDF, simplificando los procesos de extracción de datos."

    # feature loop
    - icon: "search"
      title: "Buscar texto en documentos"
      content: "Ubique rápidamente palabras o patrones específicos dentro de los documentos."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Ejemplos de código"
  description: "Algunos casos de uso típicos de operaciones de GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Extraer imágenes de documentos PDF"
      content: |
        GroupDocs.Parser for Java facilita a los desarrolladores de Java extraer imágenes de [documentos](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Extraer imágenes de documentos PDF en Java">}}
        ```java {style=abap}
        // Cree una instancia de la clase Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Extraer imágenes
            Iterable<PageImageArea> images = parser.getImages();

            // Verifique si se ha extraído algo
            if (images == null) {
                return;
            }

            // Iterar sobre las imágenes
            for (PageImageArea image : images) {
                // Imprima el índice de página, el rectángulo y el tipo de imagen
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
        // Cargue la imagen fuente en Parser
        try (Parser parser = new Parser("source.jpg")){

            // Verifique si el archivo admite la extracción de códigos de barras
            if (!parser.getFeatures().isBarcodes()) {

                // Extraer códigos de barras del archivo
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Iterar sobre los códigos de barras
                for (PageBarcodeArea barcode : barcodes) {
                    // Imprima el índice de página
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Imprima el valor del código de barras
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
