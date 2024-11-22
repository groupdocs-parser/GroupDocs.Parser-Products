---
############################# Static ############################
layout: "family"
date:  2024-02-13T17:01:03
draft: false

product: "Parser"
product_tag: "parser"

lang: fr

############################# Head ############################
head_title: ".NET, Java, API Cloud et applications d'analyse de documents en ligne"
head_description: "Bénéficiez d'une solution d'analyse de documents tout-en-un pour les applications .NET, Java et basées sur le cloud. Extrayez des données à partir de formats de documents en ligne à l'aide d'une simple fonction glisser-déposer"

############################# Header ############################
title: "Solution d'analyse de documents"
description: |
  API robuste pour l'extraction de données à partir de différents formats de fichiers.

  Analysez des documents avec un minimum d'effort de codage.

  Personnalisez les résultats de l'analyse.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Choisissez votre plateforme"
  title: "Indépendance de la plateforme"
  description: "La bibliothèque GroupDocs.Parser prend en charge les systèmes d'exploitation et les frameworks suivants :"
  details_link_title: "Apprendre encore plus"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser pour .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    .NET Framework 4.6.2 or higher
                    .NET Core 2.0 or higher
                    .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    Microsoft Visual Studio
                    JetBrains Rider
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser pour Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    Java 8 or higher
                    Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    IntelliJ IDEA
                    Eclipse
                    NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser en un coup d'œil"
  description: "API pour l'analyse des données sur PDF, Word, Excel et plus encore."

  items:
    # items loop
    - icon: "text"
      title: "Extraire le texte"
      content: "Extrayez des informations textuelles à partir de différents formats de fichiers."

    # items loop
    - icon: "image"
      title: "Extraire des images"
      content: "Récupérez du contenu visuel à partir de diverses sources."

    # items loop
    - icon: "template"
      title: "Analyser les données par modèles"
      content: "Créez des modèles personnalisés et utilisez-les pour analyser des informations spécifiques."

    # items loop
    - icon: "pdf"
      title: "Analyser les formulaires PDF"
      content: "PDF Les formulaires sont des documents numériques comportant des champs à remplir pour l'interaction de l'utilisateur."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser exemples de code"
  description: "Quelques cas d'utilisation d'opérations GroupDocs.Parser typiques en C# et Java."

  items:
    # items loop
    - title: "Comment extraire le texte de PDF documents"
      content: "L'API GroupDocs.Parser permet aux développeurs C# d'extraire facilement du texte à partir de documents en mettant en œuvre quelques étapes simples."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              <pre>
              // Create an instance of Parser class
              using (var parser = new Parser(fileName))
              {
                  // Extract a text into the reader
                  using (var textReader = parser.GetText())
                  {
                      // Print a text from the document
                      Console.WriteLine(textReader?.ReadToEnd());
                  }
              }
              </pre>
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              <pre>
              // Create an instance of Parser class
              try (Parser parser = new Parser(fileName)) {
                  // Extract a text into the reader
                  try (TextReader reader = parser.getText()) {
                      // Print a text from the document
                      System.out.println(reader == null 
                              ? "" 
                              : reader.readToEnd());
                  }
              }
              <pre>

############################# Supported Formats ###############################
formats:
  enable: true
  title: "Plus de 50 formats de fichiers pris en charge"
  description: "GroupDocs.Parser permet les opérations d'analyseur dans différentes familles de formats."

############################# Metrics ###############################
metrics:
  enable: false
  title: "Mesures détaillées et informations statistiques"
  description: "Explorez une analyse approfondie de nos chiffres clés, offrant des mesures complètes et des informations statistiques sur nos réalisations, notre influence et notre expansion."

  items:
    # items loop
    - number: "50+"
      title: "Formats pris en charge"
      content: "L'API prend en charge plus de 50 des formats de fichiers et de documents les plus largement utilisés."

    # items loop
    - number: "700k"
      title: "NuGet téléchargements"
      content: "GroupDocs.Parser for .NET a reçu plus de 800 000 téléchargements via le gestionnaire de packages NuGet."

    # items loop
    - number: "15k"
      title: "Téléchargements Maven"
      content: "GroupDocs.Parser for Java a accumulé plus de 15 000 téléchargements à partir de notre référentiel Maven."


############################# Customers ###############################
customers:
  enable: true
  title: "Nos clients satisfaits"
  description: "Les bibliothèques GroupDocs sont utilisées par des marques de renommée mondiale et distinguées à travers le monde."

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
  title: "Prêt à commencer?"
  description: "Essayez GroupDocs.Parser fonctionnalités gratuitement sur votre plateforme"

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
  title: "Questions fréquemment posées"
  description: "Réponses aux questions les plus fréquemment posées."

  items:
    # items loop
    - question: "La bibliothèque GroupDocs.Parser a-t-elle besoin d'un autre logiciel tiers pour manipuler les documents ?"
      answer: "GroupDocs.Parser ne nécessite l'installation d'aucun logiciel externe tel qu'Adobe Acrobat, Microsoft Office ou tout autre."

    # items loop
    - question: "Puis-je essayer la bibliothèque GroupDocs.Parser avant de l'acheter ?"
      answer: "Oui, vous pouvez essayer GroupDocs.Parser sans acheter de licence. Une fois installée sans licence, la bibliothèque fonctionne en mode d'essai. Dans ce mode, les badges d'essai sont ajoutés au document résultant et celui-ci est coupé aux 3 premières pages. Si vous souhaitez tester GroupDocs.Parser sans les limitations de la version d'essai, vous pouvez également demander une licence temporaire de 30 jours. Pour plus de détails, voir [purchase.groupdocs.com/temporary-license/](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "De quelles licences disposez-vous ?"
      answer: "Nous proposons plusieurs types de licences pour répondre aux besoins de développeurs ou d'entreprises particuliers. Les types de licences dépendent du nombre de développeurs, du nombre d'emplacements de sites de développeurs et de la nécessité ou non de fournir notre SDK/API à vos clients finaux. Vous pouvez également choisir des licences limitées en fonction de l'utilisation mensuelle du produit. Apprenez-en davantage sur [purchase.groupdocs.com/policies/](https://purchase.groupdocs.com/policies/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser API low code"
  description: "Intégrez des fonctionnalités d'analyseur de documents dans n'importe quelle application à l'aide de notre API REST basée sur le cloud."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Commandes cURL pour l'API Cloud d'analyseur de documents complet permettant d'analyser des documents dans une large gamme de formats de fichiers populaires pris en charge."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extrayez des images, du texte, des informations sur les documents ou analysez même n'importe quel document selon un modèle défini par l'utilisateur dans vos applications Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK Cloud permettant aux développeurs Java d'analyser des documents, d'extraire des informations et des données sur les documents dans des applications basées sur Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser Applications NoCode"
  description: "Application Web qui vous permet d'effectuer une analyse de plus de 50 formats de fichiers courants directement dans votre navigateur."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Application en ligne gratuite pour analyser Word, Excel, PowerPoint, PDF et plus de 30 types de documents supplémentaires."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Analysez Word des documents directement depuis votre navigateur Web pour extraire des images, du texte ou des métadonnées."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Application d'analyse PDF gratuite qui fonctionne sur n'importe quelle plate-forme ou appareil sans aucune limitation."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"     


---