def thuc_nguyen(a):
    if a.is_integer():
        return f"{a:.0f} là số nguyên"
    else:
        return f"{a:.0f} không phải là số nguyên"

a = float(input("Nhập số: "))
print(thuc_nguyen(a))