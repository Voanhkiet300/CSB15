from datetime import datetime
now = datetime.now()
print(now)

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
scr = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\Lab12\\input-logs.txt'
with open(scr, 'a') as file:
    file.write(f'== Inputs at {now} ==\n{b}\n')