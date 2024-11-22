---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:06
draft: false
otherformats: ott pdf pps ppsx ppt pptx rtf tex vdx vsdm vsdx vssm vssx vstm vstx vsx
ext: xlt

############################# Head ############################
head_title: ".NET API untuk Mengurai & Mengekstrak Hyperlink dari Dokumen, Halaman, atau Area Halaman"
head_description: "GroupDocs.Parser .NET API memungkinkan pemrogram perangkat lunak mengekstrak hyperlink dari dokumen, halaman, atau Area halaman PDF, DOCX, XLSX, CSV, PPTX, EML, MSG, EPUB & masih banyak lagi."

############################# Header ############################
title: "Ekstrak Hyperlink dari Dokumen, Halaman, atau Area halaman Tertentu melalui C#/VB.NET API"
description: "GroupDocs.Parser .NET API memungkinkan pengembang perangkat lunak mengurai & mengekstrak hyperlink dari dokumen, halaman, atau Area halaman PDF, DOC, DOCX, PPT, PPTX, EML, MSG , XLS, XLSX, CSV, ODT, RTF, EPUB dan banyak dokumen lainnya."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Unduh Uji Coba Gratis"
    link: "https://downloads.groupdocs.com/parser/net"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for .NET"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-net.png"
        product: "GroupDocs.Parser"
        platform: ".NET"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/net"
              text: "Referensi API"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Contoh Kode"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Demo Langsung"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/net"
              text: "Harga"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/net"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Bagaimana cara Mengurai & Mengekstrak Hyperlink dari XLT dokumen melalui .NET API?"
    content: |
        Hyperlink adalah sepotong teks atau gambar atau ikon yang menunjuk ke seluruh dokumen atau ke bagian tertentu dalam dokumen. Penggunaan hyperlink memungkinkan pengguna untuk menavigasi ke halaman web atau dokumen. Seringkali diperlukan untuk mengekstrak hyperlink dari dokumen dan menggunakannya untuk mengakses dokumen eksternal atau halaman web. GroupDocs.Parser for .NET adalah API ekstraksi teks dokumen menarik yang menyediakan fungsionalitas lengkap untuk mengimplementasikan solusi ekstraksi teks dan metadata. Ini mendukung ekstraksi teks & hyperlink dari format PDF, Email, Ebooks, Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel ( XLS, XLSX), format LibreOffice, dan banyak lagi. Ini mendukung beberapa fitur lanjutan untuk penguraian dokumen, mengekstraksi teks biasa dan terstruktur, pencarian teks dengan kata kunci, mengekstrak metadata atau gambar, wadah serta lampiran dan banyak lagi.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Ekstrak hyperlink dari XLT di .NET"
    content_left: |
        [GroupDocs.Parser for .NET](/id/parser/net/) memudahkan pengembang C# untuk mengekstrak hyperlink dari file XLT dengan menerapkan beberapa langkah mudah.
        
        * Membuat instance objek [Parser](https://reference.groupdocs.com/net/parser/groupdocs.parser/parser) untuk dokumen awal;
        * Periksa apakah dokumen mendukung ekstraksi hyperlink;
        * Panggil metode [GetHyperlinks](https://reference.groupdocs.com/parser/net/groupdocs.parser/parser/methods/gethyperlinks) dan dapatkan koleksi [PageHyperlinkArea](https://reference.groupdocs.com/parser/net/groupdocs.parser.data/pagehyperlinkarea) objek;
        * Iterasi melalui koleksi dan dapatkan teks hyperlink dan URL.

    title_right: "Pelajari lebih lanjut tentang ekstraksi hyperlink"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document/">Cara mengekstrak hyperlink dari dokumen</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page/">Cara mengekstrak hyperlink dari halaman dokumen</a>
        * <a href="https://docs.groupdocs.com/parser/net/extract-hyperlinks-from-document-page-area/">Cara mengekstrak hyperlink dari area halaman dokumen</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Cara mengekstrak hyperlink dari file XLT menggunakan kode contoh C#">}}

        ```csharp    
        // Ekstrak hyperlink dari file XLT menggunakan GroupDocs.Parser API
        // Buat instance kelas Parser
        using (Parser parser = new Parser(filePath)) {
            // Periksa apakah dokumen mendukung ekstraksi hyperlink
            if (!parser.Features.Hyperlinks) {
                Console.WriteLine("Dokumen tidak mendukung ekstraksi hyperlink.");
                return;
            }
            // Ekstrak hyperlink dari dokumen
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();
            // Iterasi melalui hyperlink
            foreach (PageHyperlinkArea h in hyperlinks) {
                // Cetak teks hyperlink
                Console.WriteLine(h.Text);
                // Cetak URL hyperlink
                Console.WriteLine(h.Url);
                Console.WriteLine();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "Persyaratan sistem"
    content_left: |
        GroupDocs.Parser for .NET API didukung di semua platform dan sistem operasi utama. Sebelum menjalankan kode di bawah ini, harap pastikan bahwa Anda telah menginstal prasyarat berikut di sistem Anda.
        
        * Sistem Operasi: Microsoft Windows, Linux, MacOS
        * Lingkungan Pengembangan: Microsoft Visual Studio, Xamarin, MonoDevelop
        * Kerangka kerja
        * Unduh versi terbaru GroupDocs.Parser for .NET dari [Nuget](https://www.nuget.org/packages/groupdocs.parser)

    title_right: "Mengapa Menggunakan GroupDocs.Parser for .NET"
    content_right: |
        * Dukungan ekstraksi teks biasa dari dokumen yang didukung    
        * Penguraian dokumen melalui templat yang ditentukan pengguna    
        * Sepenuhnya mendukung ekstraksi teks terstruktur    
        * Pencarian teks melalui kata kunci serta ekspresi reguler    
        * Ekstrak teks yang diformat, metadata, gambar, wadah, dan lampiran    
        * Ekstrak daftar isi untuk beberapa format dokumen yang didukung    
        * Mengurai data formulir dari PDF dokumen    
        * Ekstrak hyperlink dari dokumen   
        
############################# About Formats ############################
about_formats:
    enable: true

############################# More Formats ############################
more_formats:
    enable: true
    title: "Ekstrak Hyperlink Dari Format Dokumen Lain"
    content: |
        .NET dokumen mengurai & API ekstraksi hyperlink untuk format file dan gambar. Ekstrak data untuk beberapa format file populer seperti yang dinyatakan di bawah ini.

############################# Back to top ###############################
back_to_top:
    enable: true
---