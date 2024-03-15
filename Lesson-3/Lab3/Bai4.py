# def check(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return f"{n} chia hết cho 3 và n chia hết cho 5"
#     elif n % 3 == 0 and n % 5 != 0:
#         return f"{n} chia hết cho 3 nhưng không chia hết cho 5"
#     elif n % 3 != 0 and n % 5 == 0:
#         return f"{n} chia hết cho 5 nhưng không chia hết cho 3"
#     else:
#         return f"{n} không chia hết cho 3 và không chia hết cho 5"

# n = int(input("Nhập một số nguyên: "))
# print(check(n))


n = int(input("Nhập một số nguyên: "))
print(f"{n} chia het cho 3 và n chia hết cho 5") if n %3==0 and n%5==0 else print(f"{n} chia het cho 3 nhưng không chia het cho 5") if n%3==0 and n%5!=0 else print(f"{n} chia het cho 5 nhưng không chia het cho 3") if n%3!=0 and n%5==0 else print(f"{n} không chia het cho 3 và không chia het cho 5")