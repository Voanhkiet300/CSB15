prices =    {'Iphone12'     : 28000000,
            'Samsung N10'   : 16000000,
            'Oppo 93'       :  7500000,
            'Vsmart'        :  7400000,
            'Vivo'          :  4200000}


def chuong_trinh_1():
    n = input("Input name of a phone: ")
    print(f"Price of {n}: {prices[n]}")

def chuong_trinh_2():
    n = input("Input your budget: ")
    print("Phones that fit your budget:")
    for key, value in prices.items():
        if value <= int(n):
            print(f"- {key}: {value}")

chuong_trinh_1()
# chuong_trinh_2()