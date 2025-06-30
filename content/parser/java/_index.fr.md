---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
draft: false

lang: fr
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
head_title: "Applications d'analyse de documents GroupDocs.Parser for Java"
head_description: "Obtenez une solution d'analyse de documents tout-en-un pour les applications Java. Extrayez des données à partir de formats de documents en ligne à l'aide d'une fonctionnalité simple de glisser-déposer."

############################# Header ############################
title: "Analysez des documents via l'API Java"
description: "Extrayez des données à partir de documents et d'images sur n'importe quelle plateforme à l'aide de nos APIs flexibles et de solutions basées sur des applications pour les programmeurs et les utilisateurs finaux."
words:
  for: "pour"

actions:
  main: "Télécharger Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licences"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Prêt à commencer ?"
  description: "Essayez les fonctionnalités de GroupDocs.Parser gratuitement ou demandez une licence"

release:
  title: "Version {0} publiée"
  notes: "Voir les nouveautés"
  downloads: "Téléchargements"

code:
  title: "Accédez rapidement au contenu des documents"
  more: "Plus d'exemples"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Passez le fichier source à l'instance Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Passez le texte du document à TextReader
        try (TextReader reader = parser.getText())
        {
            // Traitez le texte du document
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser en un coup d'œil"
  description: "API pour effectuer l'analyse de documents dans les applications Java"
  features:
    # feature loop
    - title: "Extraire des données à partir de documents"
      content: "L'API GroupDocs.Parser for Java vous permet de récupérer du texte, des métadonnées et des images à partir d'une large gamme de formats de fichiers tels que les documents Office, les e-mails, les pièces jointes et les archives. Cet outil puissant vous aide à accéder et à traiter efficacement des informations précieuses contenues dans ces fichiers pour diverses applications comme l'analyse de données, l'indexation par les moteurs de recherche ou les systèmes de gestion de contenu."

    # feature loop
    - title: "Analyser des documents"
      content: "Extraire divers éléments tels que des hyperliens, des tableaux, des QR codes, des codes-barres et des données à partir de formulaires PDF. Analysez également toute information souhaitée à partir des documents en utilisant des modèles personnalisés."

    # feature loop
    - title: "Personnalisation des résultats"
      content: "L'API Java vous permet de récupérer des données dans divers formats tels que brut, structuré, HTML ou Markdown. De plus, l'API offre une fonctionnalité de recherche pour localiser des mots ou des phrases spécifiques dans le texte des documents."

############################# Platforms ############################
platforms:
  enable: true
  title: "Indépendance de la plateforme"
  description: "GroupDocs.Parser for Java prend en charge les systèmes d'exploitation, les frameworks et les gestionnaires de paquets suivants"
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
        ### Formats Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Images et autres formats
        * **Portable:** PDF 
        * **Images:** JPG, BMP, PNG, TIFF, GIF
        * **Autres formats de bureau:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Autres formats
        * **Web:** HTML, MHTML 
        * **Archives:** ZIP, TAR, 7Z 
        * **e-Books:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "Fonctionnalités de GroupDocs.Parser for Java"
  description: "Extraire des données des PDF, des documents Office et des images rapidement et précisément"

  items:
    # feature loop
    - icon: "text"
      title: "Extraire du texte"
      content: "Extraire des informations textuelles à partir de divers formats de fichiers tels que les documents de bureau, les fichiers PDF et les images pour une lisibilité et une analyse conviviales."

    # feature loop
    - icon: "image"
      title: "Extraire des images"
      content: "Récupérer du contenu visuel à partir de sources diverses comme les documents de bureau et les fichiers PDF pour un accès et une utilisation pratiques."

    # feature loop
    - icon: "qr"
      title: "Scanner des QR Codes"
      content: "Détecter et décoder les QR codes présents dans les documents de bureau, les fichiers PDF ou le contenu visuel pour une récupération efficace des informations."

    # feature loop
    - icon: "email"
      title: "Extraire des données à partir des pièces jointes d'emails et des archives"
      content: "Rassembler des informations précieuses à partir des messages électroniques, des pièces jointes et des sources de données compressées pour une analyse et une utilisation efficaces."

    # feature loop
    - icon: "table"
      title: "Extraire des tableaux"
      content: "Identifier et extraire des données tabulaires à partir de documents PDF pour une analyse et une utilisation organisées."

    # feature loop
    - icon: "hyperlink"
      title: "Extraire des hyperliens"
      content: "Localiser et extraire des hyperliens et des adresses électroniques dans les documents de bureau ou les fichiers PDF pour un accès efficace."

    # feature loop
    - icon: "pdf"
      title: "Analyser des formulaires PDF"
      content: "Les formulaires PDF sont des documents numériques comportant des champs remplissables permettant aux utilisateurs d'entrer des informations électroniquement. L'API .NET peut être utilisée pour extraire des données de ces formulaires pour un traitement efficace."

    # feature loop
    - icon: "template"
      title: "Analyser des données par modèles"
      content: "Créez des modèles personnalisés et utilisez-les avec l'API .NET pour analyser des informations spécifiques à partir de fichiers PDF, simplifiant ainsi les processus d'extraction de données."

    # feature loop
    - icon: "search"
      title: "Rechercher du texte dans des documents"
      content: "Localiser rapidement des mots ou des motifs spécifiques dans des documents."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Exemples de code"
  description: "Quelques cas d'utilisation des opérations typiques GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Extraire des images à partir de documents PDF"
      content: |
        GroupDocs.Parser for Java permet aux développeurs Java d'extraire des images à partir de [documents](https://docs.groupdocs.com/parser/java/extract-images-from-documents/) :
        {{< landing/code title="Extraire des images à partir de documents PDF en Java">}}
        ```java {style=abap}
        // Créez une instance de la classe Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Extraire des images
            Iterable<PageImageArea> images = parser.getImages();

            // Vérifiez si quelque chose a été extrait
            if (images == null) {
                return;
            }

            // Parcourez les images
            for (PageImageArea image : images) {
                // Imprimez l'index de la page, le rectangle et le type d'image
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraire des codes-barres à partir d'images"
      content: |
        Utilisez notre API Java pour extraire des [codes-barres](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) à partir d'images :
        {{< landing/code title="Extraire des codes-barres à partir d'images en Java">}}
        ```java {style=abap}   
        // Chargez l'image source dans Parser
        try (Parser parser = new Parser("source.jpg")){

            // Vérifiez si le fichier prend en charge l'extraction de codes-barres
            if (!parser.getFeatures().isBarcodes()) {

                // Extraire des codes-barres du fichier
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Parcourez les codes-barres
                for (PageBarcodeArea barcode : barcodes) {
                    // Imprimez l'index de la page
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Imprimez la valeur du code-barres
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
