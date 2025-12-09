---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
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
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for Java Document Parser SDK pour Java"
head_description: "SDK de parsing de documents haute performance pour Java. Extrayez le texte, les images, les métadonnées, les codes‑barres, les tableaux et d’autres données à partir de PDF, Word, Excel, e‑mails et plus de 50 formats de documents."

############################# Header ############################
title: "Document Parser SDK pour Java"
description: "Ajoutez un parsing de documents rapide et précis à vos applications Java et extrayez le texte, les images, les métadonnées et les données structurées à partir de documents et d’images."
words:
  for: "pour"

actions:
  main: "Télécharger Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Licence"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Prêt à commencer ?"
  description: "Essayez les fonctionnalités de GroupDocs.Parser gratuitement ou demandez une licence"

release:
  title: "Version {0} publiée"
  notes: "Voir les nouveautés"
  downloads: "Téléchargements"

code:
  title: "Analyser rapidement le contenu des documents avec le SDK"
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
    // Passez le fichier source à l’instance Parser
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
  description: "SDK de parsing de documents pour réaliser un parsing haute précision dans les applications Java"
  features:
    # feature loop
    - title: "Extraire des données de documents"
      content: "GroupDocs.Parser for Java API vous permet de récupérer le texte, les métadonnées et les images d’une large gamme de formats de fichiers tels que les documents Office, les e‑mails, les pièces jointes et les archives. Cet outil puissant vous aide à accéder et à traiter efficacement les informations précieuses contenues dans ces fichiers pour diverses applications comme l’analyse de données, l’indexation pour les moteurs de recherche ou les systèmes de gestion de contenu."

    # feature loop
    - title: "Analyser les documents"
      content: "Extraire divers éléments tels que les hyperliens, les tableaux, les codes QR, les codes-barres et les données des formulaires PDF. Analysez également toute information souhaitée à partir de documents en utilisant des modèles personnalisés."

    # feature loop
    - title: "Personnaliser les résultats"
      content: "Java API vous permet de récupérer des données dans divers formats tels que brut, structuré, HTML ou Markdown. De plus, l’API offre une fonction de recherche pour localiser des mots ou des expressions spécifiques dans le texte des documents."

############################# Platforms ############################
platforms:
  enable: true
  title: "Indépendance de plateforme"
  description: "GroupDocs.Parser for Java prend en charge les systèmes d’exploitation, frameworks et gestionnaires de packages suivants"
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
        * **Autres formats Office:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Autres formats
        * **Web:** HTML, MHTML 
        * **Archives:** ZIP, TAR, 7Z 
        * **e-books:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java fonctionnalités"
  description: "Extraire des données des PDF, documents Office, images et autres formats rapidement et avec précision grâce à notre SDK Java Document Parser"

  items:
    # feature loop
    - icon: "text"
      title: "Extraire du texte"
      content: "Extrayez les informations textuelles de divers formats de fichiers tels que les documents Office, les fichiers PDF et les images pour une lecture et une analyse aisées."

    # feature loop
    - icon: "image"
      title: "Extraire des images"
      content: "Récupérez le contenu visuel de diverses sources comme les documents Office ou les fichiers PDF pour un accès et une utilisation pratiques."

    # feature loop
    - icon: "qr"
      title: "Scanner les QR Codes"
      content: "Détectez et décodez les QR codes présents dans les documents Office, les fichiers PDF ou le contenu visuel pour une récupération d'informations efficace."

    # feature loop
    - icon: "email"
      title: "Extraire des données des pièces jointes d'e‑mail et des archives"
      content: "Recueillez des informations précieuses à partir des messages électroniques, des pièces jointes et des sources de données compressées pour une analyse et une utilisation efficaces."

    # feature loop
    - icon: "table"
      title: "Extraire les tableaux"
      content: "Identifiez et extrayez les données tabulaires des documents PDF pour une analyse et une utilisation organisées."

    # feature loop
    - icon: "hyperlink"
      title: "Extraire les hyperliens"
      content: "Localisez et extrayez les hyperliens et les adresses e‑mail dans les documents Office ou les fichiers PDF pour un accès efficace."

    # feature loop
    - icon: "pdf"
      title: "Analyser les formulaires PDF"
      content: "Les formulaires PDF sont des documents numériques contenant des champs remplissables pour l’interaction utilisateur, permettant de saisir des informations électroniquement. L’API .NET peut être utilisée pour extraire les données de ces formulaires afin de les traiter efficacement."

    # feature loop
    - icon: "template"
      title: "Analyser les données à l’aide de modèles"
      content: "Créez des modèles personnalisés et utilisez‑les avec l’API .NET pour analyser des informations spécifiques à partir de fichiers PDF, simplifiant ainsi les processus d’extraction de données."

    # feature loop
    - icon: "search"
      title: "Rechercher du texte dans les documents"
      content: "Localisez rapidement des mots ou des motifs spécifiques dans les documents."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Exemples de code"
  description: "Quelques cas d’utilisation des opérations typiques de GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "Extraire des images de documents PDF"
      content: |
        GroupDocs.Parser for Java facilite aux développeurs Java l’extraction d’images depuis les [documents](https://docs.groupdocs.com/parser/java/extract-images-from-documents/) :
        {{< landing/code title="Extraire des images de documents PDF en Java">}}
        ```java {style=abap}
        // Créez une instance de la classe Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Extrayez les images
            Iterable<PageImageArea> images = parser.getImages();

            // Vérifiez si quelque chose a été extrait
            if (images == null) {
                return;
            }

            // Itérez sur les images
            for (PageImageArea image : images) {
                // Affichez l'index de page, le rectangle et le type d'image
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Extraire les codes-barres des images"
      content: |
        Utilisez notre API Java pour extraire les [codes-barres](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) depuis les images :
        {{< landing/code title="Extraire les codes-barres d'images en Java">}}
        ```java {style=abap}   
        // Chargez l'image source dans Parser
        try (Parser parser = new Parser("source.jpg")){

            // Vérifiez si le fichier prend en charge l'extraction de codes-barres
            if (!parser.getFeatures().isBarcodes()) {

                // Extrayez les codes-barres du fichier
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Itérez sur les codes-barres
                for (PageBarcodeArea barcode : barcodes) {
                    // Affichez l'index de page
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Affichez la valeur du code-barres
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
