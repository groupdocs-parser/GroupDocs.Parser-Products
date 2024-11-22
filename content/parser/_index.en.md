---
############################# Static ############################
layout: "family"
date:  2024-02-13T17:01:03
draft: false

product: "Parser"
product_tag: "parser"

lang: en

############################# Head ############################
head_title: ".NET, Java, Cloud APIs & Online Document Parser Apps"
head_description: "Get all-in-one document parsing solution for .NET, Java and cloud-based applications. Extract data from document formats online using simple drag and drop feature"

############################# Header ############################
title: "Document Parsing Solution"
description: |
  Robust API for data extraction from various file formats.

  Parse documents with minimal coding effort.

  Customize parsing results.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Choose your platform"
  title: "Platform independence"
  description: "GroupDocs.Parser library supports the following operating systems and frameworks:"
  details_link_title: "Learn more"

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
          - rows: "4"
            content: |
                    .NET Framework 4.6.2 or higher
                    .NET Core 2.0 or higher
                    .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    Microsoft Visual Studio
                    JetBrains Rider
      
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
          - rows: "4"
            content: |
                    Java 8 or higher
                    Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    IntelliJ IDEA
                    Eclipse
                    NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser at a glance"
  description: "API for data parsing across PDF, Word, Excel and more."

  items:
    # items loop
    - icon: "text"
      title: "Extract text"
      content: "Extract textual information from various file formats."

    # items loop
    - icon: "image"
      title: "Extract images"
      content: "Retrieve visual content from diverse sources."

    # items loop
    - icon: "template"
      title: "Parse data by templates"
      content: "Create custom templates and utilize them to parse specific information."

    # items loop
    - icon: "pdf"
      title: "Parse PDF Forms"
      content: "PDF Forms are digital documents featuring fillable fields for user interaction."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser code samples"
  description: "Some use cases of typical GroupDocs.Parser operations in C# and Java."

  items:
    # items loop
    - title: "How to extract text from PDF documents"
      content: "GroupDocs.Parser API makes it easy for C# developers to extract text from documents by implementing a few easy steps."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              <pre>
              // Create an instance of Parser class
              using (var parser = new Parser(fileName))
              {
                  // Extract a text into the reader
                  using (var textReader = parser.GetText())
                  {
                      // Print a text from the document
                      Console.WriteLine(textReader?.ReadToEnd());
                  }
              }
              </pre>
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              <pre>
              // Create an instance of Parser class
              try (Parser parser = new Parser(fileName)) {
                  // Extract a text into the reader
                  try (TextReader reader = parser.getText()) {
                      // Print a text from the document
                      System.out.println(reader == null 
                              ? "" 
                              : reader.readToEnd());
                  }
              }
              <pre>

############################# Supported Formats ###############################
formats:
  enable: true
  title: "50+ file formats supported"
  description: "GroupDocs.Parser enables parser operations within various format families."

############################# Metrics ###############################
metrics:
  enable: false
  title: "Detailed metrics and statistical insights"
  description: "Explore a thorough analysis of our key figures, offering comprehensive metrics and statistical insights into our accomplishments, influence, and expansion."

  items:
    # items loop
    - number: "50+"
      title: "Supported formats"
      content: "The API accommodates more than 50 of the most widely used file and document formats."

    # items loop
    - number: "700k"
      title: "NuGet downloads"
      content: "GroupDocs.Parser for .NET has received over 800K downloads through the NuGet package manager."

    # items loop
    - number: "15k"
      title: "Maven downloads"
      content: "GroupDocs.Parser for Java has accumulated over 15K downloads from our Maven repository."


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
    - question: "Does the GroupDocs.Parser library need any other third-party software to manipulate documents?"
      answer: "GroupDocs.Parser does not require any external software to be installed such as Adobe Acrobat, Microsoft Office, or any other."

    # items loop
    - question: "Can I try the GroupDocs.Parser library before purchasing it?"
      answer: "Yes, you can try GroupDocs.Parser without buying a license. Once installed without a license, the library works in trial mode. In this mode, trial badges are added to the resultant document, and it is trimmed to the first 3 pages. If you wish to test GroupDocs.Parser without the limitations of the trial version, you can also request a 30-day temporary license. For more details, see [purchase.groupdocs.com/temporary-license/](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "What licenses do you have?"
      answer: "We offer several license types to fit the needs of particular developers or companies. License types depend on the number of developers, the number of developer site locations, and whether you need to deliver our SDK/API to your end customers. Alternatively, you can choose Metered licenses based on monthly usage of the product. Learn more at [purchase.groupdocs.com/policies/](https://purchase.groupdocs.com/policies/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser low code APIs"
  description: "Incorporate document parser capabilities into any application using our cloud-based REST API."
  
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
  title: "GroupDocs.Parser NoCode apps"
  description: "Web-based application that enables you to perform parse across more than 50 popular file formats directly in your browser."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Free online app to parse Word, Excel, PowerPoint, PDF & 30+ more document types."
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