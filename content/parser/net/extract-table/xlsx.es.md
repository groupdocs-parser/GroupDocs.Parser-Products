


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:40
draft: false
lang: es
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraer tablas de archivos XLSX en aplicaciones C#"
head_description: "Utiliza GroupDocs.Parser para localizar y extraer datos de tablas estructuradas de archivos XLSX en aplicaciones C# sin dependencias adicionales."

############################# Header ############################
title: "Extrae tablas de XLSX usando C#" 
description: "Identifica y extrae rápidamente estructuras de tablas de PDF, Word, Excel y otros formatos de archivo utilizando GroupDocs.Parser en tus proyectos de .NET."
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
       [GroupDocs.Parser](/parser/net/) es una API integral de análisis de documentos creada para desarrolladores de .NET. Permite la extracción precisa de texto, tablas, imágenes, hiperenlaces y otros elementos estructurados de formatos como PDF, DOCX, XLSX, PPTX y muchos otros, sin necesidad de software de terceros.

############################# Steps ############################
steps:
    enable: true
    title: "Pasos para extraer tablas de Xlsx en C#"
    content: |
      Sigue estas instrucciones para extraer tablas de archivos XLSX usando [GroupDocs.Parser](/parser/net/) dentro de tu entorno .NET:
      
      1. Inicializa una instancia de Parser y carga tu documento XLSX.
      2. Verifica si la extracción de tablas es soportada para el formato de entrada.
      3. Extrae el contenido de la tabla del archivo.
      4. Utiliza los datos de la tabla estructurada para informes, automatización o análisis.
   
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
        // Abre el documento que contiene datos de tabla utilizando Parser
        using (Parser parser = new Parser("input.xlsx")) {

            // Verifica si el formato soporta el reconocimiento de tablas
            if (!parser.Features.Tables) {
                Console.WriteLine("Maneja documentos que no soportan el análisis de tablas");
                return;
            }

            // Define cómo debe reconocerse la estructura de la tabla
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // Especifica parámetros de extracción para los datos de la tabla
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Extrae tablas del contenido del archivo
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  Itera a través de cada tabla detectada
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Potentes capacidades de extracción de datos"
  description: "Además del análisis de tablas, GroupDocs.Parser puede extraer contenido enriquecido como bloques de texto, imágenes, metadatos y otros datos estructurados para facilitar la automatización de documentos."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Reconocimiento de tablas y extracción de contenido"
  features:
    # feature loop
    - title: "Detección precisa de tablas en múltiples formatos"
      content: "Extrae datos tabulares de DOCX, XLSX, PDF, HTML y formatos similares con alta precisión."

    # feature loop
    - title: "Analiza estructuras de tablas desde archivos"
      content: "Recupera eficientemente datos de tablas de documentos y hojas de cálculo sin pérdida de formato."

    # feature loop
    - title: "Configuración flexible de extracción de tablas"
      content: "Ajusta la detección de diseño, la alineación de columnas y las opciones de encabezado/pie de página para un control preciso sobre la salida."
      
  code_samples:
    # code sample loop
    - title: "Cómo extraer tablas de hojas de cálculo de Excel"
      content: |
        Este ejemplo de código muestra cómo leer e iterar a través de datos de tabla en un archivo XLSX usando GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Abre el archivo de Excel utilizando la API Parser
        using (Parser parser = new Parser("input.xlsx"))
        {
            // Sal si no se pueden extraer tablas del archivo
            if (!parser.Features.Tables)
            {
                return;
            }

            // Utiliza reglas de diseño para localizar contenido tabular
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // Configura los parámetros de extracción para las tablas
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Realiza la operación de extracción de tablas
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // Revisa la estructura de cada tabla detectada
            foreach (PageTableArea t in tables)
            {
                // Itera a través de cada fila en la tabla
                for (int row = 0; row < t.RowCount; row++)
                {
                    // Itera sobre las celdas en cada fila
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // Accede a la celda actual de la tabla
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // Muestra el contenido de texto de cada celda
                            Console.Write(cell.Text);
                            Console.Write(" | ");
                        }
                    }
                }
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
    title: "Formatos soportados para extracción de tablas"
    exclude: "XLSX"
    description: "GroupDocs.Parser puede extraer datos de tablas de una variedad de tipos de documentos. A continuación se presentan los formatos más utilizados para el análisis estructurado de tablas."
    items: 
        # format loop 1
        - name: "Analizar PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(Formato de documento portátil)"
          
        # format loop 2
        - name: "Analizar DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Documento Word 2007+)"
          
        # format loop 3
        - name: "Analizar PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Formato de presentación Open XML)"
          
        # format loop 4
        - name: "Analizar XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Libro de trabajo Open XML)"
          
        # format loop 5
        - name: "Analizar TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(Archivo de texto)"
          
        # format loop 6
        - name: "Analizar RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(Formato de texto enriquecido)"
          
        # format loop 7
        - name: "Analizar XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(Lenguaje de marcado extensible)"
          
        # format loop 8
        - name: "Analizar EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(Archivo de eBook abierto)"
         
          

---