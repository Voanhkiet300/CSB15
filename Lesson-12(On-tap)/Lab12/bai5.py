scr = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\Lab12\\question-bank.txt'

b = []
with open(scr, 'r') as file:
    a = file.read()
    b = a.split('\n')
c = [b[i].split(',') for i in range(len(b))]
correct = 0

print('Give the correct answers to get points.')

for i in c:
    a = input(f'{i[0]}')
    if a == i[1]:
        correct += 1

print(f'== You get {correct}/{len(c)} points ==')
