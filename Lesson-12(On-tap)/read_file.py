

scr = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\a\\text.txt'
text = 'Hello World\n'*5
text2 = "llldqkfkqfqw"


# 'r' Đọc file (read) Báo lỗi nếu file không tồn tại

with open(scr, 'r') as file:
    file.read()


# 'w' Ghi file (write) Báo lỗi nếu file không tồn tại
# with open(scr, 'w') as file:
#     file.write(text2)


# 'x' Tạo file mới (exclusive create) Báo lỗi nếu file không tồn tại
# with open(scr, 'x') as file:
#     file.write(text) # Bao loi do da co file

# 'a' thêm nội dung (append) Tạo mới nếu file không tồn tại
with open(scr, 'a') as file:
    file.write(text)

