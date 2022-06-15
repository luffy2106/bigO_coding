from cgitb import small
import heapq


class PQEntry:
    """
    Use priority queue as max-heap
    """

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


def find_index_delete(h, v):
    i = 0
    for e in h:
        if e == v:
            break
        else:
            i += 1
    return i


N = int(input())
h = []  # our heap
out = []
index_value = [h[i] for i in range(len(h))]
for i in range(N):
    operation = input().split()
    operation = [int(x) for x in operation]
    if operation[0] == 1:
        heapq.heappush(h, operation[1])
        continue
    elif (
        operation[0] == 2
    ):  # Find the index of deleted number => gan phan tu tai vi tri do la -infinitive => chuan hoa heap => delete phan tu khoi top
        index_delete = find_index_delete(h, operation[1])
        # h[0], h[index_delete] = h[index_delete], h[0]
        h[index_delete] = float("-inf")
        # heapq.heappop(h)
        heapq.heapify(h)
        heapq.heappop(h)
        continue
    else:
        out.append(h[0])

for e in out:
    print(e)
