---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: pt
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

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
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK para Python"
head_description: "SDK de Document Parser de alto desempenho para Python. Extraia texto, imagens, metadados, códigos de barras, tabelas e outros dados de PDF, Word, Excel, emails e mais de 50 formatos de documento."

############################# Header ############################
title: "Document Parser SDK para Python"
description: "Adicione análise de documentos rápida e precisa aos seus aplicativos Python e extraia texto, imagens, metadados e dados estruturados de documentos e imagens."
words:
  for: "para"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI Baixar"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Licenciamento"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "Pronto para começar?"
  description: "Experimente os recursos do GroupDocs.Parser gratuitamente ou solicite uma licença"

release:
  enable: false
  title: "Versão {0} lançada"
  notes: "Veja o que há de novo"
  downloads: "Downloads"

code:
  title: "Extrair texto usando Python"
  more: "Mais exemplos"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Carregar o documento
    with Parser("sample.pdf") as parser:
        # Extrair texto do documento
        text = parser.GetText()

        # Imprimir todo o texto extraído
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "Visão geral de GroupDocs.Parser"
  description: "Document Parser SDK para realizar análise de documentos de alta precisão em aplicações Python"
  features:
    # feature loop
    - title: "Extrair dados de documentos"
      content: "GroupDocs.Parser for Python via .NET API permite recuperar texto, metadados e imagens de uma ampla variedade de formatos de arquivo, como documentos do Office, e‑mails, anexos e arquivos. Esta ferramenta poderosa ajuda a acessar e processar de forma eficiente informações valiosas contidas nesses arquivos para diversas aplicações, como análise de dados, indexação de mecanismos de busca ou sistemas de gerenciamento de conteúdo."

    # feature loop
    - title: "Analisar documentos"
      content: "Extrair vários elementos, como hyperlinks, tabelas, códigos QR, códigos de barras e dados de formulários PDF. Também analisar qualquer informação desejada dos documentos usando modelos personalizados."

    # feature loop
    - title: "Personalizar resultados"
      content: "Python API permite recuperar dados em vários formatos como bruto, estruturado, HTML ou Markdown. Além disso, a API oferece funcionalidade de pesquisa para localizar palavras ou frases específicas dentro do texto dos documentos."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independência de Plataforma"
  description: "GroupDocs.Parser for Python via .NET suporta os seguintes sistemas operacionais, frameworks e gerenciadores de pacotes"
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
    GroupDocs.Parser for Python via .NET oferece suporte a operações com os seguintes [formatos de arquivo](https://docs.groupdocs.com/parser/python-net/supported-document-formats/).
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
  title: "Recursos do GroupDocs.Parser for Python via .NET"
  description: "Extraia dados de PDFs, documentos do Office, imagens e outros formatos de forma rápida e precisa com o nosso Python Document Parser SDK"

  items:
    # feature loop
    - icon: "text"
      title: "Extrair texto"
      content: "Extrair informações textuais de vários formatos de arquivo, como documentos do Office, arquivos PDF e imagens, para fácil leitura e análise."

    # feature loop
    - icon: "image"
      title: "Extrair imagens"
      content: "Recuperar conteúdo visual de diversas fontes, como documentos do Office e arquivos PDF, para acesso e uso convenientes."

    # feature loop
    - icon: "qr"
      title: "Escanear códigos QR"
      content: "Detectar e decodificar códigos QR presentes em documentos do Office, arquivos PDF ou conteúdo visual para recuperação eficiente de informações."

    # feature loop
    - icon: "email"
      title: "Extrair dados de anexos de e‑mail e arquivos compactados"
      content: "Coletar informações valiosas de mensagens de e‑mail, anexos de arquivos e fontes de dados compactados para análise e utilização eficazes."

    # feature loop
    - icon: "table"
      title: "Extrair tabelas"
      content: "Identificar e extrair dados tabulares de documentos PDF para análise e uso organizados."

    # feature loop
    - icon: "hyperlink"
      title: "Extrair hyperlinks"
      content: "Localize e extraia hiperlinks e endereços de e‑mail em documentos do Office ou arquivos PDF para acesso eficiente."

    # feature loop
    - icon: "pdf"
      title: "Analisar formulários PDF"
      content: "Formulários PDF são documentos digitais com campos editáveis para interação do usuário, permitindo que ele insira informações eletronicamente. A API Python pode ser utilizada para extrair dados desses formulários para processamento eficiente."

    # feature loop
    - icon: "template"
      title: "Analisar dados por modelos"
      content: "Crie modelos personalizados e utilize-os com a API Python para analisar informações específicas de arquivos PDF, simplificando os processos de extração de dados."

    # feature loop
    - icon: "search"
      title: "Pesquisar texto em documentos"
      content: "Localize rapidamente palavras ou padrões específicos dentro de documentos."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Exemplos de código"
  description: "Além da extração básica de texto, aqui estão os casos de uso mais comuns para extração rápida de texto, imagens e metadados."
  items:
    # code sample loop
    - title: "Pesquisar texto em um documento"
      content: |
        Este exemplo mostra como pesquisar uma frase específica em um documento PDF e imprimir onde ela foi encontrada.
        {{< landing/code title="Pesquisar texto em um documento em Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Carregar o documento
        with Parser("sample.pdf") as parser:
            # Imprimir o índice da página e o retângulo onde a frase foi encontrada
            for area in parser.Search("Total Amount"):
                # Imprimir o índice da página e o retângulo onde a frase foi encontrada
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extrair imagens de um documento"
      content: |
        Este exemplo mostra como extrair imagens de um documento PDF e salvá‑las em um arquivo.
        {{< landing/code title="Extrair imagens de um documento em Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Carregar o documento
        with Parser("sample.docx") as parser:
            # Extrair imagens do documento
            images = parser.GetImages()

            # Salvar as imagens em um arquivo
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extrair metadados de um documento"
      content: |
        Este exemplo mostra como extrair metadados de um documento PDF e imprimi‑los.
        {{< landing/code title="Extrair metadados de um documento em Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Carregar o documento
        with Parser("sample.pdf") as parser:
            # Extrair metadados do documento
            metadata = parser.GetMetadata()

            # Imprimir os metadados
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
