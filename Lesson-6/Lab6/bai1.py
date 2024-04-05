arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

add2 = []

for i in range(len(arr)):
    add2.append(arr[i]+2)
print("add 2\t\t: ", add2)


multiply2 = []

for i in range(len(arr)):
    multiply2.append(arr[i]*2)
print("Multiply by 2\t: ", multiply2)



dich2 = []

for i in range(2, len(arr)):
    dich2.append(arr[i])
dich2.append(arr[0])
dich2.append(arr[1])
print("Shift 2\t\t: ", dich2)