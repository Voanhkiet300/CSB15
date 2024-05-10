
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil


scr = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\a\\text.txt'

dst = 'C:\\Users\\Anh Kiet\\Documents\\Computer Scientist\\CSB\\Lesson-12(On-tap)\\a'

shutil.copyfile(scr, dst + 'test_copyfile.txt')
shutil.copy(scr, dst + 'test_copy.txt')
shutil.copy2(scr, dst + 'test_copy2.txt')

