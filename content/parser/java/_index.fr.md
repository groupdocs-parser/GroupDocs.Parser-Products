---
############################# Static ############################
layout: "landing"
date: 2024-02-13T17:01:03
draft: false
#operation: 
#parsertype: 
#fileformat: 
#productName: Java
lang: "fr"
#productCode: java
#otherformats: 
#breadcrumb: Put  parser on  for Java
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: ".NET, Java, API Cloud et applications d'analyse de documents en ligne"
head_description: "Bénéficiez d'une solution d'analyse de documents tout-en-un pour les applications .NET, Java et basées sur le cloud. Extrayez des données à partir de formats de documents en ligne à l'aide d'une simple fonction glisser-déposer"

############################# Header ############################
title: "Analyser des documents<br>via l'API Java"
description: "Extrayez des données de documents et d'images sur n'importe quelle plate-forme à l'aide de nos API flexibles et de nos solutions basées sur des applications pour les programmeurs et les utilisateurs finaux."
words:
  for: "pour"

actions:
  main: "Téléchargement gratuit de Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licence"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java"
  title: "Prêt à commencer?"
  description: "Essayez GroupDocs.Parser fonctionnalités gratuitement ou demandez une licence"

release:
  title: "Version {0} publiée"
  notes: "Regardez ce qu'il y a de nouveau"
  downloads: "Téléchargements"

code:
  title: "Extraire le texte de PDF fichiers dans Java"
  more: "Plus d'exemples"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
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
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser Aperçu"
  description: "API pour effectuer l'analyse de documents dans les applications Java"
  features:
    # feature loop
    - title: "Extraire les données des documents"
      content: "L'API Java vous permet de récupérer du texte, des métadonnées et des images à partir d'un large éventail de formats de fichiers tels que des documents Office, des e-mails, des pièces jointes et des archives. Cet outil puissant vous aide à accéder et à traiter efficacement les informations précieuses contenues dans ces fichiers pour diverses applications telles que l'analyse de données, l'indexation des moteurs de recherche ou les systèmes de gestion de contenu."

    # feature loop
    - title: "Analyser des documents"
      content: "Extrayez divers éléments tels que des hyperliens, des tableaux, des codes QR, des codes-barres et des données à partir de formulaires PDF. Analysez également toutes les informations souhaitées des documents à l’aide de modèles personnalisés."

    # feature loop
    - title: "Personnalisation des résultats"
      content: "L'API Java vous permet de récupérer des données dans différents formats tels que bruts, structurés, HTML ou Markdown. De plus, l'API offre une fonctionnalité de recherche permettant de localiser des mots ou des expressions spécifiques dans le texte des documents."

############################# Platforms ############################
platforms:
  enable: true
  title: "Indépendance de la plateforme"
  description: "GroupDocs.Parser for Java prend en charge les systèmes d'exploitation, les frameworks et les gestionnaires de packages suivants :"
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
  title: "Formats de fichiers pris en charge"
  description: |
    GroupDocs.Parser for Java prend en charge les opérations avec les [formats de fichiers](https://docs.groupdocs.com/parser/java/supported-document-formats/) suivants.
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office formats
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Images et autres formats
        * **Portable:** PDF
        * **Images:** JPG, BMP, PNG, TIFF, GIF, DICOM, WEBP
        * **Autres formats de bureaux:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Autres formats
        * **la toile:** HTML, MHTML
        * **Les archives:** ZIP, TAR, 7Z
        * **Livres électroniques:** CHM, EPUB, FB2, MOBI

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser fonctionnalités"
  description: "Extrayez les données des PDF, des documents Office et des images de manière rapide et précise."

  items:
    # feature loop
    - icon: "text"
      title: "Extraire le texte"
      content: "Extrayez des informations textuelles à partir de divers formats de fichiers tels que des documents bureautiques, des fichiers PDF et des images pour une lisibilité et une analyse faciles."

    # feature loop
    - icon: "image"
      title: "Extraire des images"
      content: "Récupérez du contenu visuel à partir de diverses sources telles que des documents bureautiques et des fichiers PDF pour un accès et une utilisation pratiques."

    # feature loop
    - icon: "qr"
      title: "Scanner les codes QR"
      content: "Détectez et décodez les codes QR présents dans les documents bureautiques, les fichiers PDF ou le contenu visuel pour une récupération efficace des informations."

    # feature loop
    - icon: "email"
      title: "Extraire les données des pièces jointes et des archives des e-mails"
      content: "Rassemblez des informations précieuses à partir de messages électroniques, de pièces jointes et de sources de données compressées pour une analyse et une utilisation efficaces."

    # feature loop
    - icon: "table"
      title: "Extraire des tableaux"
      content: "Identifiez et extrayez les données tabulaires de documents PDF pour une analyse et une utilisation organisées."

    # feature loop
    - icon: "hyperlink"
      title: "Extraire les hyperliens"
      content: "Recherchez et extrayez des hyperliens et des adresses e-mail dans des documents bureautiques ou des fichiers PDF pour un accès efficace."

    # feature loop
    - icon: "pdf"
      title: "Analyser les formulaires PDF"
      content: "PDF Les formulaires sont des documents numériques comportant des champs à remplir pour l'interaction de l'utilisateur, lui permettant de saisir des informations par voie électronique. L'API Java peut être utilisée pour extraire les données de ces formulaires pour un traitement efficace."

    # feature loop
    - icon: "template"
      title: "Analyser les données par modèles"
      content: "Créez des modèles personnalisés et utilisez-les avec l'API Java pour analyser des informations spécifiques à partir de fichiers PDF, simplifiant ainsi les processus d'extraction de données."

    # feature loop
    - icon: "search"
      title: "Rechercher un texte dans des documents"
      content: "Localisez rapidement des mots ou des modèles spécifiques dans les documents."

############################# Code samples ############################
code_samples:
  enable: true
  title: "Exemple de code"
  description: "Quelques cas d'utilisation d'opérations GroupDocs.Parser for Java typiques"
  items:
    # code sample loop
    - title: "Extraire des images de PDF documents"
      content: |
        L'API Java permet aux développeurs Java d'extraire facilement des images de documents en mettant en œuvre quelques étapes simples.
        {{< landing/code title="Extraire des images de PDF documents dans Java">}}
        ```java {style=abap}
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // Extract images
            Iterable<PageImageArea> images = parser.getImages();
            // Check if images extraction is supported
            if (images != null) {
                int imageIndex = 0;
                // Iterate over images
                for (PageImageArea image : images) {
                    // Save the image to the file
                    image.save(String.format("%s%s", imageIndex, image.getFileType().getExtension()));
                }
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraire les codes-barres des images"
      content: |
        L'API Java permet aux développeurs Java d'extraire facilement les codes-barres des documents en mettant en œuvre quelques étapes simples.
        {{< landing/code title="Extraire les codes-barres des images">}}
        ```java {style=abap}   
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // // Check if the file supports barcode extracting
            if (!parser.getFeatures().isBarcodes()) {
                // Extract barcodes from the file.
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
                // Iterate over barcodes
                for (PageBarcodeArea barcode : barcodes) {
                    // Print the page index
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Print the barcode value
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
