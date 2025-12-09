---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: id
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

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
head_title: "GroupDocs.Parser for Java Document Parser SDK untuk Java"
head_description: "SDK Document Parser berperforma tinggi untuk Java. Ekstrak teks, gambar, metadata, kode batang, tabel, dan data lainnya dari PDF, Word, Excel, email, dan lebih dari 50 format dokumen."

############################# Header ############################
title: "Document Parser SDK untuk Java"
description: "Tambahkan parsing dokumen yang cepat dan akurat ke aplikasi Java Anda serta ekstrak teks, gambar, metadata, dan data terstruktur dari dokumen dan gambar."
words:
  for: "untuk"

actions:
  main: "Maven Unduh"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Lisensi"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Siap memulai?"
  description: "Coba fitur GroupDocs.Parser secara gratis atau minta lisensi"

release:
  title: "Versi {0} dirilis"
  notes: "Lihat apa yang baru"
  downloads: "Unduhan"

code:
  title: "Segera Parse Konten Dokumen dengan SDK"
  more: "Contoh lain"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Berikan file sumber ke instance Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Berikan teks dokumen ke TextReader
        try (TextReader reader = parser.getText())
        {
            // Proses teks dokumen
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser sekilas"
  description: "Document Parser SDK untuk melakukan parsing dokumen dengan akurasi tinggi pada aplikasi Java"
  features:
    # feature loop
    - title: "Ekstrak data dari dokumen"
      content: "GroupDocs.Parser for Java API memungkinkan Anda mengambil teks, metadata, dan gambar dari berbagai format file seperti dokumen Office, email, lampiran, dan arsip. Alat yang kuat ini membantu Anda mengakses dan memproses informasi berharga yang terdapat dalam file-file tersebut secara efisien untuk berbagai aplikasi seperti analisis data, pengindeksan mesin pencari, atau sistem manajemen konten."

    # feature loop
    - title: "Menganalisis dokumen"
      content: "Ekstrak berbagai elemen seperti hyperlink, tabel, kode QR, barcode, dan data dari formulir PDF. Juga mengurai informasi apa pun yang diinginkan dari dokumen menggunakan templat khusus."

    # feature loop
    - title: "Menyesuaikan hasil"
      content: "Java API memungkinkan Anda mengambil data dalam berbagai format seperti mentah, terstruktur, HTML, atau Markdown. Selain itu, API menyediakan fungsi pencarian untuk menemukan kata atau frasa tertentu dalam teks dokumen."

############################# Platforms ############################
platforms:
  enable: true
  title: "Kemandirian Platform"
  description: "GroupDocs.Parser for Java mendukung sistem operasi, kerangka kerja, dan manajer paket berikut"
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
    GroupDocs.Parser for Java mendukung operasi dengan [format file](https://docs.groupdocs.com/parser/java/supported-document-formats/) berikut.
  groups:
    # group loop
    - color: "green"
      content: |
        ### Format Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### Gambar & Format Lain
        * **Portable:** PDF 
        * **Gambar:** JPG, BMP, PNG, TIFF, GIF
        * **Format Office lainnya:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Format lain
        * **Web:** HTML, MHTML 
        * **Arsip:** ZIP, TAR, 7Z 
        * **e-Book:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "Fitur GroupDocs.Parser for Java"
  description: "Ekstrak data dari PDF, dokumen Office, gambar, dan format lain secara cepat dan akurat dengan Java Document Parser SDK kami."

  items:
    # feature loop
    - icon: "text"
      title: "Ekstrak teks"
      content: "Ekstrak informasi teks dari berbagai format file seperti dokumen Office, file PDF, dan gambar untuk memudahkan pembacaan dan analisis."

    # feature loop
    - icon: "image"
      title: "Ekstrak gambar"
      content: "Ambil konten visual dari berbagai sumber seperti dokumen Office, file PDF untuk akses dan penggunaan yang mudah."

    # feature loop
    - icon: "qr"
      title: "Pindai Kode QR"
      content: "Deteksi dan dekode kode QR yang terdapat dalam dokumen Office, file PDF, atau konten visual untuk pengambilan informasi yang efisien."

    # feature loop
    - icon: "email"
      title: "Ekstrak data dari lampiran email dan arsip"
      content: "Kumpulkan informasi berharga dari pesan email, lampiran file, dan sumber data terkompresi untuk analisis dan pemanfaatan yang efektif."

    # feature loop
    - icon: "table"
      title: "Ekstrak tabel"
      content: "Identifikasi dan ekstrak data tabular dari dokumen PDF untuk analisis dan penggunaan yang terstruktur."

    # feature loop
    - icon: "hyperlink"
      title: "Ekstrak hyperlink"
      content: "Temukan dan ekstrak hyperlink serta alamat email dalam dokumen Office atau file PDF untuk akses yang efisien."

    # feature loop
    - icon: "pdf"
      title: "Mengurai Formulir PDF"
      content: "Formulir PDF adalah dokumen digital dengan bidang yang dapat diisi untuk interaksi pengguna, memungkinkan mereka memasukkan informasi secara elektronik. API .NET dapat digunakan untuk mengekstrak data dari formulir ini untuk pemrosesan yang efisien."

    # feature loop
    - icon: "template"
      title: "Mengurai data dengan templat"
      content: "Buat templat khusus dan gunakan bersama API .NET untuk mengurai informasi spesifik dari file PDF, menyederhanakan proses ekstraksi data."

    # feature loop
    - icon: "search"
      title: "Cari teks dalam dokumen"
      content: "Temukan dengan cepat kata atau pola tertentu dalam dokumen."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Contoh kode"
  description: "Beberapa contoh penggunaan operasi GroupDocs.Parser for Java yang umum"
  items:
    # code sample loop
    - title: "Ekstrak gambar dari dokumen PDF"
      content: |
        GroupDocs.Parser for Java memudahkan pengembang Java untuk mengekstrak gambar dari [dokumen](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Ekstrak gambar dari dokumen PDF dalam Java">}}
        ```java {style=abap}
        // Buat instance kelas Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Ekstrak gambar
            Iterable<PageImageArea> images = parser.getImages();

            // Periksa apakah sesuatu telah diekstrak
            if (images == null) {
                return;
            }

            // Iterasi gambar
            for (PageImageArea image : images) {
                // Cetak indeks halaman, persegi panjang, dan tipe gambar
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Ekstrak barcode dari gambar"
      content: |
        Gunakan API Java kami untuk mengekstrak [barcode](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) dari gambar:
        {{< landing/code title="Ekstrak kode batang dari gambar dalam Java">}}
        ```java {style=abap}   
        // Muat gambar sumber ke Parser
        try (Parser parser = new Parser("source.jpg")){

            // Periksa apakah file mendukung ekstraksi kode batang
            if (!parser.getFeatures().isBarcodes()) {

                // Ekstrak kode batang dari file
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Iterasi kode batang
                for (PageBarcodeArea barcode : barcodes) {
                    // Cetak indeks halaman
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // Cetak nilai kode batang
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
