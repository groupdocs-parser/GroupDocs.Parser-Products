---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:10
draft: false
otherformats: doc docm docx dot dotm dotx epub html mht mhtml odp ods odt one otp ott pdf

############################# Head ############################
head_title: "Extraire des images de Excel, Word, PDF et autre document ou page via .NET"
head_description: "L'API GroupDocs.Parser .NET permet aux programmeurs de logiciels d'extraire des images de différents documents tels que MS Excel, Word, PowerPoint, PDF et plus dans leurs applications .NET."

############################# Header ############################
title: "Extraire des images de PDF, DOCX, PPTX, MSG, XLSX documents et pages via l'API C#.NET"
description: "GroupDocs.Parser .NET L'API permet aux programmeurs d'extraire des images de PDF, DOC, DOCX, PPT, PPTX, EML, MSG, XLS, XLSX, CSV , ODT, RTF & EPUB documents ou pages de document."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Télécharger la version d'essai gratuite"
    link: "https://downloads.groupdocs.com/parser/net"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/net"
              text: "Référence API"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Exemples de codes"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Démos en direct"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Tarification"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Comment extraire des images de documents via .NET ?"
    content: |
        Les images peuvent être utilisées pour fournir des informations d'une manière telle qu'elles ne peuvent pas être exprimées par des mots. Les images nous aident à attirer l'attention de l'utilisateur et expliquent facilement les concepts difficiles. Parfois, en lisant des documents, des revues ou en profitant de présentations, nous avons souvent trouvé des images fascinantes et avons voulu les télécharger. GroupDocs.Parser for .NET est une API puissante qui aide les utilisateurs à développer des applications utiles pour extraire des images de différents types de documents et les enregistrer en PNG, JPEG, WebP, GIF, BMP et d'autres formats. L'API a inclus des supports pour le texte ainsi que l'extraction d'images à partir de certains des formats de fichiers les plus couramment utilisés, tels que PDF, e-mails, ebooks, formats Microsoft Office : Word (DOC, DOCX), { 284} (PPT, PPTX), Excel (XLS, XLSX), formats LibreOffice et bien d'autres. L'API prend également entièrement en charge l'analyse de documents, l'extraction de texte brut et structuré, la recherche de texte par mots-clés, l'extraction de métadonnées ou d'images, de conteneurs ainsi que de pièces jointes et bien d'autres.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Extraire des images de documents dans .NET"
    content_left: |
        [GroupDocs.Parser for .NET](/fr/parser/net/) permet aux développeurs C# d'extraire facilement des images d'un document en mettant en œuvre quelques étapes simples.
        
        * Instanciez l'objet [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) pour le document initial ;
        * Appelez la méthode [GetImages](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser/methods/getimages) et obtenez la collection d'objets image ;
        * Vérifiez si le lecteur n'est pas *null* (l'extraction d'images est prise en charge pour le document) ;
        * Parcourez la collection et obtenez les tailles, les types d'images et le contenu des images.

    title_right: "En savoir plus sur l'extraction d'images"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document/">Comment extraire des images d'un document</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page/">Comment extraire des images d'une page de document</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-from-document-page-area/">Comment extraire des images de la zone de page de document</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-images-to-files/">Comment extraire des images dans des fichiers</a>

    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Comment extraire des images de documents à l'aide de l'exemple de code C#">}}

        ```csharp    
        // Extraire des images de documents à l'aide de l'API GroupDocs.Parser
        // Créer une instance de la classe Parser
        using (Parser parser = new Parser(filePath)) {
            // Extraire des images
            IEnumerable<PageImageArea> images = parser.GetImages();
            // Vérifiez si l'extraction d'images est prise en charge
            if (images == null) {
                Console.WriteLine("L'extraction d'images n'est pas prise en charge");
                return;
            }
            // Itérer sur les images
            foreach (PageImageArea image in images) {
                // Imprimer un index de page, un rectangle et un type d'image :
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "Configuration requise"
    content_left: |
        GroupDocs.Parser for .NET Les API sont prises en charge sur toutes les principales plates-formes et systèmes d'exploitation. Avant d'exécuter le code ci-dessous, assurez-vous que les prérequis suivants sont installés sur votre système.
        
        * Systèmes d'exploitation : Microsoft Windows, Linux, MacOS
        * Environnements de développement : Microsoft Visual Studio, Xamarin, MonoDevelop
        * Cadres
        * Téléchargez la dernière version de GroupDocs.Parser for .NET depuis [Nuget](https://www.nuget.org/packages/groupdocs.parser)

    title_right: "Pourquoi utiliser GroupDocs.Parser for .NET"
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
        .NET API d'analyse de documents et d'extraction d'images pour les formats de fichiers et les images. Extrayez les données pour certains des formats de fichiers populaires comme indiqué ci-dessous.

############################# Back to top ###############################
back_to_top:
    enable: true
---