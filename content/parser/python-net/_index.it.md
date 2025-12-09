---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: it
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

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
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK per Python"
head_description: "SDK Document Parser ad alte prestazioni per Python. Estrai testo, immagini, metadati, codici a barre, tabelle e altri dati da PDF, Word, Excel, email e oltre 50 formati di documento."

############################# Header ############################
title: "Document Parser SDK per Python"
description: "Aggiungi un'analisi rapida e precisa dei documenti alle tue app Python ed estrai testo, immagini, metadati e dati strutturati da documenti e immagini."
words:
  for: "per"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI Scarica"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Licenza"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "Pronto per iniziare?"
  description: "Prova le funzionalità di GroupDocs.Parser gratuitamente o richiedi una licenza"

release:
  enable: false
  title: "Versione {0} rilasciata"
  notes: "Scopri le novità"
  downloads: "Download"

code:
  title: "Estrai testo con Python"
  more: "Altri esempi"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Carica il documento
    with Parser("sample.pdf") as parser:
        # Estrai il testo dal documento
        text = parser.GetText()

        # Stampa tutto il testo estratto
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser in sintesi"
  description: "Document Parser SDK per eseguire l'analisi di documenti ad alta precisione nelle applicazioni Python"
  features:
    # feature loop
    - title: "Estrai dati dai documenti"
      content: "GroupDocs.Parser for Python via .NET API ti consente di recuperare testo, metadati e immagini da una vasta gamma di formati di file, come documenti Office, email, allegati e archivi. Questo potente strumento ti aiuta ad accedere e processare efficacemente le preziose informazioni contenute in questi file per diverse applicazioni, come analisi dei dati, indicizzazione per motori di ricerca o sistemi di gestione dei contenuti."

    # feature loop
    - title: "Analizza documenti"
      content: "Estrai diversi elementi, come collegamenti ipertestuali, tabelle, codici QR, codici a barre e dati da moduli PDF. Analizza inoltre qualsiasi informazione desiderata dai documenti utilizzando template personalizzati."

    # feature loop
    - title: "Personalizzazione dei risultati"
      content: "L'API Python ti consente di recuperare dati in vari formati, come grezzo, strutturato, HTML o Markdown. Inoltre, l'API offre una funzionalità di ricerca per individuare parole o frasi specifiche all'interno del testo dei documenti."

############################# Platforms ############################
platforms:
  enable: true
  title: "Indipendenza dalla piattaforma"
  description: "GroupDocs.Parser for Python via .NET supporta i seguenti sistemi operativi, framework e gestori di pacchetti"
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
    GroupDocs.Parser for Python via .NET supporta le operazioni con i seguenti [formati di file](https://docs.groupdocs.com/parser/python-net/supported-document-formats/).
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
  title: "Funzionalità di GroupDocs.Parser for Python via .NET"
  description: "Estrai dati da PDF, documenti Office, immagini e altri formati in modo rapido e preciso con il nostro Python Document Parser SDK"

  items:
    # feature loop
    - icon: "text"
      title: "Estrai testo"
      content: "Estrai informazioni testuali da vari formati di file, come documenti Office, file PDF e immagini, per una facile leggibilità e analisi."

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
      content: "Raccogli informazioni preziose da messaggi email, allegati di file e fonti di dati compressi per un'analisi e utilizzo efficaci."

    # feature loop
    - icon: "table"
      title: "Estrai tabelle"
      content: "Identifica ed estrai dati tabulari da documenti PDF per un'analisi e un utilizzo organizzati."

    # feature loop
    - icon: "hyperlink"
      title: "Estrai collegamenti ipertestuali"
      content: "Individuare ed estrarre collegamenti ipertestuali e indirizzi e‑mail all'interno di documenti Office o file PDF per un accesso efficiente."

    # feature loop
    - icon: "pdf"
      title: "Analizza moduli PDF"
      content: "I moduli PDF sono documenti digitali con campi compilabili per l'interazione dell'utente, che consentono di inserire informazioni elettronicamente. L'API Python può essere utilizzata per estrarre i dati da questi moduli per un'elaborazione efficiente."

    # feature loop
    - icon: "template"
      title: "Analizza dati tramite template"
      content: "Crea template personalizzati e utilizzali con l'API Python per analizzare informazioni specifiche da file PDF, semplificando i processi di estrazione dei dati."

    # feature loop
    - icon: "search"
      title: "Cerca testo nei documenti"
      content: "Individua rapidamente parole o pattern specifici all'interno dei documenti."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Esempi di codice"
  description: "Oltre all'estrazione di testo di base, ecco i casi d'uso più comuni per l'estrazione rapida di testo, immagini e metadati."
  items:
    # code sample loop
    - title: "Cerca testo in un documento"
      content: |
        Questo esempio mostra come cercare una frase specifica in un documento PDF e stampare dove è stata trovata.
        {{< landing/code title="Cerca testo in un documento in Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Carica il documento
        with Parser("sample.pdf") as parser:
            # Stampa l'indice della pagina e il rettangolo dove è stata trovata la frase
            for area in parser.Search("Total Amount"):
                # Stampa l'indice della pagina e il rettangolo dove è stata trovata la frase
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Estrai immagini da un documento"
      content: |
        Questo esempio mostra come estrarre immagini da un documento PDF e salvarle in un file.
        {{< landing/code title="Estrai immagini da un documento in Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Carica il documento
        with Parser("sample.docx") as parser:
            # Estrai le immagini dal documento
            images = parser.GetImages()

            # Salva le immagini in un file
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Estrai metadati da un documento"
      content: |
        Questo esempio mostra come estrarre i metadati da un documento PDF e stamparli.
        {{< landing/code title="Estrai metadati da un documento in Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Carica il documento
        with Parser("sample.pdf") as parser:
            # Estrai i metadati dal documento
            metadata = parser.GetMetadata()

            # Stampa i metadati
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
