import heapq

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
    Use priority queue as max-heap
    """

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value




heap_max = []
heap_min = []
cost_promo = []
last_top_min = None
last_top_max = None

for i in range(N):
    promo_i = [int(e) for e in input().split()]
    nb_promo_i = promo_i[0]
    recept_promo_i = promo_i[1:]
    for e in recept_promo_i:
        heapq.heappush(heap_max, PQEntry_max(e))        
        heapq.heappush(heap_min, PQEntry_min(e))
    largest = heap_max[0]
    heapq.heappop(heap_max)
    smallest = heap_min[0]
    heapq.heappop(heap_min)
    # if heap_min[0].value == largest.value:
    #     heapq.heappop(heap_min)
    # if heap_max[0].value == smallest.value:
    #     heapq.heappop(heap_max)
    print([e.value for e in heap_min])
    print([e.value for e in heap_max])
    cost_promo_i = largest.value - smallest.value       
    cost_promo.append(cost_promo_i)

print(sum(cost_promo))


