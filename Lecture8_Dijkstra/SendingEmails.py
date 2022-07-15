import queue


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        if dist[u] != w:  # (*)
            continue
        for neighbor in graph[u]:
            if neighbor.dist + w < dist[neighbor.id]:
                dist[neighbor.id] = neighbor.dist + w
                pq.put(Node(neighbor.id, dist[neighbor.id]))
    return dist


Q = int(input())
for q in range(Q):
    N, M, S, T = map(int, input().split())
    MAX = N
    max_weight = 10000
    INF = max_weight * M + 1
    graph = [[] for i in range(MAX)]
    dist = [INF for i in range(MAX)]
    for m in range(M):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))
    Dijkstra(S)
    if dist[T] == INF:
        print("Case #{}: unreachable".format(q + 1))
    else:
        print("Case #{}: {}".format(q + 1, dist[T]))
