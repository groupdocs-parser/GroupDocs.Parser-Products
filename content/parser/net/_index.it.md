---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
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

############################# Head ############################
head_title: "Applicazioni di Parsing Documenti GroupDocs.Parser for .NET"
head_description: "Ottieni una soluzione di parsing documenti all-in-one per applicazioni .NET. Estrai dati da formati documentali online utilizzando una semplice funzionalità di trascinamento."

############################# Header ############################
title: "Analizza documenti tramite l'API .NET"
description: "Estrai dati da documenti e immagini su qualsiasi piattaforma utilizzando le nostre API flessibili e soluzioni basate su app per programmatori e utenti finali."
words:
  for: "per"

actions:
  main: "Download Nuget"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Licenze"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Pronto per iniziare?"
  description: "Prova gratuitamente le funzionalità di GroupDocs.Parser o richiedi una licenza"

release:
  title: "Versione {0} rilasciata"
  notes: "Scopri le novità"
  downloads: "Download"

code:
  title: "Analizza rapidamente il contenuto del documento"
  more: "Ulteriori esempi"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Passa il file sorgente all'istanza Parser
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
  title: "GroupDocs.Parser in breve"
  description: "API per eseguire il parsing dei documenti nelle applicazioni .NET"
  features:
    # feature loop
    - title: "Estrai dati dai documenti"
      content: "L'API GroupDocs.Parser for .NET ti consente di recuperare testo, metadati e immagini da un'ampia gamma di formati di file come documenti Office, email, allegati e archivi. Questo potente strumento ti aiuta ad accedere e elaborare in modo efficiente informazioni preziose contenute all'interno di questi file per varie applicazioni come analisi dei dati, indicizzazione dei motori di ricerca o sistemi di gestione dei contenuti."

    # feature loop
    - title: "Analizza documenti"
      content: "Estrai vari elementi come collegamenti ipertestuali, tabelle, codici QR, codici a barre e dati da moduli PDF. Inoltre, analizza qualsiasi informazione desiderata dai documenti utilizzando modelli personalizzati."

    # feature loop
    - title: "Personalizzazione dei risultati"
      content: "L'API .NET ti consente di recuperare dati in vari formati come raw, strutturati, HTML o Markdown. Inoltre, l'API offre una funzionalità di ricerca per localizzare parole o frasi specifiche all'interno del testo dei documenti."

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
        * **Portabili:** PDF 
        * **Immagini:** JPG, BMP, PNG, TIFF, GIF
        * **Altri formati office:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
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
  title: "Caratteristiche di GroupDocs.Parser for .NET"
  description: "Estrai dati da PDF, documenti Office e immagini in modo rapido e accurato"

  items:
    # feature loop
    - icon: "text"
      title: "Estrai testo"
      content: "Estrai informazioni testuali da vari formati di file come documenti office, file PDF e immagini per una lettura e analisi agevoli."

    # feature loop
    - icon: "image"
      title: "Estrai immagini"
      content: "Recupera contenuti visivi da fonti diversificate come documenti office e file PDF per un'accessibilità e utilizzo convenienti."

    # feature loop
    - icon: "qr"
      title: "Scansiona codici QR"
      content: "Rileva e decodifica i codici QR presenti nei documenti office, nei file PDF o nei contenuti visivi per un recupero efficiente delle informazioni."

    # feature loop
    - icon: "email"
      title: "Estrai dati da allegati email e archivi"
      content: "Raccogli informazioni preziose dai messaggi email, dagli allegati di file e dalle fonti di dati compressi per un'analisi e un utilizzo efficaci."

    # feature loop
    - icon: "table"
      title: "Estrai tabelle"
      content: "Identifica ed estrai dati tabulari dai documenti PDF per un'analisi e un utilizzo organizzato."

    # feature loop
    - icon: "hyperlink"
      title: "Estrai collegamenti ipertestuali"
      content: "Individua ed estrai collegamenti ipertestuali e indirizzi email all'interno di documenti office o file PDF per un'accessibilità efficiente."

    # feature loop
    - icon: "pdf"
      title: "Analizza Moduli PDF"
      content: "I Moduli PDF sono documenti digitali che presentano campi compilabili per l'interazione dell'utente, consentendo di inserire informazioni elettronicamente. L'API .NET può essere utilizzata per estrarre dati da questi moduli per un'elaborazione efficiente."

    # feature loop
    - icon: "template"
      title: "Analizza dati tramite modelli"
      content: "Crea modelli personalizzati e utilizzali con l'API .NET per analizzare informazioni specifiche dai file PDF, semplificando i processi di estrazione dei dati."

    # feature loop
    - icon: "search"
      title: "Cerca un testo nei documenti"
      content: "Individua rapidamente parole o pattern specifici all'interno dei documenti."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Esempi di codice"
  description: "Alcuni casi d'uso delle tipiche operazioni di GroupDocs.Parser for .NET"
  items:
    # code sample loop
    - title: "Estrai immagini da documenti PDF"
      content: |
        GroupDocs.Parser for .NET semplifica per gli sviluppatori C# l'estrazione di immagini dai [documenti](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Estrai immagini da documenti PDF in C#">}}
        ```csharp {style=abap}
        // Crea un'istanza della classe Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Estrai le immagini
            var images = parser.GetImages();

            // Controlla se qualcosa è stato estratto
            if (images == null)
            {
                return;
            }
            // Itera sulle immagini
            foreach (PageImageArea image in images)
            {
                // Stampa un indice di pagina, rettangolo e tipo di immagine
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
        // Carica l'immagine sorgente su Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Controlla se il file supporta l'estrazione dei codici a barre
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
