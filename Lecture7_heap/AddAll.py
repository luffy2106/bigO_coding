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
    while len(h) > 0:
        top = h[0]
        heapq.heappop(h)
        order_num.append(top)
    print(order_num)
    total = 0
    for i in range(0, len(order_num) - 1):
        total = total + order_num[i] + order_num[i + 1]

    list_total.append(total)

for total in list_total:
    print(total)
