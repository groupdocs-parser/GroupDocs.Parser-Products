


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:45
draft: false
lang: pt
format: Txt
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Recupere texto de arquivos TXT em aplicações Java"
head_description: "Utilize GroupDocs.Parser para extrair conteúdo textual não estruturado ou estruturado de documentos TXT em Java, sem depender de bibliotecas externas."

############################# Header ############################
title: "Recupere texto de TXT usando Java" 
description: "Extraia texto legível ou estruturado de arquivos como PDF, Word, Excel e mais usando GroupDocs.Parser em seus projetos de desenvolvimento Java."
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
    title: "Apresentando a API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "Saiba mais"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) é um parser de documentos robusto e escalável projetado para desenvolvedores Java. Ele oferece recursos para extrair com precisão texto, tabelas, imagens e componentes estruturados de vários formatos, incluindo PDF, DOCX, XLSX, PPTX e outros—sem depender de utilitários externos.

############################# Steps ############################
steps:
    enable: true
    title: "Como recuperar texto de Txt usando Java"
    content: |
      Siga os passos abaixo para extrair texto de arquivos TXT usando [GroupDocs.Parser](/parser/java/) dentro do seu projeto Java:
      
      1. Carregue o documento TXT usando a classe Parser.
      2. Realize a extração de texto do conteúdo do arquivo.
      3. Verifique se o texto foi recuperado com sucesso.
      4. Use os dados textuais em sistemas de pesquisa, análise ou automação.
   
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
        // Inicialize Parser com seu documento
        try (Parser parser = new Parser("input.txt"))
        {
            // Leia e extraia todos os dados textuais
            try (TextReader reader = parser.getText())
            {
                // Retorne nulo se o conteúdo textual estiver ausente
                // Integre o texto extraído ao seu fluxo de trabalho
                System.out.println(reader == null ? 
                    "Ignore formatos de extração de texto não suportados" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Funcionalidade avançada de extração de texto"
  description: "GroupDocs.Parser vai além da extração simples de texto—suportando a recuperação de imagens, metadados e dados estruturados para aprimorar tarefas de processamento de conteúdo."
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "Extraia e estruture o conteúdo textual de documentos"
  features:
    # feature loop
    - title: "Funciona em numerosos formatos de documentos"
      content: "Capture tanto texto bruto quanto estruturado de DOCX, XLSX, PPTX, PDF, HTML e vários outros formatos."

    # feature loop
    - title: "Extraia texto de conteúdo visual e textual"
      content: "Analise texto de documentos digitalizados, slides, planilhas e outros tipos de arquivos enquanto preserva a estrutura lógica."

    # feature loop
    - title: "Controle detalhado sobre o processo de extração"
      content: "Configurar faixas de páginas, zonas de layout e parâmetros de precisão para uma análise de texto refinada."
      
  code_samples:
    # code sample loop
    - title: "Exemplo: Extraindo regiões de texto de um documento PPTX"
      content: |
        Este exemplo demonstra a extração de blocos de texto junto com suas coordenadas espaciais de uma apresentação PowerPoint usando GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Carregue seu arquivo PPTX com a API Parser
        try (Parser parser = new Parser("input.pptx"))
        {
            // Obtenha todas as zonas de texto retangulares
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // Saia se este recurso não for suportado
            if (areas == null)
            {
                return;
            }

            // Itere pelas áreas de texto por página
            for (PageTextArea a : areas)
            {
                // Processar cada bloco de texto com seu número de página e retângulo delimitador
                System.out.println(String.format("Page: %d, R: %s, Text: %s", a.getPage().getIndex(), a.getRectangle(), a.getText()));
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
    title: "Tipos de arquivos suportados para extração de texto"
    exclude: "TXT"
    description: "GroupDocs.Parser é capaz de extrair conteúdo textual de numerosos formatos de arquivos e imagens. Abaixo estão os tipos mais comumente usados que ele suporta."
    items: 
        # format loop 1
        - name: "Analisar PDF"
          format: "PDF"
          link: "/parser/java/extract-text/pdf/"
          description: "(Formato de Documento Portátil)"
          
        # format loop 2
        - name: "Analisar DOCX"
          format: "DOCX"
          link: "/parser/java/extract-text/docx/"
          description: "(Documento do Word Office 2007+)"
          
        # format loop 3
        - name: "Analisar PPTX"
          format: "PPTX"
          link: "/parser/java/extract-text/pptx/"
          description: "(Formato de Apresentação Open XML)"
          
        # format loop 4
        - name: "Analisar XLSX"
          format: "XLSX"
          link: "/parser/java/extract-text/xlsx/"
          description: "(Caderno de Trabalho Open XML)"
          
        # format loop 5
        - name: "Analisar TXT"
          format: "TXT"
          link: "/parser/java/extract-text/txt/"
          description: "(Arquivo de texto)"
          
        # format loop 6
        - name: "Analisar RTF"
          format: "RTF"
          link: "/parser/java/extract-text/rtf/"
          description: "(Formato de Texto Rico)"
          
        # format loop 7
        - name: "Analisar XML"
          format: "XML"
          link: "/parser/java/extract-text/xml/"
          description: "(Linguagem de Marcação eXtensível)"
          
        # format loop 8
        - name: "Analisar EPUB"
          format: "EPUB"
          link: "/parser/java/extract-text/epub/"
          description: "(Arquivo de eBook Open)"
         
          

---