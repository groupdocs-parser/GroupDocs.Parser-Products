---
############################# Static ############################
layout: "landing"
date: 2025-12-09T14:10:41
draft: false

lang: th
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
head_title: "GroupDocs.Parser for Java Document Parser SDK สำหรับ Java"
head_description: "Document Parser SDK ที่มีประสิทธิภาพสูงสำหรับ Java ดึงข้อความ, ภาพ, metadata, บาร์โค้ด, ตารางและข้อมูลอื่น ๆ จาก PDF, Word, Excel, อีเมล และรูปแบบเอกสารกว่า 50 ประเภท"

############################# Header ############################
title: "Document Parser SDK สำหรับ Java"
description: "เพิ่มการแยกวิเคราะห์เอกสารที่รวดเร็วและแม่นยำให้กับแอป Java ของคุณและดึงข้อความ, ภาพ, metadata และข้อมูลโครงสร้างจากเอกสารและภาพ."
words:
  for: "สำหรับ"

actions:
  main: "Maven ดาวน์โหลด"
  main_link: "https://releases.groupdocs.com/java/repo/com/groupdocs/groupdocs-parser/"
  alt: "การให้สิทธิ์ใช้"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/java/"
  title: "พร้อมเริ่มต้นแล้วหรือยัง?"
  description: "ลองใช้ฟีเจอร์ของ GroupDocs.Parser ฟรีหรือขอรับใบอนุญาต"

release:
  title: "เวอร์ชัน {0} ปล่อยแล้ว"
  notes: "ดูว่ามีอะไรใหม่"
  downloads: "ดาวน์โหลด"

code:
  title: "แยกวิเคราะห์เนื้อหาเอกสารอย่างรวดเร็วด้วย SDK"
  more: "ตัวอย่างเพิ่มเติม"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
  install: |
    <dependency>
      <groupId>com.groupdocs</groupId>
      <artifactId>groupdocs-parser</artifactId>
      <version>{0}</version>
    </dependency>
  content: |
    ```java {style=abap}  
    // ส่งไฟล์ต้นทางไปยังอินสแตนซ์ของ Parser
    try (Parser parser = new Parser("source.pdf"))
    {
        // ส่งข้อความเอกสารไปยัง TextReader
        try (TextReader reader = parser.getText())
        {
            // ประมวลผลข้อความเอกสาร
            System.out.println(reader == null 
                ? "" 
                : reader.readToEnd());
        }
    }
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser อย่างคร่าวๆ"
  description: "Document Parser SDK สำหรับการแยกวิเคราะห์เอกสารความแม่นยำสูงในแอปพลิเคชัน Java"
  features:
    # feature loop
    - title: "ดึงข้อมูลจากเอกสาร"
      content: "API ของ GroupDocs.Parser for Java ช่วยให้คุณสามารถดึงข้อความ, metadata, และภาพจากหลากหลายรูปแบบไฟล์ เช่น เอกสาร Office, อีเมล, ไฟล์แนบ และไฟล์อัดบีบนี้ได้ เครื่องมือนี้มีประสิทธิภาพช่วยให้คุณเข้าถึงและประมวลผลข้อมูลที่มีคุณค่าในไฟล์เหล่านี้ได้อย่างมีประสิทธิภาพสำหรับการประยุกต์ใช้งานต่าง ๆ เช่น การวิเคราะห์ข้อมูล, การจัดทำดัชนีเครื่องมือค้นหา, หรือระบบการจัดการเนื้อหา."

    # feature loop
    - title: "ประมวลผลเอกสาร"
      content: "ดึงเอาตัวองค์ประกอบต่าง ๆ เช่น ไฮเปอร์ลิงก์, ตาราง, QR โค้ด, บาร์โค้ด และข้อมูลจากแบบฟอร์ม PDF อีกทั้งยังสามารถประมวลผลข้อมูลใด ๆ ที่ต้องการจากเอกสารโดยใช้เทมเพลตแบบกำหนดเองได้"

    # feature loop
    - title: "ปรับแต่งผลลัพธ์"
      content: "Java API ทำให้คุณสามารถดึงข้อมูลในรูปแบบต่าง ๆ เช่น ดิบ, โครงสร้าง, HTML หรือ Markdown นอกจากนี้ API ยังมีฟังก์ชันการค้นหาเพื่อค้นหาคำหรือวลีเฉพาะภายในข้อความของเอกสาร"

############################# Platforms ############################
platforms:
  enable: true
  title: "ความเป็นอิสระของแพลตฟอร์ม"
  description: "GroupDocs.Parser for Java รองรับระบบปฏิบัติการ, เฟรมเวิร์กและตัวจัดการแพ็คเกจต่อไปนี้"
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
  title: "รูปแบบไฟล์ที่รองรับ"
  description: |
    GroupDocs.Parser for Java รองรับการทำงานกับ [รูปแบบไฟล์](https://docs.groupdocs.com/parser/java/supported-document-formats/) ต่อไปนี้.
  groups:
    # group loop
    - color: "green"
      content: |
        ### รูปแบบ Microsoft Office
        * **Word:** DOCX, DOC, DOCM, DOT, DOTX, DOTM, RTF
        * **Excel:** XLSX, XLS, XLSM, XLSB, XLTM, XLT, XLTM, XLTX, XLAM, SXC, SpreadsheetML
        * **PowerPoint:** PPT, PPTX, PPS, PPSX, PPSM, POT, POTM, POTX, PPTM
    # group loop
    - color: "blue"
      content: |
        ### รูปภาพและรูปแบบอื่น ๆ
        * **พกพา:** PDF 
        * **รูปภาพ:** JPG, BMP, PNG, TIFF, GIF
        * **รูปแบบ Office อื่น ๆ:** ODT, OTT, OTS, ODS, ODP, OTP, ODG
      # group loop
    - color: "red"
      content: |
        ### รูปแบบอื่น ๆ
        * **เว็บ:** HTML, MHTML 
        * **ไฟล์เก็บข้อมูล:** ZIP, TAR, 7Z 
        * **อีบุ๊ค:** CHM, EPUB, FB2, MOBI 
        
        

############################# Features ############################
features:
  enable: true
  title: "GroupDocs.Parser for Java คุณลักษณะ"
  description: "ดึงข้อมูลจาก PDF, เอกสาร Office, ภาพและรูปแบบอื่น ๆ อย่างรวดเร็วและแม่นยำด้วย Java Document Parser SDK ของเรา"

  items:
    # feature loop
    - icon: "text"
      title: "สกัดข้อความ"
      content: "สกัดข้อมูลข้อความจากรูปแบบไฟล์ต่าง ๆ เช่น เอกสาร Office, ไฟล์ PDF และภาพ เพื่อความอ่านง่ายและการวิเคราะห์"

    # feature loop
    - icon: "image"
      title: "สกัดรูปภาพ"
      content: "ดึงเนื้อหาภาพจากแหล่งต่าง ๆ เช่น เอกสาร Office, ไฟล์ PDF เพื่อการเข้าถึงและใช้ประโยชน์ได้สะดวก"

    # feature loop
    - icon: "qr"
      title: "สแกน QR Code"
      content: "ตรวจจับและถอดรหัส QR Code ที่อยู่ในเอกสาร Office, ไฟล์ PDF หรือเนื้อหาภาพ เพื่อการเรียกคืนข้อมูลอย่างมีประสิทธิภาพ"

    # feature loop
    - icon: "email"
      title: "สกัดข้อมูลจากไฟล์แนบอีเมลและไฟล์เก็บข้อมูล"
      content: "รวบรวมข้อมูลที่มีคุณค่าจากข้อความอีเมล, ไฟล์แนบ และแหล่งข้อมูลที่บีบอัดเพื่อการวิเคราะห์และใช้งานอย่างมีประสิทธิภาพ."

    # feature loop
    - icon: "table"
      title: "ดึงตาราง"
      content: "ระบุและดึงข้อมูลแบบตารางจากเอกสาร PDF เพื่อการวิเคราะห์และการใช้งานอย่างเป็นระบบ."

    # feature loop
    - icon: "hyperlink"
      title: "ดึงไฮเปอร์ลิงก์"
      content: "ค้นหาและดึงไฮเปอร์ลิงก์และที่อยู่อีเมลภายในเอกสาร Office หรือไฟล์ PDF เพื่อการเข้าถึงอย่างมีประสิทธิภาพ."

    # feature loop
    - icon: "pdf"
      title: "แยกวิเคราะห์แบบฟอร์ม PDF"
      content: "แบบฟอร์ม PDF คือเอกสารดิจิทัลที่มีฟิลด์ที่สามารถกรอกได้เพื่อการโต้ตอบของผู้ใช้ ให้ผู้ใช้ป้อนข้อมูลแบบอิเล็กทรอนิกส์ได้ API ของ .NET สามารถใช้เพื่อดึงข้อมูลจากแบบฟอร์มเหล่านี้เพื่อการประมวลผลที่มีประสิทธิภาพ."

    # feature loop
    - icon: "template"
      title: "แยกวิเคราะห์ข้อมูลโดยใช้เทมเพลต"
      content: "สร้างเทมเพลตที่กำหนดเองและใช้ร่วมกับ API ของ .NET เพื่อนำมาวิเคราะห์ข้อมูลเฉพาะจากไฟล์ PDF ทำให้กระบวนการดึงข้อมูลง่ายขึ้น."

    # feature loop
    - icon: "search"
      title: "ค้นหาข้อความในเอกสาร"
      content: "ค้นหาคำหรือรูปแบบเฉพาะในเอกสารได้อย่างรวดเร็ว."


############################# Code samples ############################
code_samples:
  enable: true
  title: "ตัวอย่างโค้ด"
  description: "ตัวอย่างการใช้ทั่วไปของการดำเนินการ GroupDocs.Parser for Java"
  items:
    # code sample loop
    - title: "ดึงภาพจากเอกสาร PDF"
      content: |
        GroupDocs.Parser for Java ทำให้นักพัฒนา Java สามารถดึงภาพจาก [เอกสาร](https://docs.groupdocs.com/parser/java/extract-images-from-documents/) ได้ง่าย:
        {{< landing/code title="สกัดภาพจากเอกสาร PDF ด้วย Java">}}
        ```java {style=abap}
        // สร้างอินสแตนซ์ของคลาส Parser
        try (Parser parser = new Parser("source.pdf"))
        {
            // สกัดภาพ
            Iterable<PageImageArea> images = parser.getImages();

            // ตรวจสอบว่ามีการสกัดข้อมูลหรือไม่
            if (images == null) {
                return;
            }

            // วนลูปผ่านภาพ
            for (PageImageArea image : images) {
                // พิมพ์ดัชนีหน้าที่, สี่เหลี่ยมและประเภทของภาพ
                System.out.println(String.format("Page: %d, R: %s, Type: %s", 
                    image.getPage().getIndex(), image.getRectangle(), image.getFileType()));
            }
        }
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "ดึงบาร์โค้ดจากภาพ"
      content: |
        ใช้ API Java ของเราเพื่อสกัด [บาร์โค้ด](https://docs.groupdocs.com/parser/java/extract-barcodes-from-document/) จากรูปภาพ:
        {{< landing/code title="สกัดบาร์โค้ดจากภาพด้วย Java">}}
        ```java {style=abap}   
        // โหลดภาพต้นฉบับเข้าสู่ Parser
        try (Parser parser = new Parser("source.jpg")){

            // ตรวจสอบว่าไฟล์รองรับการสกัดบาร์โค้ดหรือไม่
            if (!parser.getFeatures().isBarcodes()) {

                // สกัดบาร์โค้ดจากไฟล์
                Iterable<PageBarcodeArea> barcodes = parser.getBarcodes();

                // วนลูปผ่านบาร์โค้ด
                for (PageBarcodeArea barcode : barcodes) {
                    // พิมพ์ดัชนีหน้า
                    System.out.println("Page: " + barcode.getPage().getIndex());
                    // พิมพ์ค่าบาร์โค้ด
                    System.out.println("Value: " + barcode.getValue());
                }
            }
        }
        ```
        {{< /landing/code >}}

---
