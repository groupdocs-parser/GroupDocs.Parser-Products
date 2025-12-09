---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: id
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
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK untuk Python"
head_description: "SDK Document Parser berkinerja tinggi untuk Python. Ekstrak teks, gambar, metadata, barcode, tabel, dan data lain dari PDF, Word, Excel, email, dan lebih dari 50 format dokumen."

############################# Header ############################
title: "SDK Document Parser untuk Python"
description: "Tambahkan parsing dokumen yang cepat dan akurat ke aplikasi Python Anda serta ekstrak teks, gambar, metadata, dan data terstruktur dari dokumen dan gambar."
words:
  for: "untuk"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI Unduh"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "Lisensi"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "Siap memulai?"
  description: "Coba fitur GroupDocs.Parser secara gratis atau minta lisensi"

release:
  enable: false
  title: "Versi {0} dirilis"
  notes: "Lihat apa yang baru"
  downloads: "Unduhan"

code:
  title: "Ekstrak teks menggunakan Python"
  more: "Contoh lain"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # Muat dokumen
    with Parser("sample.pdf") as parser:
        # Ekstrak teks dari dokumen
        text = parser.GetText()

        # Cetak semua teks yang diekstrak
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser sekilas"
  description: "SDK Document Parser untuk melakukan parsing dokumen dengan akurasi tinggi dalam aplikasi Python"
  features:
    # feature loop
    - title: "Ekstrak data dari dokumen"
      content: "API GroupDocs.Parser for Python via .NET memungkinkan Anda mengambil teks, metadata, dan gambar dari berbagai format file seperti dokumen Office, email, lampiran, dan arsip. Alat yang kuat ini membantu Anda mengakses dan memproses informasi berharga yang terdapat dalam file-file tersebut secara efisien untuk berbagai aplikasi seperti analisis data, pengindeksan mesin pencari, atau sistem manajemen konten."

    # feature loop
    - title: "Parse dokumen"
      content: "Ekstrak berbagai elemen seperti hyperlink, tabel, kode QR, barcode, dan data dari formulir PDF. Juga uraikan informasi apa pun yang diinginkan dari dokumen menggunakan templat khusus."

    # feature loop
    - title: "Menyesuaikan hasil"
      content: "API Python memungkinkan Anda mengambil data dalam berbagai format seperti mentah, terstruktur, HTML, atau Markdown. Selain itu, API menyediakan fungsi pencarian untuk menemukan kata atau frasa tertentu dalam teks dokumen."

############################# Platforms ############################
platforms:
  enable: true
  title: "Kemandirian Platform"
  description: "GroupDocs.Parser for Python via .NET mendukung sistem operasi, kerangka kerja, dan manajer paket berikut"
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
    GroupDocs.Parser for Python via .NET mendukung operasi dengan [format file](https://docs.groupdocs.com/parser/python-net/supported-document-formats/).
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
  title: "Fitur GroupDocs.Parser for Python via .NET"
  description: "Ekstrak data dari PDF, dokumen Office, gambar, dan format lain dengan cepat dan akurat menggunakan Python Document Parser SDK kami"

  items:
    # feature loop
    - icon: "text"
      title: "Ekstrak teks"
      content: "Ekstrak informasi teks dari berbagai format file seperti dokumen office, file PDF, dan gambar untuk kemudahan membaca dan analisis."

    # feature loop
    - icon: "image"
      title: "Ekstrak gambar"
      content: "Ambil konten visual dari berbagai sumber seperti dokumen office, file PDF untuk akses dan penggunaan yang mudah."

    # feature loop
    - icon: "qr"
      title: "Pindai Kode QR"
      content: "Deteksi dan dekode kode QR yang terdapat dalam dokumen office, file PDF, atau konten visual untuk pengambilan informasi yang efisien."

    # feature loop
    - icon: "email"
      title: "Ekstrak data dari lampiran email dan arsip"
      content: "Kumpulkan informasi berharga dari pesan email, lampiran file, dan sumber data terkompresi untuk analisis dan pemanfaatan yang efektif."

    # feature loop
    - icon: "table"
      title: "Ekstrak tabel"
      content: "Identifikasi dan ekstrak data tabel dari dokumen PDF untuk analisis dan penggunaan yang terstruktur."

    # feature loop
    - icon: "hyperlink"
      title: "Ekstrak hyperlink"
      content: "Temukan dan ekstrak tautan hiperteks serta alamat email dalam dokumen office atau file PDF untuk akses yang efisien."

    # feature loop
    - icon: "pdf"
      title: "Mengurai Formulir PDF"
      content: "Python API dapat digunakan untuk mengekstrak data dari formulir ini untuk pemrosesan yang efisien."

    # feature loop
    - icon: "template"
      title: "Mengurai data dengan templat"
      content: "Buat templat khusus dan gunakan dengan Python API untuk mengurai informasi spesifik dari file PDF, menyederhanakan proses ekstraksi data."

    # feature loop
    - icon: "search"
      title: "Cari teks dalam dokumen"
      content: "Dengan cepat temukan kata atau pola spesifik dalam dokumen."


############################# Code samples ############################
code_samples:
  enable: true
  title: "Contoh kode"
  description: "Selain ekstraksi teks dasar, berikut adalah contoh penggunaan paling umum untuk ekstraksi cepat teks, gambar, dan metadata."
  items:
    # code sample loop
    - title: "Cari Teks dalam Dokumen"
      content: |
        Contoh ini menunjukkan cara mencari frasa spesifik dalam dokumen PDF dan mencetak lokasi temuan.
        {{< landing/code title="Cari Teks dalam Dokumen dengan Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # Muat dokumen
        with Parser("sample.pdf") as parser:
            # Cetak indeks halaman dan persegi panjang tempat frasa ditemukan
            for area in parser.Search("Total Amount"):
                # Cetak indeks halaman dan persegi panjang tempat frasa ditemukan
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Ekstrak Gambar dari Dokumen"
      content: |
        Contoh ini menunjukkan cara mengekstrak gambar dari dokumen PDF dan menyimpannya ke file.
        {{< landing/code title="Ekstrak Gambar dari Dokumen dengan Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Muat dokumen
        with Parser("sample.docx") as parser:
            # Ekstrak gambar dari dokumen
            images = parser.GetImages()

            # Simpan gambar ke file
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "Ekstrak Metadata dari Dokumen"
      content: |
        Contoh ini menunjukkan cara mengekstrak metadata dari dokumen PDF dan menampilkannya.
        {{< landing/code title="Ekstrak Metadata dari Dokumen dengan Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # Muat dokumen
        with Parser("sample.pdf") as parser:
            # Ekstrak metadata dari dokumen
            metadata = parser.GetMetadata()

            # Cetak metadata
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
