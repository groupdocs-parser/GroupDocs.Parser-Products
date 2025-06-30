


---
############################# Static ############################
layout: "format"
date:  2025-06-30T10:25:26
draft: false
lang: th
format: Xlsx
product: "Parser"
product_tag: "parser"
platform: ".NET"
platform_tag: "net"

############################# Head ############################
head_title: "ดึงลิงก์จากไฟล์ XLSX ในแอป C#"
head_description: "ใช้ GroupDocs.Parser เพื่อค้นหาและดึงลิงก์จากไฟล์ XLSX ใน C# โดยไม่ต้องใช้เครื่องมือหรือซอฟต์แวร์เพิ่มเติม."

############################# Header ############################
title: "ดึงลิงก์จาก XLSX โดยใช้ C#" 
description: "ค้นหาและดึง URL และลิงก์จาก PDF, Word, Excel และประเภทเอกสารอื่น ๆ โดยใช้ GroupDocs.Parser ในแอปพลิเคชัน .NET ของคุณ."
subtitle: "GroupDocs.Parser for .NET" 

header_actions:
  enable: true
  items:
    #  loop
    - title: "ดาวน์โหลดทดลองใช้ฟรี"
      link: "https://releases.groupdocs.com/parser/net/"
      
############################# About ############################
about:
    enable: true
    title: "เกี่ยวกับ API GroupDocs.Parser for .NET"
    link: "/parser/net/"
    link_title: "เรียนรู้เพิ่มเติม"
    picture: "about_parser.svg" # 480 X 400
    content: |
       [GroupDocs.Parser](/parser/net/) เป็น API การวิเคราะห์เอกสารที่หลากหลายสำหรับนักพัฒนาที่ใช้ .NET รองรับการดึงลิงก์, ข้อความ, รูปภาพ และเนื้อหาที่มีโครงสร้างจากหลายรูปแบบไฟล์ เช่น PDF, Word, Excel, HTML และอื่น ๆ — โดยไม่ต้องพึ่งพาซอฟต์แวร์ของบุคคลที่สาม.

############################# Steps ############################
steps:
    enable: true
    title: "ขั้นตอนในการดึงลิงก์จาก Xlsx ใน C#"
    content: |
      [GroupDocs.Parser](/parser/net/) ช่วยให้นักพัฒนาที่ใช้ .NET ดึงลิงก์จากไฟล์ XLSX โดยปฏิบัติตามขั้นตอนง่าย ๆ เหล่านี้:
      
      1. โหลดไฟล์ XLSX โดยใช้อินสแตนซ์ Parser.
      2. ตรวจสอบว่าเอกสารรองรับการดึงลิงก์.
      3. ดึงรายการลิงก์จากเอกสาร.
      4. วนซากผลลัพธ์และทำงานกับ URL ที่ดึงออกมา.
   
    code:
      platform: "net"
      copy_title: "คัดลอก"
      install:
        command: |
        command: "dotnet add package GroupDocs.Parser"
        copy_tip: "คลิกเพื่อคัดลอก"
        copy_done: "คัดลอกแล้ว"
      links:
        #  loop
        - title: "ตัวอย่างเพิ่มเติม"
          link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-.NET/"
        #  loop
        - title: "เอกสารประกอบ"
          link: "https://docs.groupdocs.com/parser/net/"
          
      content: |
        ```csharp {style=abap}
        // โหลดเอกสารที่มีลิงก์โดยใช้คลาส Parser
        using (Parser parser = new Parser("input.xlsx")) {

            // ตรวจสอบว่าไฟล์สนับสนุนการดึงลิงก์
            if (!parser.Features.Hyperlinks)
            {
                Console.WriteLine("การดึงลิงก์ไม่สามารถใช้ได้กับไฟล์นี้");
                return;
            }

            // ดึงข้อมูลลิงก์ที่ถูกดึงออกมาและประมวลผล
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks();

            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
            }
        }
        ```  

############################# More features ############################
more_features:
  enable: true
  title: "ความสามารถในการวิเคราะห์เอกสารขั้นสูง"
  description: "นอกเหนือจากการดึงลิงก์ GroupDocs.Parser ยังช่วยให้คุณสามารถดึงข้อความ, ข้อมูลเมตา, รูปภาพ และข้อมูลที่มีโครงสร้าง — รองรับการประมวลผลข้อมูลที่มีประสิทธิภาพ."
  image: "/img/parser/features_extract-hyperlink.webp" # 500x500 px
  image_description: "การตรวจจับลิงก์และการวิเคราะห์เอกสาร"
  features:
    # feature loop
    - title: "การตรวจจับลิงก์จากเอกสาร"
      content: "ดึง URL และคำอธิบายลิงก์จากเอกสารประเภท PDF, ไฟล์ Word, สเปรดชีต และอื่น ๆ ได้อย่างรวดเร็ว."

    # feature loop
    - title: "รองรับลิงก์เว็บและลิงก์ภายใน"
      content: "ตรวจจับและดึงทั้ง URL เว็บปกติและลิงก์ภายในเอกสารจากรูปแบบหลาย ๆ รูปแบบ."

    # feature loop
    - title: "ตัวเลือกการวิเคราะห์ที่ยืดหยุ่น"
      content: "ปรับแต่งการตั้งค่าการดึงข้อมูลเพื่อสแกนส่วนหรือหน้าที่เฉพาะเพื่อปรับปรุงประสิทธิภาพและความแม่นยำ."
      
  code_samples:
    # code sample loop
    - title: "วิธีดึงลิงก์จาก PDF โดยใช้ตัวเลือกลิงก์"
      content: |
        นี่คือตัวอย่างโค้ดที่แสดงวิธีดึงลิงก์ทั้งหมดจากไฟล์ PDF โดยใช้ตัวเลือกที่กำหนดเอง.
        {{< landing/code title="C#">}}
        ```csharp {style=abap}
        //  เริ่มต้น Parser ด้วยเอกสาร PDF
        using (Parser parser = new Parser("input.docx"))
        {
            // ตรวจสอบว่าการดึงลิงก์ได้รับการสนับสนุน
            if (!parser.Features.Hyperlinks)
            {
                return;
            }

            // ตั้งค่าตัวเลือกการดึงลิงก์เพื่อลดขอบเขตผลลัพธ์
            PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(380, 90), new Size(150, 50)));

            // ดึงข้อมูลลิงก์จากเอกสาร
            IEnumerable<PageHyperlinkArea> hyperlinks = parser.GetHyperlinks(options);

            // จัดการกับรายการลิงก์ที่ถูกดึงออกมา
            foreach (PageHyperlinkArea h in hyperlinks)
            {
                Console.WriteLine(h.Text);
                Console.WriteLine(h.Url);
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
    - title: "ดาวน์โหลด Nuget"
      link: "https://releases.groupdocs.com/parser/net/"
      color: "red"
        #  loop
    - title: "การอนุญาต"
      link: "https://purchase.groupdocs.com/pricing/parser/net/"
      color: "light"


############################# More Formats #####################
more_formats:
    enable: true
    title: "รูปแบบที่รองรับในการดึงลิงก์"
    exclude: "XLSX"
    description: "GroupDocs.Parser สามารถดึงลิงก์จากประเภทเอกสารที่หลากหลาย ดูด้านล่างสำหรับรูปแบบที่มักจะรองรับ."
    items: 
        # format loop 1
        - name: "解析 PDF"
          format: "PDF"
          link: "/parser/net/extract-hyperlink/pdf/"
          description: "(รูปแบบเอกสารแบบพกพา)"
          
        # format loop 2
        - name: "解析 DOCX"
          format: "DOCX"
          link: "/parser/net/extract-hyperlink/docx/"
          description: "(เอกสาร Word 2007+)"
          
        # format loop 3
        - name: "解析 PPTX"
          format: "PPTX"
          link: "/parser/net/extract-hyperlink/pptx/"
          description: "(รูปแบบการนำเสนอ Open XML)"
          
        # format loop 4
        - name: "解析 XLSX"
          format: "XLSX"
          link: "/parser/net/extract-hyperlink/xlsx/"
          description: "(สมุดงาน Open XML)"
          
        # format loop 5
        - name: "解析 TXT"
          format: "TXT"
          link: "/parser/net/extract-hyperlink/txt/"
          description: "(ไฟล์ข้อความ)"
          
        # format loop 6
        - name: "解析 RTF"
          format: "RTF"
          link: "/parser/net/extract-hyperlink/rtf/"
          description: "(รูปแบบข้อความที่มีความรวย)"
          
        # format loop 7
        - name: "解析 XML"
          format: "XML"
          link: "/parser/net/extract-hyperlink/xml/"
          description: "(ภาษาเครื่องหมายขยาย)"
          
        # format loop 8
        - name: "解析 EPUB"
          format: "EPUB"
          link: "/parser/net/extract-hyperlink/epub/"
          description: "(ไฟล์ eBook แบบเปิด)"
         
          

---