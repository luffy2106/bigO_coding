import heapq
import math
N = int(input())

"""
Tao ra 2 heap
1 heap min chua top n phan tu lon nhat
1 heap max chua cac phan tu con lai, dc cap nhat dan

neu len min heap be hon n thi pop tu heap max sang
neu len min heap bang n thi kiem tra xem top thằng max có lớn hơn top thằng min ko, nếu có thì đổi chỗ

"""


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


min_top_heap = []
max_heap = []
len_reviews = 0
for i in range(N):
    operation = [int(x) for x in input().split()]
    if operation[0] == 1:
        len_reviews+=1
        nb_reviews_display = math.floor(len_reviews/3)
        heapq.heappush(max_heap, PQEntry_max(operation[1]))
        if len(min_top_heap) < nb_reviews_display:
            top_max = max_heap[0].value
            heapq.heappop(max_heap)
            heapq.heappush(min_top_heap, PQEntry_min(top_max))
        else:
            if len(min_top_heap) > 0:
                top_max = max_heap[0].value
                top_max_min = min_top_heap[0].value
                if top_max > top_max_min:
                    heapq.heappop(max_heap)
                    heapq.heappop(min_top_heap)
                    heapq.heappush(max_heap, PQEntry_max(top_max_min))
                    heapq.heappush(min_top_heap, PQEntry_min(top_max))
    elif operation[0] == 2:
        if len(min_top_heap) == 0:
            print("No reviews yet")
        else:
            print(min_top_heap[0].value)




