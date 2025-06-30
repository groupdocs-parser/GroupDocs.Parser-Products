


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:19
draft: false
lang: es
format: Ods
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraiga códigos de barras de archivos ODS en aplicaciones C#"
head_description: "Utilice GroupDocs.Parser para detectar y extraer datos de códigos de barras de archivos ODS en C# sin software adicional."

############################# Header ############################
title: "Extraiga códigos de barras de ODS utilizando C#" 
description: "Detecte y extraiga información de códigos de barras de archivos PDF, Word, Excel e imágenes utilizando GroupDocs.Parser en sus aplicaciones .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Descargar Prueba Gratuita"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Acerca de la API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Aprender más"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) es una potente API de análisis de documentos para desarrolladores de .NET. Permite la extracción de texto, imágenes, contenido estructurado y códigos de barras de varios formatos de archivo, incluidos PDF, Word, Excel, PowerPoint y más, todo sin depender de herramientas externas.

############################# Steps ############################
steps:
    enable: true
    title: "Pasos para extraer códigos de barras de Ods en C#"
    content: |
      [GroupDocs.Parser](/parser/net/) le permite extraer datos de códigos de barras de archivos ODS en aplicaciones .NET siguiendo estos pasos sencillos:
      
      1. Cargue el archivo ODS utilizando una instancia de Parser.
      2. Verifique que el documento admita la extracción de códigos de barras.
      3. Recupere la lista de códigos de barras del documento.
      4. Itere a través de los resultados y utilice los valores de código de barras extraídos.
   
    code:
      platform: "net"
      copy_title: "Copiar"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "haga clic para copiar"
        copy_done: "copiado"
      links:
        #  loop
        - title: "Más ejemplos"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Documentación"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Cargue el documento que contiene códigos de barras utilizando la clase Parser
        using (Parser parser = new Parser("input.ods")) {

            // Verifique que el archivo admita la extracción de códigos de barras
            if (!parser.Features.Barcodes) {
                Console.WriteLine("La extracción de códigos de barras no es compatible");
                return;
            }

            // Recupere y procese los códigos de barras extraídos
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            foreach (PageBarcodeArea barcode in barcodes) {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Funciones avanzadas de análisis de documentos"
  description: "Más allá de la extracción de códigos de barras, GroupDocs.Parser le permite extraer texto plano, imágenes y datos estructurados para apoyar la automatización avanzada y flujos de trabajo de procesamiento de datos."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Reconocimiento de códigos de barras y análisis de documentos"
  features:
    # feature loop
    - title: "Soporte para múltiples formatos de códigos de barras"
      content: "Reconozca tipos de códigos de barras comunes, incluidos QR Code, Code 128, Data Matrix, EAN, Aztec y más."

    # feature loop
    - title: "Extraiga códigos de barras de documentos e imágenes"
      content: "Lea códigos de barras de documentos PDF, Word, Excel y formatos de imagen como JPEG, PNG y BMP."

    # feature loop
    - title: "Configuraciones de extracción personalizables"
      content: "Configure opciones de detección como regiones de escaneo y procesamiento de documentos multipágina."
      
  code_samples:
    # code sample loop
    - title: "Cómo extraer códigos de barras de un PDF utilizando opciones de código de barras"
      content: |
        Este ejemplo demuestra cómo extraer códigos de barras de un archivo PDF utilizando opciones específicas de extracción de códigos de barras.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Cargue el archivo PDF con la clase Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Confirme que la extracción de códigos de barras es compatible
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // Utilice opciones de códigos de barras para filtrar los resultados
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Recupere los datos de códigos de barras del documento
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // Procese la lista de códigos de barras extraídos
            foreach (PageBarcodeArea barcode in barcodes)
            {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "¿Listo para comenzar?"
  description: "Pruebe las características de GroupDocs.Parser gratis o solicite una licencia"
  items:
    #  loop
    - title: "Descarga de Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Licenciamiento"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Formatos compatibles para la extracción de códigos de barras"
    exclude: "ODS"
    description: "GroupDocs.Parser admite la detección de códigos de barras en una amplia gama de formatos de documentos e imágenes. Consulte a continuación los tipos de archivos comúnmente soportados."
    items: 
        # format loop 1
        - name: "Analizar PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(Formato de documento portátil)"
          
        # format loop 2
        - name: "Analizar DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(Documento Word 2007+)"
          
        # format loop 3
        - name: "Analizar PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(Formato de presentación Open XML)"
          
        # format loop 4
        - name: "Analizar XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(Libro de trabajo Open XML)"
          
        # format loop 5
        - name: "Analizar ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(Documento de texto OpenDocument)"
          
        # format loop 6
        - name: "Analizar ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(Hoja de cálculo OpenDocument)"
          
        # format loop 7
        - name: "Analizar ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(Presentación OpenDocument)"
          
        # format loop 8
        - name: "Analizar EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(Archivo de eBook abierto)"
          
        # format loop 9
        - name: "Analizar FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---