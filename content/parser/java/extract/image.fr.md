---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Comment extraire des images de Excel, Word, PDF et d'autres documents via Java ?"
head_description: "L'API GroupDocs.Parser for Java permet aux développeurs de logiciels d'analyser et d'extraire des images de PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX documents et e-mails dans les applications Java."

############################# Header ############################
title: "Java API pour analyser et extraire des images de Excel, Word, PowerPoint, PDF et d'autres pages de documents"
description: "L'API GroupDocs.Parser for Java permet aux programmeurs d'extraire des images de PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV, {358 }, les documents RTF et EPUB ou les pages de document dans les applications Java."
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
    title: "Découvrez comment extraire des images de documents {{EXT}} ou d'une page spécifique via l'API Java"
    content: |
        Une image vaut mille mots et ne peut être ignorée dans le monde visuel d'aujourd'hui tout en créant un contenu attrayant. Les images peuvent être une excellente source de communication d'informations et attirer l'attention de l'utilisateur. Il est souvent nécessaire d'obtenir des images à partir de documents, de revues ou de présentations et de les utiliser ailleurs. GroupDocs.Parser for Java est une API puissante qui aide les développeurs de logiciels et les programmeurs à créer une solution pour analyser et extraire des images ou d'autres informations à partir de nombreux types de documents. Il prend également en charge l'enregistrement d'images dans PNG, JPEG, WebP, GIF, BMP et d'autres formats. L'API a inclus la prise en charge de certains formats de documents populaires, tels que les formats PDF, Microsoft Office : Word (DOC, DOCX), PowerPoint (PPT, PPTX), {282 } (XLS, XLSX), formats LibreOffice, e-mails, livres électroniques et bien d'autres. Il a également inclus la prise en charge de certaines fonctionnalités avancées liées à l'analyse de documents, à l'extraction de texte brut et structuré, à la recherche de texte par mots-clés, à l'extraction de métadonnées ou d'images, de conteneurs ainsi que de pièces jointes et bien d'autres.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extraire des images de documents dans Java"
    content_left: |
        [GroupDocs.Parser for Java](/fr/parser/java/) permet aux développeurs Java d'extraire facilement des images d'un document en mettant en œuvre quelques étapes simples.
        
        * Instanciez l'objet [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) pour le document initial ;
        * Appelez la méthode [getImages](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getImages--) et obtenez la collection d'objets image ;
        * Vérifiez si le lecteur n'est pas *null* (l'extraction d'images est prise en charge pour le document) ;
        * Parcourez la collection et obtenez les tailles, les types d'images et le contenu des images.

    title_right: "En savoir plus sur l'extraction d'images"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document/">Comment extraire des images d'un document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page/">Comment extraire des images d'une page de document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-from-document-page-area/">Comment extraire des images de la zone de page de document</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-images-to-files/">Comment extraire des images dans des fichiers</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Comment extraire des images de documents à l'aide de l'exemple de code Java">}}

        ```java    
        // Extraire des images de documents à l'aide de l'API GroupDocs.Parser
        // Créer une instance de la classe Parser
        try (Parser parser = new Parser(Constants.SampleImagesPdf)) {
            // Extraire des images
            Iterable<PageImageArea> images = parser.getImages();
            // Vérifiez si l'extraction d'images est prise en charge
            if (images == null) {
                System.out.println("L'extraction d'images n'est pas prise en charge");
                return;
            }
            // Itérer sur les images
            for (PageImageArea image : images) {
                // Imprimer un index de page, un rectangle et un type d'image :
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
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
    title: "Démos en direct - Extraire des images de documents en ligne"
    content: |
       Extrayez des images de documents dès maintenant en visitant le site Web [GroupDocs.Parser Live Demos](https://products.groupdocs.app/parser/images/).
       La démo en direct présente les avantages suivants.
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Extraire des images d'autres formats de documents"
    content: |
        Java API d'analyse de documents et d'extraction d'images pour les formats de fichiers et les images. Extrayez les données pour certains des formats de fichiers populaires comme indiqué ci-dessous.

############################# Back to top ###############################
back_to_top:
    enable: true
---