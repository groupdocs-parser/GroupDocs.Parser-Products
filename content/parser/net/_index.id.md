---
############################# Static ############################
layout: "landing"
date: 2025-06-30T10:26:00
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

############################# Head ############################
head_title: "Aplikasi Penguraian Dokumen GroupDocs.Parser for .NET"
head_description: "Dapatkan solusi penguraian dokumen serba ada untuk aplikasi .NET. Ekstrak data dari format dokumen secara online menggunakan fitur drag and drop sederhana."

############################# Header ############################
title: "Uraikan dokumen melalui API .NET"
description: "Ekstrak data dari dokumen dan gambar di mana saja menggunakan API yang fleksibel dan solusi berbasis aplikasi kami untuk programmer dan pengguna akhir."
words:
  for: "untuk"

actions:
  main: "Unduh Nuget"
  main_link: "https://www.nuget.org/packages/GroupDocs.Parser"
  alt: "Lisensi"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/net/"
  title: "Siap untuk memulai?"
  description: "Coba fitur GroupDocs.Parser secara gratis atau minta lisensi"

release:
  title: "Versi {0} dirilis"
  notes: "Lihat apa yang baru"
  downloads: "Unduhan"

code:
  title: "Dengan Cepat Uraikan Konten Dokumen"
  more: "Lebih banyak contoh"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "dotnet add package GroupDocs.Parser"
  content: |
    ```csharp {style=abap}   
    // Kirim file sumber ke instance Parser
    using (var parser = new Parser("source.pdf"))
    {
        // Kirim teks dokumen ke TextReader
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
  description: "API untuk melakukan penguraian dokumen dalam aplikasi .NET"
  features:
    # feature loop
    - title: "Ekstrak data dari dokumen"
      content: "GroupDocs.Parser for .NET API memungkinkan Anda untuk mengambil teks, metadata, dan gambar dari berbagai format file seperti dokumen Office, email, lampiran, dan arsip. Alat yang kuat ini membantu Anda dengan efisien mengakses dan memproses informasi berharga yang terkandung dalam file ini untuk berbagai aplikasi seperti analisis data, pengindeksan mesin pencari, atau sistem manajemen konten."

    # feature loop
    - title: "Uraikan dokumen"
      content: "Ekstrak berbagai elemen seperti hyperlink, tabel, kode QR, kode batang dan data dari formulir PDF. Juga uraikan informasi yang diinginkan dari dokumen menggunakan template kustom."

    # feature loop
    - title: "Kustomisasi hasil"
      content: ".NET API memungkinkan Anda untuk mengambil data dalam berbagai format seperti mentah, terstruktur, HTML, atau Markdown. Selain itu, API menawarkan fungsi pencarian untuk menemukan kata atau frasa tertentu dalam teks dokumen."

############################# Platforms ############################
platforms:
  enable: true
  title: "Independensi Platform"
  description: "GroupDocs.Parser for .NET mendukung sistem operasi, framework dan pengelola paket berikut."
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
  title: "Fitur GroupDocs.Parser for .NET"
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
  description: "Beberapa kasus penggunaan operasi GroupDocs.Parser for .NET yang khas"
  items:
    # code sample loop
    - title: "Ekstrak gambar dari dokumen PDF"
      content: |
        GroupDocs.Parser for .NET memudahkan pengembang C# untuk mengekstrak gambar dari [dokumen](https://docs.groupdocs.com/parser/net/extract-images-from-documents/):
        {{< landing/code title="Ekstrak gambar dari dokumen PDF di C#">}}
        ```csharp {style=abap}
        // Buat instance dari kelas Parser
        using (var parser = new Parser("source.pptx"))
        {
            // Ekstrak gambar
            var images = parser.GetImages();

            // Periksa apakah ada yang diekstrak
            if (images == null)
            {
                return;
            }
            // Iterasi melalui gambar
            foreach (PageImageArea image in images)
            {
                // Cetak indeks halaman, kotak pembatas, dan jenis gambar
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
        {{< landing/code title="Ekstrak kode batang dari gambar di C#">}}
        ```csharp {style=abap}   
        // Muat gambar sumber ke Parser
        using (var parser = new Parser("source.jpg"))
        {
            // Periksa apakah file mendukung ekstraksi kode batang
            if (parser.Features.Barcodes)
            {
                // Ekstrak kode batang dari file
                var barcodes = parser.GetBarcodes();

                // Iterasi melalui kode batang
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
