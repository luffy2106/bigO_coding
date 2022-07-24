


    



T = int(input())
for t in range(T):
    N,M = map(int, input().split())
    line_t = list(map(int, input().split()))
    list_M = line_t[N:]
    set_N = set(line_t[:N])
    for m in list_M:
        if m in set_N:
            print("YES")
        else:
            print("NO")
            set_N.add(m)