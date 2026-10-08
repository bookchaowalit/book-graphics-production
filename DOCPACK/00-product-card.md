---
title: Book Graphics Production — Product Card
doc_id: CARD-book-graphics-production
doc_type: product-card
verdict: merge
version: 0.1
date: 2026-10-08
status: ร่างเพื่อพิจารณา
owner: Product owner (Book Dev)
---

# Book Graphics Production — Product Card

## 1. สรุปคุณค่าในหนึ่งประโยค

แปลง JSON request เป็นกราฟิก SVG ที่แก้ไขได้และ PNG preview แบบ deterministic — แต่ README ระบุเองว่าเจ้าของงานนี้คือ `book-production-platform` แล้ว และ repo นี้เป็น fork ที่ถูกแช่แข็ง

## 2. ปัญหาและผู้ใช้เป้าหมาย

- ปัญหา: ผลิตกราฟิก (quote card, product card, announcement) หลายขนาดพร้อมฟอนต์ไทยที่ถูกต้องโดยไม่ใช้บริการภายนอก
- ผู้ใช้: operator คอนเทนต์ของ Solo Empire

## 3. สิ่งที่ทำได้จริงตอนนี้

- template V1A: `quote_card`, `product_card`, `announcement` × square/portrait/story
- CLI batch, render ผ่าน Edge/Chrome headless ในเครื่อง (shaping ภาษาไทย), QA, manifest แบบ replay-safe
- ปฏิเสธ URL/traversal/SVG ไม่ปลอดภัย; benchmark 30 output แบบ synthetic
- package `graphics-production-ir` + service `graphics-production-api` พร้อม test

## 4. หลักฐานสถานะ

| รายการ | ค่า (ตรวจจาก repository) |
|---|---|
| Stack | ไม่พบ manifest ของ stack (ตัวตรวจไม่ระบุ) |
| Commits | 8 (แรก 2026-09-24 → ล่าสุด 2026-10-01) |
| Source | 29 ไฟล์ / 1,803 บรรทัด |
| Tests | 15 ไฟล์ |
| CI | 1 workflow |
| Deploy config | ไม่มี |
| Live URL | ไม่มี |
| README | 62 บรรทัด (`Book Graphics Production`) |
| โครงสร้างซ้ำ (template family) | 1 repo ที่มี structure signature เดียวกัน |

README: "frozen fork kept until it is archived: safety fixes are mirrored here, new features are not"

## 5. คุณค่าและจุดต่าง

- คุณค่าทั้งหมดย้ายไปอยู่ใน `book-production-platform` (`graphics_production`, `graphics_ir`) ซึ่งมี artifact แยกต่อ batch และ parity check (`scripts/graphics_fork_parity.py`)

## 6. ช่องว่างสำคัญ

- การรักษา fork ทำให้ต้อง mirror safety fix สองที่
- ไม่มีเหตุผลเชิงผลิตภัณฑ์ให้คง repo แยก

## 7. คำตัดสิน

**`merge`** — ซ้ำกับ canonical `book-production-platform` ตามที่ README ประกาศเอง ให้รวมแล้ว archive จะไม่เปลี่ยน verdict เว้นแต่ platform ถูกยกเลิก

## 8. ขั้นต่อไป

1. รัน `graphics_fork_parity.py` ใน platform เพื่อยืนยันว่าไม่มี module ที่ fork มีแต่ platform ไม่มี
2. archive repo นี้หลังเจ้าของอนุมัติ

## การอนุมัติ

| บทบาท | สถานะ | วันที่ | ลงนาม |
|---|---|---|---|
| Product owner (Book Dev) | รอพิจารณา | — | ________ |

## แหล่งข้อมูล

- `README.md`
- `services/graphics-production-api/graphics_production/cli.py`
- `(book-dev) bookchaowalit/book-production-platform/README.md`
