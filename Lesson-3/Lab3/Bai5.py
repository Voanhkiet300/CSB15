def dang_nhap():
    ten_tai_khoan = input("Nhập tên tài khoản: ")
    mat_khau = int(input("Nhập mật khẩu: "))

    if ten_tai_khoan == "admin" and mat_khau == 12345:
        return "Đăng nhập thành công, admin."
    else:
        return "Sai tên tài khoản hoặc mật khẩu"

print(dang_nhap())