import queue
import heapq


def Dijkstra(node_s):
    pq = []
    heapq.heappush(pq, node_s)
    dist[node_s.id] = 0
    while len(pq) > 0:
        top = heapq.heappop(pq)
        u = top.id
        w = top.dist
        if (dist[u] != w): 
        #Kiểm tra xem đường đi đến u có phải là phiên bản tốt nhất không, 
        #nếu nó bằng w thì nó là phiên bản tốt nhất rồi, tiếp tục duyệt. Còn không thì nó ko phải là phiên bản tốt nhất => bỏ qua 
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
