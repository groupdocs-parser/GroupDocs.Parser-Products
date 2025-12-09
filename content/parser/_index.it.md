---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: it

############################# Head ############################
head_title: "SDK per l'analisi dei documenti PDF, Word e Excel | GroupDocs"
head_description: "SDK per l'analisi dei documenti per estrarre testo, immagini, metadati, codici a barre e tabelle da PDF, Word, Excel, email e oltre 50 altri formati di documento per applicazioni .NET, Java e Python."

############################# Header ############################
title: "SDK per l'analisi dei documenti"
description:  |
  SDK per l'analisi dei documenti, facile per gli sviluppatori, per estrarre testo, immagini, codici a barre, metadati e tabelle da oltre 50 formati di documenti e immagini.

  Integra l'analisi dei documenti ad alte prestazioni nelle tue applicazioni .NET, Java e Python con un minimo sforzo di codifica.

  Utilizza template flessibili e API avanzate per personalizzare le regole di parsing e fornire output di dati puliti e strutturati.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Scegli la tua piattaforma"
  title: "Indipendenza dalla piattaforma"
  description: "La libreria GroupDocs.Parser supporta i seguenti sistemi operativi e framework:"
  details_link_title: "Scopri di più"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser for .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    .NET Framework 4.6.2 or higher <br> .NET Core 2.0 or higher <br> .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    Microsoft Visual Studio <br> JetBrains Rider <br> Microsoft Visual Code
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser for Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Java 8 or higher <br> Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    IntelliJ IDEA <br> Eclipse <br> NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats


    # items loop
    - title: "Python"
      description: GroupDocs.Parser for Python
      color: "yellow"
      tag: "python-net"
      link: "/parser/python-net/"
      features_link: "https://docs.groupdocs.com/parser/python-net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Python 3.5+
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> macOS
      
          # features loop
          - rows: "4"
            content: |
                    PyCharm, VS Code, Jupyter Notebook
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats                    

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser in sintesi"
  description: "Potente SDK per l'analisi dei documenti per estrarre dati strutturati e non strutturati da PDF, documenti Office, immagini, email e archivi."

  items:
    # items loop
    - icon: "text"
      title: "Estrai testo"
      content: "Estrai informazioni testuali da vari formati di file"

    # items loop
    - icon: "image"
      title: "Estrai immagini"
      content: "Recupera contenuti visivi da diverse origini"

    # items loop
    - icon: "template"
      title: "Analizza dati tramite template"
      content: "Crea template personalizzati e usali per analizzare informazioni specifiche"

    # items loop
    - icon: "pdf"
      title: "Analizza i moduli PDF"
      content: "I moduli PDF sono documenti digitali con campi compilabili per l'interazione utente"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser esempi di codice"
  description: "Alcuni casi d'uso tipici delle operazioni di GroupDocs.Parser in C#, Java e Python"

  items:
    # items loop
    - title: "Come estrarre testo da documenti PDF"
      content: "L'API di GroupDocs.Parser semplifica l'estrazione del testo dai documenti mediante pochi passaggi."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // Crea un'istanza della classe Parser passando il file desiderato
                using (var parser = new Parser("source.pdf"))
                {
                    // Estrai il testo
                    using (var textReader = parser.GetText())
                    {
                        // Elabora il testo estratto
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // Crea un'istanza della classe Parser passando il file desiderato
                try (Parser parser = new Parser("source.pdf"))
                {
                    // Estrai il testo
                    try (TextReader reader = parser.getText())
                    {
                        // Elabora il testo estratto
                        System.out.println(reader == null 
                                ? "" 
                                : reader.readToEnd());
                    }
                }  
              ```
          # samples loop
          - language: "Python"
            color: "green"
            content: |
              ```python {style=abap}
                from groupdocs.parser import Parser

                # Crea un'istanza della classe Parser passando il file desiderato
                with Parser("source.pdf") as parser:
                    # Estrai il testo
                    text = parser.get_text()

                    # Elabora il testo estratto
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "Supportati oltre 50 formati di documenti e immagini"
  description: "GroupDocs.Parser Document Parser SDK consente operazioni di parsing su documenti Office, PDF, immagini, email, archivi e molto altro."

############################# Metrics ###############################
metrics:
  enable: true
  title: "Risultati di GroupDocs.Parser"
  description: "Scopri i principali indicatori dei risultati della nostra libreria"

  items:
    # items loop
    - number: "50+"
      title: "Formati supportati"
      content: "GroupDocs.Parser supporta operazioni con oltre 50 formati di file popolari."

    # items loop
    - number: "1600k"
      title: "Download NuGet"
      content: "Il pacchetto NuGet di GroupDocs.Parser per .NET è stato scaricato più di 1,600,000 volte."

    # items loop
    - number: "18k"
      title: "Download Maven"
      content: "GroupDocs.Parser ha 18,000 download su Maven. Funzionalità avanzate di parsing Java."

    # items loop
    - number: "140+"
      title: "Clienti soddisfatti"
      content: "Sia le aziende famose sia gli sviluppatori individuali preferiscono i prodotti GroupDocs per creare soluzioni innovative."


############################# Customers ###############################
customers:
  enable: true
  title: "I nostri clienti soddisfatti"
  description: "Le librerie GroupDocs sono utilizzate da marchi di fama mondiale e distinti in tutto il mondo."

  items:
    # items loop
    - title: "BenQ Corporation"
      logo: "benq"
      
    # items loop
    - title: "Nasdaq Stock Market"
      logo: "nasdaq"
      
    # items loop
    - title: "AT&T Inc."
      logo: "att"
      
    # items loop
    - title: "Customer logo AstraZeneca"
      logo: "astrazeneca"
      
    # items loop
    - title: "Central Bank of Argentina"
      logo: "argentinacentralbank"
      
    # items loop
    - title: "Roche Holding AG"
      logo: "roche"
      
    # items loop
    - title: "Capita"
      logo: "capita"
      
    # items loop
    - title: "Axa S.A."
      logo: "axa"
      
    # items loop
    - title: "Instructure Inc."
      logo: "instructure"
      
    # items loop
    - title: "Wipro"
      logo: "wipro"


############################# Actions ###############################
actions:
  enable: true
  title: "Pronto per iniziare?"
  description: "Prova le funzionalità di GroupDocs.Parser gratuitamente sulla tua piattaforma"

  items:
    # items loop
    - title: ".NET"
      color: "blue"
      link: "/parser/net/"

    # items loop
    - title: "Java"
      color: "red"
      link: "/parser/java/"

############################# FAQ ###############################
faq:
  enable: true
  title: "Domande frequenti"
  description: "Risposte alle domande più comuni."

  items:
    # items loop
    - question: "La libreria GroupDocs.Parser richiede altro software di terze parti per manipolare i documenti?"
      answer: "GroupDocs.Parser non richiede l'installazione di alcun software esterno, come Adobe Acrobat, Microsoft Office o altri."

    # items loop
    - question: "Posso provare la libreria GroupDocs.Parser prima di acquistarla?"
      answer: "Sì, puoi provare GroupDocs.Parser senza acquistare una licenza. Una volta installata senza licenza, la libreria funziona in modalità di prova. In questa modalità, i badge di prova vengono aggiunti al documento risultante e viene limitato alle prime 3 pagine. Se desideri testare GroupDocs.Parser senza le limitazioni della versione di prova, puoi anche richiedere una licenza temporanea di 30 giorni. Per ulteriori dettagli, [vedi](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "Quali licenze offrite?"
      answer: "Offriamo diversi tipi di licenza per soddisfare le esigenze di sviluppatori o aziende specifiche. I tipi di licenza dipendono dal numero di sviluppatori, dal numero di sedi dei siti di sviluppo e dal fatto se è necessario fornire il nostro SDK/API ai clienti finali. In alternativa, è possibile scegliere licenze a consumo basate sull'utilizzo mensile del prodotto. Scopri di più [qui](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser API di parsing documenti low‑code"
  description: "Incorpora le funzionalità di parsing dei documenti in qualsiasi applicazione utilizzando la nostra API REST e le SDK basate su cloud."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "comandi cURL per l'API Cloud di parsing documenti RESTful per analizzare documenti su un'ampia gamma di formati di file supportati e popolari."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Estrai immagini, testo, informazioni del documento o anche analizza qualsiasi documento con un modello definito dall'utente nelle tue applicazioni Microsoft .NET."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK Cloud per sviluppatori Java per analizzare documenti, estrarre informazioni e dati del documento all'interno di applicazioni basate su Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser Applicazioni No‑Code per il Parsing di Documenti"
  description: "Applicazioni web di parsing documenti che ti consentono di estrarre dati da oltre 50 formati di file popolari direttamente nel browser."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "App online gratuita per analizzare Word, Excel, PowerPoint, PDF e oltre 50 altri tipi di documento."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Analizza documenti Word direttamente dal browser per estrarre immagini, testo o metadati."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "App gratuita per il parsing di PDF che funziona su qualsiasi piattaforma o dispositivo senza limitazioni."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---