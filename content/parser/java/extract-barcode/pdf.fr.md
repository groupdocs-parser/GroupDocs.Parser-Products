


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:17
draft: false
lang: fr
format: Pdf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Lire les codes-barres des fichiers PDF dans les applications Java"
head_description: "Avec GroupDocs.Parser, extrayez les données des codes-barres à partir de documents PDF en utilisant Java sans outils externes."

############################# Header ############################
title: "Lire les codes-barres des fichiers PDF avec Java" 
description: "Extrayez le contenu des codes-barres à partir de fichiers PDF, Word, Excel et d'images en utilisant GroupDocs.Parser dans vos applications Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Télécharger la version d'essai gratuite"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Vue d'ensemble de l'API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "En savoir plus"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) offre une solution complète pour l'analyse de documents dans Java. Il permet aux développeurs d'extraire des codes-barres, du texte, des images et des informations structurées à partir de plusieurs formats de fichier tels que PDF, Word, Excel, PowerPoint et d'autres—sans avoir besoin de bibliothèques tierces.

############################# Steps ############################
steps:
    enable: true
    title: "Comment lire des codes-barres à partir de Pdf en Java"
    content: |
      Avec [GroupDocs.Parser](/parser/java/), les développeurs Java peuvent extraire des codes-barres des documents PDF en quelques étapes :
      
      1. Chargez le document PDF à l'aide de Parser.
      2. Vérifiez que le document prend en charge l'extraction de codes-barres.
      3. Utilisez l'API pour récupérer les données des codes-barres.
      4. Parcourez les résultats des codes-barres et appliquez-les selon vos besoins.
   
    code:
      platform: "net"
      copy_title: "Copier"
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
        copy_tip: "Cliquez pour copier"
        copy_done: "copié"
      links:
        #  loop
        - title: "Plus d'exemples"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "Documentation"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // Ouvrez un document contenant des codes-barres à l'aide de Parser
        try (Parser parser = new Parser("input.pdf"))
        {
            // Vérifiez la prise en charge des codes-barres pour le fichier
            if (!parser.getFeatures().isBarcodes())
            {
                System.out.println("Gérez les types de fichiers non pris en charge");
                return;
            }

            // Extrayez et utilisez les données des codes-barres
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
            for(PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + barcode.getPage().getIndex());
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Autres capacités d'analyse"
  description: "GroupDocs.Parser va au-delà de l'extraction de codes-barres—il vous permet également d'extraire du texte brut, des images et des éléments structurés pour soutenir des flux de travail basés sur les données."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Fonctionnalités d'extraction de codes-barres et de données"
  features:
    # feature loop
    - title: "Large prise en charge des formats de codes-barres"
      content: "Détectez les formats de codes-barres standards, y compris QR Code, Code 39, Data Matrix, EAN, Aztec, et d'autres."

    # feature loop
    - title: "Lire des codes-barres à partir de plusieurs sources"
      content: "Extrayez les informations des codes-barres à partir de documents Office, de fichiers PDF et d'images telles que PNG, JPG et BMP."

    # feature loop
    - title: "Configuration de lecture des codes-barres personnalisée"
      content: "Affinez l'extraction des codes-barres avec des options pour cibler des régions spécifiques et des fichiers multi-pages."
      
  code_samples:
    # code sample loop
    - title: "Exemple : extraire des codes-barres d'un PDF avec des options"
      content: |
        Cet exemple démontre l'extraction de codes-barres à partir d'un document PDF en utilisant des paramètres personnalisés.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Initialisez le parser avec un document PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // Assurez-vous que le document prend en charge la lecture des codes-barres
            if (!parser.getFeatures().isBarcodes())
            {
                return;
            }

            // Appliquez un filtre avec des options de codes-barres
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Extrayez les codes-barres à l'aide du parser
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes(options);

            // Gérez chaque résultat de code-barres
            for (PageBarcodeArea barcode : barcodes)
            {
                System.out.println("Page: " + String.valueOf(barcode.getPage().getIndex()));
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "Prêt à commencer ?"
  description: "Essayez les fonctionnalités de GroupDocs.Parser gratuitement ou demandez une licence"
  items:
    #  loop
    - title: "Téléchargement Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "Licences"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Formats de fichiers pris en charge pour la lecture de codes-barres"
    exclude: "PDF"
    description: "GroupDocs.Parser peut lire les codes-barres à partir de nombreux types de documents et d'images. Voici quelques-uns des formats couramment pris en charge."
    items: 
        # format loop 1
        - name: "Analyse PDF"
          format: "PDF"
          link: "/parser/java/extract-barcode/pdf/"
          description: "(Format de document portable)"
          
        # format loop 2
        - name: "Analyse DOCX"
          format: "DOCX"
          link: "/parser/java/extract-barcode/docx/"
          description: "(Document Word 2007+)"
          
        # format loop 3
        - name: "Analyse PPTX"
          format: "PPTX"
          link: "/parser/java/extract-barcode/pptx/"
          description: "(Format de présentation Open XML)"
          
        # format loop 4
        - name: "Analyse XLSX"
          format: "XLSX"
          link: "/parser/java/extract-barcode/xlsx/"
          description: "(Classeur Open XML)"
          
        # format loop 5
        - name: "Analyse ODT"
          format: "ODT"
          link: "/parser/java/extract-barcode/odt/"
          description: "(Document texte OpenDocument)"
          
        # format loop 6
        - name: "Analyse ODS"
          format: "ODS"
          link: "/parser/java/extract-barcode/ods/"
          description: "(Tableur OpenDocument)"
          
        # format loop 7
        - name: "Analyse ODP"
          format: "ODP"
          link: "/parser/java/extract-barcode/odp/"
          description: "(Présentation OpenDocument)"
          
        # format loop 8
        - name: "Analyse EPUB"
          format: "EPUB"
          link: "/parser/java/extract-barcode/epub/"
          description: "(Fichier eBook Open)"
          
        # format loop 9
        - name: "Analyse FB2"
          format: "FB2"
          link: "/parser/java/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---