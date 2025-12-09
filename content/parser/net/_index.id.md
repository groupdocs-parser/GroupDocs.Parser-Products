---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: id
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
head_title: "GroupDocs.Parser for .NET SDK Parser Dokumen untuk .NET"
head_description: "SDK Parser Dokumen berkinerja tinggi untuk .NET. Ekstrak teks, gambar, metadata, kode batang, tabel, dan data lainnya dari PDF, Word, Excel, email, dan lebih dari 50 format dokumen."

############################# Header ############################
title: "SDK Parser Dokumen untuk .NET"
description: "Tambahkan parsing dokumen yang cepat dan akurat ke aplikasi .NET Anda dan ekstrak teks, gambar, metadata, serta data terstruktur dari dokumen dan gambar."
words:
  for: "untuk"

actions:
  main: "Nuget Unduh"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Lisensi"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Siap memulai?"
  description: "Coba fitur GroupDocs.Parser secara gratis atau minta lisensi"

release:
  title: "Versi {0} dirilis"
  notes: "Lihat apa yang baru"
  downloads: "Unduhan"

code:
  title: "Parse Konten Dokumen dengan Cepat menggunakan SDK"
  more: "Contoh lain"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Berikan file sumber ke instance Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Berikan teks dokumen ke TextReader
        using (var textReader = parser.GetText())
        {
            // Proses teks dokumen
            Console.WriteLine(textReader?.ReadToEnd());
        }
    }  
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser sekilas"
  description: "SDK Parser Dokumen untuk melakukan parsing dokumen dengan akurasi tinggi pada aplikasi .NET"
  features:
    # feature loop
    - title: "Ekstrak data dari dokumen"
      content: "GroupDocs.Parser for .NET API memungkinkan Anda mengambil teks, metadata, dan gambar dari berbagai format file seperti dokumen Office, email, lampiran, dan arsip. Alat kuat ini membantu Anda mengakses dan memproses informasi berharga yang terdapat dalam file tersebut secara efisien untuk berbagai aplikasi seperti analisis data, pengindeksan mesin pencari, atau sistem manajemen konten."

    # feature loop
    - title: "Parse dokumen"
      content: "Ekstrak berbagai elemen seperti hyperlink, tabel, kode QR, kode batang, dan data dari formulir PDF. Juga parse informasi apa pun yang diinginkan dari dokumen menggunakan templat khusus."

    # feature loop
    - title: "Menyesuaikan hasil"
      content: ".NET API memungkinkan Anda mengambil data dalam berbagai format seperti mentah, terstruktur, HTML, atau Markdown. Selain itu, API menyediakan fungsi pencarian untuk menemukan kata atau frasa tertentu dalam teks dokumen."

############################# Platforms ############################
platforms:
  enable: true
  title: "Kemandirian Platform"
  description: "GroupDocs.Parser for .NET mendukung sistem operasi, kerangka kerja, dan manajer paket berikut"
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
  title: "Format file yang didukung"
  description: |
    GroupDocs.Parser for .NET mendukung operasi dengan [format file](https://docs.groupdocs.com/parser/net/supported-document-formats/) berikut.
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
  title: "Fitur GroupDocs.Parser for .NET"
  description: "Ekstrak data dari PDF, dokumen Office, gambar, dan format lainnya dengan cepat dan akurat menggunakan SDK Parser Dokumen .NET kami"

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
  description: "Beberapa contoh penggunaan operasi GroupDocs.Parser for .NET yang umum"
  items:
    # code sample loop
    - title: "Ekstrak gambar dari dokumen PDF"
      content: |
        GroupDocs.Parser for .NET memudahkan pengembang C# untuk mengekstrak gambar dari [dokumen](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Ekstrak gambar dari dokumen PDF dalam C#">}}
        ```csharp {style=abap}
        // Buat instance kelas Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Ekstrak gambar
            var images = parser.GetImages();

            // Periksa apakah sesuatu telah diekstrak
            if (images == null)
            {
                return;
            }
            // Iterasi gambar
            foreach (PageImageArea image in images)
            {
                // Cetak indeks halaman, persegi panjang, dan tipe gambar
                Console.WriteLine(string.Format("Page: {0}, R: {1}, Type: {2}", 
                    image.Page.Index, image.Rectangle, image.FileType));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Ekstrak kode batang dari gambar"
      content: |
        Gunakan API .NET kami untuk mengekstrak [kode batang](https://docs.groupdocs.com/parser/net/extract-barcodes-from-document/) dari gambar:
        {{< landing/code title="Ekstrak kode batang dari gambar dalam C#">}}
        ```csharp {style=abap}   
        // Muat gambar sumber ke Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Periksa apakah file mendukung ekstraksi kode batang
            if (parser.Features.Barcodes)
            {
                // Ekstrak kode batang dari file
                var barcodes = parser.GetBarcodes();

                // Iterasi kode batang
                foreach (var barcode in barcodes)
                {
                    // Cetak indeks halaman
                    Console.WriteLine("Page: " + barcode.Page.Index.ToString());
                    // Cetak nilai kode batang
                    Console.WriteLine("Value: " + barcode.Value);
                }
            }
        }
        ```
        {{< /landing/code >}}

---
