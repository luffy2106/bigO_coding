from cgitb import small
import heapq


"""
Solution 1 :

Neu phan tu bi xoa bang phan tu top heap, xoa phan tu top ra khoi heap.
Se co kha nang la sau khi xoa xong, phan tu con cua no se leo len top.
=> minh can luu phan tu nay trong mot heap khac va xoa, dieu nay se dam bao dc rang
phan tu con se bi xoa la phan tu be nhat trong nhung thang con
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


deleted_element = []

N = int(input())
h = []  # our heap
out = []
for i in range(N):
    operation = input().split()
    operation = [int(x) for x in operation]
    if operation[0] == 1:
        heapq.heappush(h, operation[1])
    elif operation[0] == 2:
        if h[0] == operation[1]:
            heapq.heappop(h)
            while (
                len(h) > 0 and len(deleted_element) > 0 and h[0] == deleted_element[0]
            ):
                heapq.heappop(deleted_element)
                heapq.heappop(h)
        else:
            heapq.heappush(deleted_element, operation[1])
    elif operation[0] == 3:
        if len(h) > 0:
            out.append(h[0])

for e in out:
    print(e)
