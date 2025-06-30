---
############################# Static ############################
layout: "family"
date:  2025-06-30T10:26:00
draft: false

product: "Parser"
product_tag: "parser"

lang: pt

############################# Head ############################
head_title: "APIs de Documentos para .NET, Java e Cloud"
head_description: "Obtenha uma solução de parsing de documentos tudo-em-um para aplicações .NET, Java e baseadas na nuvem. Extraia dados de formatos de documentos online usando um recurso simples de arrastar e soltar."

############################# Header ############################
title: "Solução de Parsing de Documentos"
description:  |
  API robusta para extração de dados de vários formatos de arquivo.

  Analise documentos com esforço mínimo de codificação.

  Personalize os resultados da análise.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Escolha sua plataforma"
  title: "Independência da Plataforma"
  description: "A biblioteca GroupDocs.Parser suporta os seguintes sistemas operacionais e frameworks:"
  details_link_title: "Saiba mais"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser .NET 
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
      description: GroupDocs.Parser Java
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

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser em resumo"
  description: "API para análise de dados em PDF, Word, Excel e mais"

  items:
    # items loop
    - icon: "text"
      title: "Extrair texto"
      content: "Extraia informações textuais de vários formatos de arquivo."

    # items loop
    - icon: "image"
      title: "Extrair imagens"
      content: "Recuperar conteúdo visual de diversas fontes."

    # items loop
    - icon: "template"
      title: "Analisar dados por modelos"
      content: "Crie modelos personalizados e utilize-os para extrair informações específicas."

    # items loop
    - icon: "pdf"
      title: "Analisar Formulários PDF"
      content: "Formulários PDF são documentos digitais com campos preenchíveis para interação do usuário."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "Exemplos de código GroupDocs.Parser"
  description: "Alguns casos de uso das operações típicas do GroupDocs.Parser em C# e Java"

  items:
    # items loop
    - title: "Como extrair texto de documentos PDF"
      content: "A API GroupDocs.Parser simplifica a extração de texto de documentos através de alguns passos."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
                    <code class="language-csharp" data-lang="csharp">

                        // Crie uma instância da classe Parser, passando o arquivo desejado.
                        using (var parser = new Parser("source.pdf"))
                        {
                            // Extraia um texto.
                            using (var textReader = parser.GetText())
                            {
                                // Processar o texto extraído.
                                Console.WriteLine(textReader?.ReadToEnd());
                            }
                        }     
                        
                    </code>

          # samples loop
          - language: "Java"
            color: "red"
            content: |
                    <code class="language-java" data-lang="java">

                        // Crie uma instância da classe Parser, passando o arquivo desejado.
                        try (Parser parser = new Parser("source.pdf"))
                        {
                            // Extraia um texto.
                            try (TextReader reader = parser.getText())
                            {
                                // Processar o texto extraído.
                                System.out.println(reader == null 
                                        ? "" 
                                        : reader.readToEnd());
                            }
                        }  

                    </code>


############################# Supported Formats ###############################
formats:
  enable: true
  title: "Mais de 50 formatos de arquivo suportados"
  description: "O GroupDocs.Parser permite operações de parsing dentro de várias famílias de formatos."

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser conquistas"
  description: "Descubra as Métricas Chave das Conquistas de Nossa Biblioteca"

  items:
    # items loop
    - number: "50+"
      title: "Formatos suportados"
      content: "O GroupDocs.Parser suporta operações com mais de 50 formatos de arquivo populares."

    # items loop
    - number: "1600k"
      title: "Downloads do NuGet"
      content: "O pacote GroupDocs.Parser para .NET foi baixado mais de 1.600.000 vezes."

    # items loop
    - number: "18k"
      title: "Downloads do Maven"
      content: "O GroupDocs.Parser possui 18.000 downloads no Maven. Recursos Poderosos de Parsing em Java."

    # items loop
    - number: "140+"
      title: "Clientes satisfeitos"
      content: "Empresas renomadas e desenvolvedores individuais preferem os produtos da GroupDocs para construir soluções inovadoras."


############################# Customers ###############################
customers:
  enable: true
  title: "Nossos clientes satisfeitos"
  description: "As bibliotecas GroupDocs são utilizadas por marcas renomadas e respeitadas em todo o mundo."

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
  description: "Experimente os recursos do GroupDocs.Parser gratuitamente em sua plataforma."

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
  description: "Respostas para as perguntas mais comuns."

  items:
    # items loop
    - question: "A biblioteca GroupDocs.Parser precisa de algum outro software de terceiros para manipular documentos?"
      answer: "O GroupDocs.Parser não requer nenhum software externo, como Adobe Acrobat, Microsoft Office ou qualquer outro."

    # items loop
    - question: "Posso experimentar a biblioteca GroupDocs.Parser antes de comprá-la?"
      answer: "Sim, você pode experimentar o GroupDocs.Parser sem comprar uma licença. Uma vez instalado sem uma licença, a biblioteca funciona em modo de teste. Nesse modo, emblemas de teste são adicionados ao documento resultante, e ele é truncado para as primeiras 3 páginas. Se você deseja testar o GroupDocs.Parser sem as limitações da versão de teste, também pode solicitar uma licença temporária de 30 dias. Para mais detalhes, [veja](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "Que licenças vocês têm?"
      answer: "Oferecemos vários tipos de licenças para atender às necessidades de desenvolvedores ou empresas específicas. Os tipos de licenças dependem do número de desenvolvedores, do número de locais de desenvolvedores e se você precisa entregar nosso SDK/API aos seus clientes finais. Alternativamente, você pode escolher licenças Metered com base no uso mensal do produto. Saiba mais [aqui](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "APIs de baixa codificação GroupDocs.Parser"
  description: "Incorpore capacidades de parsing de documentos em qualquer aplicação usando nossa API REST baseada na nuvem."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Comandos cURL para a API Cloud RESTful de parsing de documentos para analisar documentos em uma ampla gama de formatos de arquivo populares suportados."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extraia imagens, texto, informações do documento ou até mesmo analise qualquer documento seguindo um modelo definido pelo usuário em suas aplicações Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK da nuvem para desenvolvedores Java para analisar documentos, extrair informações de documentos e dados dentro de aplicações baseadas em Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "Aplicativos Sem Código GroupDocs.Parser"
  description: "Aplicação web que permite realizar análise em mais de 50 tipos de arquivos populares diretamente no seu navegador."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Aplicativo gratuito online para analisar Word, Excel, PowerPoint, PDF e mais de 50 tipos de documentos."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Analise documentos Word diretamente do seu navegador para extrair imagens, texto ou metadados."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Aplicativo de parsing de PDF gratuito que funciona em qualquer plataforma ou dispositivo sem limitações."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---