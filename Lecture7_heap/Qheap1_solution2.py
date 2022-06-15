from cgitb import small
import heapq

"""
Solution 1 :

Neu phan tu bi xoa bang phan tu top heap, xoa phan tu top ra khoi heap
"""


class PQEntry:
    """
    Use priority queue as max-heap
    """

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


def index_parent(i):
    return int((i - 1) / 2)


N = int(input())
h = []  # our heap
out = []
index_value = [h[i] for i in range(len(h))]
min = 0
for i in range(N):
    operation = input().split()
    operation = [int(x) for x in operation]
    if operation[0] == 1:
        heapq.heappush(h, operation[1])
    elif operation[0] == 2:
        while len(h) > 0 and h[0] == operation[1]:
            heapq.heappop(h)
    else:
        out.append(h[0])

for e in out:
    print(e)
