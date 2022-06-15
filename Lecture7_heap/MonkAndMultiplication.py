"""
1. keep putting element to heap-max
2. during the time heap is building, keep taking the top elements in the heap and calculate the product
"""

import heapq

N = int(input())
A = [int(x) for x in input().split()]


class PQEntry:
    """
    Use priority queue as max-heap
    """

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


h = []  # our heap
for x in A:
    heapq.heappush(h, PQEntry(x))
    if len(h) < 3:
        print(-1)
    else:
        top_first = h[0]
        heapq.heappop(h)
        top_second = h[0]
        heapq.heappop(h)
        top_third = h[0]
        heapq.heappop(h)
        top_3 = top_first.value * top_second.value * top_third.value
        print(top_3)
        heapq.heappush(h, top_third)
        heapq.heappush(h, top_second)
        heapq.heappush(h, top_first)
