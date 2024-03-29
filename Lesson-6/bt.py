def bai1():
    random_number = [4, 2, 3, 1, 543, 654, 24, 765]
    number = 0
    for i in range(len(random_number)):
        for j in range(len(random_number)):
            if random_number[i]<random_number[j]:
                random_number[i], random_number[j] = random_number[j], random_number[i]
    print(random_number)

def bai2():
    name = ["John", "Lisa", "Mike", "Lisa", "Kate", "John"]
    for i, value in enumerate(name):
        count = name.count(value)
        if count>1:
            name.remove(name[i])
    print(name)
# bai2()

def bai3():
    list = ["adad", 3124, "dsah", 1423, 5674, "fseggd"]
    string = []
    int = []
    for i in list:
        if i.isalpha():
            string.append(i)
        elif i.isdigit():
            int.append(i)
bai3()