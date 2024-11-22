---
############################# Static ############################
layout: "family"
date:  2024-02-13T17:01:03
draft: false

product: "Parser"
product_tag: "parser"

lang: id

############################# Head ############################
head_title: ".NET, Java, Cloud API & Aplikasi Parser Dokumen Online"
head_description: "Dapatkan solusi penguraian dokumen lengkap untuk .NET, Java dan aplikasi berbasis cloud. Ekstrak data dari format dokumen online menggunakan fitur drag and drop sederhana"

############################# Header ############################
title: "Solusi Penguraian Dokumen"
description: |
  API yang kuat untuk ekstraksi data dari berbagai format file.

  Parsing dokumen dengan upaya pengkodean minimal.

  Sesuaikan hasil penguraian.

############################# Supported Platforms ###############################
supported_platforms:
  enable: true
  head_title: "Pilih platform Anda"
  title: "Independensi platform"
  description: "Pustaka GroupDocs.Parser mendukung sistem operasi dan kerangka kerja berikut:"
  details_link_title: "Belajarlah lagi"

  items:
    # items loop
    - title: ".NET"
      description: GroupDocs.Parser untuk .NET 
      color: "blue"
      tag: "net"
      link: "/parser/net/"
      features_link: "https://docs.groupdocs.com/parser/net/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    .NET Framework 4.6.2 or higher
                    .NET Core 2.0 or higher
                    .NET 6.0 or higher
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    Microsoft Visual Studio
                    JetBrains Rider
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats
      

    # items loop
    - title: "Java"
      description: GroupDocs.Parser untuk Java
      color: "red"
      tag: "java"
      link: "/parser/java/"
      features_link: "https://docs.groupdocs.com/parser/java/system-requirements/"
      features:
          # features loop
          - rows: "4"
            content: |
                    Java 8 or higher
                    Kotlin
      
          # features loop
          - rows: "1"
            content: |
                    Windows, Linux, Mac OS
      
          # features loop
          - rows: "3"
            content: |
                    IntelliJ IDEA
                    Eclipse
                    NetBeans
      
          # features loop
          - rows: "1"
            content: |
                    50+ file formats

############################# Features ###############################
features:
  enable: true
  title: "GroupDocs.Parser sekilas"
  description: "API untuk penguraian data di PDF, Word, Excel dan lainnya."

  items:
    # items loop
    - icon: "text"
      title: "Ekstrak teks"
      content: "Ekstrak informasi tekstual dari berbagai format file."

    # items loop
    - icon: "image"
      title: "Ekstrak gambar"
      content: "Ambil konten visual dari berbagai sumber."

    # items loop
    - icon: "template"
      title: "Parsing data berdasarkan templat"
      content: "Buat templat khusus dan gunakan untuk mengurai informasi spesifik."

    # items loop
    - icon: "pdf"
      title: "Parsing PDF Formulir"
      content: "PDF Formulir adalah dokumen digital yang menampilkan kolom yang dapat diisi untuk interaksi pengguna."

############################# Code Samples ###############################
code_samples:
  enable: true
  title: "GroupDocs.Parser contoh kode"
  description: "Beberapa kasus penggunaan operasi GroupDocs.Parser umum di C# dan Java."

  items:
    # items loop
    - title: "Cara mengekstrak teks dari PDF dokumen"
      content: "GroupDocs.Parser API memudahkan pengembang C# mengekstrak teks dari dokumen dengan menerapkan beberapa langkah mudah."
      samples:
          # samples loop
          - language: "C#"
            color: "blue"
            content: |
              <pre>
              // Create an instance of Parser class
              using (var parser = new Parser(fileName))
              {
                  // Extract a text into the reader
                  using (var textReader = parser.GetText())
                  {
                      // Print a text from the document
                      Console.WriteLine(textReader?.ReadToEnd());
                  }
              }
              </pre>
          # samples loop
          - language: "Java"
            color: "red"
            content: |
              <pre>
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
              <pre>

############################# Supported Formats ###############################
formats:
  enable: true
  title: "50+ format file didukung"
  description: "GroupDocs.Parser memungkinkan operasi parser dalam berbagai kelompok format."

############################# Metrics ###############################
metrics:
  enable: false
  title: "Metrik terperinci dan wawasan statistik"
  description: "Jelajahi analisis menyeluruh terhadap tokoh-tokoh utama kami, yang menawarkan metrik komprehensif dan wawasan statistik mengenai pencapaian, pengaruh, dan ekspansi kami."

  items:
    # items loop
    - number: "50+"
      title: "Format yang didukung"
      content: "API ini mengakomodasi lebih dari 50 format file dan dokumen yang paling banyak digunakan."

    # items loop
    - number: "700k"
      title: "NuGet unduhan"
      content: "GroupDocs.Parser for .NET telah menerima lebih dari 800 ribu unduhan melalui pengelola paket NuGet."

    # items loop
    - number: "15k"
      title: "Unduhan Maven"
      content: "GroupDocs.Parser for Java telah mengumpulkan lebih dari 15 ribu unduhan dari repositori Maven kami."


############################# Customers ###############################
customers:
  enable: true
  title: "Pelanggan kami yang bahagia"
  description: "GroupDocs perpustakaan digunakan oleh merek-merek terkenal dan ternama di seluruh dunia."

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
  title: "Siap untuk memulai?"
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
  title: "Pertanyaan yang sering diajukan"
  description: "Jawaban atas pertanyaan yang paling sering diajukan."

  items:
    # items loop
    - question: "Apakah perpustakaan GroupDocs.Parser memerlukan perangkat lunak pihak ketiga lainnya untuk memanipulasi dokumen?"
      answer: "GroupDocs.Parser tidak memerlukan instalasi perangkat lunak eksternal apa pun seperti Adobe Acrobat, Microsoft Office, atau lainnya."

    # items loop
    - question: "Bisakah saya mencoba perpustakaan GroupDocs.Parser sebelum membelinya?"
      answer: "Ya, Anda dapat mencoba GroupDocs.Parser tanpa membeli lisensi. Setelah diinstal tanpa lisensi, perpustakaan berfungsi dalam mode uji coba. Dalam mode ini, lencana percobaan ditambahkan ke dokumen yang dihasilkan, dan dipotong menjadi 3 halaman pertama. Jika Anda ingin menguji GroupDocs.Parser tanpa batasan versi uji coba, Anda juga dapat meminta lisensi sementara selama 30 hari. Untuk lebih jelasnya, lihat [purchase.groupdocs.com/temporary-license/](https://purchase.groupdocs.com/temporary-license/)"

    # items loop
    - question: "Lisensi apa yang Anda miliki?"
      answer: "Kami menawarkan beberapa jenis lisensi untuk memenuhi kebutuhan pengembang atau perusahaan tertentu. Jenis lisensi bergantung pada jumlah pengembang, jumlah lokasi situs pengembang, dan apakah Anda perlu mengirimkan SDK/API kami ke pelanggan akhir Anda. Alternatifnya, Anda dapat memilih Lisensi terukur berdasarkan penggunaan bulanan produk. Pelajari lebih lanjut di [purchase.groupdocs.com/policies/](https://purchase.groupdocs.com/policies/)"

############################# Cloud Links ###############################
cloud_links:
  enable: true
  title: "GroupDocs.Parser API kode rendah"
  description: "Menggabungkan kemampuan pengurai dokumen ke dalam aplikasi apa pun menggunakan API berbasis cloud kami."
  
  items:
    # items loop
    - title: "GroupDocs.Parser Cloud for cURL"
      content: "perintah cURL untuk pengurai dokumen lengkap Cloud API untuk mengurai dokumen dalam berbagai format file populer yang didukung."
      icon: "groupdocs_parser-for-curl"
      link: "https://products.groupdocs.cloud/parser/curl"

    # items loop
    - title: "GroupDocs.Parser Cloud for .NET"
      content: "Ekstrak gambar, teks, informasi dokumen, atau bahkan parsing dokumen apa pun menggunakan templat yang ditentukan pengguna di aplikasi Microsoft Anda."
      icon: "groupdocs_parser-for-net"
      link: "https://products.groupdocs.cloud/parser/net"

    # items loop
    - title: "GroupDocs.Parser Cloud for Java"
      content: "Cloud SDK untuk Java pengembang untuk mengurai dokumen, mengekstrak informasi dan data dokumen dalam aplikasi berbasis Java."
      icon: "groupdocs_parser-for-java"
      link: "https://products.groupdocs.cloud/parser/java"

############################# App links ###############################
app_links:
  enable: true
  title: "GroupDocs.Parser Aplikasi NoCode"
  description: "Aplikasi berbasis web yang memungkinkan Anda melakukan parsing pada lebih dari 50 format file populer langsung di browser Anda."

  items:
    # items loop
    - title: "GroupDocs.Parser Total"
      content: "Aplikasi online gratis untuk mengurai Word, Excel, PowerPoint, PDF & 30+ jenis dokumen lainnya."
      icon: "groupdocs_parser-app"
      link: "https://products.groupdocs.app/parser/total"

    # items loop
    - title: "GroupDocs.Parser DOCX"
      content: "Parsing Word dokumen langsung dari browser web Anda untuk mengekstrak gambar, teks, atau metadata."
      icon: "groupdocs_words-app"
      link: "https://products.groupdocs.app/parser/docx"

    # items loop
    - title: "GroupDocs.Parser PDF"
      content: "Aplikasi parsing gratis yang berfungsi pada platform atau perangkat apa pun tanpa batasan apa pun."
      icon: "groupdocs_pdf-app"
      link: "https://products.groupdocs.app/parser/pdf"     


---