


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:34
draft: false
lang: pt
format: Fb2
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraia imagens de arquivos FB2 em apps C#"
head_description: "Use GroupDocs.Parser para detectar e extrair imagens de arquivos FB2 em C# sem ferramentas adicionais."

############################# Header ############################
title: "Extraia imagens de FB2 usando C#" 
description: "Localize e extraia imagens incorporadas de PDFs, documentos do Word, planilhas do Excel e outros tipos de arquivo usando GroupDocs.Parser em seus apps .NET."
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
       [GroupDocs.Parser](/parser/net/) é uma biblioteca robusta de análise de documentos para desenvolvedores .NET. Ela permite extrair imagens, texto, hiperlinks e dados estruturados de formatos de arquivo populares como PDF, DOCX, XLSX, PPTX e outros — tudo isso sem a necessidade de aplicativos de terceiros.

############################# Steps ############################
steps:
    enable: true
    title: "Etapas para extrair imagens de Fb2 em C#"
    content: |
      Com [GroupDocs.Parser](/parser/net/), você pode extrair imagens de documentos FB2 em seus projetos .NET em apenas algumas etapas:
      
      1. Inicialize o Parser com o arquivo FB2.
      2. Recupere elementos de imagem do documento.
      3. Use as imagens extraídas conforme necessário em seu fluxo de trabalho.
   
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
        // Abra o documento contendo imagens usando Parser
        using (Parser parser = new Parser("input.fb2")) {

            // Extraia todas as imagens incorporadas do arquivo
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Trate casos em que nenhuma imagem é encontrada
            if (images == null)
            {
                return;
            }

            // Processar ou salvar as imagens recuperadas
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
  title: "Extração abrangente de conteúdo de documentos"
  description: "GroupDocs.Parser oferece mais do que apenas extração de imagens — você também pode extrair texto bruto, hiperlinks, metadados e conteúdo estruturado para cenários avançados de automação."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Fluxo de trabalho de extração de imagens e análise de documentos"
  features:
    # feature loop
    - title: "Extraia imagens de múltiplos formatos"
      content: "Extraia imagens incorporadas de uma variedade de formatos de arquivo, incluindo DOCX, PDF, PPTX, XLSX e arquivos de imagem como PNG, JPG e TIFF."

    # feature loop
    - title: "Preservar a qualidade original da imagem"
      content: "As imagens são extraídas com alta fidelidade, mantendo sua resolução original, formato e perfil de cor."

    # feature loop
    - title: "Opções avançadas de extração"
      content: "Personalize a extração de imagens com filtragem por página, formato ou resolução, e suporte para documentos de várias páginas."
      
  code_samples:
    # code sample loop
    - title: "Como extrair e salvar imagens de um documento PDF"
      content: |
        Este exemplo demonstra como extrair todos os ativos de imagem de um arquivo PDF e salvá-los no sistema de arquivos local.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Carregue o PDF usando a classe Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Extraia imagens incorporadas do arquivo
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Defina o formato de saída e as opções de imagem (por exemplo, PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Grave as imagens extraídas no disco
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
    title: "Formatos suportados para extração de imagens"
    exclude: "FB2"
    description: "GroupDocs.Parser permite uma extração precisa de imagens de uma ampla gama de formatos de documentos e imagens. Verifique a lista abaixo dos tipos comumente suportados."
    items: 
        # format loop 1
        - name: "Analisar PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(Formato de Documento Portátil)"
          
        # format loop 2
        - name: "Analisar DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Documento do Word Office 2007+)"
          
        # format loop 3
        - name: "Analisar PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Formato de Apresentação Open XML)"
          
        # format loop 4
        - name: "Analisar XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Caderno de Trabalho Open XML)"
          
        # format loop 5
        - name: "Analisar ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(Documento de texto OpenDocument)"
          
        # format loop 6
        - name: "Analisar ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(Planilha OpenDocument)"
          
        # format loop 7
        - name: "Analisar ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(Apresentação OpenDocument)"
          
        # format loop 8
        - name: "Analisar EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(Arquivo de eBook Open)"
          
        # format loop 9
        - name: "Analisar FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---