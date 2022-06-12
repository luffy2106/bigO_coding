
per_a = 3
per_b = 3
list_a = [1,2,3]
list_b = [3,4,5]
"""
# Excess timeout

from itertools import combinations

def compare_list(comb_a, comb_b):
    if max(comb_a) < min(comb_b):
        return True
    else:
        return False
comb_a = combinations(list_a, per_a)
comb_b = combinations(list_b, per_b)

def check_possilbe(comb_a, comb_b):
    for a in comb_a:
        for b in comb_b:
            if compare_list(a, b):
                return "YES"
    return "NO"
print(check_possilbe(comb_a, comb_b))
"""

def compare_list(comb_a, comb_b):
    if max(comb_a) < min(comb_b):
        return True
    else:
        return False




left = []
def find_per(list_num, left, n):
    for i in range(0, len(list_num)):
        left.append(list_num[i])
        list_num = [x for x in list_num]

