


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:33
draft: false
lang: it
format: Epub
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Estrai immagini da file EPUB in app C#"
head_description: "Utilizza GroupDocs.Parser per rilevare ed estrarre immagini da file EPUB in C# senza strumenti aggiuntivi."

############################# Header ############################
title: "Estrai immagini da EPUB usando C#" 
description: "Localizza ed estrai facilmente immagini incorporate da PDF, documenti Word, fogli Excel e altri tipi di file utilizzando GroupDocs.Parser nelle tue app .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Scarica la versione di prova gratuita"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Informazioni sull'API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Scopri di più"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) è una robusta libreria di parsing documentale per sviluppatori .NET. Ti consente di estrarre immagini, testo, collegamenti ipertestuali e dati strutturati da formati di file popolari come PDF, DOCX, XLSX, PPTX e altri, il tutto senza necessitare di applicazioni di terze parti.

############################# Steps ############################
steps:
    enable: true
    title: "Passaggi per estrarre immagini da Epub in C#"
    content: |
      Con [GroupDocs.Parser](/parser/net/), puoi estrarre immagini da documenti EPUB nei tuoi progetti .NET in pochi semplici passaggi:
      
      1. Inizializza il Parser con il file EPUB.
      2. Recupera gli elementi immagine dal documento.
      3. Utilizza le immagini estratte secondo necessità nel tuo flusso di lavoro.
   
    code:
      platform: "net"
      copy_title: "Copia"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "clicca per copiare"
        copy_done: "copiato"
      links:
        #  loop
        - title: "Altri esempi"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "Documentazione"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // Apri il documento contenente immagini utilizzando Parser
        using (Parser parser = new Parser("input.epub")) {

            // Estrai tutte le immagini incorporate dal file
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Gestisci i casi in cui non sono state trovate immagini
            if (images == null)
            {
                return;
            }

            // Elabora o salva le immagini recuperate
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
  title: "Estrazione completa del contenuto del documento"
  description: "GroupDocs.Parser offre più dell'estrazione delle immagini — puoi anche estrarre testo grezzo, collegamenti ipertestuali, metadati e contenuti strutturati per scenari di automazione avanzati."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "Flusso di lavoro per l'estrazione delle immagini e il parsing dei documenti"
  features:
    # feature loop
    - title: "Estrai immagini da più formati"
      content: "Estrai immagini incorporate da una varietà di formati di file, tra cui DOCX, PDF, PPTX, XLSX e file immagine come PNG, JPG e TIFF."

    # feature loop
    - title: "Preserva la qualità originale dell'immagine"
      content: "Le immagini vengono estratte con alta fedeltà, mantenendo la loro risoluzione originale, formato e profilo colore."

    # feature loop
    - title: "Opzioni di estrazione avanzate"
      content: "Personalizza l'estrazione delle immagini filtrando per pagina, formato o risoluzione, e supporta documenti multi-pagina."
      
  code_samples:
    # code sample loop
    - title: "Come estrarre e salvare immagini da un documento PDF"
      content: |
        Questo esempio dimostra come estrarre tutte le risorse immagine da un file PDF e salvarle nel file system locale.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Carica il PDF utilizzando la classe Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Estrai le immagini incorporate dal file
            IEnumerable<PageImageArea> images = parser.GetImages();

            // Imposta il formato di output e le opzioni per le immagini (es. PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // Scrivi le immagini estratte su disco
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
  title: "Pronto per iniziare?"
  description: "Prova le funzionalità di GroupDocs.Parser gratuitamente o richiedi una licenza"
  items:
    #  loop
    - title: "Download di Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "Licenze"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "Formati supportati per l'estrazione delle immagini"
    exclude: "EPUB"
    description: "GroupDocs.Parser consente un'accurata estrazione delle immagini da un'ampia gamma di formati di documenti e immagini. Consulta l'elenco sottostante per i tipi comunemente supportati."
    items: 
        # format loop 1
        - name: "Analizza PDF"
          format: "PDF"
          link: "/parser/net/extract-image/pdf/"
          description: "(Formato Documento Portatile)"
          
        # format loop 2
        - name: "Analizza DOCX"
          format: "DOCX"
          link: "/parser/net/extract-image/docx/"
          description: "(Documento Word Office 2007+)"
          
        # format loop 3
        - name: "Analizza PPTX"
          format: "PPTX"
          link: "/parser/net/extract-image/pptx/"
          description: "(Formato di presentazione Open XML)"
          
        # format loop 4
        - name: "Analizza XLSX"
          format: "XLSX"
          link: "/parser/net/extract-image/xlsx/"
          description: "(Cartella di lavoro Open XML)"
          
        # format loop 5
        - name: "Analizza ODT"
          format: "ODT"
          link: "/parser/net/extract-image/odt/"
          description: "(Documento di testo OpenDocument)"
          
        # format loop 6
        - name: "Analizza ODS"
          format: "ODS"
          link: "/parser/net/extract-image/ods/"
          description: "(Foglio di calcolo OpenDocument)"
          
        # format loop 7
        - name: "Analizza ODP"
          format: "ODP"
          link: "/parser/net/extract-image/odp/"
          description: "(Presentazione OpenDocument)"
          
        # format loop 8
        - name: "Analizza EPUB"
          format: "EPUB"
          link: "/parser/net/extract-image/epub/"
          description: "(File eBook Open)"
          
        # format loop 9
        - name: "Analizza FB2"
          format: "FB2"
          link: "/parser/net/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---