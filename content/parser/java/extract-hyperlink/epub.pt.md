


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: pt
format: Epub
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Extraia hiperlinks de arquivos EPUB em aplicativos Java"
head_description: "Utilize GroupDocs.Parser para encontrar e extrair links URL de documentos EPUB em projetos Java—sem necessidade de software adicional."

############################# Header ############################
title: "Extraia hiperlinks de EPUB com Java" 
description: "Extraia links da web e hiperlinks de PDFs, arquivos Word, planilhas Excel e outros documentos utilizando GroupDocs.Parser em seu ambiente Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Baixar Versão Grátis"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Sobre a API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Saiba mais"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) é uma API robusta de extração de conteúdo projetada para desenvolvedores Java. Oferece ferramentas para extrair hiperlinks, dados estruturados, imagens e texto de formatos populares como DOCX, XLSX, PDF, HTML e mais—tudo sem precisar de plugins externos.

############################# Steps ############################
steps:
    enable: true
    title: "Como extrair hiperlinks de Epub em Java"
    content: |
      [GroupDocs.Parser](/parser/java/) simplifica a extração de hiperlinks de arquivos EPUB em aplicações Java com estes passos básicos:
      
      1. Abra o arquivo EPUB usando uma instância do Parser.
      2. Assegure-se de que a extração de hiperlinks está disponível para o formato do arquivo.
      3. Extraia todos os hiperlinks utilizando o método apropriado.
      4. Percorra os resultados e processe cada link conforme necessário.
   
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
        // Carregue o arquivo que pode conter hiperlinks utilizando o Parser
        try (Parser parser = new Parser("input.epub")) {

            // Verifique se o formato do documento suporta a extração de hiperlinks
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("A extração de hiperlinks não está disponível para o arquivo");
                return;
            }

            // Extraia e utilize os dados de hiperlink do documento
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Ferramentas abrangentes de análise de documentos"
  description: "Além de extrair hiperlinks, GroupDocs.Parser permite coletar outros conteúdos úteis, como texto simples, mídia incorporada e dados estruturados para uso em fluxos de trabalho automatizados."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Extração de hiperlinks e análise de documentos"
  features:
    # feature loop
    - title: "Detecção precisa de links"
      content: "Capture todos os tipos de hiperlinks de diferentes layouts de documentos, incluindo texto clicável e URLs ocultas."

    # feature loop
    - title: "Funciona com documentos e conteúdo da web"
      content: "Extraia links de arquivos PDF, DOCX, XLSX, HTML e imagens que contêm hiperlinks incorporados."

    # feature loop
    - title: "Comportamento de extração personalizada"
      content: "Refine como os hiperlinks são extraídos utilizando opções como intervalos de páginas, tipos de links ou filtros de conteúdo."
      
  code_samples:
    # code sample loop
    - title: "Exemplo: extraindo hiperlinks de um PDF com opções personalizadas"
      content: |
        Este exemplo demonstra como extrair todos os links de um arquivo PDF utilizando configurações de extração de links.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Abra o PDF utilizando a classe Parser
        try (Parser parser = new Parser("input.docx"))
        {
            // Verifique se o suporte a hiperlinks está habilitado para este documento
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // Aplique opções para filtrar links
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Use o parser para obter dados de hiperlink
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // Itere pelos links e manuseie-os conforme necessário
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    title: "Formatos de documentos que suportam extração de hiperlinks"
    exclude: "EPUB"
    description: "Com GroupDocs.Parser, você pode extrair hiperlinks de muitos formatos de arquivo amplamente utilizados. Abaixo está uma lista de formatos normalmente suportados."
    items: 
        # format loop 1
        - name: "Analisar PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(Formato de Documento Portátil)"
          
        # format loop 2
        - name: "Analisar DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Documento do Word Office 2007+)"
          
        # format loop 3
        - name: "Analisar PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Formato de Apresentação Open XML)"
          
        # format loop 4
        - name: "Analisar XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Caderno de Trabalho Open XML)"
          
        # format loop 5
        - name: "Analisar TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(Arquivo de texto)"
          
        # format loop 6
        - name: "Analisar RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(Formato de Texto Rico)"
          
        # format loop 7
        - name: "Analisar XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(Linguagem de Marcação eXtensível)"
          
        # format loop 8
        - name: "Analisar EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(Arquivo de eBook Open)"
         
          

---