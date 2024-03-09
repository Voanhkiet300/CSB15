def thuc_nguyen(a):
    if a.is_integer():
        return f"{a} là số nguyên"
    else:
        return f"{a} không phải là số nguyên"

a = float(input("Nhập số: "))
print(thuc_nguyen(a))