---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Java Document Parser SDK para Java"
head_description: "SDK de Analisador de Documentos de alto desempenho para Java. Extraia texto, imagens, metadados, códigos de barras, tabelas e outros dados de PDF, Word, Excel, e‑mails e mais de 50 formatos de documentos."

############################# Header ############################
title: "SDK de Analisador de Documentos para Java"
description: "Adicione análise de documentos rápida e precisa aos seus aplicativos Java e extraia texto, imagens, metadados e dados estruturados de documentos e imagens."
words:
  for: "para"

actions:
  main: "Download Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licenciamento"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Pronto para começar?"
  description: "Experimente os recursos do GroupDocs.Parser gratuitamente ou solicite uma licença"

release:
  title: "Versão {0} lançada"
  notes: "Veja o que há de novo"
  downloads: "Downloads"

code:
  title: "Analise rapidamente o conteúdo de documentos com o SDK"
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
    // Passe o arquivo de origem para a instância Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Passe o texto do documento para TextReader
        try (TextReader reader = parser.getText())
        {
            // Processar o texto do documento
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "Visão geral de GroupDocs.Parser"
  description: "SDK de Analisador de Documentos para realizar análise de documentos de alta precisão em aplicativos Java"
  features:
    # feature loop
    - title: "Extrair dados de documentos"
      content: "GroupDocs.Parser for Java API permite recuperar texto, metadados e imagens de uma ampla variedade de formatos de arquivo, como documentos do Office, e‑mails, anexos e arquivos compactados. Esta ferramenta poderosa ajuda a acessar e processar de forma eficiente as informações valiosas contidas nesses arquivos para diversas aplicações, como análise de dados, indexação de mecanismos de busca ou sistemas de gerenciamento de conteúdo."

    # feature loop
    - title: "Analisar documentos"
      content: "Extraia vários elementos, como hyperlinks, tabelas, códigos QR, códigos de barras e dados de formulários PDF. Também analise quaisquer informações desejadas de documentos usando modelos personalizados."

    # feature loop
    - title: "Personalizando resultados"
      content: "Java API permite recuperar dados em vários formatos, como bruto, estruturado, HTML ou Markdown. Além disso, a API oferece funcionalidade de busca para localizar palavras ou frases específicas no texto dos documentos."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independência de Plataforma"
  description: "GroupDocs.Parser for Java suporta os seguintes sistemas operacionais, frameworks e gerenciadores de pacotes"
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
    GroupDocs.Parser for Java oferece suporte a operações com os seguintes [formatos de arquivo](https://docs.groupdocs.com/parser/java/supported-document-formats/).
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
        * **Outros formatos de Office:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
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
  title: "GroupDocs.Parser for Java recursos"
  description: "Extraia dados de PDFs, documentos do Office, imagens e outros formatos de forma rápida e precisa com o nosso SDK Java Document Parser"

  items:
    # feature loop
    - icon: "text"
      title: "Extrair texto"
      content: "Extraia informações textuais de vários formatos de arquivo, como documentos do Office, arquivos PDF e imagens, para fácil leitura e análise."

    # feature loop
    - icon: "image"
      title: "Extrair imagens"
      content: "Recupere conteúdo visual de diversas fontes, como documentos do Office e arquivos PDF, para acesso e uso conveniente."

    # feature loop
    - icon: "qr"
      title: "Digitalizar códigos QR"
      content: "Detecte e decodifique códigos QR presentes em documentos do Office, arquivos PDF ou conteúdo visual para recuperação eficiente de informações."

    # feature loop
    - icon: "email"
      title: "Extrair dados de anexos de e‑mail e arquivos"
      content: "Coleta informações valiosas de mensagens de email, anexos de arquivos e fontes de dados compactadas para análise e utilização eficazes."

    # feature loop
    - icon: "table"
      title: "Extrair tabelas"
      content: "Identifique e extraia dados tabulares de documentos PDF para análise e uso organizados."

    # feature loop
    - icon: "hyperlink"
      title: "Extrair hiperlinks"
      content: "Localize e extraia hiperlinks e endereços de email em documentos do Office ou arquivos PDF para acesso eficiente."

    # feature loop
    - icon: "pdf"
      title: "Analisar formulários PDF"
      content: "Formulários PDF são documentos digitais com campos preenchíveis para interação do usuário, permitindo que eles insiram informações eletronicamente. A API .NET pode ser utilizada para extrair dados desses formulários para processamento eficiente."

    # feature loop
    - icon: "template"
      title: "Analisar dados com templates"
      content: "Crie templates personalizados e utilize-os com a API .NET para analisar informações específicas de arquivos PDF, simplificando os processos de extração de dados."

    # feature loop
    - icon: "search"
      title: "Pesquisar texto em documentos"
      content: "Localize rapidamente palavras ou padrões específicos em documentos."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Exemplos de código"
  description: "Alguns casos de uso típicos das operações do GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Extrair imagens de documentos PDF"
      content: |
        GroupDocs.Parser for Java facilita para desenvolvedores Java a extração de imagens de [documentos](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Extrair imagens de documentos PDF em Java">}}
        ```java {style=abap}
        // Crie uma instância da classe Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Extrair imagens
            Iterable<PageImageArea> images = parser.getImages();

            // Verifique se algo foi extraído
            if (images == null) {
                return;
            }

            // Iterar sobre as imagens
            for (PageImageArea image : images) {
                // Imprima o índice da página, o retângulo e o tipo de imagem
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
        // Carregue a imagem fonte no Parser
        try (Parser parser = new Parser("source.jpg")){

            // Verifique se o arquivo suporta extração de códigos de barras
            if (!parser.getFeatures().isBarcodes()) {

                // Extrair códigos de barras do arquivo
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Iterar sobre os códigos de barras
                for (PageBarcodeArea barcode : barcodes) {
                    // Imprima o índice da página
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Imprima o valor do código de barras
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
