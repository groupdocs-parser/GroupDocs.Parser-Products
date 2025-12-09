---
############################# Static ############################
layout: "family"
date:  2025-12-09T14:52:35
draft: false

product: "Parser"
product_tag: "parser"

lang: id

############################# Head ############################
head_title: "SDK Pengurai Dokumen untuk PDF, Word & Excel | GroupDocs"
head_description: "SDK Pengurai Dokumen untuk mengekstrak teks, gambar, metadata, kode batang, dan tabel dari PDF, Word, Excel, email, serta lebih dari 50 format dokumen lainnya untuk aplikasi .NET, Java, dan Python."

############################# Header ############################
title: "SDK Pengurai Dokumen"
description:  |
  SDK Pengurai Dokumen yang ramah pengembang untuk mengekstrak teks, gambar, kode batang, metadata, dan tabel dari lebih dari 50 format dokumen dan gambar.

  Integrasikan penguraian dokumen berperforma tinggi ke dalam aplikasi .NET, Java, dan Python Anda dengan upaya coding minimal.

  Gunakan templat fleksibel dan API canggih untuk menyesuaikan aturan penguraian serta menghasilkan output data yang bersih dan terstruktur.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Pilih platform Anda"
  title: "Kemandirian Platform"
  description: "Perpustakaan GroupDocs.Parser mendukung sistem operasi dan kerangka kerja berikut:"
  details_link_title: "Pelajari lebih lanjut"

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
          - rows: "3"
            content: |
                    .NET Framework 4.6.2 or higher <br> .NET Core 2.0 or higher <br> .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    Microsoft Visual Studio <br> JetBrains Rider <br> Microsoft Visual Code
      
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
          - rows: "3"
            content: |
                    Java 8 or higher <br> Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> Mac OS
      
          # features loop
          - rows: "4"
            content: |
                    IntelliJ IDEA <br> Eclipse <br> NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats


    # items loop
    - title: "Python"
      description: GroupDocs.Parser for Python
      color: "yellow"
      tag: "python-net"
      link: "/parser/python-net/"
      features_link: "https://docs.groupdocs.com/parser/python-net/system-requirements/"
      features:
          # features loop
          - rows: "3"
            content: |
                    Python 3.5+
      
          # features loop
          - rows: "1"
            content: |
                    Windows <br> Linux <br> macOS
      
          # features loop
          - rows: "4"
            content: |
                    PyCharm, VS Code, Jupyter Notebook
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats                    

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser sekilas"
  description: "SDK Pengurai Dokumen yang kuat untuk mengekstrak data terstruktur dan tidak terstruktur dari PDF, dokumen Office, gambar, email, dan arsip."

  items:
    # items loop
    - icon: "text"
      title: "Ekstrak teks"
      content: "Ekstrak informasi teks dari berbagai format file"

    # items loop
    - icon: "image"
      title: "Ekstrak gambar"
      content: "Ambil konten visual dari berbagai sumber"

    # items loop
    - icon: "template"
      title: "Urai data dengan templat"
      content: "Buat templat khusus dan gunakan untuk mengurai informasi spesifik"

    # items loop
    - icon: "pdf"
      title: "Urai Formulir PDF"
      content: "Formulir PDF adalah dokumen digital dengan bidang yang dapat diisi untuk interaksi pengguna"

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser contoh kode"
  description: "Beberapa contoh penggunaan operasi GroupDocs.Parser umum dalam C# dan Java dan Python"

  items:
    # items loop
    - title: "Cara mengekstrak teks dari dokumen PDF"
      content: "API GroupDocs.Parser memudahkan mengekstrak teks dari dokumen dengan beberapa langkah."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              ```csharp {style=abap}  
                // Buat instance kelas Parser dengan memberikan file yang diinginkan
                using (var parser = new Parser("source.pdf"))
                {
                    // Ekstrak teks
                    using (var textReader = parser.GetText())
                    {
                        // Proses teks yang diekstrak
                        Console.WriteLine(textReader?.ReadToEnd());
                    }
                }     
              ```
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              ```java {style=abap}
                // Buat instance kelas Parser dengan memberikan file yang diinginkan
                try (Parser parser = new Parser("source.pdf"))
                {
                    // Ekstrak teks
                    try (TextReader reader = parser.getText())
                    {
                        // Proses teks yang diekstrak
                        System.out.println(reader == null 
                                ? "" 
                                : reader.readToEnd());
                    }
                }  
              ```
          # samples loop
          - language: "Python"
            color: "green"
            content: |
              ```python {style=abap}
                from groupdocs.parser import Parser

                # Buat instance kelas Parser dengan memberikan file yang diinginkan
                with Parser("source.pdf") as parser:
                    # Ekstrak teks
                    text = parser.get_text()

                    # Proses teks yang diekstrak
                    print(text)
              ```
############################# Supported Formats ###############################
formats:
  enable: true
  title: "Dukungan lebih dari 50 format dokumen dan gambar"
  description: "SDK Pengurai Dokumen GroupDocs.Parser memungkinkan operasi penguraian pada dokumen Office, PDF, gambar, email, arsip, dan lainnya."

############################# Metrics ###############################
metrics:
  enable: true
  title: "Pencapaian GroupDocs.Parser"
  description: "Temukan metrik kunci dari pencapaian perpustakaan kami"

  items:
    # items loop
    - number: "50+"
      title: "Format yang didukung"
      content: "GroupDocs.Parser mendukung operasi dengan lebih dari 50 format file populer."

    # items loop
    - number: "1600k"
      title: "Unduhan NuGet"
      content: "GroupDocs.Parser untuk paket NuGet .NET telah diunduh lebih dari 1,600,000 kali."

    # items loop
    - number: "18k"
      title: "Unduhan Maven"
      content: "GroupDocs.Parser memiliki 18,000 unduhan di Maven. Fitur Parsing Java yang kuat."

    # items loop
    - number: "140+"
      title: "Pelanggan puas"
      content: "Perusahaan ternama maupun pengembang individual memilih produk GroupDocs untuk membangun solusi inovatif."


############################# Customers ###############################
customers:
  enable: true
  title: "Pelanggan kami yang puas"
  description: "Pustaka GroupDocs digunakan oleh merek-merek terkenal dan terhormat di seluruh dunia."

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
  title: "Siap memulai?"
  description: "Coba fitur GroupDocs.Parser secara gratis di platform Anda"

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
  title: "Pertanyaan yang Sering Diajukan"
  description: "Jawaban atas pertanyaan yang paling sering diajukan."

  items:
    # items loop
    - question: "Apakah pustaka GroupDocs.Parser memerlukan perangkat lunak pihak ketiga lainnya untuk memanipulasi dokumen?"
      answer: "GroupDocs.Parser tidak memerlukan perangkat lunak eksternal apa pun untuk diinstal, seperti Adobe Acrobat, Microsoft Office, atau yang lainnya."

    # items loop
    - question: "Bisakah saya mencoba pustaka GroupDocs.Parser sebelum membeli?"
      answer: "Ya, Anda dapat mencoba GroupDocs.Parser tanpa membeli lisensi. Setelah diinstal tanpa lisensi, pustaka beroperasi dalam mode percobaan. Dalam mode ini, badge percobaan ditambahkan ke dokumen hasil, dan dokumen dipangkas menjadi 3 halaman pertama. Jika Anda ingin menguji GroupDocs.Parser tanpa batasan versi percobaan, Anda juga dapat meminta lisensi sementara selama 30 hari. Untuk detail lebih lanjut, [lihat](https://purchase.groupdocs.com/temporary-license/)."

    # items loop
    - question: "Lisensi apa yang tersedia?"
      answer: "Kami menawarkan beberapa jenis lisensi untuk memenuhi kebutuhan pengembang atau perusahaan tertentu. Jenis lisensi bergantung pada jumlah pengembang, jumlah lokasi situs pengembang, dan apakah Anda perlu menyediakan SDK/API kami kepada pelanggan akhir Anda. Sebagai alternatif, Anda dapat memilih lisensi Metered berdasarkan penggunaan bulanan produk. Pelajari lebih lanjut [di sini](https://purchase.groupdocs.com/pricing/parser/net/)."

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser API Parser Dokumen low‑code"
  description: "Integrasikan kemampuan parsing dokumen ke dalam aplikasi apa pun menggunakan REST API dan SDK berbasis cloud kami."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "Perintah cURL untuk Cloud API parser dokumen RESTful guna memparsing dokumen di berbagai format file populer yang didukung."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Ekstrak gambar, teks, informasi dokumen, atau bahkan memparsing dokumen apa pun dengan templat yang didefinisikan pengguna dalam aplikasi Microsoft .NET Anda."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "SDK Cloud untuk pengembang Java guna memparsing dokumen, mengekstrak informasi dokumen, dan data dalam aplikasi berbasis Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser Aplikasi Parser Dokumen Tanpa Kode"
  description: "Aplikasi parser dokumen berbasis web yang memungkinkan Anda mengekstrak data dari lebih dari 50 format file populer langsung di peramban Anda."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Aplikasi online gratis untuk memparsing Word, Excel, PowerPoint, PDF, & lebih dari 50 tipe dokumen lainnya."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Memparsing dokumen Word langsung dari peramban web Anda untuk mengekstrak gambar, teks, atau metadata."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Aplikasi parsing PDF gratis yang bekerja di platform atau perangkat apa pun tanpa batasan."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"


      


---