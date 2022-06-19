import heapq


"""
Tao 2 heap, heap min va heap max. Moi lan lay phan tu dau tien cua tung heap ra de tinh cost
Dung mot mang tan so de dem so lan xuat hien
mỗi lần nhập giá x thì sẽ cập nhật cnt[x] += 1
khi mà lấy ra khỏi max heap và min heap thì cnt[x] -= 1

nhưng trước đó phải kiểm tra xem nó đã được lấy ra trước đó hay chưa, nếu mà cnt[x] = 0 thì tức là nó đã được lấy ra từ trước đó rồi,
can pop ra va kiem tra tiep
"""

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


def get_top(heap, frequent_recept):
    if frequent_recept[heap[0].value] > 0:
        top = heap[0]
        frequent_recept[heap[0].value] -= 1
        heapq.heappop(heap)
        return top
    else:
        heapq.heappop(heap)
        return get_top(heap, frequent_recept)


heap_max = []
heap_min = []
cost_promo = []
frequent_recept = [0] * (pow(10, 6) + 1)
for i in range(N):
    promo_i = [int(e) for e in input().split()]
    nb_promo_i = promo_i[0]
    recept_promo_i = promo_i[1:]
    for e in recept_promo_i:
        frequent_recept[e] += 1
        heapq.heappush(heap_max, PQEntry_max(e))
        heapq.heappush(heap_min, PQEntry_min(e))
    largest = get_top(heap_max, frequent_recept)
    smallest = get_top(heap_min, frequent_recept)
    cost_promo_i = largest.value - smallest.value
    cost_promo.append(cost_promo_i)
print(sum(cost_promo))
