import msvcrt
import random
import os


print("== THE ESCAPE GAME ==")
print("Use W,A,S,D to move (P)layer.")
print("Find (K)ey first then exit through the (D)oor.")
print("Press any key to start...")

ch = msvcrt.getch().decode('utf-8')



finish = False
key = False



os.system('cls')
map = []
def print_map(map, row, col):
    for i in range(col):
        for j in range(row):
            print(map[i][j], end=" ")
        print()

        


row = 10
col = 5
for i in range(col):
    map.append([])
for i in range(col):
    for j in range(row):
        map[i].append("-")
map[0][0] = "P"
P_row = 0
P_col = 0
K_row = random.randint(1, row-1)
K_col = random.randint(1, col-1)
map[K_col][K_row] = "K"
D_row = random.randint(1, row-1)
D_col = random.randint(1, col-1)
while D_row == K_row and D_col == K_col:
    D_row = random.randint(1, row-1)
    D_col = random.randint(1, col-1)
map[D_col][D_row] = "D"
print_map(map, row, col)


def check_K():
    if P_row == K_row and P_col == K_col:
        return True
    else:
        return False
    
def check_end():
    if P_row == D_row and P_col == D_col:
        return True
    else:
        return False
while finish == False:

    ch = msvcrt.getch().decode('utf-8')

    if ch == "w" and P_col>0:
        map[P_col][P_row] = "-"
        P_col -= 1
        map[P_col][P_row] = "P"
    elif ch == "s" and P_col<col-1:
        map[P_col][P_row] = "-"
        P_col += 1
        map[P_col][P_row] = "P"
    elif ch == "a" and P_row>0:
        map[P_col][P_row] = "-"
        P_row -= 1
        map[P_col][P_row] = "P"
    elif ch == "d" and P_row<row-1:
        map[P_col][P_row] = "-"
        P_row += 1
        map[P_col][P_row] = "P"

    os.system('cls')
    print_map(map, row, col)
    if check_K():
        key = True
    end = check_end()
    if end == True and key == True:
        print("You win")
        finish = True
    elif end == True and key == False:
        print("You lose")
        finish = True