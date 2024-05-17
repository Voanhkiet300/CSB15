import os
import shutil

scr = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\c\\c.txt'

# xoa file
# try:
#     os.remove(scr)
# except FileNotFoundError:
#     print('File not found!')
# else:
#     print('File deleted')


# xoa folder
path_dir = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\c'
try:
    os.rmdir(path_dir)
except FileNotFoundError:
    print('Folder not found!')
except PermissionError:
    print('You do not have permission')
except OSError:
    print('Folder can not delete by this function')
    shutil.rmtree(path_dir)
    print('Deleted file and folder')
else:
    print('Folder deleted')