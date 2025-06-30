


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:24
draft: false
lang: th
format: Rtf
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "ดึงลิงก์ใช้งานจากไฟล์ RTF ในแอพ Java"
head_description: "ใช้ GroupDocs.Parser เพื่อค้นหาและดึงลิงก์ URL จากเอกสาร RTF ในโปรเจค Java—ไม่ต้องใช้ซอฟต์แวร์เพิ่มเติม."

############################# Header ############################
title: "ดึงลิงก์ใช้งานจาก RTF ด้วย Java" 
description: "ดึงลิงก์เว็บและลิงก์ใช้งานออกจากไฟล์ PDF, เอกสาร Word, แผ่น Excel และเอกสารอื่น ๆ โดยใช้ GroupDocs.Parser ในสภาพแวดล้อม Java ของคุณ."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "ดาวน์โหลดเวอร์ชันทดลองใช้ฟรี"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "เกี่ยวกับ API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "เรียนรู้เพิ่มเติม"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) เป็น API การดึงข้อมูลที่มีประสิทธิภาพ ออกแบบมาสำหรับนักพัฒนา Java มันมีเครื่องมือสำหรับการดึงลิงก์ใช้งาน, ข้อมูลที่มีโครงสร้าง, รูปภาพ, และข้อความจากรูปแบบที่นิยมเช่น DOCX, XLSX, PDF, HTML และอื่น ๆ — ทั้งหมดนี้ไม่ต้องใช้ปลั๊กอินภายนอก.

############################# Steps ############################
steps:
    enable: true
    title: "วิธีการดึงลิงก์ใช้งานจาก Rtf ใน Java"
    content: |
      [GroupDocs.Parser](/parser/java/) ทำให้การดึงลิงก์ใช้งานจากไฟล์ RTF ในแอพ Java เป็นเรื่องง่ายด้วยขั้นตอนเหล่านี้:
      
      1. เปิดไฟล์ RTF โดยใช้ตัวอย่างของ Parser.
      2. ตรวจสอบว่าการดึงลิงก์ใช้งานสามารถใช้ได้กับรูปแบบไฟล์นี้.
      3. ดึงลิงก์ใช้งานทั้งหมดโดยใช้วิธีที่เหมาะสม.
      4. วนรอบผลลัพธ์และประมวลผลแต่ละลิงก์ตามที่ต้องการ.
   
    code:
      platform: "net"
      copy_title: "คัดลอก"
      install:
        command: |
          <dependencies>
            <dependency>
              <groupId>com.groupdocs</groupId>
              <artifactId>groupdocs-parser</artifactId>
              <version>{0}</version>
            </dependency>
          </dependencies>

          <repositories>
            <repository>
              <id>repository.groupdocs.com</id>
              <name>GroupDocs Repository</name>
              <url>https://repository.groupdocs.com/repo/</url>
            </repository>
          </repositories>
        copy_tip: "คลิกเพื่อคัดลอก"
        copy_done: "คัดลอกแล้ว"
      links:
        #  loop
        - title: "ตัวอย่างเพิ่มเติม"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Java/"
        #  loop
        - title: "เอกสารประกอบ"
          link: "https://docs.groupdocs.com/parser/java/"
          
      content: |
        ```java {style=abap}
        // โหลดไฟล์ที่อาจมีลิงก์ใช้งานโดยใช้ Parser
        try (Parser parser = new Parser("input.rtf")) {

            // ตรวจสอบว่าเอกสารรูปแบบสนับสนุนการวิเคราะห์ลิงก์ใช้งานหรือไม่
            if (!parser.getFeatures().isHyperlinks()) {
                System.out.println("การดึงลิงก์ใช้งานไม่สามารถใช้ได้กับไฟล์นี้");
                return;
            }

            // ดึงและใช้ข้อมูลลิงก์ใช้งานจากเอกสาร
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks();

            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "เครื่องมือการวิเคราะห์เอกสารที่ครอบคลุม"
  description: "นอกเหนือจากการดึงลิงก์ใช้งาน, GroupDocs.Parser ยังช่วยให้คุณสามารถรวบรวมเนื้อหาที่มีประโยชน์อื่น ๆ เช่น ข้อความธรรมดา, สื่อที่ฝังตัว, และข้อมูลที่มีโครงสร้างสำหรับใช้ในเวิร์กโฟลว์อัตโนมัติ."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "การดึงลิงก์ใช้งานและการวิเคราะห์เอกสาร"
  features:
    # feature loop
    - title: "การตรวจจับลิงก์ที่แม่นยำ"
      content: "จับลิงก์ใช้งานทุกประเภทจากเลย์เอาต์เอกสารที่แตกต่างกัน รวมถึงข้อความที่สามารถคลิกได้และ URL ที่ซ่อนอยู่."

    # feature loop
    - title: "ทำงานกับเอกสารและเนื้อหาเว็บ"
      content: "ดึงลิงก์จากไฟล์ PDF, DOCX, XLSX, HTML, และไฟล์ภาพที่มีลิงก์ใช้งานฝังอยู่."

    # feature loop
    - title: "พฤติกรรมการดึงข้อมูลที่ปรับแต่งได้"
      content: "ปรับปรุงวิธีที่ลิงก์ใช้งานถูกดึงออกโดยใช้ตัวเลือกเช่น ระยะหน้า, ประเภทลิงก์, หรือการกรองเนื้อหา."
      
  code_samples:
    # code sample loop
    - title: "ตัวอย่าง: การดึงลิงก์ใช้งานจาก PDF ด้วยตัวเลือกที่ปรับแต่ง"
      content: |
        ตัวอย่างนี้แสดงวิธีการดึงลิงก์ทั้งหมดจากไฟล์ PDF โดยใช้การตั้งค่าการดึงลิงก์.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  เปิด PDF โดยใช้คลาส Parser
        try (Parser parser = new Parser("input.docx"))
        {
            // ตรวจสอบว่าการสนับสนุนลิงก์ใช้งานเปิดใช้งานสำหรับเอกสารนี้หรือไม่
            if (!parser.getFeatures().isHyperlinks()) {
                return;
            }

            // ใช้ตัวเลือกเพื่อต filtr ลิงก์
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // ใช้ parser เพื่อรับข้อมูลลิงก์ใช้งาน
            Iterable<PageHyperlinkArea> hyperlinks = parser.getHyperlinks(options);

            // วนรอบลิงก์และจัดการตามความเหมาะสม
            for (PageHyperlinkArea h : hyperlinks) {
                System.out.println(h.getText());
                System.out.println(h.getUrl());
            }
        }
        ```
        {{< /landing/code >}}


############################# Actions ############################

actions:
  enable: true
  title: "พร้อมเริ่มต้นหรือยัง?"
  description: "ลองฟีเจอร์ของ GroupDocs.Parser ฟรี หรือติดต่อขอใบอนุญาต"
  items:
    #  loop
    - title: "ดาวน์โหลด Maven"
      link: "https://releases.groupdocs.com/parser/java/"
      color: "red"
        #  loop
    - title: "การอนุญาต"
      link: "https://purchase.groupdocs.com/pricing/parser/java/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "รูปแบบเอกสารที่รองรับการดึงลิงก์ใช้งาน"
    exclude: "RTF"
    description: "ด้วย GroupDocs.Parser, คุณสามารถดึงลิงก์ใช้งานจากหลายรูปแบบไฟล์ที่ใช้อย่างแพร่หลาย ด้านล่างเป็นรายการรูปแบบที่มักจะรองรับ."
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/java/extract-hyperlink/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/java/extract-hyperlink/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/java/extract-hyperlink/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/java/extract-hyperlink/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/java/extract-hyperlink/txt/"
          description: "(ไฟล์ข้อความ)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/java/extract-hyperlink/rtf/"
          description: "(รูปแบบข้อความที่มีความรวย)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/java/extract-hyperlink/xml/"
          description: "(ภาษาเครื่องหมายขยาย)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/java/extract-hyperlink/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
         
          

---