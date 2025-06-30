


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:33
draft: false
lang: fr
format: Ods
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraire des images à partir de fichiers ODS dans des applications C#"
head_description: "Utilisez GroupDocs.Parser pour détecter et extraire des images de fichiers ODS dans C# sans outils supplémentaires."

############################# Header ############################
title: "Extraire des images de ODS en utilisant C#" 
description: "Localisez et extrayez les images intégrées à partir de PDF, documents Word, feuilles Excel et d'autres types de fichiers à l'aide de GroupDocs.Parser dans vos applications .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Télécharger l'essai gratuit"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "À propos de l'API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "En savoir plus"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) est une bibliothèque robuste de parsing de documents pour les développeurs .NET. Elle vous permet d'extraire des images, du texte, des hyperliens et des données structurées à partir de formats de fichiers populaires tels que PDF, DOCX, XLSX, PPTX et d'autres — le tout sans nécessiter d'applications tierces.

############################# Steps ############################
steps:
    enable: true
    title: "Étapes pour extraire des images de Ods en C#"
    content: |
      Avec [GroupDocs.Parser](/parser/net/), vous pouvez extraire des images de documents ODS dans vos projets .NET en quelques étapes :
      
      1. Initialisez le Parser avec le fichier ODS.
      2. Récupérez les éléments d'image du document.
      3. Utilisez les images extraites selon vos besoins dans votre flux de travail.
   
    code:
      platform: "net"
      copy_title: "Copier"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "Cliquez pour copier"
        copy_done: "copié"
      links:
        #  loop
        - title: "Plus d'exemples"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Documentation"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Ouvrez le document contenant des images à l'aide de Parser
        using (Parser parser = new Parser("input.ods")) {

            // Extraire toutes les images intégrées du fichier
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Gérer les cas où aucune image n'est trouvée
            if (images == null)
            {
                return;
            }

            // Traiter ou enregistrer les images récupérées
            foreach (PageImageArea image in images)
            {
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Extraction complète du contenu des documents"
  description: "GroupDocs.Parser offre plus que l'extraction d'images — vous pouvez également extraire du texte brut, des hyperliens, des métadonnées et du contenu structuré pour des scénarios d'automatisation avancés."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Flux de travail d'extraction d'images et de parsing de documents"
  features:
    # feature loop
    - title: "Extraire des images de plusieurs formats"
      content: "Extraire des images intégrées à partir d'une variété de formats de fichiers, y compris DOCX, PDF, PPTX, XLSX, ainsi que des fichiers d'image tels que PNG, JPG et TIFF."

    # feature loop
    - title: "Préserver la qualité d'image d'origine"
      content: "Les images sont extraites avec une grande fidélité, conservant leur résolution, format et profil de couleur d'origine."

    # feature loop
    - title: "Options d'extraction avancées"
      content: "Personnalisez l'extraction d'images avec un filtrage par page, format ou résolution, et prise en charge des documents multi-pages."
      
  code_samples:
    # code sample loop
    - title: "Comment extraire et enregistrer des images d'un document PDF"
      content: |
        Cet exemple montre comment extraire tous les actifs d'image d'un fichier PDF et les enregistrer dans le système de fichiers local.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Chargez le PDF à l'aide de la classe Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Extraire les images intégrées du fichier
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Définir le format de sortie et les options d'image (ex. : PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Écrire les images extraites sur le disque
            int imageNumber = 0;
            foreach (PageImageArea image in images)
            {
                image.Save(imageNumber.ToString() + ".png", options);
                imageNumber++;
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
    - title: "Téléchargement Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Licences"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Formats pris en charge pour l'extraction d'images"
    exclude: "ODS"
    description: "GroupDocs.Parser permet une extraction précise d'images à partir d'une large gamme de formats de documents et d'images. Consultez la liste ci-dessous pour les types couramment pris en charge."
    items: 
        # format loop 1
        - name: "Analyse PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(Format de document portable)"
          
        # format loop 2
        - name: "Analyse DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Document Word 2007+)"
          
        # format loop 3
        - name: "Analyse PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Format de présentation Open XML)"
          
        # format loop 4
        - name: "Analyse XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Classeur Open XML)"
          
        # format loop 5
        - name: "Analyse ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(Document texte OpenDocument)"
          
        # format loop 6
        - name: "Analyse ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(Tableur OpenDocument)"
          
        # format loop 7
        - name: "Analyse ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(Présentation OpenDocument)"
          
        # format loop 8
        - name: "Analyse EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(Fichier eBook Open)"
          
        # format loop 9
        - name: "Analyse FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---