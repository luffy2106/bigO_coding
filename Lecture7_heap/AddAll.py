import heapq

list_total = []
while True:
    N = int(input())
    if N == 0:
        break
    numbers = [int(x) for x in input().split(" ")]
    # total = []
    h = []
    order_num = []
    for num in numbers:
        heapq.heappush(h, num)

    count = 0
    list_sum = []
    while len(h) > 1:
        top_first = h[0]
        heapq.heappop(h)
        top_second = h[0]
        heapq.heappop(h)
        min_sum = top_first + top_second
        heapq.heappush(h, min_sum)
        list_sum.append(min_sum)
    total = sum(list_sum)
    list_total.append(total)

for total in list_total:
    print(total)
