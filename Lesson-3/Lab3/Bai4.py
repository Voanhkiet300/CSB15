def check(n):
    if n % 3 == 0 and n % 5 == 0:
        return f"{n} chia hết cho 3 và n chia hết cho 5"
    elif n % 3 == 0 and n % 5 != 0:
        return f"{n} chia hết cho 3 nhưng không chia hết cho 5"
    elif n % 3 != 0 and n % 5 == 0:
        return f"{n} chia hết cho 5 nhưng không chia hết cho 3"
    else:
        return f"{n} không chia hết cho 3 và không chia hết cho 5"

n = int(input("Nhập một số nguyên: "))
print(check(n))