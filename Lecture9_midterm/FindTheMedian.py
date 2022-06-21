n = int(input())
list_n = list(map(int, input().split()))

list_n.sort()

index = int(n/2)

print(list_n[index])