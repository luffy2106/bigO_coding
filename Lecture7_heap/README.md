# Heap
### Implement
Python already support us the library to build and manipulate Heap. There are 2 ways;
- Using PriotityQueue
- Using heapq(faster)

To make thing simpler, we will practice with heapq only.
By default, heappush is set for min heap(the smallest element on the top), if you want to use max heap, you need to redefine __lt__ operator.

```
# if you want to convert array to min heap
h = heappq.heapify(a)


# if you want to convert array to max heap
h = heappq.heapify(a)
class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
# if you want to convert array to max heap
a  = [7,12,6,10,17,15,2,4]
h = []
for x in a:
    heapq.heapush(h, PQEntry(x))
```

Some function need to know:
- heapq.heappush(heap, PQEntry(number)) : add element to heap with the modified operatior
- heapq.heappop(heap) : take top heap
- heappq.heapify(a): conver array to min heap

### Complexity
- Build heap from array : O(n)
- Find the max/min elements in Heap:0(1)
- Add an element to Heap : O(log(n))
- Delete an element in Heap: O(log(n))



