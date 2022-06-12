length = 6
e1 = [1,5]
e2 = [2,3]
e3 = [1,10]
e4 = [7,5]
e5 = [7,7]
e6 = [10,10]


length = int(input())
list_a = []
list_b = []
for i in range(0, length):
    line_i = [int(x) for x in input().split()]
    list_a.append(line_i[0])
    list_b.append(line_i[1])

    


list_e = [e1,e2,e3,e4,e5,e6]
list_a = [e1[0], e2[0], e3[0], e4[0], e5[0], e6[0]]
list_b = [e1[1], e2[1], e3[1], e4[1], e5[1], e6[1]]
# cover = [0,0]
# for e in list_e:


# def check_possible(comb_a, comb_b):
#     if comb_a[-1] < comb_b[0]:
#         return "YES"
#     else:
#         return "NO"


length = int(input())
list_a = []
list_b = []
for i in range(0, length):
    line_i = [int(x) for x in input().split()]
    list_a.append(line_i[0])
    list_b.append(line_i[1])

def find_min_position(list_a):
    min  = pow(10, 9)
    index_min = []
    for i in range(0, length):
        if list_a[i] < min:
            min = list_a[i]
            index_min = [i]
        elif list_a[i] == min:
            index_min.append(i)
    index_min = [index+1 for index in index_min]
    return index_min

def find_max_position(list_b):
    max  = 1
    index_max = []
    for i in range(0, length):
        if list_b[i] > max:
            max = list_b[i]
            index_max = [i]
        elif list_b[i] == max:
            index_max.append(i)
    index_max = [index+1 for index in index_max]
    return index_max


min_list = find_min_position(list_a)
max_list = find_max_position(list_b)
common = [i for i in min_list if i in max_list]

if len(common) == 0:
    print(-1)
else:
    print(common[0])

# def check_possible(comb_a, comb_b):
#     if comb_a[-1] < comb_b[0]:
#         return "YES"
#     elif comb_a[-1] == comb_b[0]:
#         if max(comb_b) == comb_b[0]:
#             return "NO"
#         else:
#             return "YES"
#     else:
#         return "NO"

print("ha")