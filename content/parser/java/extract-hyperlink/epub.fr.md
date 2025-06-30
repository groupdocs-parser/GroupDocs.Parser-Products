


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: fr
format: Epub
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "Extraire des hyperliens des fichiers EPUB dans des applications Java"
head_description: "Utilisez GroupDocs.Parser pour trouver et extraire des liens URL à partir de documents EPUB dans des projets Java—aucun logiciel supplémentaire requis."

############################# Header ############################
title: "Extraire des hyperliens des EPUB avec Java" 
description: "Extrayez des liens web et des hyperliens de fichiers PDF, documents Word, feuilles Excel, et d'autres documents en utilisant GroupDocs.Parser dans votre environnement Java."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Télécharger l'Essai Gratuit"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "À propos de l'API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "En savoir plus"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) est une API robuste d'extraction de contenu conçue pour les développeurs Java. Elle offre des outils pour extraire des hyperliens, des données structurées, des images et du texte à partir de formats populaires tels que DOCX, XLSX, PDF, HTML, et plus—sans avoir besoin de plugins externes.

############################# Steps ############################
steps:
    enable: true
    title: "Comment extraire des hyperliens des Epub en Java"
    content: |
      [GroupDocs.Parser](/parser/java/) facilite l'extraction d'hyperliens des fichiers EPUB dans les applications Java avec ces étapes de base :
      
      1. Ouvrez le fichier EPUB en utilisant une instance de Parser.
      2. Assurez-vous que l'extraction des hyperliens est disponible pour le format de fichier.
      3. Extraire tous les hyperliens en utilisant la méthode appropriée.
      4. Parcourez les résultats et traitez chaque lien selon vos besoins.
   
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
        // Chargez le fichier pouvant contenir des hyperliens en utilisant le Parser
        try (Parser parser = new Parser("input.epub")) {

            // Vérifiez si le format du document prend en charge l'analyse des hyperliens
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("L'extraction des hyperliens n'est pas disponible pour le fichier");
                return;
            }

            // Extraire et utiliser les données des hyperliens du document
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "Outils complets de parsing de documents"
  description: "En plus d'extraire des hyperliens, GroupDocs.Parser vous permet de collecter d'autres contenus utiles tels que du texte brut, des médias intégrés et des données structurées pour une utilisation dans des flux de travail automatisés."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "Extraction d'hyperliens et analyse de documents"
  features:
    # feature loop
    - title: "Détection précise des liens"
      content: "Capturer tous les types d'hyperliens à partir de différentes mises en page de documents, y compris le texte cliquable et les URL cachées."

    # feature loop
    - title: "Fonctionne avec des documents et du contenu web"
      content: "Extraire des liens à partir de fichiers PDF, DOCX, XLSX, HTML et d'images contenant des hyperliens intégrés."

    # feature loop
    - title: "Comportement d'extraction personnalisé"
      content: "Affinez la manière dont les hyperliens sont extraits en utilisant des options telles que les plages de pages, les types de liens ou les filtres de contenu."
      
  code_samples:
    # code sample loop
    - title: "Exemple : extraction d'hyperliens d'un PDF avec des options personnalisées"
      content: |
        Cet exemple montre comment extraire tous les liens d'un fichier PDF en utilisant des paramètres d'extraction des liens.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  Ouvrez le PDF en utilisant la classe Parser
        try (Parser parser = new Parser("input.docx"))
        {
            // Vérifiez que le support des hyperliens est activé pour ce document
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // Appliquez des options pour filtrer les liens
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // Utilisez le parser pour obtenir les données des hyperliens
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // Itérez à travers les liens et gérez-les en conséquence
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
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
    title: "Formats de documents prenant en charge l'extraction d'hyperliens"
    exclude: "EPUB"
    description: "Avec GroupDocs.Parser, vous pouvez extraire des hyperliens de nombreux formats de fichiers couramment utilisés. Voici une liste de formats généralement pris en charge."
    items: 
        # format loop 1
        - name: "Analyse PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(Format de document portable)"
          
        # format loop 2
        - name: "Analyse DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(Document Word 2007+)"
          
        # format loop 3
        - name: "Analyse PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(Format de présentation Open XML)"
          
        # format loop 4
        - name: "Analyse XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(Classeur Open XML)"
          
        # format loop 5
        - name: "Analyse TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(Fichier texte)"
          
        # format loop 6
        - name: "Analyse RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(Format de texte enrichi)"
          
        # format loop 7
        - name: "Analyse XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(Langage de balisage extensible)"
          
        # format loop 8
        - name: "Analyse EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(Fichier eBook Open)"
         
          

---