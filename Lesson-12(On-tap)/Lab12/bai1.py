scr = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\Lab12\\name.txt'

with open(scr, 'r') as file:
    a = file.readlines()
    print(f'List of names:\n- {'- '.join(a)}')