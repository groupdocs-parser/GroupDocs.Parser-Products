


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:38
draft: false
lang: th
format: Docx
product: "Parser"
product_tag: "parser"
platform: "Java"
platform_tag: "java"

############################# Head ############################
head_title: "ดึงตารางจากเอกสาร DOCX ในแอปพลิเคชัน Java"
head_description: "ดึงข้อมูลตารางที่มีโครงสร้างจากไฟล์ DOCX ในแอปพลิเคชัน Java ด้วย GroupDocs.Parser—ไม่ต้องใช้เครื่องมือภายนอก."

############################# Header ############################
title: "ดึงข้อมูลตารางจาก DOCX โดยใช้ Java" 
description: "ตรวจจับและดึงตารางจากรูปแบบต่างๆ เช่น PDF, DOCX และ XLSX อย่างไร้รอยต่อด้วย GroupDocs.Parser ในการทำงานของ Java ของคุณ."
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
    title: "แนะนำ API ของ GroupDocs.Parser for Java"
    link: "/parser/java/"
    link_title: "เรียนรู้เพิ่มเติม"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/java/) คือ API การดึงข้อมูลที่มีฟีเจอร์ครบถ้วนสำหรับแพลตฟอร์ม Java ช่วยให้นักพัฒนาสามารถวิเคราะห์ตาราง ข้อความ กราฟิก ลิงก์ และข้อมูลที่มีโครงสร้างจากไฟล์ PDF เอกสาร Word แผ่น Excel งานนำเสนอ PowerPoint และอื่นๆ ได้อย่างแม่นยำ—โดยไม่จำเป็นต้องใช้ปลั๊กอินของบุคคลที่สาม.

############################# Steps ############################
steps:
    enable: true
    title: "วิธีการดึงตารางจาก Docx ใน Java"
    content: |
      ในการวิเคราะห์ตารางจากเอกสาร DOCX โดยใช้ [GroupDocs.Parser](/parser/java/) ให้ปฏิบัติตามขั้นตอนเหล่านี้ในสภาพแวดล้อม Java ของคุณ:
      
      1. สร้างอินสแตนซ์ของ Parser และโหลดไฟล์ DOCX ที่ต้องการ.
      2. ตรวจสอบว่าไฟล์นั้นรองรับการดึงตารางที่มีโครงสร้าง.
      3. ใช้ API เพื่อตรวจจับองค์ประกอบตารางจากเอกสาร.
      4. ใช้ข้อมูลที่ดึงมาในการวิเคราะห์ การทำรายงาน หรือระบบอัตโนมัติ.
   
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
        // โหลดเอกสารที่มี Parser ซึ่งรวมถึงองค์ประกอบตาราง
        try (Parser parser = new Parser("input.docx"))
        {
            // ตรวจสอบว่าเอกสารประเภทนั้นอนุญาตให้ตรวจจับตาราง
            if (!parser.getFeatures().isTables()) {
                System.out.println("เพิ่มตรรกะสำหรับไฟล์ที่ไม่รองรับตาราง");
                return;
            }

            // กำหนดกฎสำหรับการตีความโครงสร้างตาราง
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // ตั้งค่าพารามิเตอร์สำหรับการดึงตาราง
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            //  ดำเนินการดึงตารางจากเอกสารที่โหลดแล้ว
            Iterable<PageTableArea> tables = parser.getTables(options);

            //  ประมวลผลแต่ละตารางที่ดึงออกมาจากผลลัพธ์
            for (PageTableArea t : tables) 
            {
            }
        }
        ```            

############################# More features ############################
more_features:
  enable: true
  title: "เครื่องมือการดึงข้อมูลขั้นสูง"
  description: "นอกเหนือจากการอ่านตารางแล้ว GroupDocs.Parser ยังรองรับการจับข้อมูลพื้นฐาน องค์ประกอบภาพ เมตาดาต้าแบบฝัง และวัตถุที่มีโครงสร้างเพื่อเสริมสร้างงานประมวลผลเอกสาร."
  image: "/img/parser/features_extract-table.webp" # 500x500 px
  image_description: "การดึงเนื้อหาที่มีโครงสร้างและข้อมูลตาราง"
  features:
    # feature loop
    - title: "การวิเคราะห์ตารางอย่างแม่นยำในหลายรูปแบบ"
      content: "รองรับการดึงตารางจากประเภทเอกสารมาตรฐาน เช่น PDF, Word, Excel และ HTML อย่างมีความแม่นยำสูง."

    # feature loop
    - title: "อ่านโครงสร้างตารางจากแหล่งที่หลากหลาย"
      content: "ดึงข้อมูลตารางจากแผ่นงาน เอกสาร และรายงาน ในขณะที่ยังรักษาโครงสร้างและการจัดตำแหน่ง."

    # feature loop
    - title: "การตั้งค่าการดึงตารางที่ปรับแต่งได้"
      content: "ควบคุมการตรวจจับเลย์เอาต์ จัดการส่วนหัวและส่วนท้าย และปรับแต่งการดึงข้อมูลด้วยตัวเลือกการกำหนดค่าที่ยืดหยุ่น."
      
  code_samples:
    # code sample loop
    - title: "ตัวอย่าง: ดึงตารางจากเอกสาร Excel"
      content: |
        ตัวอย่างนี้แสดงวิธีการดึงและวนลูปผ่านเนื้อหาตารางในไฟล์ Excel (XLSX) โดยใช้ GroupDocs.Parser.
        {{< landing/code title="Java">}}
        ```java {style=abap}
        //  เริ่มต้น Parser ด้วยไฟล์ Excel
        try (Parser parser = new Parser("input.pdf"))
        {
            // ออกจากระบบหากการดึงข้อมูลตารางไม่รองรับสำหรับเอกสารนี้
            if (!parser.getFeatures().isTables())
            {
                return;
            }

            // ใช้กฎเพื่อค้นหาเลย์เอาต์ตาราง
            TemplateTableLayout layout = new TemplateTableLayout(
                    java.util.Arrays.asList(new Double[]{50.0, 95.0, 275.0, 415.0, 485.0, 545.0}),
                    java.util.Arrays.asList(new Double[]{325.0, 340.0, 365.0, 395.0}));

            // กำหนดค่าการตั้งสำหรับการดึงตาราง
            PageTableAreaOptions options = new PageTableAreaOptions(layout);

            // เรียกใช้กระบวนการดึงข้อมูล
            Iterable<PageTableArea> tables = parser.getTables(options);

            // วนลูปผ่านโครงสร้างตารางที่วิเคราะห์ทั้งหมด
            for (PageTableArea t : tables)
            {
                // วนซ้ำแต่ละแถวภายในตาราง
                for (int row = 0; row < t.getRowCount(); row++)
                {
                    // ประมวลผลแต่ละเซลล์ในแถวปัจจุบัน
                    for (int column = 0; column < t.getColumnCount(); column++) 
                    {
                        // เข้าถึงและอ่านเนื้อหาของเซลล์ปัจจุบัน
                        PageTableAreaCell cell = t.getCell(row, column);
                        if (cell != null)
                        {
                            // แสดงค่าข้อความของเซลล์ตารางแต่ละเซลล์
                            System.out.print(cell.getText());
                            System.out.print(" | ");
                        }
                    }
                }
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
    title: "ประเภทเอกสารที่รองรับสำหรับการดึงตาราง"
    exclude: "DOCX"
    description: "GroupDocs.Parser ให้การตรวจจับตารางที่เชื่อถือได้จากหลายประเภทไฟล์ นี่คือรายการรูปแบบเอกสารที่ได้รับการสนับสนุนอย่างกว้างขวางสำหรับการดึงตาราง."
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/java/extract-table/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/java/extract-table/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/java/extract-table/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/java/extract-table/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/java/extract-table/txt/"
          description: "(ไฟล์ข้อความ)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/java/extract-table/rtf/"
          description: "(รูปแบบข้อความที่มีความรวย)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/java/extract-table/xml/"
          description: "(ภาษาเครื่องหมายขยาย)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/java/extract-table/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
         
          

---