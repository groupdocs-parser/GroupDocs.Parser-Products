---
############################# Static ############################
layout: "family"
date:  2025-06-26T17:35:47
draft: false

product: "Parser"
product_tag: "parser"

lang: en

############################# Head ############################
head_title: ".NET, Java, Cloud APIs & Online Document Parser Apps"
head_description: "Get all-in-one document parsing solution for .NET, Java and cloud-based applications. Extract data from document formats online using simple drag and drop feature"

############################# Header ############################
title: "Document Parsing Solution"
description:  |
  Robust API for data extraction from various file formats.

  Parse documents with minimal coding effort.

  Customize parsing results.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Choose your platform"
  title: "Platform Independence"
  description: "GroupDocs.Parser library supports the following operating systems and frameworks:"
  details_link_title: "Learn more"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser .NET 
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
      description: GroupDocs.Parser Java
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

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser at a glance"
  description: "API for data parsing across PDF, Word, Excel and more"

  items:
    # items loop
    - icon: "text"
      title: "Extract text"
      content: "Extract textual information from various file formats"

    # items loop
    - icon: "image"
      title: "Extract images"
      content: "Retrieve visual content from diverse sources"

    # items loop
    - icon: "template"
      title: "Parse data by templates"
      content: "Create custom templates and utilize them to parse specific information"

    # items loop
    - icon: "pdf"
      title: "Parse PDF Forms"
      content: "PDF Forms are digital documents featuring fillable fields for user interaction"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser code samples"
  description: "Some use cases of typical GroupDocs.Parser operations in C# and Java"

  items:
    # items loop
    - title: "How to extract text from PDF documents"
      content: "GroupDocs.Parser API makes it easy to extract text from documents by implementing a few steps."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
                    <code class="language-csharp" data-lang="csharp">

                        // Create an instance of Parser class passing desired file
                        using (var parser = new Parser("source.pdf"))
                        {
                            // Extract a text to {{textReader}}
                            using (var textReader = parser.GetText())
                            {
                                // Process the extracted text
                                Console.WriteLine(textReader?.ReadToEnd());
                            }
                        }     
                        
                    </code>

          # samples loop
          - language: "Java"
            color: "red"
            content: |
                    <code class="language-java" data-lang="java">

                        // Create an instance of Parser class passing desired file
                        try (Parser parser = new Parser("source.pdf"))
                        {
                            // Extract a text to {{textReader}}
                            try (TextReader reader = parser.getText())
                            {
                                // Process the extracted text
                                System.out.println(reader == null 
                                        ? "" 
                                        : reader.readToEnd());
                            }
                        }  

                    </code>


############################# Supported Formats ###############################
formats:
  enable: true
  title: "50+ file formats supported"
  description: "GroupDocs.Parser enables parser operations within various format families"

############################# Metrics ###############################
metrics:
  enable: true
  title: "GroupDocs.Parser achievements"
  description: "Discover the Key Metrics of Our Library's Accomplishments"

  items:
    # items loop
    - number: "50+"
      title: "Supported formats"
      content: "GroupDocs.Parser supports operations with more than 50 popular file formats."

    # items loop
    - number: "1600k"
      title: "NuGet downloads"
      content: "GroupDocs.Parser for .NET NuGet package was downloaded more than 1,600,000 times."

    # items loop
    - number: "18k"
      title: "Maven downloads"
      content: "GroupDocs.Parser has 18,000 downloads on Maven. Powerful Java Parsing Features."

    # items loop
    - number: "140+"
      title: "Happy customers"
      content: "As famous companies as individual developers prefer GroupDocs products to build innovative solutions."


############################# Customers ###############################
customers:
  enable: true
  title: "Our happy customers"
  description: "GroupDocs libraries are employed by globally renowned and distinguished brands across the world."

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
  title: "Ready to get started?"
  description: "Try GroupDocs.Parser features for free on your platform"

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
  title: "Frequently asked questions"
  description: "Answers to most commonly asked questions."

  items:
    # items loop
    - question: "Does GroupDocs.Parser library need any other third-party software to manipulate documents?"
      answer: "GroupDocs.Parser does not require any external software to be installed such as Adobe Acrobat, Microsoft Office, or any other."

    # items loop
    - question: "Can I try the GroupDocs.Parser library before purchasing it?"
      answer: "Yes, you can try GroupDocs.Parser without buying a license. Once installed without a license, the library works in trial mode. In this mode, trial badges are added to the resultant document, and it is trimmed to the first 3 pages. If you wish to test GroupDocs.Parser without the limitations of the trial version, you can also request a 30-day temporary license. For more details, [see](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "What licenses do you have?"
      answer: "We offer several license types to fit the needs of particular developers or companies. License types depend on the number of developers, the number of developer site locations, and whether you need to deliver our SDK/API to your end customers. Alternatively, you can choose Metered licenses based on monthly usage of the product. Learn more [here](https://purchase.groupdocs.com/pricing/parser/net/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser low code APIs"
  description: "Incorporate document parser capabilities into any application using our cloud-based REST API"
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "cURL commands for RESTful document parser Cloud API to parse documents across wide range of supported popular file formats."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Extract images, text, document information or even parse any document by user-defined template in your Microsoft .NET applications."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Cloud SDK for Java developers to parse documents, extract document information and data within Java based applications."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser No Code Apps"
  description: "Web-based application that enables you to perform parse across more than 50 popular file formats directly in your browser. "

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Free online app to parse Word, Excel, PowerPoint, PDF & 50+ more document types."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Parse Word documents directly from your web browser to extract images, text or metadata."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Free PDF parsing app that works on any platform or device without any limitations."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---