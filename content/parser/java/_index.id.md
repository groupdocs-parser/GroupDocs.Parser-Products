---
layout: "product"
date: 2022-07-07T12:44:18+03:00
draft: false

product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

head_title: "Java API untuk Mengurai Teks, Gambar & Metadata dari PDF Word Excel HTML"
head_description: "API pengurai dokumen Java untuk mengekstrak teks, gambar, metadata & penyandian dari database, Word, Excel, presentasi, PDF, email, EPUB, dan file ZIP."

title: "Java Parser API untuk Mengekstrak Data"
description: "Java API untuk mengurai & mengekstrak gambar dan teks dengan metadata dari dokumen, presentasi, arsip & email."
button:
    enable: true

submenu:
    enable: true
    
    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:
            - link: "#overview"
              text: "Ringkasan"

            - link: "#features"
              text: "Fitur"

            - link: "#support"
              text: "Mendukung"

            - link: "https://products.groupdocs.app/parser"
              text: "Demo Langsung"

            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Harga"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java/"
        link_buy: "https://purchase.groupdocs.com"

overview:
    enable: true
    content: |
      GroupDocs.Parser untuk Java adalah API ekstraktor teks, gambar, dan metadata, mendukung lebih dari 50 jenis dokumen populer untuk membantu membangun aplikasi bisnis dengan fitur penguraian teks mentah, terstruktur & terformat. Ini juga mendukung penguraian dokumen menggunakan templat yang telah ditentukan sebelumnya dan memungkinkan penggalian data kompleks dari faktur dan dokumen tipikal lainnya dengan kecepatan dan akurasi. GroupDocs.Parser untuk Java memungkinkan Anda mengekstrak teks dan metadata dari file yang dilindungi kata sandi dari semua format populer termasuk dokumen pemrosesan Word, spreadsheet Excel, presentasi PowerPoint, OneNote, file PDF, dan arsip ZIP.
    tabs:
      enable: true     
      
      tab_one:
        description: |
          Berikut ini adalah ikhtisar GroupDocs.Parser untuk Java:

        left:
          enable: true
          icon: "fas fa-tools"
          title: "Fitur"
          content: |
            * Ekstrak Gambar
            * Ekstrak Teks Mentah
            * Ekstrak Teks Terformat
            * Ekstrak Teks Terstruktur
            * Ekstrak Metadata
            * Ekstrak dari File dalam file ZIP
            * Ekstrak dengan Mencari
            * Ekstrak dengan Pemformat Teks
            * Deteksi Standar Pengkodean
            * Deteksi Jenis Media
        
        right:
          enable: true
          icon: "fab fa-html5"
          title: "API"
          content: |
            * Mendapat File Masukan
            * Mengambil Teks Mentah atau Terformat
            * Mengambil Metadata
      
      tab_two:
        description: |
          GroupDocs.Parser untuk Java mendukung [format file dokumen](https://docs.groupdocs.com/parser/java/supported-document-formats/ berikut):

        left:
          enable: true
          table:
            - title: "Ekstraksi Teks"
              content: |
                * **Teks**: DOC, DOCX, DOT, DOTM, DOTX, DOCM, RTF, ODT, OTT, TXT, MD, WordprocessingML (XML)
                * **Spreadsheet**: XLS, XLSX, CSV, XLSM, XLSB, ODS, SpreadsheetML (XML), XLT, XLTX, XLTM, OTS, XLA,, XLAM, TSV
                * **Presentasi**: PPT, PPTX, PPTM, PPS, PPSX, PPSM, POT, POTX, POTM, ODP, OTP
                * **OneNote**: SATU
                * **Email**: MSG, EML, EMLX, PST, OST, MS EXCHANGE SERVER, POP, IMAP
                * **Penerbitan Elektronik**: EPUB, FB2
                * **Dokumen Portabel**: PDF, Portofolio PDF, PDF Terenkripsi
                * **Berbasis DOM**: XML, HTML, XHTML, MHTML
                * **Kompresi & Kemasan**: ZIP, CHM
                * **Database**: ADO.NET

            - title: "Deteksi Pengkodean"
              content: |
                * **BOM**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, dan UTF7
                * **Konten**: UTF32 LE, UTF32 BE, UTF16 LE, UTF16 BE, UTF8, dan ANSI

        right:
          enable: true
          table:
            - title: "Ekstraksi Metadata"
              content: |
                * **Teks**: DOC, DOCX, DOT, DOTX, DOTM, OTT, ODT
                * **Spreadsheet**: XLS, XLSX, XLT, XLTX, XLTM, XLA, XLAM, OTS, ODS
                * **Presentasi**: PPT, PPTX, POT, POTX, POTM, PPSM, PPTM, OTP, ODP
                * **Email**: MSG, EML, EMLX
                * **Penerbitan Elektronik**: EPUB, FB2
                * **Lainnya**: PDF

            - title: "Ekstraksi Teks & Metadata"
              content: |
                * **Templat**: DOTX, POTX
                * **Template Berkemampuan Makro**: DOTM, POTM, PPSM, PPTM
                * **Template OpenDocument**: OTT

            - title: "Ekstraksi Gambar"
              content: |
                * **Teks**: DOC, DOCX, DOCM, RTF, DOT, DOTM, DOTX, ODT
                * **Spreadsheet**: XLS, XLSX, XLSM, XLSB, ODS, XLT, XLTM, XLTX
                * **Presentasi**: PPT, PPTX, PPTM, ODP, POT, POTM, POTX, PPS, PPSX, PPSM
                * **Dokumen Portabel**: PDF, POT, POTM, POTX
                * **Ebook**: CHM, EPUB, FB2
                * **Markup**: HTML

      tab_three:
        description: |
          GroupDocs.Parser untuk Java mendukung Sistem Operasi, Kerangka Kerja & Manajer Paket berikut:
        
        left:
          enable: true
          table:
            - icon: "fab fa-windows"
              title: "Sistem operasi"
              content: |
                * Microsoft Windows Desktop
                * Microsoft Windows Server
                * Linux
                * MacOS

            - icon: "fas fa-code"
              title: "Kerangka yang Didukung"
              content: |
                * Java 7 (1.7) ke atas

        right:
          enable: true
          table:
            - icon: "fas fa-cogs"
              title: "Lingkungan Pengembangan"
              content: |
                * NetBeans
                * IntelliJ IDEA
                * Eclipse
            - icon: "fas fa-tools"
              title: "Bangun Alat Otomatisasi"
              content: |
                * Maven

features:
    enable: true
    title: "GroupDocs.Parser untuk Fitur Java"

    feature:
      - icon: "fas fa-copy"
        content: "Hitung Kemunculan Kata untuk Satu atau Beberapa Dokumen Secara Statistik"

      - icon: "fas fa-eye"
        content: "Ekstrak Teks dan Metadata dari Excel Spreadsheets dan PowerPoint Presentation Templates"

      - icon: "fas fa-bolt"
        content: "Ambil Teks dari File atau Aliran, Tanpa Menginstal Pembaca Dokumen"
      
      - icon: "fas fa-file-powerpoint"
        content: "Tarik Teks Terformat dari Dokumen Menggunakan Mode Ekstraksi Teks Cepat atau Standar"

      - icon: "fas fa-code"
        content: "Deteksi Jenis Media Dokumen XML yang Dilindungi Kata Sandi & Ekstrak Teks dari Mereka"

      - icon: "fas fa-cloud"
        content: "Ambil Teks Terformat dari Presentasi PowerPoint, Email & Lampiran Secara Terprogram"

      - icon: "fas fa-remove-format"
        content: "Keluarkan Teks dari Satu atau Beberapa Halaman Dokumen OneNote"

      - icon: "fas fa-comment-slash"
        content: "Tarik Teks Mentah dari File PDF Sederhana atau Dokumen Portofolio PDF"

      - icon: "fas fa-location-arrow"
        content: "Ekstrak Data dari PDF, MS Word, Excel dan Dokumen Presentasi"

      - icon: "fas fa-border-all"
        content: "Ekstrak Teks Mentah atau Diformat dari Sel, Baris Dan Kolom dari Excel Spreadsheet"

      - icon: "fas fa-wrench"
        content: "Kumpulkan Teks Berformat Mentah atau HTML dari Dokumen Word & Kutipan Teks yang Disorot dari Dokumen"

      - icon: "fas fa-columns"
        content: "Dapatkan Data dari Formulir PDF & Dapatkan Tabel Berformat Dari Dokumen PDF atau Word"

      - icon: "fas fa-file-word"
        content: "Tarik Satu Kalimat atau Seluruh Teks dari File EPUB, CHM, Penurunan Harga & FB2"

      - icon: "fas fa-envelope"
        content: "Kutipan Daftar Isi dari Database, PDF, EPUB, CHM & Dokumen Pengolah Kata"

      - icon: "fas fa-print"
        content: "Ambil Area Teks dari Dokumen untuk Analisis & Tarik Teks dengan Struktur Kontennya yang Utuh"

      - icon: "fas fa-file-archive"
        content: "Dapatkan Metadata dari Format Dokumen yang Didukung"

      - icon: "fas fa-lock"
        content: "Gambar Semua atau Gambar yang Dipilih dari Format yang Didukung & Putar Gambar yang Diekstrak"

      - icon: "fas fa-file-code"
        content: "Ekstrak Teks dari File dalam Arsip Zip & Kontainer OST – Deteksi Jenis Media untuk Item Kontainer Zip"
      
      - icon: "fas fa-fill-drip"
        content: "Ambil Data dari Wadah Email (Exchange Web Server, POP3, IMAP)"

      - icon: "fas fa-file-excel"
        content: "Keluarkan Teks dari Wadah Basis Data dengan Cara Cepat, Andal, dan Efisien"

      - icon: "fas fa-heading"
        content: "Temukan Teks Sederhana, Seluruh Kata & Ekspresi Reguler dalam Dokumen"

      - icon: "fas fa-project-diagram"
        content: "Siapkan Template Dokumen, Ekstrak Data dari Dokumen dan Analisis Bidang & Tabel Data"

      - icon: "fas fa-cube"
        content: "Cari & Ekstrak Ekspresi yang Disorot dalam Dokumen"

      - icon: "fab fa-uncharted"
        content: "Tarik Teks dengan Pemformat Teks Biasa (Sederhana & ASCII) atau Pemformatan Kustom dengan Tepi, Sudut, & Persimpangan"

      - icon: "fab fa-uncharted"
        content: "Ambil & Format Teks (Font, Hyperlink, Judul, Daftar & Tabel) dengan Formatter Penurunan Harga"

      - icon: "fab fa-uncharted"
        content: "Dapatkan Teks dengan Formatter HTML & Terapkan Formatter ke Paragraf, Hyperlink, Font, Judul, Daftar & Tabel"

      - icon: "fab fa-uncharted"
        content: "Pindahkan Tata Letak Tabel & Deteksi Tabel di Area Persegi Panjang dengan Pemisah Kolom"

      - icon: "fab fa-uncharted"
        content: "Ekstrak Teks dari Bentuk, Objek WordArt & Kotak Teks dalam Format File Microsoft Office"

      - icon: "fab fa-uncharted"
        content: "Ekstrak Gambar ke File – Simpan ke Format JPG, PNG, GIF, BMP, PNG atau WEBP"

      - icon: "fab fa-uncharted"
        content: "Ekstrak Teks dari Server Email dan Database melalui JDBC"

    more_feature:
      - title: "Dapatkan Teks dengan Pemformat Teks Biasa atau HTML"
        content: |
          Dengan GroupDocs.Parser untuk Java, Anda dapat menerapkan berbagai formatter ke Teks dan HTML. Anda dapat menarik teks dengan Pemformat Teks Biasa untuk Sederhana dan ASCII. Anda juga bisa mendapatkan Teks dengan HTML Formatter dan menerapkan pemformatan ke paragraf, hyperlink, font, heading, daftar, dan tabel.

support:
    enable: true

solutions:
    enable: true
    title: "GroupDocs.Parser menawarkan API tampilan dokumen untuk lingkungan pengembangan populer lainnya"

    solution:
        - img_alt: "GroupDocs.Parser for .NET"
          image: "https://www.groupdocs.cloud/templates/groupdocs/images/product-logos/groupdocs-parser-net.png"
          product: "GroupDocs.Parser"
          platform: ".NET"
          link: "/parser/net/"

back_to_top:
  enable: true
---
