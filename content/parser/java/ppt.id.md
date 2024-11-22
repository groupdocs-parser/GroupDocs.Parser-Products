---
############################# Static ############################
layout: "auto-gen-parser"
date: 2024-02-13T17:01:06
draft: false
otherformats: tex vdx vsdm vsdx vssm vssx vstm vstx vsx vtx xlam xls xlsb xlsm xlsx xlt
ext: ppt

############################# Head ############################
head_title: "Ekstrak Hyperlink dari dokumen di Java"
head_description: "GroupDocs.Parser for Java API memungkinkan pengembang mengekstrak hyperlink dari dokumen, halaman dokumen, atau area halaman tertentu dari Excel, PowerPoint, PDF, Outlook & lainnya."

############################# Header ############################
title: "Java API untuk Mengekstrak Hyperlink dari Dokumen, Halaman, atau Area Halaman Tertentu"
description: "GroupDocs.Parser for Java API memudahkan pekerjaan pengembang dengan memungkinkan mereka mengekstrak hyperlink dari dokumen, halaman dokumen atau halaman tertentu Area PDF, DOCX, PPTX, EML, MSG, XLS, {322 }, CSV, RTF, EPUB dan banyak lagi."
bg_image: "https://cms.admin.containerize.com/templates/aspose/App_Themes/V3/images/bg/header1.png"
bg_overlay: false
button:
    enable: true
    icon: "fas fa-arrow-down"
    label: "Unduh Uji Coba Gratis"
    link: "https://downloads.groupdocs.com/parser/java"

############################# SubMenu ############################
submenu:
    enable: true

    left:
        img_alt: "GroupDocs.Parser for Java"
        image: "https://cms.admin.containerize.com/templates/groupdocs/images/product-logos/90x90-noborder/groupdocs-parser-java.png"
        product: "GroupDocs.Parser"
        platform: "Java"

    middle:
        button:

            # button loop
            - link: "https://apireference.groupdocs.com/parser/java"
              text: "Referensi API"

            # button loop
            - link: "https://github.com/groupdocs-parser"
              text: "Contoh Kode"

            # button loop
            - link: "https://products.groupdocs.app/parser/family"
              text: "Demo Langsung"

            # button loop
            - link: "https://purchase.groupdocs.com/pricing/parser/java"
              text: "Harga"

    right:
        link_download: "https://downloads.groupdocs.com/parser"
        link_learn: "https://docs.groupdocs.com/parser/java"
        link_buy: "https://purchase.groupdocs.com"

############################# About ############################
about:
    enable: true
    title: "Bagaimana cara Mengurai & Mengekstrak Hyperlink dari PPT dokumen melalui Java API?"
    content: |
        Hyperlink adalah sepotong teks atau gambar atau ikon yang menunjuk ke seluruh dokumen atau ke bagian tertentu dalam dokumen. Penggunaan hyperlink memungkinkan pengguna untuk menavigasi ke halaman web atau dokumen. Seringkali diperlukan untuk mengekstrak hyperlink dari dokumen dan menggunakannya untuk mengakses dokumen eksternal atau halaman web. GroupDocs.Parser for Java adalah API ekstraksi teks dokumen menarik yang menyediakan fungsionalitas lengkap untuk mengimplementasikan solusi ekstraksi teks dan metadata. Ini mendukung ekstraksi teks & hyperlink dari format PDF, Email, Ebooks, Microsoft Office: Word (DOC, DOCX), PowerPoint (PPT, PPTX), Excel ( XLS, XLSX), format LibreOffice, dan banyak lagi. Ini mendukung beberapa fitur lanjutan untuk penguraian dokumen, mengekstraksi teks biasa dan terstruktur, pencarian teks dengan kata kunci, mengekstrak metadata atau gambar, wadah serta lampiran dan banyak lagi.
        
        

############################# Steps ############################
steps:
    enable: true
    title_left: "Ekstrak hyperlink dari PPT di Java"
    content_left: |
        [GroupDocs.Parser for Java](/id/parser/java/) memudahkan pengembang Java untuk mengekstrak hyperlink dari file PPT dengan menerapkan beberapa langkah mudah.
        
        * Membuat instance objek [Parser](https://reference.groupdocs.com/java/parser/com.groupdocs.parser/Parser) untuk dokumen awal;
        * Periksa apakah dokumen mendukung ekstraksi hyperlink;
        * Panggil metode [getHyperlinks](https://reference.groupdocs.com/parser/java/com.groupdocs.parser/parser/#getHyperlinks--) dan dapatkan kumpulan [PageHyperlinkArea](https://reference.groupdocs.com/parser/java/com.groupdocs.parser.data/PageHyperlinkArea) objek;
        * Iterasi melalui koleksi dan dapatkan teks hyperlink dan URL.

    title_right: "Pelajari lebih lanjut tentang ekstraksi hyperlink"
    content_right: |
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document/">Cara mengekstrak hyperlink dari dokumen</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page/">Cara mengekstrak hyperlink dari halaman dokumen</a>
        * <a href="https://docs.groupdocs.com/parser/java/extract-hyperlinks-from-document-page-area/">Cara mengekstrak hyperlink dari area halaman dokumen</a>
    
    code: |
     {{% parser/additional-styles %}}
     {{< parser/code-parser title="Cara mengekstrak hyperlink dari file PPT menggunakan kode contoh Java">}}

        ```java    
        // Ekstrak hyperlink dari file PPT menggunakan GroupDocs.Parser API
        // Buat instance kelas Parser
        try (Parser parser = new Parser(Constants.HyperlinksPdf)) {
            // Periksa apakah dokumen mendukung ekstraksi hyperlink
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("Dokumen tidak mendukung ekstraksi hyperlink.");
                return;
            }
            // Ekstrak hyperlink dari dokumen
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();
            // Iterasi melalui hyperlink
            for (PageHyperlinkArea h : hyperlinks) {
                // Cetak teks hyperlink
                System.out.println(h.getText());
                // Cetak URL hyperlink
                System.out.println(h.getUrl());
                System.out.println();
            }
        }
        ```
     {{< /parser/code-parser >}}

############################# More ############################
more:
    enable: true
    title_left: "Persyaratan sistem"
    content_left: |
        GroupDocs.Parser for Java API didukung di semua platform dan sistem operasi utama. Sebelum menjalankan kode di bawah ini, harap pastikan bahwa Anda telah menginstal prasyarat berikut di sistem Anda.
        
        * Sistem Operasi: Microsoft Windows, Linux, MacOS
        * Lingkungan Pengembangan: NetBeans, Intellij IDEA, Eclipse, etc.
        * Kerangka kerja
        * Unduh versi terbaru GroupDocs.Parser for Java dari [Maven](https://repository.groupdocs.com/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-parser)

    title_right: "Mengapa Menggunakan GroupDocs.Parser for Java"
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
        Java dokumen mengurai & API ekstraksi hyperlink untuk format file dan gambar. Ekstrak data untuk beberapa format file populer seperti yang dinyatakan di bawah ini.

############################# Back to top ###############################
back_to_top:
    enable: true
---