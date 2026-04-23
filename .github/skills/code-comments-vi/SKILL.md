---
name: code-comments-vi
description: "Thêm comment tiếng Việt giải thích lý do và luồng hoạt động của code. Dùng khi: viết comment bằng tiếng Việt, giải thích tại sao viết code như vậy, giải thích logic đằng sau quyết định, không dùng khi: chỉ cần mô tả cái gì (what) - đó là documentation, không phải comment giải thích."
user-invocable: true
tags:
  - comments
  - vietnamese
  - code-understanding
---

# Code Comments (Tiếng Việt)

## Mục tiêu

Thêm comment vào code Python để giải thích:
1. **Tại sao** (why) - Lý do quyết định, logic đằng sau
2. **Cách hoạt động** (how) - Luồng xử lý, flow của code

## Nguyên tắc

### KHÔNG viết
- Comment mô tả cái gì (what) - đã thấy trong code rồi
- Comment dạng giới thiệu: `# Hàm này làm gì`
- Comment trùng lặp với tên biến/hàm

### NÊN viết
- **Lý do tại sao**: Tại sao dùng thuật toán này? Tại sao xử lý theo thứ tự này?
- **Quyết định quan trọng**: Tại sao chọn cách này thay vì cách khác?
- **Edge cases**: Tại sao cần xử lý trường hợp đặc biệt?
- **Hạn chế**: Tại sao không dùng cách tốt hơn (nếu có lý do)?

## Quy trình

1. **Đọc code** - Hiểu logic và flow
2. **Xác định điểm cần comment**:
   - Điểm rẽ nhánh (if/else, try/except)
   - Quyết định quan trọng về cấu trúc
   - Logic không tường minh
   - Edge cases được xử lý
3. **Viết comment** - Ngắn gọn, tiếng Việt, tập trung vào "tại sao"

## Ví dụ

```python
# KHÔNG NÊN - Comment what, không phải why:
def load_documents(source_path):
    # Hàm load tài liệu từ đường dẫn
    ...

# NÊN - Comment giải thích tại sao:
def load_documents(source_path):
    # Dùng glob thay vì os.walk vì cần filter theo extension
    # trước khi đọc, giảm số lần gọi hệ thống
    ...
```

## Áp dụng

Khi được gọi, sẽ:
1. Đọc file code được chọn
2. Thêm comment tiếng Việt vào các vị trí cần giải thích
3. Giữ nguyên code, chỉ thêm comment