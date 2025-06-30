


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:17
draft: false
lang: pt
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Leia códigos de barras de arquivos XLSX em aplicações Java"
head_description: "Com GroupDocs.Parser, extraia dados de código de barras de documentos XLSX usando Java sem ferramentas externas."

############################# Header ############################
title: "Leia códigos de barras de XLSX usando Java" 
description: "Extraia o conteúdo de códigos de barras de arquivos PDF, Word, Excel e de imagens utilizando GroupDocs.Parser em suas aplicações Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Baixar Versão de Avaliação Gratuita"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Visão Geral da API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Saiba mais"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) oferece uma solução abrangente para a análise de documentos em Java. Permite que desenvolvedores extraiam códigos de barras, texto, imagens e informações estruturadas de vários formatos de arquivo, como PDF, Word, Excel, PowerPoint e outros—sem a necessidade de bibliotecas de terceiros.

############################# Steps ############################
steps:
    enable: true
    title: "Como ler códigos de barras de Xlsx em Java"
    content: |
      Com [GroupDocs.Parser](/parser/java/), desenvolvedores Java podem extrair códigos de barras de documentos XLSX em apenas algumas etapas:
      
      1. Carregue o documento XLSX usando Parser.
      2. Verifique se o documento suporta extração de código de barras.
      3. Use a API para recuperar os dados do código de barras.
      4. Percorra os resultados do código de barras e aplique conforme necessário.
   
    code:
      platform: "net"
      copy_title: "Copiar"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "clique para copiar"
        copy_done: "copiado"
      links:
        #  loop
        - title: "Mais exemplos"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Documentação"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Abra um documento contendo códigos de barras usando Parser
        try (Parser parser = new Parser("input.xlsx"))
        {
            // Verifique o suporte a código de barras para o arquivo
            if (!parser.getFeatures().isBarcodes())
            {
                System.out.println("Lide com tipos de arquivos não suportados");
                return;
            }

            // Extraia e use os dados do código de barras
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
            for(PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + barcode.getPage().getIndex());
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Mais capacidades de análise"
  description: "GroupDocs.Parser vai além da extração de códigos de barras—também permite extrair texto simples, imagens e elementos estruturados para apoiar fluxos de trabalho baseados em dados."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Recursos de extração de código de barras e dados"
  features:
    # feature loop
    - title: "Suporte amplo a formatos de código de barras"
      content: "Detecte formatos de código de barras padrão, incluindo QR Code, Code 39, Data Matrix, EAN, Aztec e outros."

    # feature loop
    - title: "Leitura de códigos de barras de múltiplas fontes"
      content: "Extraia informações de códigos de barras de documentos do Office, PDFs e arquivos de imagem como PNG, JPG e BMP."

    # feature loop
    - title: "Configuração personalizada de leitura de código de barras"
      content: "Ajuste a extração de códigos de barras com opções para direcionar regiões específicas e arquivos de várias páginas."
      
  code_samples:
    # code sample loop
    - title: "Exemplo: extraia códigos de barras de PDF com opções"
      content: |
        Este exemplo demonstra a extração de códigos de barras de um documento PDF usando configurações personalizadas.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Inicialize o parser com o documento PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // Garanta que o documento suporte leitura de código de barras
            if (!parser.getFeatures().isBarcodes())
            {
                return;
            }

            // Aplique filtragem com opções de código de barras
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Extraia códigos de barras usando o parser
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes(options);

            // Lide com cada resultado de código de barras
            for (PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + String.valueOf(barcode.getPage().getIndex()));
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "Pronto para começar?"
  description: "Experimente os recursos do GroupDocs.Parser gratuitamente ou solicite uma licença"
  items:
    #  loop
    - title: "Download do Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Licenciamento"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Formatos de arquivo suportados para leitura de códigos de barras"
    exclude: "XLSX"
    description: "GroupDocs.Parser pode ler códigos de barras de muitos tipos de documentos e imagens. Abaixo estão alguns dos formatos comumente suportados."
    items: 
        # format loop 1
        - name: "Analisar PDF"
          format: "PDF"
          link: "/parser/java/extract-barcode/pdf/"
          description: "(Formato de Documento Portátil)"
          
        # format loop 2
        - name: "Analisar DOCX"
          format: "DOCX"
          link: "/parser/java/extract-barcode/docx/"
          description: "(Documento do Word Office 2007+)"
          
        # format loop 3
        - name: "Analisar PPTX"
          format: "PPTX"
          link: "/parser/java/extract-barcode/pptx/"
          description: "(Formato de Apresentação Open XML)"
          
        # format loop 4
        - name: "Analisar XLSX"
          format: "XLSX"
          link: "/parser/java/extract-barcode/xlsx/"
          description: "(Caderno de Trabalho Open XML)"
          
        # format loop 5
        - name: "Analisar ODT"
          format: "ODT"
          link: "/parser/java/extract-barcode/odt/"
          description: "(Documento de texto OpenDocument)"
          
        # format loop 6
        - name: "Analisar ODS"
          format: "ODS"
          link: "/parser/java/extract-barcode/ods/"
          description: "(Planilha OpenDocument)"
          
        # format loop 7
        - name: "Analisar ODP"
          format: "ODP"
          link: "/parser/java/extract-barcode/odp/"
          description: "(Apresentação OpenDocument)"
          
        # format loop 8
        - name: "Analisar EPUB"
          format: "EPUB"
          link: "/parser/java/extract-barcode/epub/"
          description: "(Arquivo de eBook Open)"
          
        # format loop 9
        - name: "Analisar FB2"
          format: "FB2"
          link: "/parser/java/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---