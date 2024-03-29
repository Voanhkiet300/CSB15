
import time

import sys
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32

init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
# print(Fore.RED + 'some red text', file=stream)

end = 0
start = 0
#tạo hàm thuật toán
def thuat_toan():
  for i in range(1,11):
        print(i)

start = time.time()
thuat_toan()
end = time.time()
print(Fore.BLUE + f"{end-start}", Style.RESET_ALL)