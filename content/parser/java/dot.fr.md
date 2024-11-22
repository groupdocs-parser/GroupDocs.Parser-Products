---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:06
draft: false
otherformats: dotm dotx epub html mht mhtml odp ods odt one otp ott pdf pps ppsx ppt
ext: dot

############################# Head ############################
head_title: "Extraire les hyperliens des documents dans Java"
head_description: "L'API GroupDocs.Parser for Java permet aux développeurs d'extraire des hyperliens à partir de documents, d'une page de documentation ou d'une zone de page spécifique de Excel, PowerPoint, PDF, Outlook et plus."

############################# Header ############################
title: "Java API pour extraire des hyperliens à partir de documents, de pages ou d'une zone de page particulière"
description: "GroupDocs.Parser for Java L'API facilite le travail des développeurs en leur permettant d'extraire des hyperliens à partir de documents, de la page d'un document ou d'une page spécifique Zone de PDF, DOCX, PPTX, EML, MSG, XLS, {322 }, CSV, RTF, EPUB et bien d'autres."
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
    title: "Comment analyser et extraire les hyperliens des documents DOT via l'API Java ?"
    content: |
        Un lien hypertexte est un morceau de texte ou une image ou une icône qui pointe vers un document entier ou vers une partie particulière d'un document. L'utilisation d'hyperliens permet aux utilisateurs de naviguer vers une page Web ou un document. Il est souvent nécessaire d'extraire des hyperliens d'un document et de l'utiliser pour accéder à un document externe ou à une page Web. GroupDocs.Parser for Java est une fascinante API d'extraction de texte de document qui fournit des fonctionnalités complètes pour la mise en œuvre de solutions d'extraction de texte et de métadonnées. Il prend en charge l'extraction de texte et d'hyperliens à partir des formats PDF, e-mails, livres électroniques, Microsoft Office : Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel ( XLS, XLSX), les formats LibreOffice et bien d'autres. Il prend en charge plusieurs fonctionnalités avancées pour l'analyse de documents, l'extraction de texte brut et structuré, la recherche de texte par mots-clés, l'extraction de métadonnées ou d'images, de conteneurs ainsi que de pièces jointes et bien d'autres.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extraire les hyperliens de DOT dans Java"
    content_left: |
        [GroupDocs.Parser for Java](/fr/parser/java/) permet aux développeurs Java d'extraire facilement des liens hypertexte d'un fichier DOT en mettant en œuvre quelques étapes simples.
        
        * Instanciez l'objet [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) pour le document initial ;
        * Vérifiez si le document prend en charge l'extraction de lien hypertexte ;
        * Appelez la méthode [getHyperlinks](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getHyperlinks--) et obtenez la collection de [PageHyperlinkArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/PageHyperlinkArea) objets ;
        * Parcourez la collection et obtenez un texte de lien hypertexte et une URL.

    title_right: "En savoir plus sur l'extraction des hyperliens"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document/">Comment extraire des hyperliens d'un document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page/">Comment extraire les hyperliens de la page du document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page-area/">Comment extraire des hyperliens de la zone de page du document</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Comment extraire des hyperliens du fichier DOT à l'aide de l'exemple de code Java">}}

        ```java    
        // Extraire les hyperliens du fichier DOT à l'aide de l'API GroupDocs.Parser
        // Créer une instance de la classe Parser
        try (Parser parser = new Parser(Constants.HyperlinksPdf)) {
            // Vérifiez si le document prend en charge l'extraction de lien hypertexte
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("Le document ne prend pas en charge l'extraction de liens hypertexte.");
                return;
            }
            // Extraire les hyperliens du document
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();
            // Itérer sur les hyperliens
            for (PageHyperlinkArea h : hyperlinks) {
                // Imprimer le texte du lien hypertexte
                System.out.println(h.getText());
                // Imprimer l'URL du lien hypertexte
                System.out.println(h.getUrl());
                System.out.println();
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
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extraire des liens hypertexte à partir d'autres formats de documents"
    content: |
        Java API d'analyse de documents et d'extraction d'hyperliens pour les formats de fichiers et les images. Extrayez les données pour certains des formats de fichiers populaires comme indiqué ci-dessous.

############################# Back to top ###############################
back_to_top:
    enable: true
---