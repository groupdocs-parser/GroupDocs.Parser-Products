---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
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

############################# Head ############################
head_title: "Aplikasi Penguraian Dokumen GroupDocs.Parser for Java"
head_description: "Dapatkan solusi penguraian dokumen serba ada untuk aplikasi Java. Ekstrak data dari format dokumen secara online menggunakan fitur drag and drop sederhana."

############################# Header ############################
title: "Uraikan dokumen melalui API Java"
description: "Ekstrak data dari dokumen dan gambar di mana saja menggunakan API yang fleksibel dan solusi berbasis aplikasi kami untuk programmer dan pengguna akhir."
words:
  for: "untuk"

actions:
  main: "Unduh Maven"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "Lisensi"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "Siap untuk memulai?"
  description: "Coba fitur GroupDocs.Parser secara gratis atau minta lisensi"

release:
  title: "Versi {0} dirilis"
  notes: "Lihat apa yang baru"
  downloads: "Unduhan"

code:
  title: "Dengan Cepat Dapatkan Konten Dokumen"
  more: "Lebih banyak contoh"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // Kirim file sumber ke instance Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // Kirim teks dokumen ke TextReader
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
  description: "API untuk melakukan penguraian dokumen dalam aplikasi Java"
  features:
    # feature loop
    - title: "Ekstrak data dari dokumen"
      content: "GroupDocs.Parser for Java API memungkinkan Anda untuk mengambil teks, metadata, dan gambar dari berbagai format file seperti dokumen Office, email, lampiran, dan arsip. Alat yang kuat ini membantu Anda dengan efisien mengakses dan memproses informasi berharga yang terkandung dalam file ini untuk berbagai aplikasi seperti analisis data, pengindeksan mesin pencari, atau sistem manajemen konten."

    # feature loop
    - title: "Uraikan dokumen"
      content: "Ekstrak berbagai elemen seperti hyperlink, tabel, kode QR, kode batang dan data dari formulir PDF. Juga uraikan informasi yang diinginkan dari dokumen menggunakan template kustom."

    # feature loop
    - title: "Kustomisasi hasil"
      content: "Java API memungkinkan Anda untuk mengambil data dalam berbagai format seperti mentah, terstruktur, HTML, atau Markdown. Selain itu, API menawarkan fungsi pencarian untuk menemukan kata atau frasa tertentu dalam teks dokumen."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independensi Platform"
  description: "GroupDocs.Parser for Java mendukung sistem operasi, framework dan pengelola paket berikut."
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
        ### Gambar & Format Lainnya
        * **Portabel:** PDF 
        * **Gambar:** JPG, BMP, PNG, TIFF, GIF
        * **Format kantor lainnya:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### Format Lainnya
        * **Web:** HTML, MHTML 
        * **Arsip:** ZIP, TAR, 7Z 
        * **e-Book:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "Fitur GroupDocs.Parser for Java"
  description: "Ekstrak data dari PDF, Dokumen Office, dan Gambar dengan cepat dan akurat"

  items:
    # feature loop
    - icon: "text"
      title: "Ekstrak teks"
      content: "Ekstrak informasi tekstual dari berbagai format file seperti dokumen office, file PDF, dan gambar untuk keterbacaan dan analisis yang mudah."

    # feature loop
    - icon: "image"
      title: "Ekstrak gambar"
      content: "Dapatkan konten visual dari berbagai sumber seperti dokumen office, file PDF untuk akses dan penggunaan yang nyaman."

    # feature loop
    - icon: "qr"
      title: "Pindai Kode QR"
      content: "Deteksi dan dekode kode QR yang terdapat dalam dokumen kantor, file PDF, atau konten visual untuk pengambilan informasi yang efisien."

    # feature loop
    - icon: "email"
      title: "Ekstrak data dari lampiran email dan arsip"
      content: "Kumpulkan informasi berharga dari pesan email, lampiran file, dan sumber data terkompresi untuk analisis dan pemanfaatan yang efektif."

    # feature loop
    - icon: "table"
      title: "Ekstrak tabel"
      content: "Identifikasi dan ekstrak data tabel dari dokumen PDF untuk analisis dan penggunaan yang terorganisir."

    # feature loop
    - icon: "hyperlink"
      title: "Ekstrak hyperlink"
      content: "Temukan dan ekstrak hyperlink serta alamat email dalam dokumen office atau file PDF untuk akses yang efisien."

    # feature loop
    - icon: "pdf"
      title: "Parse Formulir PDF"
      content: "Formulir PDF adalah dokumen digital yang memiliki bidang isian untuk interaksi pengguna, memungkinkan mereka untuk memasukkan informasi secara elektronik. API .NET dapat digunakan untuk mengekstrak data dari formulir ini untuk pemrosesan yang efisien."

    # feature loop
    - icon: "template"
      title: "Parse data dengan template"
      content: "Buat template kustom dan gunakan dengan API .NET untuk menguraikan informasi spesifik dari file PDF, menyederhanakan proses ekstraksi data."

    # feature loop
    - icon: "search"
      title: "Cari teks dalam dokumen"
      content: "Dengan cepat locasikan kata atau pola tertentu dalam dokumen."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Contoh kode"
  description: "Beberapa kasus penggunaan operasi GroupDocs.Parser for Java yang khas"
  items:
    # code sample loop
    - title: "Ekstrak gambar dari dokumen PDF"
      content: |
        GroupDocs.Parser for Java memudahkan pengembang Java untuk mengekstrak gambar dari [dokumen](https://docs.groupdocs.com/parser/java/extract-images-from-documents/):
        {{< landing/code title="Ekstrak gambar dari dokumen PDF di Java">}}
        ```java {style=abap}
        // Buat instance dari kelas Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // Ekstrak gambar
            Iterable<PageImageArea> images = parser.getImages();

            // Periksa apakah ada yang diekstrak
            if (images == null) {
                return;
            }

            // Iterasi melalui gambar
            for (PageImageArea image : images) {
                // Cetak indeks halaman, kotak pembatas, dan jenis gambar
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Ekstrak kode batang dari gambar"
      content: |
        Gunakan API Java kami untuk mengekstrak [kode batang](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) dari gambar:
        {{< landing/code title="Ekstrak kode batang dari gambar di Java">}}
        ```java {style=abap}   
        // Muat gambar sumber ke Parser
        try (Parser parser = new Parser("source.jpg")){

            // Periksa apakah file mendukung ekstraksi kode batang
            if (!parser.getFeatures().isBarcodes()) {

                // Ekstrak kode batang dari file
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // Iterasi melalui kode batang
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
