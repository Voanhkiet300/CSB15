import os

scr = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\a\\text.txt'



if os.path.exists(scr):
    print("File existed")
    if os.path.isfile(scr):
        print("This is a file")
    elif os.path.isdir(scr):
        print("This is an folder")
else:
    print("This location doesn't exist")