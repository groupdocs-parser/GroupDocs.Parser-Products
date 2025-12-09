---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: fr

############################# Head ############################
head_title: "SDK d'analyseur de documents pour PDF, Word et Excel | GroupDocs"
head_description: "SDK d'analyseur de documents pour extraire du texte, des images, des métadonnées, des codes-barres et des tableaux à partir de PDF, Word, Excel, e‑mails et plus de 50 autres formats de documents pour les applications .NET, Java et Python."

############################# Header ############################
title: "SDK d'analyseur de documents"
description:  |
  SDK d'analyseur de documents convivial pour les développeurs, permettant d'extraire du texte, des images, des codes‑barres, des métadonnées et des tableaux à partir de plus de 50 formats de documents et d'images.

  Intégrez une analyse de documents haute performance dans vos applications .NET, Java et Python avec un effort de codage minimal.

  Utilisez des modèles flexibles et des API avancées pour personnaliser les règles d'analyse et fournir des sorties de données propres et structurées.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Choisissez votre plateforme"
  title: "Indépendance de plateforme"
  description: "La bibliothèque GroupDocs.Parser prend en charge les systèmes d'exploitation et les cadres suivants :"
  details_link_title: "En savoir plus"

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
  title: "GroupDocs.Parser en un coup d'œil"
  description: "SDK d'analyseur de documents puissant pour extraire des données structurées et non structurées à partir de PDF, de documents Office, d'images, d'e‑mails et d'archives."

  items:
    # items loop
    - icon: "text"
      title: "Extraire du texte"
      content: "Extraire les informations textuelles de divers formats de fichiers"

    # items loop
    - icon: "image"
      title: "Extraire des images"
      content: "Récupérer le contenu visuel à partir de sources diverses"

    # items loop
    - icon: "template"
      title: "Analyser les données à l'aide de modèles"
      content: "Créer des modèles personnalisés et les utiliser pour analyser des informations spécifiques"

    # items loop
    - icon: "pdf"
      title: "Analyser les formulaires PDF"
      content: "Les formulaires PDF sont des documents numériques contenant des champs remplissables pour l'interaction utilisateur"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser exemples de code"
  description: "Quelques cas d'utilisation typiques des opérations GroupDocs.Parser en C#, Java et Python"

  items:
    # items loop
    - title: "Comment extraire du texte à partir de documents PDF"
      content: "L'API GroupDocs.Parser facilite l'extraction de texte à partir de documents en suivant quelques étapes."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // Créez une instance de la classe Parser en transmettant le fichier souhaité
                using (var parser = new Parser("source.pdf"))
                {
                    // Extrayez le texte
                    using (var textReader = parser.GetText())
                    {
                        // Traitez le texte extrait
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // Créez une instance de la classe Parser en transmettant le fichier souhaité
                try (Parser parser = new Parser("source.pdf"))
                {
                    // Extrayez le texte
                    try (TextReader reader = parser.getText())
                    {
                        // Traitez le texte extrait
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

                # Créez une instance de la classe Parser en transmettant le fichier souhaité
                with Parser("source.pdf") as parser:
                    # Extrayez le texte
                    text = parser.get_text()

                    # Traitez le texte extrait
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "Plus de 50 formats de documents et d'images pris en charge"
  description: "Le SDK d'analyseur de documents GroupDocs.Parser permet des opérations d'analyse sur les documents Office, les PDF, les images, les e‑mails, les archives et bien plus."

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser réalisations"
  description: "Découvrez les indicateurs clés des réalisations de notre bibliothèque"

  items:
    # items loop
    - number: "50+"
      title: "Formats pris en charge"
      content: "GroupDocs.Parser prend en charge les opérations avec plus de 50 formats de fichiers populaires."

    # items loop
    - number: "1600k"
      title: "Téléchargements NuGet"
      content: "Le package NuGet GroupDocs.Parser pour .NET a été téléchargé plus de 1 600 000 fois."

    # items loop
    - number: "18k"
      title: "Téléchargements Maven"
      content: "GroupDocs.Parser compte 18 000 téléchargements sur Maven. Fonctionnalités puissantes d'analyse Java."

    # items loop
    - number: "140+"
      title: "Clients satisfaits"
      content: "Des entreprises renommées ainsi que des développeurs individuels préfèrent les produits GroupDocs pour créer des solutions innovantes."


############################# Customers ###############################
customers:
  enable: true
  title: "Nos clients satisfaits"
  description: "Les bibliothèques GroupDocs sont utilisées par des marques mondialement reconnues et distinguées à travers le monde."

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
  title: "Prêt à commencer ?"
  description: "Essayez les fonctionnalités de GroupDocs.Parser gratuitement sur votre plateforme"

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
  title: "Questions fréquentes"
  description: "Réponses aux questions les plus fréquemment posées."

  items:
    # items loop
    - question: "La bibliothèque GroupDocs.Parser nécessite-t-elle un autre logiciel tiers pour manipuler les documents ?"
      answer: "GroupDocs.Parser ne nécessite aucun logiciel externe à installer, tel qu'Adobe Acrobat, Microsoft Office ou tout autre."

    # items loop
    - question: "Puis-je essayer la bibliothèque GroupDocs.Parser avant de l'acheter ?"
      answer: "Oui, vous pouvez essayer GroupDocs.Parser sans acheter de licence. Une fois installé sans licence, la bibliothèque fonctionne en mode d'essai. Dans ce mode, des badges d'essai sont ajoutés au document résultant, qui est limité aux trois premières pages. Si vous souhaitez tester GroupDocs.Parser sans les limitations de la version d'essai, vous pouvez également demander une licence temporaire de 30 jours. Pour plus de détails, [voir](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "Quelles licences proposez‑vous ?"
      answer: "Nous proposons plusieurs types de licence adaptés aux besoins de développeurs ou d'entreprises spécifiques. Les types de licence dépendent du nombre de développeurs, du nombre de sites de développeurs et de la nécessité de fournir notre SDK/API à vos clients finaux. Vous pouvez également choisir des licences à l'usage basées sur la consommation mensuelle du produit. En savoir plus [ici](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser API low‑code de parsing de documents"
  description: "Intégrez les capacités de parsing de documents dans n'importe quelle application en utilisant notre API REST et nos SDK cloud."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Commandes cURL pour l'API Cloud de parsing de documents RESTful afin d'analyser des documents parmi une large gamme de formats de fichiers populaires supportés."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extrayez des images, du texte, des informations de document ou même analysez tout document à l'aide d'un modèle défini par l'utilisateur dans vos applications Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK cloud pour les développeurs Java afin d'analyser des documents, d'extraire les informations et les données du document dans les applications basées sur Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser applications de parsing de documents sans code"
  description: "Applications web de parsing de documents qui vous permettent d'extraire des données de plus de 50 formats de fichiers populaires directement dans votre navigateur."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Application en ligne gratuite pour analyser Word, Excel, PowerPoint, PDF et plus de 50 autres types de documents."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Analysez les documents Word directement depuis votre navigateur web pour extraire des images, du texte ou des métadonnées."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Application gratuite de parsing PDF fonctionnant sur n'importe quelle plateforme ou dispositif, sans aucune limitation."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---