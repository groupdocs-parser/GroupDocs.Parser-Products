


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:20
draft: false
lang: it
format: Fb2
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "Estrai codici a barre da file FB2 in app C#"
head_description: "Utilizza GroupDocs.Parser per rilevare ed estrarre dati da codici a barre presenti in file FB2 in C# senza software aggiuntivo."

############################# Header ############################
title: "Estrai codici a barre da FB2 utilizzando C#" 
description: "Rileva ed estrai informazioni sui codici a barre da file PDF, Word, Excel e immagini utilizzando GroupDocs.Parser nelle tue applicazioni .NET."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "Scarica la prova gratuita"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "Informazioni sull'API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "Scopri di più"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) è un potente API di parsing dei documenti per gli sviluppatori .NET. Consente l'estrazione di testo, immagini, contenuti strutturati e codici a barre da vari formati di file, tra cui PDF, Word, Excel, PowerPoint e altro — il tutto senza fare affidamento su strumenti esterni.

############################# Steps ############################
steps:
    enable: true
    title: "Passaggi per estrarre codici a barre da Fb2 in C#"
    content: |
      [GroupDocs.Parser](/parser/net/) ti consente di estrarre dati da codici a barre da file FB2 nelle applicazioni .NET seguendo questi semplici passaggi:
      
      1. Carica il file FB2 utilizzando un'istanza di Parser.
      2. Verifica che il documento supporti l'estrazione dei codici a barre.
      3. Recupera l'elenco dei codici a barre dal documento.
      4. Itera attraverso i risultati e utilizza i valori dei codici a barre estratti.
   
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
        // Carica il documento contenente codici a barre utilizzando la classe Parser
        using (Parser parser = new Parser("input.fb2")) {

            // Verifica che il file supporti l'estrazione dei codici a barre
            if (!parser.Features.Barcodes) {
                Console.WriteLine("L'estrazione dei codici a barre non è supportata");
                return;
            }

            // Recupera e processa i codici a barre estratti
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

            foreach (PageBarcodeArea barcode in barcodes) {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "Funzionalità avanzate di parsing dei documenti"
  description: "Oltre all'estrazione dei codici a barre, GroupDocs.Parser ti consente di estrarre testo semplice, immagini e dati strutturati per supportare flussi di lavoro di automazione e elaborazione dati avanzati."
  image: "/img/parser/features_extract-barcode.webp" # 500x500 px
  image_description: "Riconoscimento dei codici a barre e parsing dei documenti"
  features:
    # feature loop
    - title: "Supporto per più formati di codici a barre"
      content: "Riconosci i tipi di codice a barre comuni, inclusi QR Code, Code 128, Data Matrix, EAN, Aztec e altro."

    # feature loop
    - title: "Estrai codici a barre da documenti e immagini"
      content: "Leggi codici a barre da documenti PDF, Word, Excel e formati immagine come JPEG, PNG e BMP."

    # feature loop
    - title: "Impostazioni di estrazione personalizzabili"
      content: "Configura opzioni di rilevamento come aree di scansione e elaborazione di documenti multipagina."
      
  code_samples:
    # code sample loop
    - title: "Come estrarre codici a barre da un PDF utilizzando opzioni per codici a barre"
      content: |
        Questo esempio dimostra come estrarre codici a barre da un file PDF utilizzando opzioni specifiche per l'estrazione dei codici a barre.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  Carica il file PDF con la classe Parser
        using (Parser parser = new Parser("input.pdf"))
        {
            // Conferma che l'estrazione dei codici a barre è supportata
            if (!parser.Features.Barcodes)
            {
                return;
            }

            // Utilizza opzioni per codici a barre per filtrare i risultati
            BarcodeOptions options = new BarcodeOptions(QualityMode.Low, QualityMode.Low, "QR");

            // Recupera i dati dei codici a barre dal documento
            IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

            // Elabora l'elenco dei codici a barre estratti
            foreach (PageBarcodeArea barcode in barcodes)
            {
                Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                Console.WriteLine("Value: " + barcode.Value);
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
    title: "Formati supportati per l'estrazione dei codici a barre"
    exclude: "FB2"
    description: "GroupDocs.Parser supporta il rilevamento dei codici a barre in un'ampia gamma di formati di documenti e immagini. Vedi di seguito i tipi di file comunemente supportati."
    items: 
        # format loop 1
        - name: "Analizza PDF"
          format: "PDF"
          link: "/parser/net/extract-barcode/pdf/"
          description: "(Formato Documento Portatile)"
          
        # format loop 2
        - name: "Analizza DOCX"
          format: "DOCX"
          link: "/parser/net/extract-barcode/docx/"
          description: "(Documento Word Office 2007+)"
          
        # format loop 3
        - name: "Analizza PPTX"
          format: "PPTX"
          link: "/parser/net/extract-barcode/pptx/"
          description: "(Formato di presentazione Open XML)"
          
        # format loop 4
        - name: "Analizza XLSX"
          format: "XLSX"
          link: "/parser/net/extract-barcode/xlsx/"
          description: "(Cartella di lavoro Open XML)"
          
        # format loop 5
        - name: "Analizza ODT"
          format: "ODT"
          link: "/parser/net/extract-barcode/odt/"
          description: "(Documento di testo OpenDocument)"
          
        # format loop 6
        - name: "Analizza ODS"
          format: "ODS"
          link: "/parser/net/extract-barcode/ods/"
          description: "(Foglio di calcolo OpenDocument)"
          
        # format loop 7
        - name: "Analizza ODP"
          format: "ODP"
          link: "/parser/net/extract-barcode/odp/"
          description: "(Presentazione OpenDocument)"
          
        # format loop 8
        - name: "Analizza EPUB"
          format: "EPUB"
          link: "/parser/net/extract-barcode/epub/"
          description: "(File eBook Open)"
          
        # format loop 9
        - name: "Analizza FB2"
          format: "FB2"
          link: "/parser/net/extract-barcode/fb2/"
          description: "(eBook FictionBook)"
         
          

---