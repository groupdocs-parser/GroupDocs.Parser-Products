


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: fr
format: Odp
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Extraire des images des fichiers ODP dans les applications Java"
head_description: "Avec GroupDocs.Parser, vous pouvez extraire des images des fichiers ODP dans Java sans avoir recours à des outils tiers."

############################# Header ############################
title: "Extraire des images des ODP en utilisant Java" 
description: "Récupérez les images intégrées dans des fichiers tels que PDF, Word, Excel, et plus encore en utilisant GroupDocs.Parser dans votre environnement de développement Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Télécharger l'essai gratuit"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "Qu'est-ce que GroupDocs.Parser for Java ?"
    link: "/parser/java/"
    link_title: "En savoir plus"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) est une API de parsing riche en fonctionnalités, conçue pour les développeurs Java. Elle permet l'extraction d'images, de texte, de liens, et d'éléments structurés de divers formats de fichiers, y compris DOCX, XLSX, PDF, PNG, JPG, et bien d'autres — le tout sans nécessiter de bibliothèques ou d'applications externes.

############################# Steps ############################
steps:
    enable: true
    title: "Comment extraire des images de Odp en Java"
    content: |
      Suivez ces étapes pour extraire des images des documents ODP en utilisant [GroupDocs.Parser](/parser/java/) dans votre application Java :
      
      1. Créer une instance de Parser et charger le fichier ODP.
      2. Extraire les données d'image du document chargé.
      3. Utiliser ou exporter les images extraites selon vos besoins.
   
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
        // Initialiser le parseur et charger le document contenant des images en utilisant Parser
        try (Parser parser = new Parser("input.odp"))
        {
            // Collecter tous les éléments d'image intégrés dans le document
            Iterable<PageImageArea> images = parser.getImages();

            // Ignorer le traitement si le document ne contient pas d'images
            if (images == null) {
                return;
            }

            // Traiter chaque image selon les besoins
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Plus de capacités de parsing de documents"
  description: "En plus de l'extraction d'images, GroupDocs.Parser vous permet d'extraire du contenu brut tel que du texte, des liens, des métadonnées, et des données structurées pour le traitement et l'analyse."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Extraire des images et du contenu des documents"
  features:
    # feature loop
    - title: "Fonctionne avec une variété de formats"
      content: "Extraire des images de différents types de documents, y compris PDF, DOCX, PPTX, XLSX, et des formats d'image tels que PNG, JPEG, et GIF."

    # feature loop
    - title: "Maintenir la clarté et la résolution des images"
      content: "Toutes les images extraites conservent leur résolution et leur type de fichier d'origine pour garantir une qualité et une utilité cohérentes."

    # feature loop
    - title: "Options de configuration flexibles"
      content: "Personnalisez le processus d'extraction d'images en filtrant les images par type, taille, index de page, ou format de fichier."
      
  code_samples:
    # code sample loop
    - title: "Extraire et enregistrer des images à partir de fichiers PDF"
      content: |
        Cet exemple montre comment extraire des images d'un document PDF et les enregistrer individuellement sur votre appareil.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Utiliser Parser pour ouvrir le fichier PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // Obtenir les images du contenu du document
            Iterable<PageImageArea> images = parser.getImages();

            // Définir des paramètres de sortie tels que le format (par exemple, JPEG ou PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Enregistrer les images extraites dans un répertoire local
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
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
    title: "Types de fichiers supportés pour l'extraction d'images"
    exclude: "ODP"
    description: "GroupDocs.Parser prend en charge l'extraction d'images à travers une large gamme de documents et d'images. Explorez les formats couramment pris en charge ci-dessous."
    items: 
        # format loop 1
        - name: "Analyse PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(Format de document portable)"
          
        # format loop 2
        - name: "Analyse DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(Document Word 2007+)"
          
        # format loop 3
        - name: "Analyse PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(Format de présentation Open XML)"
          
        # format loop 4
        - name: "Analyse XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(Classeur Open XML)"
          
        # format loop 5
        - name: "Analyse ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(Document texte OpenDocument)"
          
        # format loop 6
        - name: "Analyse ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(Tableur OpenDocument)"
          
        # format loop 7
        - name: "Analyse ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(Présentation OpenDocument)"
          
        # format loop 8
        - name: "Analyse EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(Fichier eBook Open)"
          
        # format loop 9
        - name: "Analyse FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---