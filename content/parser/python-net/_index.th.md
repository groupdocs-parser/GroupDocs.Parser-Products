---
############################# Static ############################
layout: "landing"
date: 2025-12-09T21:34:38
draft: false

lang: th
product: "Parser"
product_tag: "parser"
platform: "Python"
platform_tag: "python-net"

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
head_title: "GroupDocs.Parser for Python via .NET Document Parser SDK สำหรับ Python"
head_description: "Document Parser SDK ประสิทธิภาพสูงสำหรับ Python. สกัดข้อความ, รูปภาพ, metadata, barcodes, ตารางและข้อมูลอื่นจาก PDF, Word, Excel, อีเมลและรูปแบบเอกสารกว่า 50 แบบ"

############################# Header ############################
title: "Document Parser SDK สำหรับ Python"
description: "เพิ่มการแยกเอกสารที่เร็วและแม่นยำให้กับแอป Python ของคุณและสกัดข้อความ, รูปภาพ, metadata และข้อมูลเชิงโครงสร้างจากเอกสารและรูปภาพ"
words:
  for: "สำหรับ"

actions:
  hidden: true # Hide version 0 is released
  main: "PyPI ดาวน์โหลด"
  main_link: "https://pypi.org/project/groupdocs-parser-net/"
  alt: "การให้สิทธิ์ใช้"
  alt_link: "https://purchase.groupdocs.com/pricing/parser/python-net/"
  title: "พร้อมเริ่มต้นแล้วหรือยัง?"
  description: "ลองใช้ฟีเจอร์ของ GroupDocs.Parser ฟรีหรือขอรับใบอนุญาต"

release:
  enable: false
  title: "เวอร์ชัน {0} ปล่อยแล้ว"
  notes: "ดูว่ามีอะไรใหม่"
  downloads: "ดาวน์โหลด"

code:
  title: "สกัดข้อความโดยใช้ Python"
  more: "ตัวอย่างเพิ่มเติม"
  more_link: "https://github.com/groupdocs-parser/GroupDocs.Parser-for-Python-via-.NET/"
  install: "pip install groupdocs-parser-net"
  content: |
    ```python {style=abap}  
    from groupdocs.parser import Parser

    # โหลดเอกสาร
    with Parser("sample.pdf") as parser:
        # สกัดข้อความจากเอกสาร
        text = parser.GetText()

        # พิมพ์ข้อความที่สกัดทั้งหมด
        print(text)
    ```

############################# Overview ############################
overview:
  enable: true
  title: "GroupDocs.Parser อย่างคร่าวๆ"
  description: "Document Parser SDK สำหรับการแยกเอกสารที่ความแม่นยำสูงในแอปพลิเคชัน Python"
  features:
    # feature loop
    - title: "สกัดข้อมูลจากเอกสาร"
      content: "GroupDocs.Parser for Python via .NET API ช่วยให้คุณดึงข้อความ, metadata, และรูปภาพจากรูปแบบไฟล์หลากหลาย เช่น เอกสาร Office, อีเมล, ไฟล์แนบ และไฟล์บีบอัด เครื่องมือนี้ช่วยให้คุณเข้าถึงและประมวลผลข้อมูลที่มีค่าในไฟล์เหล่านี้ได้อย่างมีประสิทธิภาพสำหรับการใช้งานต่างๆ เช่น การวิเคราะห์ข้อมูล, การทำดัชนีของเครื่องมือค้นหา, หรือระบบจัดการเนื้อหา"

    # feature loop
    - title: "แยกเอกสาร"
      content: "สกัดส่วนประกอบต่าง ๆ เช่น ไฮเปอร์ลิงก์, ตาราง, QR code, barcode และข้อมูลจากแบบฟอร์ม PDF. นอกจากนี้ยังสามารถแยกข้อมูลที่ต้องการใด ๆ จากเอกสารโดยใช้เทมเพลตกำหนดเอง"

    # feature loop
    - title: "ปรับแต่งผลลัพธ์"
      content: "Python API ช่วยให้คุณดึงข้อมูลในรูปแบบต่าง ๆ เช่น raw, structured, HTML หรือ Markdown. นอกจากนี้ API ยังมีฟังก์ชันการค้นหาเพื่อหาคำหรือวลีเฉพาะในข้อความของเอกสาร"

############################# Platforms ############################
platforms:
  enable: true
  title: "ความเป็นอิสระของแพลตฟอร์ม"
  description: "GroupDocs.Parser for Python via .NET รองรับระบบปฏิบัติการ, เฟรมเวิร์กและตัวจัดการแพคเกจต่อไปนี้"
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
    - title: "VS Code"
      image: "vs_code"
    # platform loop
    - title: "ReSharper"
      image: "resharper"
    # platform loop
    - title: "macOS"
      image: "finder"
    # platform loop
    - title: "Linux"
      image: "linux"
    # platform loop
    - title: "NuGet"
      image: "nuget"

############################# File formats ############################
formats:
  enable: true
  title: "รูปแบบไฟล์ที่รองรับ"
  description: |
    GroupDocs.Parser for Python via .NET รองรับการทำงานกับ [รูปแบบไฟล์](https://docs.groupdocs.com/parser/python-net/supported-document-formats/) ต่อไปนี้.
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
  title: "คุณลักษณะของ GroupDocs.Parser for Python via .NET"
  description: "สกัดข้อมูลจาก PDF, เอกสาร Office, รูปภาพและรูปแบบอื่น ๆ อย่างรวดเร็วและแม่นยำด้วย Python Document Parser SDK ของเรา"

  items:
    # feature loop
    - icon: "text"
      title: "สกัดข้อความ"
      content: "สกัดข้อมูลข้อความจากรูปแบบไฟล์ต่าง ๆ เช่น เอกสาร Office, ไฟล์ PDF และรูปภาพ เพื่อความง่ายในการอ่านและวิเคราะห์"

    # feature loop
    - icon: "image"
      title: "สกัดรูปภาพ"
      content: "ดึงเนื้อหาภาพจากแหล่งต่าง ๆ เช่น เอกสาร Office, ไฟล์ PDF เพื่อการเข้าถึงและใช้งานที่สะดวก"

    # feature loop
    - icon: "qr"
      title: "สแกน QR Code"
      content: "ตรวจหาและถอดรหัส QR code ที่อยู่ในเอกสาร Office, ไฟล์ PDF หรือเนื้อหาภาพเพื่อการรับข้อมูลที่มีประสิทธิภาพ"

    # feature loop
    - icon: "email"
      title: "สกัดข้อมูลจากไฟล์แนบอีเมลและไฟล์บีบอัด"
      content: "รวบรวมข้อมูลที่มีค่าจากข้อความอีเมล, ไฟล์แนบ และแหล่งข้อมูลที่บีบอัดเพื่อการวิเคราะห์และใช้งานอย่างมีประสิทธิภาพ"

    # feature loop
    - icon: "table"
      title: "สกัดตาราง"
      content: "ระบุและสกัดข้อมูลในรูปแบบตารางจากเอกสาร PDF เพื่อการวิเคราะห์และใช้งานอย่างเป็นระบบ"

    # feature loop
    - icon: "hyperlink"
      title: "สกัดไฮเปอร์ลิงก์"
      content: "ค้นหาและดึงลิงก์ไฮเปอร์และที่อยู่อีเมลภายในเอกสาร office หรือไฟล์ PDF เพื่อการเข้าถึงที่มีประสิทธิภาพ"

    # feature loop
    - icon: "pdf"
      title: "ประมวลผลฟอร์ม PDF"
      content: "ฟอร์ม PDF คือเอกสารดิจิทัลที่มีช่องกรอกข้อมูลให้ผู้ใช้กรอกข้อมูลได้อย่างอิเล็กทรอนิกส์ API ของ Python สามารถใช้เพื่อดึงข้อมูลจากฟอร์มเหล่านี้เพื่อการประมวลผลที่มีประสิทธิภาพ"

    # feature loop
    - icon: "template"
      title: "ประมวลผลข้อมูลด้วยเทมเพลต"
      content: "สร้างเทมเพลตที่กำหนดเองและใช้ร่วมกับ API ของ Python เพื่อแยกข้อมูลเฉพาะจากไฟล์ PDF ลดความซับซ้อนของกระบวนการดึงข้อมูล"

    # feature loop
    - icon: "search"
      title: "ค้นหาข้อความในเอกสาร"
      content: "ค้นหาคำหรือรูปแบบเฉพาะในเอกสารได้อย่างรวดเร็ว"


############################# Code samples ############################
code_samples:
  enable: true
  title: "ตัวอย่างโค้ด"
  description: "นอกเหนือจากการดึงข้อความพื้นฐาน นี่คือกรณีการใช้งานที่พบบ่อยที่สุดสำหรับการดึงข้อความ ภาพ และเมตาดาต้าอย่างรวดเร็ว"
  items:
    # code sample loop
    - title: "ค้นหาข้อความในเอกสาร"
      content: |
        ตัวอย่างนี้แสดงวิธีการค้นหาวลีเฉพาะในเอกสาร PDF และพิมพ์ตำแหน่งที่พบ
        {{< landing/code title="ค้นหาข้อความในเอกสารด้วย Python">}}
        ```python {style=abap}
        from groupdocs.parser import Parser

        # โหลดเอกสาร
        with Parser("sample.pdf") as parser:
            # พิมพ์ดัชนีหน้าและสี่เหลี่ยมที่พบวลี
            for area in parser.Search("Total Amount"):
                # พิมพ์ดัชนีหน้าและสี่เหลี่ยมที่พบวลี
                print(f"Page {area.PageIndex}, Rectangle: {area.Rectangle}")
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "ดึงรูปภาพจากเอกสาร"
      content: |
        ตัวอย่างนี้แสดงวิธีการดึงรูปภาพจากเอกสาร PDF และบันทึกลงไฟล์
        {{< landing/code title="ดึงรูปภาพจากเอกสารด้วย Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # โหลดเอกสาร
        with Parser("sample.docx") as parser:
            # ดึงรูปภาพจากเอกสาร
            images = parser.GetImages()

            # บันทึกรูปภาพลงไฟล์
            index = 1
            for image in images:
                image.Save(f"image_{index}.png")
                index += 1
        ```
        {{< /landing/code >}}
    # code sample loop
    - title: "ดึงเมตาดาต้าจากเอกสาร"
      content: |
        ตัวอย่างนี้แสดงวิธีการดึงเมตาดาต้าจากเอกสาร PDF และพิมพ์ออก
        {{< landing/code title="ดึงเมตาดาต้าจากเอกสารด้วย Python">}}
        ```python {style=abap}    
        from groupdocs.parser import Parser

        # โหลดเอกสาร
        with Parser("sample.pdf") as parser:
            # ดึงเมตาดาต้าจากเอกสาร
            metadata = parser.GetMetadata()

            # พิมพ์เมตาดาต้า
            for item in metadata:
                print(f"{item.Name}: {item.Value}")
        ```
        {{< /landing/code >}}
---
