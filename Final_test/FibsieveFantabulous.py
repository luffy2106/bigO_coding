
dict_mattrix = dict()
dict_mattrix[1] = (1,1)
dict_mattrix[2] = (1,2)
dict_mattrix[3] = (2,2)
dict_mattrix[4] = (2,1)
dict_mattrix[5] = (3,1)
dict_mattrix[6] = (3,2)
dict_mattrix[7] = (3,3)
dict_mattrix[8] = (2,3)
dict_mattrix[9] = (1,3)
dict_mattrix[10] = (1,4)
dict_mattrix[11] = (2,4)
dict_mattrix[12] = (3,4)
dict_mattrix[13] = (4,4)
dict_mattrix[14] = (4,3)
dict_mattrix[15] = (4,2)
dict_mattrix[16] = (4,1)
dict_mattrix[17] = (5,1)
dict_mattrix[18] = (5,2)
dict_mattrix[19] = (5,3)
dict_mattrix[20] = (5,4)
dict_mattrix[21] = (5,5)
dict_mattrix[22] = (4,5)
dict_mattrix[23] = (3,5)
dict_mattrix[24] = (2,5)
dict_mattrix[25] = (1,5)


def hash(x):
    if x % 25 == 0:
        return 25
    else:
        return x % 25

T = int(input())
case = 0
for t in range(T):
    case+=1
    # x  = int(input())
    ans = dict_mattrix[hash(int(input()))]
    print("Case {}: {} {}".format(case, ans[0], ans[1]))