---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:05
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Extrayez les codes-barres de Excel, Word, PDF et d'autres documents via l'API Java"
head_description: "GroupDocs.Parser for Java permet aux développeurs de logiciels d'extraire les codes-barres de PDF, MS Excel, Word, PowerPoint, Outlook, OneNote et d'autres documents dans les applications Java."

############################# Header ############################
title: "Comment extraire les codes-barres de PDF, DOCX, PPTX, EML, MSG, XLSX et EPUB via l'API {ProductName}}"
description: "L'API GroupDocs.Parser for Java permet aux développeurs de logiciels d'extraire les codes-barres de PDF, Word (DOC, DOCX), Excel (XLS, XLSX), PowerPoint( PPT, { 330}), Outlook (EML, MSG) et de nombreux autres documents Zone de page."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Télécharger la version d'essai gratuite"
    link: "https://downloads.groupdocs.com/parser/java"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/java"
              text: "Référence API"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Exemples de codes"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Démos en direct"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Tarification"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Comment extraire les codes-barres de l'API Excel, Word, PDF et d'autres documents Java ?"
    content: |
        L'image des codes-barres se compose d'une série de lignes noires parallèles et d'espaces blancs de largeurs variables qui peuvent être utilisés pour coder des informations dans un motif visuel. Il a été introduit dans les années 1970 et fait maintenant partie intégrante des entreprises commerciales. GroupDocs.Parser for Java est une API puissante qui permet aux programmeurs de logiciels de créer des applications pour analyser différents types de documents et en extraire du texte, des images et des codes-barres. Il a inclus la prise en charge de certains des types de documents les plus courants tels que PDF, les e-mails, les livres électroniques, les formats Microsoft Office : Word (DOC, DOCX), PowerPoint (PPT, {330 }), Excel (XLS, XLSX), e-mails (EML, MSG) et bien d'autres. L'API Java inclut la prise en charge de plusieurs fonctionnalités importantes liées à l'analyse de documents et à l'extraction de données, telles que l'extraction de texte brut, l'extraction de texte structuré, l'extraction de texte au format Markdown, l'extraction de texte d'une page ou d'une zone de page spécifique, l'extraction de code-barres d'un document, l'extraction métadonnées ou images et bien d'autres.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extraire les codes-barres des documents dans Java"
    content_left: |
        [GroupDocs.Parser for Java](/fr/parser/java/) permet aux développeurs Java d'extraire facilement les codes-barres des documents en mettant en œuvre quelques étapes simples.
        
        * Instanciez l'objet [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) pour le document initial ;
        * Vérifiez si le fichier prend en charge l'extraction de code-barres ;
        * Appelez la méthode [getBarcodes](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getBarcodes--) et obtenez la collection de [PageBarcodeArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/pagebarcodearea/) objets ;
        * Parcourez la collection et obtenez une valeur de code-barres.

    title_right: "En savoir plus sur l'extraction de code-barres"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/">Comment extraire les codes-barres d'un document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-barcodes-from-document-page/">Comment extraire les codes-barres de la page du document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-barcodes-from-document-page-area/">Comment extraire les codes-barres de la zone de page du document</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Comment extraire des codes-barres de documents à l'aide de l'exemple de code Java">}}

        ```java    
        // Extrayez les codes-barres des documents à l'aide de l'API GroupDocs.Parser
        // Créer une instance de la classe Parser
        try (Parser parser = new Parser(Constants.SamplePdfWithBarcodes)) {
            // // Vérifiez si le fichier prend en charge l'extraction de code-barres
            if (!parser.getFeatures().isBarcodes()) {
                System.out.println("Le fichier ne prend pas en charge l'extraction de code-barres.");
                return;
            }

            // {steps.code.scan}
            Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

            // Itérer sur les codes-barres
            for (PageBarcodeArea barcode : barcodes) {
                // Imprimer l'index des pages
                System.out.println("Page: " + barcode.getPage().getIndex());
                // Imprimer la valeur du code-barres
                System.out.println("Value: " + barcode.getValue());
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "Configuration requise"
    content_left: |
        GroupDocs.Parser for Java Les API sont prises en charge sur toutes les principales plates-formes et systèmes d'exploitation. Avant d'exécuter le code ci-dessous, assurez-vous que les prérequis suivants sont installés sur votre système.
        
        * Systèmes d'exploitation : Microsoft Windows, Linux, MacOS
        * Environnements de développement : NetBeans, Intellij IDEA, Eclipse, etc.
        * Cadres
        * Téléchargez la dernière version de GroupDocs.Parser for Java depuis [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)

    title_right: "Pourquoi utiliser GroupDocs.Parser for Java"
    content_right: |
        * Prise en charge de l'extraction de texte brut à partir de tous les documents pris en charge    
        * Analyse de documents via des modèles définis par l'utilisateur    
        * Prise en charge complète de l'extraction de texte structuré    
        * Recherche de texte par mot-clé ainsi que par expression régulière    
        * Extraire du texte formaté, des métadonnées, des images, des conteneurs et des pièces jointes    
        * Extraire la table des matières pour certains formats de document pris en charge    
        * Analyser les données de formulaire de PDF documents    
        * Extraire les hyperliens du document    

############################# Demos ############################
demos:
    enable: true
    title: "Démos en direct - Extrayez les codes-barres des documents en ligne"
    content: |
       Extrayez les codes-barres des documents dès maintenant en visitant le site Web [GroupDocs.Parser Live Demos](https://products.groupdocs.app/parser/barcodes/).
       La démo en direct présente les avantages suivants.
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extraire les codes-barres d'autres formats de documents"
    content: |
        API d'analyse de documents et d'extraction de codes-barres Java pour les formats de fichiers et les images. Extrayez les données pour certains des formats de fichiers populaires comme indiqué ci-dessous.

############################# Back to top ###############################
back_to_top:
    enable: true
---