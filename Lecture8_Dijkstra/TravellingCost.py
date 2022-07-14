import queue
import heapq


"""
Nhận xét (*):
Giả sử trong heap hiện tại có rất nhiều cặp có chung đích u nhưng khác trọng số w. Vì priority heap sẽ xét cặp có w nhỏ nhất,
nên khi lấy cặp u,w này ra, nếu đường đi đến u khác với w, chứng tỏ cặp đang xét không nằm trong đường đi ngắn nhất đến u => bỏ qua

Ví dụ: priorityheap = [(10,2), (10,4),(10,5)]

sau khi cặp u, w = (10,2) được lấy ra và xử lý. Lúc này dist[10] = 2 và đường đi ngắn nhất đến đỉnh 10 là 2. 
Tiếp đến lấy cặp (10,4) ra để xử lý, lúc này dist[10] = 2 < 4 nên cặp (10,4) không nằm trong đường đi tối ưu => có thể bỏ
(dist[10] = 2 < 4 hay dist[10] = 2 != 4) là như nhau vì priorityheap luôn xử lý thằng có trọng số bé nhất trước, nên nếu thằng đằng 
sau có trọng số khác thì chắc chắn là nó có trọng số nhỏ hơn.


"""

def Dijkstra(node_s):
    pq = []
    heapq.heappush(pq, node_s)
    dist[node_s.id] = 0
    while len(pq) > 0:
        top = heapq.heappop(pq)
        u = top.id
        w = top.dist
        if (dist[u] != w): # (*)
            continue
        for neighbor in graph[u]:
            if neighbor.dist + w < dist[neighbor.id]:
                dist[neighbor.id] = neighbor.dist + w
                heapq.heappush(pq, Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u
    return


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


N = int(input())
MAX = 500 + 1
graph = [[] for i in range(MAX)]
dist = [float("inf") for i in range(MAX)]
path = [-1 for i in range(MAX)]

# build graph
for n in range(N):
    a, b, w = map(int, input().split())
    node_a = Node(a, w)
    node_b = Node(b, w)
    graph[a].append(node_b)
    graph[b].append(node_a)

source = int(input())
node_s = Node(source, 0)
Dijkstra(node_s)
Q = int(input())
for q in range(Q):
    dest = int(input())
    print(dist[dest] if dist[dest] != float("inf") else "NO PATH")
