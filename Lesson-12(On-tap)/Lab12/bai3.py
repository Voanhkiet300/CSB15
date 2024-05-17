a = ['']
print('== Input file content below ==')
a.append(input())
count = 1
while a[count] != '':
    a.append(input())
    count += 1
del a[0]
del a[len(a)-1]
b = '\n'.join(a)

with open('user-inputs.txt', 'w') as file:
    file.write(b)