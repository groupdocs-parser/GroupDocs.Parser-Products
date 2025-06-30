---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: pt
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"

############################# Head ############################
head_title: "Aplicativos de Parsing de Documentos GroupDocs.Parser for Java"
head_description: "Obtenha uma solução de parsing de documentos tudo-em-um para aplicações Java. Extraia dados de formatos de documentos online usando um recurso simples de arrastar e soltar."

############################# Header ############################
title: "Analise documentos através da API Java"
description: "Extraia dados de documentos e imagens em qualquer plataforma usando nossas APIs flexíveis e soluções baseadas em aplicativos para programadores e usuários finais."
words:
  for: "para"

actions:
  main: "Download Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licenciamento"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Pronto para começar?"
  description: "Experimente os recursos do GroupDocs.Parser gratuitamente ou peça uma licença."

release:
  title: "Versão {0} lançada"
  notes: "Veja o que há de novo"
  downloads: "Downloads"

code:
  title: "Recupere rapidamente o Conteúdo do Documento"
  more: "Mais exemplos"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Passe o arquivo fonte para a instância Parser.
    try (Parser parser = new Parser("source.pdf"))
    {
        // Passe o texto do documento para TextReader.
        try (TextReader reader = parser.getText())
        {
            // Processar o texto do documento.
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser em resumo"
  description: "API para realizar parsing de documentos em aplicações Java."
  features:
    # feature loop
    - title: "Extrair dados de documentos"
      content: "A API GroupDocs.Parser for Java permite que você recupere texto, metadados, e imagens de uma ampla gama de formatos de arquivo, como documentos do Office, e-mails, anexos e arquivos compactados. Esta ferramenta poderosa ajuda você a acessar e processar de forma eficiente informações valiosas contidas nesses arquivos para várias aplicações, como análise de dados, indexação de motores de busca ou sistemas de gerenciamento de conteúdo."

    # feature loop
    - title: "Analisar documentos"
      content: "Extraia vários elementos, como hiperlinks, tabelas, QR codes, códigos de barras e dados de formulários PDF. Além disso, analise qualquer informação desejada de documentos usando modelos personalizados."

    # feature loop
    - title: "Personalização de resultados"
      content: "A API Java permite que você recupere dados em vários formatos, como bruto, estruturado, HTML ou Markdown. Além disso, a API oferece uma funcionalidade de pesquisa para localizar palavras ou frases específicas dentro do texto dos documentos."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independência da Plataforma"
  description: "O GroupDocs.Parser for Java suporta os seguintes sistemas operacionais, frameworks e gerenciadores de pacotes."
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
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "Formatos de arquivo suportados"
  description: |
    O GroupDocs.Parser for Java suporta operações com os seguintes [formatos de arquivo](https://docs.groupdocs.com/parser/java/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Formatos Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Imagens e Outros Formatos
        * **Portátil:** PDF 
        * **Imagens:** JPG, BMP, PNG, TIFF, GIF
        * **Outros formatos de escritório:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Outros formatos
        * **Web:** HTML, MHTML 
        * **Arquivos:** ZIP, TAR, 7Z 
        * **e-Books:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "Recursos GroupDocs.Parser for Java"
  description: "Extraia dados de PDFs, Documentos do Office e Imagens de forma rápida e precisa."

  items:
    # feature loop
    - icon: "text"
      title: "Extrair texto"
      content: "Extraia informações textuais de vários formatos de arquivo, como documentos do office, arquivos PDF e imagens para fácil legibilidade e análise."

    # feature loop
    - icon: "image"
      title: "Extrair imagens"
      content: "Recupere conteúdo visual de fontes diversas, como documentos do office e arquivos PDF para acesso e uso convenientes."

    # feature loop
    - icon: "qr"
      title: "Escanear códigos QR"
      content: "Detecte e decodifique códigos QR presentes em documentos do office, arquivos PDF ou conteúdo visual para eficaz recuperação de informações."

    # feature loop
    - icon: "email"
      title: "Extrair dados de anexos de e-mail e arquivos compactados"
      content: "Colete informações valiosas de mensagens de e-mail, anexos de arquivos e fontes de dados compactadas para análise e utilização eficaz."

    # feature loop
    - icon: "table"
      title: "Extrair tabelas"
      content: "Identifique e extraia dados tabulares de documentos PDF para análise e uso organizados."

    # feature loop
    - icon: "hyperlink"
      title: "Extrair hiperlinks"
      content: "Localize e extraia hiperlinks e endereços de e-mail em documentos de escritório ou arquivos PDF para acesso eficiente."

    # feature loop
    - icon: "pdf"
      title: "Analisar Formulários PDF"
      content: "Formulários PDF são documentos digitais com campos preenchíveis para interação do usuário, permitindo que eles insiram informações eletronicamente. A API .NET pode ser utilizada para extrair dados desses formulários para processamento eficiente."

    # feature loop
    - icon: "template"
      title: "Analisar dados por modelos"
      content: "Crie modelos personalizados e utilize-os com a API .NET para analisar informações específicas de arquivos PDF, simplificando os processos de extração de dados."

    # feature loop
    - icon: "search"
      title: "Pesquisar um texto em documentos"
      content: "Localize rapidamente palavras ou padrões específicos dentro de documentos."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Exemplos de código"
  description: "Alguns casos de uso das operações típicas do GroupDocs.Parser for Java."
  items:
    # code sample loop
    - title: "Extrair imagens de documentos PDF"
      content: |
        GroupDocs.Parser for Java facilita para os desenvolvedores Java a extração de imagens de [documentos](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Extrair imagens de documentos PDF em Java">}}
        ```java {style=abap}
        // Crie uma instância da classe Parser.
        try (Parser parser = new Parser("source.pdf"))
        {
            // Extraia imagens.
            Iterable<PageImageArea> images = parser.getImages();

            // Verifique se algo foi extraído.
            if (images == null) {
                return;
            }

            // Itere sobre as imagens.
            for (PageImageArea image : images) {
                // Imprima um índice de página, retângulo e tipo de imagem.
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extrair códigos de barras de imagens"
      content: |
        Use nossa API Java para extrair [códigos de barras](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) de imagens:
        {{< landing/code title="Extrair códigos de barras de imagens em Java">}}
        ```java {style=abap}   
        // Carregue a imagem fonte para Parser.
        try (Parser parser = new Parser("source.jpg")){

            // Verifique se o arquivo suporta extração de códigos de barras.
            if (!parser.getFeatures().isBarcodes()) {

                // Extraia códigos de barras do arquivo.
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Itere sobre os códigos de barras.
                for (PageBarcodeArea barcode : barcodes) {
                    // Imprima o índice da página.
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Imprima o valor do código de barras.
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
