import os
scr = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\a\\text.txt'

dst = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\b\\b.txt'

try:
    if os.path.exists(dst):
        print("There is already a file there")

    else:
        os.replace(scr, dst)
        print(scr + " was moved")
except FileNotFoundError:
    print(scr, "was not found")


# move folder:
scr_dir = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\a'
dst_dir = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\c'

try:
    if os.path.exists(dst_dir):
        print("There is already a folder there")

    else:
        os.replace(scr, dst_dir)
        print(scr_dir + " was moved")
except FileNotFoundError:
    print(scr_dir, "was not found")