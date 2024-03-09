def ky_tu_so(a):
    if a.isdigit():
        return f"{a} is a digit"
    else:
        return f"{a} is not a digit"

a = input("Nhập một ký tự: ")
print(ky_tu_so(a))