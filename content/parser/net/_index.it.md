---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: it
product: "Parser"
product_tag: "parser"
platform: "Net"
platform_tag: "net"

############################# Drop-down ############################
supported_platforms:
  items:
    # supported_platforms loop
    - title: ".NET"
      tag: "net"
    # supported_platforms loop
    - title: "Java"
      tag: "java"
    # supported_platforms loop
    - title: "Python"
      tag: "python-net"

############################# Head ############################
head_title: "GroupDocs.Parser for .NET Document Parser SDK per .NET"
head_description: "SDK Document Parser ad alte prestazioni per .NET. Estrai testo, immagini, metadati, codici a barre, tabelle e altri dati da PDF, Word, Excel, email e oltre 50 formati di documento."

############################# Header ############################
title: "Document Parser SDK per .NET"
description: "Aggiungi analisi rapida e accurata dei documenti alle tue applicazioni .NET ed estrai testo, immagini, metadati e dati strutturati da documenti e immagini."
words:
  for: "per"

actions:
  main: "Nuget Download"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Licenza"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Pronto per iniziare?"
  description: "Prova le funzionalità di GroupDocs.Parser gratuitamente o richiedi una licenza"

release:
  title: "Versione {0} rilasciata"
  notes: "Scopri le novità"
  downloads: "Download"

code:
  title: "Analizza rapidamente il contenuto dei documenti con l'SDK"
  more: "Altri esempi"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Passa il file di origine all'istanza Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Passa il testo del documento a TextReader
        using (var textReader = parser.GetText())
        {
            // Elabora il testo del documento
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser in sintesi"
  description: "Document Parser SDK per eseguire l'analisi ad alta precisione dei documenti nelle applicazioni .NET"
  features:
    # feature loop
    - title: "Estrai dati dai documenti"
      content: "GroupDocs.Parser for .NET API ti consente di recuperare testo, metadati e immagini da una vasta gamma di formati di file, tra cui documenti Office, email, allegati e archivi. Questo potente strumento ti aiuta ad accedere e processare in modo efficiente le informazioni preziose contenute in questi file per varie applicazioni come l'analisi dei dati, l'indicizzazione per motori di ricerca o i sistemi di gestione dei contenuti."

    # feature loop
    - title: "Analizza i documenti"
      content: "Estrai diversi elementi come collegamenti ipertestuali, tabelle, codici QR, codici a barre e dati dai moduli PDF. Inoltre, analizza qualsiasi informazione desiderata dai documenti utilizzando modelli personalizzati."

    # feature loop
    - title: "Personalizzazione dei risultati"
      content: ".NET API ti consente di recuperare dati in vari formati come grezzo, strutturato, HTML o Markdown. Inoltre, l'API offre una funzionalità di ricerca per individuare parole o frasi specifiche nel testo dei documenti."

############################# Platforms ############################
platforms:
  enable: true
  title: "Indipendenza dalla piattaforma"
  description: "GroupDocs.Parser for .NET supporta i seguenti sistemi operativi, framework e gestori di pacchetti"
  items:
    # platform loop
    - title: "Amazon"
      image: "amazon"
    # platform loop
    - title: "Docker"
      image: "docker"
    # platform loop
    - title: "Azure"
      image: "azure"
    # platform loop
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "Formati di file supportati"
  description: |
    GroupDocs.Parser for .NET supporta operazioni con i seguenti [formati di file](https://docs.groupdocs.com/parser/net/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Formati Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Immagini e altri formati
        * **Portatile:** PDF 
        * **Immagini:** JPG, BMP, PNG, TIFF, GIF
        * **Altri formati Office:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Altri formati
        * **Web:** HTML, MHTML 
        * **Archivi:** ZIP, TAR, 7Z 
        * **e-Book:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for .NET caratteristiche"
  description: "Estrai dati da PDF, documenti Office, immagini e altri formati in modo rapido e preciso con il nostro Document Parser SDK per .NET"

  items:
    # feature loop
    - icon: "text"
      title: "Estrai testo"
      content: "Estrai informazioni testuali da vari formati di file, come documenti Office, PDF e immagini, per una facile leggibilità e analisi."

    # feature loop
    - icon: "image"
      title: "Estrai immagini"
      content: "Recupera contenuti visivi da diverse fonti, come documenti Office e file PDF, per un accesso e utilizzo pratici."

    # feature loop
    - icon: "qr"
      title: "Scansiona codici QR"
      content: "Rileva e decodifica i codici QR presenti in documenti Office, file PDF o contenuti visivi per un recupero efficiente delle informazioni."

    # feature loop
    - icon: "email"
      title: "Estrai dati da allegati email e archivi"
      content: "Raccogli informazioni preziose da messaggi email, allegati di file e sorgenti di dati compressi per un'analisi e un utilizzo efficaci."

    # feature loop
    - icon: "table"
      title: "Estrai tabelle"
      content: "Identifica ed estrai dati tabulari da documenti PDF per un'analisi e utilizzo organizzati."

    # feature loop
    - icon: "hyperlink"
      title: "Estrai collegamenti ipertestuali"
      content: "Individua ed estrae collegamenti ipertestuali e indirizzi email all'interno di documenti Office o file PDF per un accesso efficiente."

    # feature loop
    - icon: "pdf"
      title: "Analizza moduli PDF"
      content: "I moduli PDF sono documenti digitali con campi compilabili per l'interazione dell'utente, consentendo l'inserimento elettronico delle informazioni. L'API .NET può essere utilizzata per estrarre dati da questi moduli per un'elaborazione efficiente."

    # feature loop
    - icon: "template"
      title: "Analizza dati tramite template"
      content: "Crea template personalizzati e utilizzali con l'API .NET per analizzare informazioni specifiche da file PDF, semplificando i processi di estrazione dei dati."

    # feature loop
    - icon: "search"
      title: "Cerca testo nei documenti"
      content: "Individua rapidamente parole o pattern specifici all'interno dei documenti."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Esempi di codice"
  description: "Alcuni casi d'uso tipici delle operazioni di GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Estrai immagini da documenti PDF"
      content: |
        GroupDocs.Parser for .NET semplifica per gli sviluppatori C# l'estrazione di immagini da [documenti](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Estrai immagini da documenti PDF in C#">}}
        ```csharp {style=abap}
        // Crea un'istanza della classe Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Estrai immagini
            var images = parser.GetImages();

            // Verifica se è stato estratto qualcosa
            if (images == null)
            {
                return;
            }
            // Itera sulle immagini
            foreach (PageImageArea image in images)
            {
                // Stampa l'indice della pagina, il rettangolo e il tipo di immagine
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Estrai codici a barre dalle immagini"
      content: |
        Utilizza la nostra API .NET per estrarre [codici a barre](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) dalle immagini:
        {{< landing/code title="Estrai codici a barre dalle immagini in C#">}}
        ```csharp {style=abap}   
        // Carica l'immagine sorgente in Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Verifica se il file supporta l'estrazione di codici a barre
            if (parser.Features.Barcodes)
            {
                // Estrai i codici a barre dal file
                var barcodes = parser.GetBarcodes();

                // Itera sui codici a barre
                foreach (var barcode in barcodes)
                {
                    // Stampa l'indice della pagina
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Stampa il valore del codice a barre
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
