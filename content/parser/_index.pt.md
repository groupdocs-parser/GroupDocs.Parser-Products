---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: pt

############################# Head ############################
head_title: "SDKs de Analisador de Documentos para PDF, Word e Excel | GroupDocs"
head_description: "SDK de Analisador de Documentos para extrair texto, imagens, metadados, códigos de barras e tabelas de PDFs, Word, Excel, e‑mails e mais de 50 outros formatos de documentos para aplicativos .NET, Java e Python."

############################# Header ############################
title: "SDK de Analisador de Documentos"
description:  |
  SDK de Analisador de Documentos voltado para desenvolvedores, que extrai texto, imagens, códigos de barras, metadados e tabelas de mais de 50 formatos de documentos e imagens.

  Integre o parsing de documentos de alto desempenho em suas aplicações .NET, Java e Python com esforço mínimo de codificação.

  Use modelos flexíveis e APIs avançadas para personalizar as regras de parsing e gerar saídas de dados claras e estruturadas.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Escolha sua plataforma"
  title: "Independência de Plataforma"
  description: "A biblioteca GroupDocs.Parser oferece suporte aos seguintes sistemas operacionais e frameworks:"
  details_link_title: "Saiba mais"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser for .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    .NET Framework 4.6.2 or higher <br> .NET Core 2.0 or higher <br> .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    Microsoft Visual Studio <br> JetBrains Rider <br> Microsoft Visual Code
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser for Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Java 8 or higher <br> Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    IntelliJ IDEA <br> Eclipse <br> NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats


    # items loop
    - title: "Python"
      description: GroupDocs.Parser for Python
      color: "yellow"
      tag: "python-net"
      link: "/parser/python-net/"
      features_link: "https://docs.groupdocs.com/parser/python-net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Python 3.5+
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> macOS
      
          # features loop
          - rows: "4"
            content: |
                    PyCharm, VS Code, Jupyter Notebook
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats                    

############################# Features ###############################
features:
  enable: true
  title: "Visão geral de GroupDocs.Parser"
  description: "Potente SDK de Analisador de Documentos para extrair dados estruturados e não estruturados de PDFs, documentos do Office, imagens, e‑mails e arquivos compactados."

  items:
    # items loop
    - icon: "text"
      title: "Extrair texto"
      content: "Extrair informações textuais de vários formatos de arquivo"

    # items loop
    - icon: "image"
      title: "Extrair imagens"
      content: "Recuperar conteúdo visual de diversas fontes"

    # items loop
    - icon: "template"
      title: "Analisar dados por meio de modelos"
      content: "Crie modelos personalizados e os utilize para analisar informações específicas"

    # items loop
    - icon: "pdf"
      title: "Analisar Formulários PDF"
      content: "Formulários PDF são documentos digitais que apresentam campos preenchíveis para interação do usuário"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser exemplos de código"
  description: "Alguns casos de uso típicos das operações do GroupDocs.Parser em C#, Java e Python"

  items:
    # items loop
    - title: "Como extrair texto de documentos PDF"
      content: "A API GroupDocs.Parser facilita a extração de texto de documentos ao implementar algumas etapas."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // Crie uma instância da classe Parser passando o arquivo desejado
                using (var parser = new Parser("source.pdf"))
                {
                    // Extraia o texto
                    using (var textReader = parser.GetText())
                    {
                        // Processar o texto extraído
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // Crie uma instância da classe Parser passando o arquivo desejado
                try (Parser parser = new Parser("source.pdf"))
                {
                    // Extraia o texto
                    try (TextReader reader = parser.getText())
                    {
                        // Processar o texto extraído
                        System.out.println(reader == null 
                                ? "" 
                                : reader.readToEnd());
                    }
                }  
              ```
          # samples loop
          - language: "Python"
            color: "green"
            content: |
              ```python {style=abap}
                from groupdocs.parser import Parser

                # Crie uma instância da classe Parser passando o arquivo desejado
                with Parser("source.pdf") as parser:
                    # Extraia o texto
                    text = parser.get_text()

                    # Processar o texto extraído
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "Mais de 50 formatos de documentos e imagens suportados"
  description: "O SDK de Analisador de Documentos GroupDocs.Parser possibilita operações de parsing em documentos do Office, PDFs, imagens, e‑mails, arquivos compactados e muito mais."

############################# Metrics ###############################
metrics:
  enable: true
  title: "Conquistas do GroupDocs.Parser"
  description: "Descubra os principais indicadores das realizações da nossa biblioteca"

  items:
    # items loop
    - number: "50+"
      title: "Formatos suportados"
      content: "GroupDocs.Parser suporta operações com mais de 50 formatos de arquivo populares."

    # items loop
    - number: "1600k"
      title: "Downloads do NuGet"
      content: "GroupDocs.Parser for .NET NuGet package was downloaded more than 1,600,000 times."

    # items loop
    - number: "18k"
      title: "Downloads do Maven"
      content: "GroupDocs.Parser has 18,000 downloads on Maven. Powerful Java Parsing Features."

    # items loop
    - number: "140+"
      title: "Clientes satisfeitos"
      content: "Empresas renomadas e desenvolvedores individuais preferem os produtos da GroupDocs para criar soluções inovadoras."


############################# Customers ###############################
customers:
  enable: true
  title: "Nossos clientes satisfeitos"
  description: "GroupDocs bibliotecas são usadas por marcas mundialmente renomadas e distintas em todo o mundo."

  items:
    # items loop
    - title: "BenQ Corporation"
      logo: "benq"
      
    # items loop
    - title: "Nasdaq Stock Market"
      logo: "nasdaq"
      
    # items loop
    - title: "AT&T Inc."
      logo: "att"
      
    # items loop
    - title: "Customer logo AstraZeneca"
      logo: "astrazeneca"
      
    # items loop
    - title: "Central Bank of Argentina"
      logo: "argentinacentralbank"
      
    # items loop
    - title: "Roche Holding AG"
      logo: "roche"
      
    # items loop
    - title: "Capita"
      logo: "capita"
      
    # items loop
    - title: "Axa S.A."
      logo: "axa"
      
    # items loop
    - title: "Instructure Inc."
      logo: "instructure"
      
    # items loop
    - title: "Wipro"
      logo: "wipro"


############################# Actions ###############################
actions:
  enable: true
  title: "Pronto para começar?"
  description: "Experimente os recursos do GroupDocs.Parser gratuitamente na sua plataforma"

  items:
    # items loop
    - title: ".NET"
      color: "blue"
      link: "/parser/net/"

    # items loop
    - title: "Java"
      color: "red"
      link: "/parser/java/"

############################# FAQ ###############################
faq:
  enable: true
  title: "Perguntas frequentes"
  description: "Respostas às perguntas mais frequentes."

  items:
    # items loop
    - question: "A biblioteca GroupDocs.Parser precisa de algum outro software de terceiros para manipular documentos?"
      answer: "GroupDocs.Parser não requer a instalação de nenhum software externo, como Adobe Acrobat, Microsoft Office ou outro."

    # items loop
    - question: "Posso experimentar a biblioteca GroupDocs.Parser antes de comprá‑la?"
      answer: "Sim, você pode experimentar o GroupDocs.Parser sem comprar uma licença. Quando instalado sem licença, a biblioteca funciona em modo de avaliação. Nesse modo, marcas de avaliação são adicionadas ao documento resultante, e ele é truncado para as primeiras 3 páginas. Se desejar testar o GroupDocs.Parser sem as limitações da versão de avaliação, também pode solicitar uma licença temporária de 30 dias. Para mais detalhes, [veja](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "Quais licenças você tem?"
      answer: "Oferecemos vários tipos de licença para atender às necessidades de desenvolvedores ou empresas específicas. Os tipos de licença dependem do número de desenvolvedores, do número de locais de site de desenvolvedor e se você precisa disponibilizar nosso SDK/API para seus clientes finais. Como alternativa, você pode escolher licenças por consumo (Metered) baseadas no uso mensal do produto. Saiba mais [aqui](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser APIs low‑code de Análise de Documentos"
  description: "Incorpore recursos de análise de documentos em qualquer aplicação usando nossa API REST baseada em nuvem e SDKs."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Comandos cURL para a API Cloud de analisador de documentos RESTful para analisar documentos em uma ampla variedade de formatos de arquivo populares suportados."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extraia imagens, texto, informações do documento ou até mesmo analise qualquer documento por meio de um modelo definido pelo usuário em suas aplicações Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK Cloud para desenvolvedores Java para analisar documentos, extrair informações e dados do documento em aplicações baseadas em Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser Aplicativos No‑Code de Analisador de Documentos"
  description: "Aplicativos web de análise de documentos que permitem extrair dados de mais de 50 formatos de arquivo populares diretamente no seu navegador."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Aplicativo online gratuito para analisar Word, Excel, PowerPoint, PDF e mais de 50 tipos de documentos."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Analise documentos Word diretamente do seu navegador para extrair imagens, texto ou metadados."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Aplicativo gratuito de análise de PDF que funciona em qualquer plataforma ou dispositivo sem limitações."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---