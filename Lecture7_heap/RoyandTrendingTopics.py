import heapq


class Topic:
    def __init__(self, topic):
        self.id = topic[0]
        self.Z = topic[1]
        self.P = topic[2]
        self.L = topic[3]
        self.C = topic[4]
        self.S = topic[5]
        self.Z_update = self.P * 50 + self.L * 5 + self.C * 10 + self.S * 20
        self.change = self.Z_update - self.Z

    def __lt__(self, other):
        """
        Use priority queue as max-heap
        """
        if (self.change > other.change) or (
            self.change == other.change and self.id > other.id
        ):
            return True
        return False


N = int(input())
h = []
for i in range(N):
    topic_i = [int(e) for e in input().split()]
    heapq.heappush(h, Topic(topic_i))

for i in range(5):
    top = h[0]
    print(str(top.id) + " " + str(top.Z_update))
    heapq.heappop(h)
