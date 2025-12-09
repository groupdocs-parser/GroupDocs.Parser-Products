---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: es
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

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
head_title: "GroupDocs.Parser for .NET SDK de Análisis de Documentos para .NET"
head_description: "SDK de Análisis de Documentos de alto rendimiento para .NET. Extrae texto, imágenes, metadatos, códigos de barras, tablas y otros datos de PDF, Word, Excel, correos electrónicos y más de 50 formatos de documentos."

############################# Header ############################
title: "SDK de Análisis de Documentos para .NET"
description: "Añade un análisis de documentos rápido y preciso a tus aplicaciones .NET y extrae texto, imágenes, metadatos y datos estructurados de documentos e imágenes."
words:
  for: "para"

actions:
  main: "Nuget Descargar"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Licencias"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "¿Listo para comenzar?"
  description: "Pruebe las funciones de GroupDocs.Parser de forma gratuita o solicite una licencia."

release:
  title: "Versión {0} lanzada"
  notes: "Ver qué hay de nuevo"
  downloads: "Descargas"

code:
  title: "Analiza rápidamente el contenido de documentos con el SDK"
  more: "Más ejemplos"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Pasa el archivo fuente a la instancia de Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Pasa el texto del documento a TextReader
        using (var textReader = parser.GetText())
        {
            // Procesa el texto del documento
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser en un vistazo"
  description: "SDK de Análisis de Documentos para realizar un análisis de documentos de alta precisión en aplicaciones .NET"
  features:
    # feature loop
    - title: "Extraer datos de documentos"
      content: "GroupDocs.Parser for .NET API le permite recuperar texto, metadatos e imágenes de una amplia gama de formatos de archivo, como documentos de Office, correos electrónicos, adjuntos y archivos. Esta potente herramienta le ayuda a acceder y procesar de manera eficiente la información valiosa contenida en estos archivos para diversas aplicaciones, como análisis de datos, indexación de motores de búsqueda o sistemas de gestión de contenidos."

    # feature loop
    - title: "Analizar documentos"
      content: "Extrae varios elementos como hipervínculos, tablas, códigos QR, códigos de barras y datos de formularios PDF. También analiza cualquier información deseada de los documentos utilizando plantillas personalizadas."

    # feature loop
    - title: "Personalizar resultados"
      content: ".NET API le permite recuperar datos en varios formatos, como crudo, estructurado, HTML o Markdown. Además, la API ofrece una funcionalidad de búsqueda para localizar palabras o frases específicas dentro del texto de los documentos."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independencia de plataforma"
  description: "GroupDocs.Parser for .NET admite los siguientes sistemas operativos, frameworks y administradores de paquetes"
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
    GroupDocs.Parser for .NET admite operaciones con los siguientes [formatos de archivo](https://docs.groupdocs.com/parser/net/supported-document-formats/).
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
  title: "GroupDocs.Parser for .NET características"
  description: "Extraiga datos de PDFs, documentos de Office, imágenes y otros formatos de forma rápida y precisa con nuestro SDK de Análisis de Documentos .NET"

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
  description: "Algunos casos de uso típicos de operaciones de GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Extraer imágenes de documentos PDF"
      content: |
        GroupDocs.Parser for .NET facilita a los desarrolladores de C# extraer imágenes de [documentos](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Extraer imágenes de documentos PDF en C#">}}
        ```csharp {style=abap}
        // Cree una instancia de la clase Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Extraer imágenes
            var images = parser.GetImages();

            // Verifique si se ha extraído algo
            if (images == null)
            {
                return;
            }
            // Iterar sobre las imágenes
            foreach (PageImageArea image in images)
            {
                // Imprima el índice de página, el rectángulo y el tipo de imagen
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraer códigos de barras de imágenes"
      content: |
        Utilice nuestra API .NET para extraer [códigos de barras](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) de imágenes:
        {{< landing/code title="Extraer códigos de barras de imágenes en C#">}}
        ```csharp {style=abap}   
        // Cargue la imagen fuente en Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Verifique si el archivo admite la extracción de códigos de barras
            if (parser.Features.Barcodes)
            {
                // Extraer códigos de barras del archivo
                var barcodes = parser.GetBarcodes();

                // Iterar sobre los códigos de barras
                foreach (var barcode in barcodes)
                {
                    // Imprima el índice de página
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Imprima el valor del código de barras
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
