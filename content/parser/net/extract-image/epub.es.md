


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:33
draft: false
lang: es
format: Epub
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraer imágenes de archivos EPUB en aplicaciones C#"
head_description: "Utiliza GroupDocs.Parser para detectar y extraer imágenes de archivos EPUB en C# sin herramientas adicionales."

############################# Header ############################
title: "Extrae imágenes de EPUB usando C#" 
description: "Localiza y extrae imágenes incrustadas de PDFs, documentos de Word, hojas de Excel y otros tipos de archivos utilizando GroupDocs.Parser en tus aplicaciones .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Descargar Prueba Gratis"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Acerca de la API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Aprender más"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) es una biblioteca robusta de análisis de documentos para desarrolladores .NET. Permite extraer imágenes, texto, hipervínculos y datos estructurados de formatos de archivo populares como PDF, DOCX, XLSX, PPTX y otros, todo sin necesidad de aplicaciones de terceros.

############################# Steps ############################
steps:
    enable: true
    title: "Pasos para extraer imágenes de Epub en C#"
    content: |
      Con [GroupDocs.Parser](/parser/net/), puedes extraer imágenes de documentos EPUB en tus proyectos .NET en solo unos pocos pasos:
      
      1. Inicializa el Parser con el archivo EPUB.
      2. Recupera los elementos de imagen del documento.
      3. Utiliza las imágenes extraídas según sea necesario en tu flujo de trabajo.
   
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
        // Abre el documento que contiene imágenes utilizando Parser
        using (Parser parser = new Parser("input.epub")) {

            // Extrae todas las imágenes incrustadas del archivo
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Maneja casos donde no se encuentran imágenes
            if (images == null)
            {
                return;
            }

            // Procesa o guarda las imágenes recuperadas
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Extracción integral del contenido del documento"
  description: "GroupDocs.Parser ofrece más que solo extracción de imágenes: también puedes extraer texto sin formato, hipervínculos, metadatos y contenido estructurado para escenarios de automatización avanzados."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Flujo de trabajo de extracción de imágenes y análisis de documentos"
  features:
    # feature loop
    - title: "Extrae imágenes de múltiples formatos"
      content: "Extrae imágenes incrustadas de una variedad de formatos de archivo, incluyendo DOCX, PDF, PPTX, XLSX, y archivos de imagen como PNG, JPG y TIFF."

    # feature loop
    - title: "Preservar la calidad original de la imagen"
      content: "Las imágenes se extraen con alta fidelidad, manteniendo su resolución original, formato y perfil de color."

    # feature loop
    - title: "Opciones avanzadas de extracción"
      content: "Personaliza la extracción de imágenes filtrando por página, formato o resolución, y soportando documentos de varias páginas."
      
  code_samples:
    # code sample loop
    - title: "Cómo extraer y guardar imágenes de un documento PDF"
      content: |
        Este ejemplo demuestra cómo extraer todos los activos de imagen de un archivo PDF y guardarlos en el sistema de archivos local.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Cargar el PDF utilizando la clase Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Extraer imágenes incrustadas del archivo
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Establecer formato de salida y opciones de imagen (por ejemplo, PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Escribir las imágenes extraídas en el disco
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
                imageNumber++;
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
    title: "Formatos compatibles para extracción de imágenes"
    exclude: "EPUB"
    description: "GroupDocs.Parser permite la extracción precisa de imágenes de una amplia gama de formatos de documentos e imágenes. Consulta la lista a continuación para los tipos comúnmente soportados."
    items: 
        # format loop 1
        - name: "Analizar PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(Formato de documento portátil)"
          
        # format loop 2
        - name: "Analizar DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Documento Word 2007+)"
          
        # format loop 3
        - name: "Analizar PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Formato de presentación Open XML)"
          
        # format loop 4
        - name: "Analizar XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Libro de trabajo Open XML)"
          
        # format loop 5
        - name: "Analizar ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(Documento de texto OpenDocument)"
          
        # format loop 6
        - name: "Analizar ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(Hoja de cálculo OpenDocument)"
          
        # format loop 7
        - name: "Analizar ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(Presentación OpenDocument)"
          
        # format loop 8
        - name: "Analizar EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(Archivo de eBook abierto)"
          
        # format loop 9
        - name: "Analizar FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---