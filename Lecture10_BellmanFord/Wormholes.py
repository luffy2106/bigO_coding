"""
Chứng kiến dc vụ nổ big bang tương đương với việc quay về thời gian âm vô cùng. Vậy chỉ cần tìm được một chu trình âm, sau đó đi đi lại lại 
chu trình âm đó thì sẽ có thể quay dc về thời gian âm vô cùng vì sau khi kết thúc 1 chu trình âm, thời gian bị giảm đi.
=> xác định đồ thị tồn tại chu trình âm hay không => dùng BellmanFord
"""


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


def BellmanFord(s):
    dist[0] = 0
    # loop on vertice
    for i in range(1, n):
        # loop on edges
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(m):
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        if (dist[u] != INF) and (dist[u] + w < dist[v]):
            return True
    return False


T = int(input())
INF = 10 ** 4
for t in range(T):
    n, m = map(int, input().split())
    MAX = n
    dist = [INF for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]
    graph = []
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append(Edge(u, v, w))
    s = 0
    res = BellmanFord(s)
    if res:
        print("possible")
    else:
        print("not possible")
