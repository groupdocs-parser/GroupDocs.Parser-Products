


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:40
draft: false
lang: fr
format: Pptx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Extraire des tables à partir de fichiers PPTX dans des applications C#"
head_description: "Utilisez GroupDocs.Parser pour localiser et extraire des données de table structurées à partir de fichiers PPTX dans des applications C# sans dépendances supplémentaires."

############################# Header ############################
title: "Extraire des tables à partir de PPTX en utilisant C#" 
description: "Identifiez et extrayez rapidement les structures de table à partir de PDF, Word, Excel et d'autres formats de fichiers à l'aide de GroupDocs.Parser dans vos projets .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Télécharger l'Essai Gratuit"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "À propos de l'API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "En savoir plus"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) est une API de parsing de documents complète conçue pour les développeurs .NET. Elle permet l'extraction précise de texte, tableaux, images, hyperliens et autres éléments structurés à partir de formats tels que PDF, DOCX, XLSX, PPTX et bien d'autres — sans avoir besoin d'un logiciel tiers.

############################# Steps ############################
steps:
    enable: true
    title: "Étapes pour extraire des tables à partir de Pptx dans C#"
    content: |
      Suivez ces instructions pour extraire des tables à partir de fichiers PPTX en utilisant [GroupDocs.Parser](/parser/net/) dans votre environnement .NET :
      
      1. Initialisez une instance de Parser et chargez votre document PPTX.
      2. Vérifiez si l'extraction de tables est supportée pour le format d'entrée.
      3. Extraire le contenu de la table depuis le fichier.
      4. Utilisez les données de la table structurée pour la génération de rapports, l'automatisation ou l'analyse.
   
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
        // Ouvrez le document contenant des données de table en utilisant Parser
        using (Parser parser = new Parser("input.pptx")) {

            // Vérifiez si le format prend en charge la reconnaissance des tables
            if (!parser.Features.Tables) {
                Console.WriteLine("Gérez les documents qui ne prennent pas en charge le parsing des tables");
                return;
            }

            // Définissez comment la structure de la table doit être reconnue
            TemplateTableLayout layout = new TemplateTableLayout(
                new double[] { 50, 95, 275, 415, 485, 545 },
                new double[] { 325, 340, 365, 395 });

            // Spécifiez les paramètres d'extraction pour les données de table
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  Extraire des tables à partir du contenu du fichier
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            //  Parcourez chaque table détectée
            foreach (PageTableArea t in tables)
            {
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Capacités puissantes d'extraction de données"
  description: "En plus du parsing des tables, GroupDocs.Parser peut extraire un contenu riche tel que des blocs de texte, des images, des métadonnées et d'autres données structurées pour faciliter l'automatisation des documents."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "Reconnaissance des tables et extraction de contenu"
  features:
    # feature loop
    - title: "Détection de tables multi-formats précise"
      content: "Extraire des données tabulaires à partir de DOCX, XLSX, PDF, HTML et formats similaires avec une grande précision."

    # feature loop
    - title: "Analyser les structures de table à partir de fichiers"
      content: "Récupérer efficacement des données de table à partir de documents et de feuilles de calcul sans perte de formatage."

    # feature loop
    - title: "Configuration flexible pour l'extraction de tables"
      content: "Ajustez la détection de mise en page, l'alignement des colonnes et les options d'en-tête/pied de page pour un contrôle précis sur la sortie."
      
  code_samples:
    # code sample loop
    - title: "Comment extraire des tables à partir de feuilles de calcul Excel"
      content: |
        Cet exemple de code montre comment lire et parcourir les données des tables dans un fichier XLSX en utilisant GroupDocs.Parser.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Ouvrez le fichier Excel en utilisant l'API Parser
        using (Parser parser = new Parser("input.xlsx"))
        {
            // Quittez si les tables ne peuvent pas être extraites du fichier
            if (!parser.Features.Tables)
            {
                return;
            }

            // Utilisez des règles de mise en page pour localiser le contenu tabulaire
            TemplateTableLayout layout = new TemplateTableLayout(
                    new double[] { 50, 95, 275, 415, 485, 545 },
                    new double[] { 325, 340, 365, 395 });

            // Configurez les paramètres d'extraction pour les tables
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // Effectuez l'opération d'extraction des tables
            IEnumerable<PageTableArea> tables = parser.GetTables(options);

            // Parcourez chaque structure de table détectée
            foreach (PageTableArea t in tables)
            {
                // Parcourez chaque ligne dans la table
                for (int row = 0; row < t.RowCount; row++)
                {
                    // Parcourez les cellules de chaque ligne
                    for (int column = 0; column < t.ColumnCount; column++)
                    {
                        // Accédez à la cellule de table actuelle
                        PageTableAreaCell cell = t[row, column];
                        if (cell != null)
                        {
                            // Affichez le contenu texte de chaque cellule
                            Console.Write(cell.Text);
                            Console.Write(" | ");
                        }
                    }
                }
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
    title: "Formats pris en charge pour l'extraction de tables"
    exclude: "PPTX"
    description: "GroupDocs.Parser peut extraire des données de table à partir de divers types de documents. Voici les formats les plus couramment utilisés pour le parsing de tableaux structurés."
    items: 
        # format loop 1
        - name: "Analyse PDF"
          format: "PDF"
          link: "/parser/net/extract-table/pdf/"
          description: "(Format de document portable)"
          
        # format loop 2
        - name: "Analyse DOCX"
          format: "DOCX"
          link: "/parser/net/extract-table/docx/"
          description: "(Document Word 2007+)"
          
        # format loop 3
        - name: "Analyse PPTX"
          format: "PPTX"
          link: "/parser/net/extract-table/pptx/"
          description: "(Format de présentation Open XML)"
          
        # format loop 4
        - name: "Analyse XLSX"
          format: "XLSX"
          link: "/parser/net/extract-table/xlsx/"
          description: "(Classeur Open XML)"
          
        # format loop 5
        - name: "Analyse TXT"
          format: "TXT"
          link: "/parser/net/extract-table/txt/"
          description: "(Fichier texte)"
          
        # format loop 6
        - name: "Analyse RTF"
          format: "RTF"
          link: "/parser/net/extract-table/rtf/"
          description: "(Format de texte enrichi)"
          
        # format loop 7
        - name: "Analyse XML"
          format: "XML"
          link: "/parser/net/extract-table/xml/"
          description: "(Langage de balisage extensible)"
          
        # format loop 8
        - name: "Analyse EPUB"
          format: "EPUB"
          link: "/parser/net/extract-table/epub/"
          description: "(Fichier eBook Open)"
         
          

---