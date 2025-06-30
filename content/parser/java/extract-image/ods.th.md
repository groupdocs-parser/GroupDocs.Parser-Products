


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:30
draft: false
lang: th
format: Ods
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "ดึงภาพจากไฟล์ ODS ในแอปพลิเคชัน Java"
head_description: "ด้วย GroupDocs.Parser คุณสามารถดึงภาพจากไฟล์ ODS ใน Java ได้อย่างมีประสิทธิภาพ โดยไม่ต้องใช้เครื่องมือของบุคคลที่สาม."

############################# Header ############################
title: "ดึงภาพจาก ODS โดยใช้ Java" 
description: "ดึงภาพที่ฝังอยู่จากไฟล์เช่น PDF, Word, Excel และอื่น ๆ โดยใช้ GroupDocs.Parser ในสภาพแวดล้อมการพัฒนา Java ของคุณ."
subtitle: "GroupDocs.Parser for Java" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "ดาวน์โหลดทดลองใช้ฟรี"
      link: "https://releases.groupdocs.com/parser/java/"
      
############################# About ############################
about:
    enable: true
    title: "GroupDocs.Parser for Java คืออะไร?"
    link: "/parser/java/"
    link_title: "เรียนรู้เพิ่มเติม"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) เป็น API สำหรับการวิเคราะห์ที่มีฟีเจอร์หลากหลาย ออกแบบมาสำหรับนักพัฒนา Java ช่วยในการดึงภาพ ข้อความ ลิงค์ และองค์ประกอบที่มีโครงสร้างจากไฟล์หลายรูปแบบ รวมถึง DOCX, XLSX, PDF, PNG, JPG และอื่น ๆ โดยไม่ต้องใช้ไลบรารีหรือแอปพลิเคชันภายนอก.

############################# Steps ############################
steps:
    enable: true
    title: "วิธีการดึงภาพจาก Ods ใน Java"
    content: |
      ปฏิบัติตามขั้นตอนเหล่านี้เพื่อดึงภาพจากเอกสาร ODS โดยใช้ [GroupDocs.Parser](/parser/java/) ในแอปพลิเคชัน Java ของคุณ:
      
      1. สร้างอ instance ของ Parser และโหลดไฟล์ ODS.
      2. ดึงข้อมูลภาพจากเอกสารที่โหลด.
      3. ใช้หรือส่งออกภาพที่ดึงมาได้ตามต้องการ.
   
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
        // เริ่มต้นตัว parser และโหลดเอกสารที่มีภาพโดยใช้ Parser
        try (Parser parser = new Parser("input.ods"))
        {
            // รวบรวมส่วนประกอบภาพทั้งหมดที่ฝังอยู่ในเอกสาร
            Iterable<PageImageArea> images = parser.getImages();

            // ข้ามการประมวลผลหากเอกสารไม่มีภาพ
            if (images == null) {
                return;
            }

            // จัดการกับแต่ละภาพตามที่ต้องการ
            for (PageImageArea image : images) {
                System.out.println(String.format("Page: %d, R: %s, Type: %s", image.getPage().getIndex(), 
                    image.getRectangle(), image.getFileType()));
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "ความสามารถในการวิเคราะห์เอกสารเพิ่มเติม"
  description: "นอกเหนือจากการดึงภาพแล้ว GroupDocs.Parser ยังช่วยให้คุณสามารถดึงเนื้อหาที่เป็นดิบ เช่น ข้อความ ลิงค์ เมตาดาต้า และข้อมูลที่มีโครงสร้างเพื่อการประมวลผลและการวิเคราะห์."
  image: "/img/parser/features_extract-image.webp" # 500x500 px
  image_description: "ดึงภาพและเนื้อหาจากเอกสาร"
  features:
    # feature loop
    - title: "ใช้งานได้กับรูปแบบที่หลากหลาย"
      content: "ดึงภาพจากประเภทเอกสารต่าง ๆ รวมถึง PDF, DOCX, PPTX, XLSX และรูปภาพ เช่น PNG, JPEG และ GIF."

    # feature loop
    - title: "รักษาความชัดเจนและความละเอียดของภาพ"
      content: "ภาพที่ดึงมาได้ทั้งหมดจะคงความละเอียดและประเภทไฟล์เดิมเพื่อให้มีคุณภาพและความสามารถในการใช้งานที่สอดคล้องกัน."

    # feature loop
    - title: "ตัวเลือกการกำหนดค่าที่ยืดหยุ่น"
      content: "ปรับแต่งกระบวนการดึงภาพโดยการกรองภาพตามประเภท ขนาด ดัชนีหน้า หรือรูปแบบไฟล์."
      
  code_samples:
    # code sample loop
    - title: "ดึงและบันทึกภาพจากไฟล์ PDF"
      content: |
        ตัวอย่างนี้แสดงวิธีการดึงภาพจากเอกสาร PDF และบันทึกภาพแต่ละภาพลงในอุปกรณ์ของคุณ.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  ใช้ Parser เพื่อเปิดไฟล์ PDF
        try (Parser parser = new Parser("input.pdf"))
        {
            // ดึงภาพจากเนื้อหาเอกสาร
            Iterable<PageImageArea> images = parser.getImages();

            // กำหนดค่าพารามิเตอร์ส่งออก เช่น รูปแบบ (เช่น JPEG หรือ PNG)
            ImageOptions options = new ImageOptions(ImageFormat.Png);

            // บันทึกรูปภาพที่ดึงมาได้ลงในไดเรกทอรีท้องถิ่น
            int imageNumber = 0;
            for (PageImageArea image : images)
            {
                image.save(Constants.getOutputFilePath(String.format("%d.png", imageNumber)), options);
                imageNumber++;
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
    title: "ประเภทไฟล์ที่รองรับสำหรับการดึงภาพ"
    exclude: "ODS"
    description: "GroupDocs.Parser รองรับการดึงภาพจากเอกสารและภาพหลากหลายประเภท สำรวจประเภทไฟล์ที่รองรับโดยทั่วไปด้านล่าง."
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/java/extract-image/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/java/extract-image/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/java/extract-image/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/java/extract-image/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 ODT"
          format: "ODT"
          link: "/parser/java/extract-image/odt/"
          description: "(เอกสารข้อความ OpenDocument)"
          
        # format loop 6
        - name: "解析 ODS"
          format: "ODS"
          link: "/parser/java/extract-image/ods/"
          description: "(สเปรดชีต OpenDocument)"
          
        # format loop 7
        - name: "解析 ODP"
          format: "ODP"
          link: "/parser/java/extract-image/odp/"
          description: "(การนำเสนอ OpenDocument)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/java/extract-image/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
          
        # format loop 9
        - name: "解析 FB2"
          format: "FB2"
          link: "/parser/java/extract-image/fb2/"
          description: "(eBook FictionBook)"
         
          

---