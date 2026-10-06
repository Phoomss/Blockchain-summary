# Blockchain summary

ทั้งสองเวอร์ชันอยู่ใน repository เดียว และใช้เนื้อหาชุดเดียวกัน

- ธีมมืด: `index.html` หรือ `dist/dark.html`
- เวอร์ชันอ่านสบาย: `dist/index.html`
- มีลิงก์สลับเวอร์ชันบนทั้งสองหน้า

## แก้ไขเนื้อหา

แก้บทที่ 1–15 ใน `สรุปสอบปลายภาค_เน้นอัตนัย.md` และบทที่ 16–23 ใน
`exam-site/deep-dive.md` แล้วสร้างทั้งสองเวอร์ชันพร้อมกัน:

```sh
python3 -m pip install -r requirements.txt
python3 build.py
```

`exam-site/build.py` เป็นทางเข้าที่เรียก build เดียวกันสำหรับคำสั่งเดิม
ไฟล์ HTML และ Markdown ใน `dist/` รวมถึง `index.html` ที่รากเป็นผลลัพธ์ build
ให้แก้เนื้อหาที่ไฟล์ต้นฉบับแทนการแก้ผลลัพธ์โดยตรง

รูปแบบหน้าทั้งสองอยู่ใน `exam-site/dark-template.html` และ
`exam-site/light-template.html`; CSS ของเวอร์ชันอ่านสบายอยู่ใน `exam-site/style.css`
หากเพิ่มหรือลบบท ให้ปรับ section และสารบัญใน dark template ให้ตรงกับบทด้วย

## เปิดอ่านในเครื่อง

```sh
python3 -m http.server 8000
```

เปิด `http://localhost:8000/` หรือ `http://localhost:8000/dist/`
การเผยแพร่ใช้ `.openai/hosting.json` ที่รากและ output ใน `dist/`
โดยเก็บทั้งสองหน้าไว้ในการเผยแพร่เดียวกัน
