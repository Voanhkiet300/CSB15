numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
numbers_2 = {'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15, 'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20}
number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X','XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

# bai 1:
def bai1(numbers):
    n = input("Input a Roman number: ")

    if n in numbers:
        print(f'Arabic number: {numbers[n]}')
    else:
        print('Not found.')


# bai 2:
def bai2():
    for k, v in numbers_2.items():
        numbers.update({k: v})
    print(numbers)

# bai 3:
def bai3():
    # for i in range(len(number_list)):
    #     new_list = 
    numbers_dic = {number_list[i]: i+1 for i in range(len(number_list))}
    bai1(numbers_dic)


bai1(numbers)
bai2()
bai3()