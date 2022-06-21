import queue
import heapq


class PQEntry_max:
    """
    Use priority queue as max-heap
    """

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    jobs = list(map(int, input().split()))
    queue_pr = queue.Queue()
    heap_max = []
    index_queue_pr = queue.Queue()
    index = 0
    total_time = 0
    for job in jobs:
        index_queue_pr.put(index)
        queue_pr.put(job)
        heapq.heappush(heap_max, PQEntry_max(job))
        index+=1
    while True:
        if queue_pr.queue[0] < heap_max[0].value:
            #move
            top = queue_pr.get()
            queue_pr.put(top)
            top_index = index_queue_pr.get()
            index_queue_pr.put(top_index)
        elif queue_pr.queue[0] == heap_max[0].value:
            #print
            top = queue_pr.get()
            top_index = index_queue_pr.get()
            heapq.heappop(heap_max)
            total_time = total_time + 1
            if top_index == m:
                print(total_time)
                break
    