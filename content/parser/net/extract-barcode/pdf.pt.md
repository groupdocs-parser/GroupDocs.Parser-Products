


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:20
draft: false
lang: pt
format: Pdf
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraia códigos de barras de arquivos PDF em aplicativos C#"
head_description: "Utilize GroupDocs.Parser para detectar e extrair dados de código de barras de arquivos PDF em C# sem precisar de software adicional."

############################# Header ############################
title: "Extraia códigos de barras de PDF usando C#" 
description: "Detecte e extraia informações de códigos de barras de arquivos PDF, Word, Excel e imagens usando GroupDocs.Parser em suas aplicações .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Baixar Versão de Avaliação Gratuita"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Sobre a API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Saiba mais"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) é uma poderosa API de análise de documentos para desenvolvedores .NET. Ela permite a extração de texto, imagens, conteúdo estruturado e códigos de barras de diversos formatos de arquivo, incluindo PDF, Word, Excel, PowerPoint e mais — tudo sem depender de ferramentas externas.

############################# Steps ############################
steps:
    enable: true
    title: "Passos para extrair códigos de barras de Pdf em C#"
    content: |
      [GroupDocs.Parser](/parser/net/) permite extrair dados de códigos de barras de arquivos PDF em aplicações .NET seguindo estes passos simples:
      
      1. Carregue o arquivo PDF usando uma instância de Parser.
      2. Verifique se o documento suporta a extração de códigos de barras.
      3. Recupere a lista de códigos de barras do documento.
      4. Itere pelos resultados e utilize os valores dos códigos de barras extraídos.
   
    code:
      platform: "net"
      copy_title: "Copiar"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "clique para copiar"
        copy_done: "copiado"
      links:
        #  loop
        - title: "Mais exemplos"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Documentação"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Carregue o documento contendo códigos de barras usando a classe Parser
        using (Parser parser = new Parser("input.pdf")) {

            // Verifique se o arquivo suporta extração de códigos de barras
            if (!parser.Features.Barcodes) {
                Console.WriteLine("A extração de códigos de barras não é suportada");
                return;
            }

            // Recupere e processe os códigos de barras extraídos
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
  title: "Recursos avançados de análise de documentos"
  description: "Além da extração de códigos de barras, GroupDocs.Parser permite extrações de texto simples, imagens e dados estruturados para apoiar automações avançadas e fluxos de trabalho de processamento de dados."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Reconhecimento de códigos de barras e análise de documentos"
  features:
    # feature loop
    - title: "Suporte a múltiplos formatos de códigos de barras"
      content: "Reconheça tipos comuns de códigos de barras, incluindo QR Code, Code 128, Data Matrix, EAN, Aztec e mais."

    # feature loop
    - title: "Extraia códigos de barras de documentos e imagens"
      content: "Leia códigos de barras de documentos PDF, Word, Excel e formatos de imagem como JPEG, PNG e BMP."

    # feature loop
    - title: "Configurações de extração personalizáveis"
      content: "Configure opções de detecção como regiões de escaneamento e processamento de documentos de várias páginas."
      
  code_samples:
    # code sample loop
    - title: "Como extrair códigos de barras de um PDF usando opções de código de barras"
      content: |
        Este exemplo demonstra como extrair códigos de barras de um arquivo PDF utilizando opções específicas de extração de códigos de barras.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Carregue o arquivo PDF com a classe Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Confirme que a extração de códigos de barras é suportada
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // Utilize opções de códigos de barras para filtrar resultados
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Recupere os dados do código de barras do documento
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // Processe a lista de códigos de barras extraídos
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
  title: "Pronto para começar?"
  description: "Experimente os recursos do GroupDocs.Parser gratuitamente ou solicite uma licença"
  items:
    #  loop
    - title: "Download do Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Licenciamento"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Formatos suportados para extração de códigos de barras"
    exclude: "PDF"
    description: "GroupDocs.Parser suporta a detecção de códigos de barras em uma ampla gama de formatos de documentos e imagens. Veja abaixo os tipos de arquivos comumente suportados."
    items: 
        # format loop 1
        - name: "Analisar PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(Formato de Documento Portátil)"
          
        # format loop 2
        - name: "Analisar DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(Documento do Word Office 2007+)"
          
        # format loop 3
        - name: "Analisar PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(Formato de Apresentação Open XML)"
          
        # format loop 4
        - name: "Analisar XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(Caderno de Trabalho Open XML)"
          
        # format loop 5
        - name: "Analisar ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(Documento de texto OpenDocument)"
          
        # format loop 6
        - name: "Analisar ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(Planilha OpenDocument)"
          
        # format loop 7
        - name: "Analisar ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(Apresentação OpenDocument)"
          
        # format loop 8
        - name: "Analisar EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(Arquivo de eBook Open)"
          
        # format loop 9
        - name: "Analisar FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---