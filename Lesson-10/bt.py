import math
# input: {'1': 1, '2': 5, '3': 9}
# out: Max: {'3': 9}
def gtln (dic):
    max = -math.inf
    maxKey = ''
    for i in dic:
        if max < dic[i]:
            maxKey = i
            max = dic[i]
    print(f"Max: ({maxKey} : {max})")
gtln({'1': -1, '2': 5, '3': 9})