---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:12
draft: false
otherformats: pdf pps ppsx ppt pptx rtf tex vdx vsdm vsdx vssm vssx vstm vstx vsx vtx

############################# Head ############################
head_title: "Extrayez les tables de PDF, DOCX, PPTX, XLSX, EPUB et plus via l'API Java"
head_description: "GroupDocs.Parser Java L'API permet aux programmeurs d'extraire des tables de PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV , ODT, RTF et de nombreux autres types de documents dans les applications Java."

############################# Header ############################
title: "Extraire les tables des documents Excel, Word, PDF et PowerPoint via l'API Java"
description: "GroupDocs.Parser Java L'API permet aux programmeurs d'extraire des tables de PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV , ODT, RTF & EPUB documents ou pages."
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
    title: "Comment extraire des tables de fichiers XLTM via l'API Java ?"
    content: |
        Le tableau est la collection de cellules disposées en lignes et en colonnes. Les tableaux jouent un rôle très important dans le stockage et l'organisation de données détaillées ou compliquées permettant aux utilisateurs de les lire et de les visualiser facilement. Les tableaux peuvent être utilisés de plusieurs manières, telles que la création de listes, la comparaison d'informations, l'alignement de données, le regroupement d'informations, la mise en évidence de tendances ou de modèles dans les données, etc. GroupDocs.Parser for Java est une API useufly qui permet aux programmeurs de logiciels de développer une solution pour extraire des tableaux, du texte et des images à partir de divers types de formats de documents pris en charge, tels que PDF, e-mails, livres électroniques, Word (DOC, { 318}), PowerPoint (PPT, PPTX), Excel (XLS, XLSX), e-mails (EML, MSG) et bien d'autres. L'API Java a inclus plusieurs fonctionnalités importantes pour travailler avec des tableaux, telles que l'extraction de tous les tableaux d'un document, l'extraction d'un tableau d'une page particulière, l'obtention de données de cellule de tableau, l'obtention du nombre total de lignes et de colonnes d'un tableau, la hauteur de ligne, imprimer les données d'une table et peut-être plus.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extraire les tables de XLTM dans Java"
    content_left: |
        [GroupDocs.Parser for Java](/fr/parser/java/) permet aux développeurs Java d'extraire facilement des tables d'un fichier XLTM en mettant en œuvre quelques étapes simples.
        
        * Instanciez l'objet [Parser](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/) pour le document initial ;
        * Vérifiez si le document prend en charge l'extraction de table ;
        * Instanciez [PageTableAreaOptions](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.options/pagetableareaoptions/) et [TemplateTableLayout](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.templates/templatetablelayout/) pour définir la disposition des tableaux
        * Appelez la méthode [getTables](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getTables-com.groupdocs.parser.options.PageTableAreaOptions-) et obtenez la collection de [PageTableArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/pagetablearea/) objets ;

    title_right: "En savoir plus sur l'extraction des tables"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document/">Comment extraire des tableaux d'un document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-tables-from-document-page/">Comment extraire des tableaux d'une page de document</a>
 
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Comment extraire des tables du fichier XLTM à l'aide de l'exemple de code Java">}}

        ```java    
        // Extraire les tables du fichier XLTM à l'aide de l'API GroupDocs.Parser
        // Créer une instance de la classe Parser
        try (Parser parser = new Parser(Constants.SampleInvoicePagesPdf)) {
            // Vérifiez si le document prend en charge l'extraction de table
            if (!parser.getFeatures().isTables()) {
                System.out.println("Le document ne prend pas en charge l'extraction de tableaux.");
                return;
            }
            // Créer la disposition des tableaux
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));
            // Créer les options d'extraction de table
            PageTableAreaOptions options = new PageTableAreaOptions(layout);
            // Extraire les tableaux du document.
            Iterable<PageTableArea> tables = parser.getTables(options);
            // Itérer sur les tables
            for (PageTableArea t : tables) {
                // Itérer sur les lignes
                for (int row = 0; row < t.getRowCount(); row++) {
                    // Itérer sur les colonnes
                    for (int column = 0; column < t.getColumnCount(); column++) {
                        // Obtenir la cellule du tableau
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null) {
                            // Imprimer le texte de la cellule du tableau
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                    System.out.println();
                }
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
    title: "Extraire des tableaux d'autres formats de document"
    content: |
        API d'analyse de documents et d'extraction de tables Java pour les formats de fichiers et les images. Extrayez les données pour certains des formats de fichiers populaires comme indiqué ci-dessous.

############################# Back to top ###############################
back_to_top:
    enable: true
---