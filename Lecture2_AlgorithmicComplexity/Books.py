


N, T = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
print(A)
count = 0
time = 0
for a in A:
    if time + a > T:
        break
    else:
        time = time + a
        count+=1

print(count)

x = [1, 1, 1, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 9, 9, 10, 10, 12, 12, 15, 16, 17, 18, 18, 18, 20, 20, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 23, 23, 23, 24, 25, 25]