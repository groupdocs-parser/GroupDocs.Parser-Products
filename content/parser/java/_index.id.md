---
############################# Static ############################
layout: "landing"
date: 2024-02-13T17:01:03
draft: false
#operation: 
#parsertype: 
#fileformat: 
#productName: Java
lang: "id"
#productCode: java
#otherformats: 
#breadcrumb: Put  parser on  for Java
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: ".NET, Java, Cloud API & Aplikasi Parser Dokumen Online"
head_description: "Dapatkan solusi penguraian dokumen lengkap untuk .NET, Java dan aplikasi berbasis cloud. Ekstrak data dari format dokumen online menggunakan fitur drag and drop sederhana"

############################# Header ############################
title: "Parsing dokumen<br>melalui Java API"
description: "Ekstrak data dari dokumen dan gambar pada platform apa pun menggunakan API fleksibel dan solusi berbasis aplikasi kami untuk pemrogram dan pengguna akhir."
words:
  for: "untuk"

actions:
  main: "Unduhan Maven Gratis"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Perizinan"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java"
  title: "Siap untuk memulai?"
  description: "Coba fitur GroupDocs.Parser secara gratis atau minta lisensi"

release:
  title: "Versi {0} dirilis"
  notes: "Lihat apa yang baru"
  downloads: "Unduhan"

code:
  title: "Ekstrak teks dari file PDF di Java"
  more: "Lebih banyak contoh"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
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
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser Ikhtisar"
  description: "API untuk melakukan penguraian dokumen di Java aplikasi"
  features:
    # feature loop
    - title: "Ekstrak data dari dokumen"
      content: "Java API memungkinkan Anda mengambil teks, metadata, dan gambar dari berbagai format file seperti dokumen Office, email, lampiran, dan arsip. Alat canggih ini membantu Anda mengakses dan memproses informasi berharga secara efisien yang terkandung dalam file ini untuk berbagai aplikasi seperti analisis data, pengindeksan mesin pencari, atau sistem manajemen konten."

    # feature loop
    - title: "Parsing dokumen"
      content: "Ekstrak berbagai elemen seperti hyperlink, tabel, kode QR, kode batang, dan data dari formulir PDF. Parsing juga informasi yang diinginkan dari dokumen menggunakan templat khusus."

    # feature loop
    - title: "Menyesuaikan hasil"
      content: "Java API memungkinkan Anda mengambil data dalam berbagai format seperti mentah, terstruktur, HTML, atau Penurunan harga. Selain itu, API menawarkan fungsi pencarian untuk menemukan kata atau frasa tertentu dalam teks dokumen."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independensi platform"
  description: "GroupDocs.Parser for Java mendukung sistem operasi, kerangka kerja, dan pengelola paket berikut"
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
    - title: "Eclipse"
      image: "eclipse"
    # platform loop
    - title: "IntelliJ"
      image: "intellij"
    # platform loop
    - title: "Windows"
      image: "windows"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "Maven"
      image: "maven"

############################# File formats ############################
formats:
  enable: true
  title: "Format file yang didukung"
  description: |
    GroupDocs.Parser for Java mendukung operasi dengan [format file] berikut(https://docs.groupdocs.com/parser/java/supported-document-formats/).
  groups:
    # group loop
    - color: "green"
      content: |
        ### Microsoft Office format
        * **Word:**  DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Gambar & Format Lainnya
        * **Portable:** PDF
        * **Gambar-gambar:** JPG, BMP, PNG, TIFF, GIF, DICOM, WEBP
        * **Format kantor lainnya:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Format lainnya
        * **jaring:** HTML, MHTML
        * **Arsip:** ZIP, TAR, 7Z
        * **Ebook:** CHM, EPUB, FB2, MOBI

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser fitur"
  description: "Ekstrak data dari PDF, Dokumen Office, dan Gambar dengan cepat dan akurat."

  items:
    # feature loop
    - icon: "text"
      title: "Ekstrak teks"
      content: "Ekstrak informasi tekstual dari berbagai format file seperti dokumen office, file, dan gambar agar mudah dibaca dan dianalisis."

    # feature loop
    - icon: "image"
      title: "Ekstrak gambar"
      content: "Ambil konten visual dari beragam sumber seperti dokumen kantor, file PDF untuk kemudahan akses dan penggunaan."

    # feature loop
    - icon: "qr"
      title: "Pindai Kode QR"
      content: "Deteksi dan dekode kode QR yang ada dalam dokumen kantor, file PDF, atau konten visual untuk pengambilan informasi yang efisien."

    # feature loop
    - icon: "email"
      title: "Ekstrak data dari lampiran dan arsip email"
      content: "Kumpulkan informasi berharga dari pesan email, lampiran file, dan sumber data terkompresi untuk analisis dan pemanfaatan yang efektif."

    # feature loop
    - icon: "table"
      title: "Ekstrak tabel"
      content: "Identifikasi dan ekstrak data tabel dari PDF dokumen untuk analisis dan penggunaan yang terorganisir."

    # feature loop
    - icon: "hyperlink"
      title: "Ekstrak hyperlink"
      content: "Temukan dan ekstrak hyperlink dan alamat email dalam dokumen atau file Office untuk akses yang efisien."

    # feature loop
    - icon: "pdf"
      title: "Parsing PDF Formulir"
      content: "PDF Formulir adalah dokumen digital yang menampilkan kolom yang dapat diisi untuk interaksi pengguna, sehingga memungkinkan mereka memasukkan informasi secara elektronik. Java API dapat digunakan untuk mengekstrak data dari formulir ini untuk pemrosesan yang efisien."

    # feature loop
    - icon: "template"
      title: "Parsing data berdasarkan templat"
      content: "Buat template khusus dan gunakan dengan Java API untuk mengurai informasi spesifik dari file PDF, sehingga menyederhanakan proses ekstraksi data."

    # feature loop
    - icon: "search"
      title: "Cari teks dalam dokumen"
      content: "Temukan kata atau pola tertentu dalam dokumen dengan cepat."

############################# Code samples ############################
code_samples:
  enable: true
  title: "Contoh kode"
  description: "Beberapa kasus penggunaan operasi umum"
  items:
    # code sample loop
    - title: "Ekstrak gambar dari PDF dokumen"
      content: |
        Java API memudahkan Java pengembang mengekstrak gambar dari dokumen dengan menerapkan beberapa langkah mudah.
        {{< landing/code title="Ekstrak gambar dari PDF dokumen di Java">}}
        ```java {style=abap}
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // Extract images
            Iterable<PageImageArea> images = parser.getImages();
            // Check if images extraction is supported
            if (images != null) {
                int imageIndex = 0;
                // Iterate over images
                for (PageImageArea image : images) {
                    // Save the image to the file
                    image.save(String.format("%s%s", imageIndex, image.getFileType().getExtension()));
                }
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Ekstrak kode batang dari gambar"
      content: |
        Java API memudahkan Java pengembang mengekstrak kode batang dari dokumen dengan menerapkan beberapa langkah mudah.
        {{< landing/code title="Ekstrak kode batang dari gambar">}}
        ```java {style=abap}   
        // Create an instance of Parser class
        try (Parser parser = new Parser(fileName)) {
            // // Check if the file supports barcode extracting
            if (!parser.getFeatures().isBarcodes()) {
                // Extract barcodes from the file.
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();
                // Iterate over barcodes
                for (PageBarcodeArea barcode : barcodes) {
                    // Print the page index
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Print the barcode value
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
