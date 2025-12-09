---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: pt
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

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
head_title: "GroupDocs.Parser for .NET Document Parser SDK para .NET"
head_description: "SDK de análise de documentos de alto desempenho para .NET. Extraia texto, imagens, metadados, códigos de barras, tabelas e outros dados de PDF, Word, Excel, e‑mails e mais de 50 formatos de documentos."

############################# Header ############################
title: "Document Parser SDK para .NET"
description: "Adicione análise rápida e precisa de documentos aos seus aplicativos .NET e extraia texto, imagens, metadados e dados estruturados de documentos e imagens."
words:
  for: "para"

actions:
  main: "Nuget Download"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Licenciamento"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Pronto para começar?"
  description: "Experimente os recursos do GroupDocs.Parser gratuitamente ou solicite uma licença"

release:
  title: "Versão {0} lançada"
  notes: "Veja o que há de novo"
  downloads: "Downloads"

code:
  title: "Analise rapidamente o conteúdo de documentos com o SDK"
  more: "Mais exemplos"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Passe o arquivo de origem para a instância Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Passe o texto do documento para TextReader
        using (var textReader = parser.GetText())
        {
            // Processar o texto do documento
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "Visão geral de GroupDocs.Parser"
  description: "Document Parser SDK para realizar análise de documentos de alta precisão em aplicações .NET"
  features:
    # feature loop
    - title: "Extrair dados de documentos"
      content: "GroupDocs.Parser for .NET API permite recuperar texto, metadados e imagens de uma ampla variedade de formatos de arquivo, como documentos do Office, e‑mails, anexos e arquivos. Esta ferramenta poderosa ajuda a acessar e processar de forma eficiente as informações valiosas contidas nesses arquivos para várias aplicações, como análise de dados, indexação de motores de busca ou sistemas de gerenciamento de conteúdo."

    # feature loop
    - title: "Analisar documentos"
      content: "Extraia diversos elementos como hiperlinks, tabelas, códigos QR, códigos de barras e dados de formulários PDF. Também analise qualquer informação desejada de documentos usando modelos personalizados."

    # feature loop
    - title: "Personalizar resultados"
      content: ".NET API permite recuperar dados em vários formatos, como bruto, estruturado, HTML ou Markdown. Além disso, a API oferece funcionalidade de pesquisa para localizar palavras ou frases específicas no texto dos documentos."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independência de Plataforma"
  description: "GroupDocs.Parser for .NET oferece suporte aos seguintes sistemas operacionais, frameworks e gerenciadores de pacotes"
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
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "Formatos de arquivo suportados"
  description: |
    GroupDocs.Parser for .NET oferece suporte a operações com os seguintes [formatos de arquivo](https://docs.groupdocs.com/parser/net/supported-document-formats/).
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
  title: "Recursos do GroupDocs.Parser for .NET"
  description: "Extraia dados de PDFs, documentos do Office, imagens e outros formatos de forma rápida e precisa com o nosso .NET Document Parser SDK"

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
  description: "Alguns casos de uso típicos das operações do GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Extrair imagens de documentos PDF"
      content: |
        GroupDocs.Parser for .NET facilita para desenvolvedores C# a extração de imagens de [documentos](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Extrair imagens de documentos PDF em C#">}}
        ```csharp {style=abap}
        // Crie uma instância da classe Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Extrair imagens
            var images = parser.GetImages();

            // Verifique se algo foi extraído
            if (images == null)
            {
                return;
            }
            // Iterar sobre as imagens
            foreach (PageImageArea image in images)
            {
                // Imprima o índice da página, o retângulo e o tipo de imagem
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extrair códigos de barras de imagens"
      content: |
        Use nossa API .NET para extrair [códigos de barras](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) de imagens:
        {{< landing/code title="Extrair códigos de barras de imagens em C#">}}
        ```csharp {style=abap}   
        // Carregue a imagem fonte no Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Verifique se o arquivo suporta extração de códigos de barras
            if (parser.Features.Barcodes)
            {
                // Extrair códigos de barras do arquivo
                var barcodes = parser.GetBarcodes();

                // Iterar sobre os códigos de barras
                foreach (var barcode in barcodes)
                {
                    // Imprima o índice da página
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Imprima o valor do código de barras
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
