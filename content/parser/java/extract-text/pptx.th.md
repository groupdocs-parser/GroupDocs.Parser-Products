


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:45
draft: false
lang: th
format: Pptx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "ดึงข้อความจากไฟล์ PPTX ในแอปพลิเคชัน Java"
head_description: "ใช้ GroupDocs.Parser เพื่อดึงเนื้อหาข้อความที่ไม่มีโครงสร้างหรือมีโครงสร้างจากเอกสาร PPTX ใน Java โดยไม่ต้องพึ่งพาส่วนเสริมภายนอก"

############################# Header ############################
title: "ดึงข้อความจาก PPTX โดยใช้ Java" 
description: "ดึงข้อความที่อ่านได้หรือมีโครงสร้างจากไฟล์เช่น PDF, Word, Excel และอื่น ๆ โดยใช้ GroupDocs.Parser ในโครงการพัฒนา Java ของคุณ"
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "ดาวน์โหลดรุ่นทดลองใช้ฟรี"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "แนะนำ API GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "เรียนรู้เพิ่มเติม"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) เป็นโปรแกรมจัดการเอกสารที่มีความสามารถและขยายตัวได้ ออกแบบมาสำหรับนักพัฒนาที่ใช้ Java โดยมีฟังก์ชันการทำงานที่ช่วยให้สามารถดึงข้อความ ตาราง รูปภาพ และส่วนประกอบที่มีโครงสร้างจากฟอร์แมตต่าง ๆ เช่น PDF, DOCX, XLSX, PPTX และอื่น ๆ โดยไม่ต้องพึ่งพาเครื่องมือภายนอก

############################# Steps ############################
steps:
    enable: true
    title: "วิธีการดึงข้อความจาก Pptx โดยใช้ Java"
    content: |
      ทำตามขั้นตอนด้านล่างเพื่อดึงข้อความจากไฟล์ PPTX โดยใช้ [GroupDocs.Parser](/parser/java/) ภายในโครงการ Java ของคุณ:
      
      1. โหลดเอกสาร PPTX โดยใช้คลาส Parser
      2. ดำเนินการดึงข้อความจากเนื้อหาไฟล์
      3. ตรวจสอบว่าข้อความถูกรับคืนอย่างถูกต้องหรือไม่
      4. ใช้ข้อมูลข้อความในระบบค้นหา การวิเคราะห์ หรือระบบอัตโนมัติ
   
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
        // เริ่มต้น Parser ด้วยเอกสารของคุณ
        try (Parser parser = new Parser("input.pptx"))
        {
            // อ่านและดึงข้อมูลข้อความทั้งหมด
            try (TextReader reader = parser.getText())
            {
                // ส่งคืน null หากไม่มีเนื้อหาข้อความ
                // รวมข้อความที่ดึงเข้าไปในกระบวนการทำงานของคุณ
                System.out.println(reader == null ? 
                    "ข้ามรูปแบบการดึงข้อความที่ไม่รองรับ" : reader.readToEnd());
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "ฟังก์ชันการดึงข้อความที่หลากหลาย"
  description: "GroupDocs.Parser ไม่เพียงแต่ดึงข้อความแบบธรรมดา - ยังรองรับการดึงรูปภาพ เมตาและข้อมูลที่มีโครงสร้างเพื่อเสริมการทำงานกับเนื้อหา"
  image: "/img/parser/features_extract-text.webp" # 500x500 px
  image_description: "ดึงและจัดระเบียบเนื้อหาข้อความจากเอกสาร"
  features:
    # feature loop
    - title: "ทำงานกับรูปแบบเอกสารมากมาย"
      content: "จับข้อความทั้งที่เป็นดิบและมีโครงสร้างจาก DOCX, XLSX, PPTX, PDF, HTML และรูปแบบต่าง ๆ"

    # feature loop
    - title: "ดึงข้อความจากเนื้อหาภาพและข้อความ"
      content: "วิเคราะห์ข้อความจากเอกสารที่สแกน สไลด์ สเปรดชีต และประเภทไฟล์อื่น ๆ ในขณะรักษาโครงสร้างที่เข้าใจได้"

    # feature loop
    - title: "ควบคุมรายละเอียดการดึงข้อมูล"
      content: "กำหนดขอบเขตหน้าที่ต้องการ โซนเลย์เอาต์ และพารามิเตอร์ความแม่นยำสำหรับการวิเคราะห์ข้อความที่ละเอียด"
      
  code_samples:
    # code sample loop
    - title: "ตัวอย่าง: การดึงเนื้อหาข้อความจากเอกสาร PPTX"
      content: |
        ตัวอย่างนี้แสดงถึงการดึงบล็อกข้อความพร้อมกับพิกัดเชิงพื้นที่จากการนำเสนอ PowerPoint โดยใช้ GroupDocs.Parser
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  โหลดไฟล์ PPTX ของคุณด้วย API Parser
        try (Parser parser = new Parser("input.pptx"))
        {
            // รับเขตข้อความที่เป็นรูปทรงสี่เหลี่ยมทั้งหมด
            IEnumerable<PageTextArea> areas = parser.GetTextAreas();

            // ออกจากโปรแกรมหากฟังก์ชันนี้ไม่รองรับ
            if (areas == null)
            {
                return;
            }

            // วนลูปผ่านพื้นที่ข้อความตามหน้า
            for (PageTextArea a : areas)
            {
                // ประมวลผลบล็อกข้อความแต่ละบล็อกพร้อมหมายเลขหน้าและสี่เหลี่ยมพิมพ์
                System.out.println(String.format("Page: %d, R: %s, Text: %s", a.getPage().getIndex(), a.getRectangle(), a.getText()));
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
    title: "ประเภทไฟล์ที่รองรับสำหรับการดึงข้อความ"
    exclude: "PPTX"
    description: "GroupDocs.Parser สามารถดึงเนื้อหาข้อความจากรูปแบบไฟล์และรูปภาพต่าง ๆ ได้ ด้านล่างนี้คือประเภทที่ใช้งานบ่อยที่สุดที่รองรับ"
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/java/extract-text/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/java/extract-text/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/java/extract-text/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/java/extract-text/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/java/extract-text/txt/"
          description: "(ไฟล์ข้อความ)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/java/extract-text/rtf/"
          description: "(รูปแบบข้อความที่มีความรวย)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/java/extract-text/xml/"
          description: "(ภาษาเครื่องหมายขยาย)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/java/extract-text/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
         
          

---