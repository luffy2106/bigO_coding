from pickle import FALSE
import queue

INF = 1e9


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def printMST():
    ans = 0
    for i in range(1, N + 1):
        if path[i] == -1:
            continue
        ans += dist[i]
    print(ans)


def prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        if dist[u] != w:  # optimize like dijkstra
            continue
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u


N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
dist = [INF for i in range(N + 1)]
path = [-1 for i in range(N + 1)]
visited = [False for i in range(N + 1)]
for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))
prim(1)
printMST()
