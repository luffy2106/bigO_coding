N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
freq_a = [0] * (pow(10, 6) + 1)
freq_b = [0] * (pow(10, 6) + 1)
unique_a = 0
unique_b_in_a = 0
for a in A:
    if freq_a[a] == 0:
        unique_a += 1
    freq_a[a] += 1


for b in B:
    if freq_a[b] > 0:
        if freq_b[b] == 0:
            unique_b_in_a += 1
        else:
            continue
    else:
        unique_b_in_a += 1
    freq_b[b] += 1


print(unique_a - unique_b_in_a)
