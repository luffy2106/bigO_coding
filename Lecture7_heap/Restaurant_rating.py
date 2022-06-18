import heapq
import math
N = int(input())


class PQEntry_max:
    """
    Use priority queue as max-heap
    """

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

class PQEntry_min:
    """
    Use priority queue as min-heap
    """

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

max_heap = []
for i in range(N):
    operation = [int(x) for x in input().split()]
    if operation[0] == 1:
        heapq.heappush(max_heap, PQEntry_max(operation[1]))
    elif operation[0] == 2:
        nb_reviews_display = math.floor(len(max_heap)/3)
        if nb_reviews_display == 0:
            print("No reviews yet")
        else:
            min_heap = []
            while nb_reviews_display > 0:
                top_max = max_heap[0].value
                heapq.heappop(max_heap)
                heapq.heappush(min_heap, PQEntry_min(top_max))
                nb_reviews_display-=1
            top_min = min_heap[0]
            print(top_min.value)
            for e in min_heap:
                heapq.heappush(max_heap, PQEntry_max(e.value))



