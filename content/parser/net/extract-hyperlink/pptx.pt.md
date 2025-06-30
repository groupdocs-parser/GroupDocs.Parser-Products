


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: pt
format: Pptx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraia hyperlinks de arquivos PPTX em aplicativos C#"
head_description: "Use GroupDocs.Parser para detectar e extrair hyperlinks de arquivos PPTX em C# sem ferramentas ou softwares adicionais."

############################# Header ############################
title: "Extraia hyperlinks de PPTX usando C#" 
description: "Detecte e extraia URLs e hyperlinks de PDF, Word, Excel e outros tipos de documentos utilizando GroupDocs.Parser em suas aplicações .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Baixar Avaliação Gratuita"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Sobre a API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Saiba mais"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) é uma API versátil de parsing de documentos para desenvolvedores .NET. Ela suporta a extração de hyperlinks, textos, imagens e conteúdo estruturado de vários formatos de arquivo, como PDF, Word, Excel, HTML, entre outros—sem depender de software externo.

############################# Steps ############################
steps:
    enable: true
    title: "Passos para extrair hyperlinks de Pptx em C#"
    content: |
      [GroupDocs.Parser](/parser/net/) permite que desenvolvedores .NET extraiam hyperlinks de arquivos PPTX seguindo estes passos simples:
      
      1. Carregue o arquivo PPTX usando uma instância de Parser.
      2. Verifique se o documento suporta a extração de hyperlinks.
      3. Recupere a lista de hyperlinks do documento.
      4. Percorra os resultados e trabalhe com as URLs extraídas.
   
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
        // Carregue o documento contendo hyperlinks usando a classe Parser
        using (Parser parser = new Parser("input.pptx")) {

            // Verifique se o arquivo suporta a extração de hyperlinks
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("A extração de hyperlinks não está disponível para o arquivo");
                return;
            }

            // Recupere e processe os hyperlinks extraídos
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Capacidades avançadas de parsing de documentos"
  description: "Além da extração de hyperlinks, GroupDocs.Parser permite extrair texto, metadados, imagens e dados estruturados—apoiando poderosos fluxos de trabalho de processamento de dados."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Detecção de hyperlinks e parsing de documentos"
  features:
    # feature loop
    - title: "Detecção de hyperlinks em documentos"
      content: "Extraia rapidamente URLs e anotações de links de documentos como PDFs, arquivos do Word, planilhas e mais."

    # feature loop
    - title: "Suporte a links da web e incorporados"
      content: "Detecte e extraia tanto URLs da web padrão quanto links incorporados de documentos em múltiplos formatos."

    # feature loop
    - title: "Opções de parsing flexíveis"
      content: "Personalize as configurações de extração para escanear seções ou páginas específicas para melhorar performance e precisão."
      
  code_samples:
    # code sample loop
    - title: "Como extrair hyperlinks de um PDF usando opções de link"
      content: |
        Este exemplo de código mostra como extrair todos os hyperlinks de um arquivo PDF usando opções personalizadas.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Inicialize o Parser com o documento PDF
        using (Parser parser = new Parser("input.docx"))
        {
            // Verifique se a extração de hyperlinks é suportada
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // Defina opções de extração de link para restringir resultados
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Extraia os dados dos hyperlinks do documento
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // Gerencie a lista de links extraídos
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    title: "Formatos suportados para extração de hyperlinks"
    exclude: "PPTX"
    description: "GroupDocs.Parser pode extrair hyperlinks de uma ampla variedade de tipos de documentos. Veja abaixo os formatos comumente suportados."
    items: 
        # format loop 1
        - name: "Analisar PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(Formato de Documento Portátil)"
          
        # format loop 2
        - name: "Analisar DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(Documento do Word Office 2007+)"
          
        # format loop 3
        - name: "Analisar PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(Formato de Apresentação Open XML)"
          
        # format loop 4
        - name: "Analisar XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(Caderno de Trabalho Open XML)"
          
        # format loop 5
        - name: "Analisar TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(Arquivo de texto)"
          
        # format loop 6
        - name: "Analisar RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(Formato de Texto Rico)"
          
        # format loop 7
        - name: "Analisar XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(Linguagem de Marcação eXtensível)"
          
        # format loop 8
        - name: "Analisar EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(Arquivo de eBook Open)"
         
          

---