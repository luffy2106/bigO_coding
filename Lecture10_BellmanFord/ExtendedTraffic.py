"""
Bài toán trở về thành tìm đường đi ngắn nhất từ nguồn đến đích với đồ thị với cạnh có độ dài weight nếu đi từ u đến v. 
weight sẽ được tính bằng (busyness dest - business source)^3
Nếu tồn tại chu trình âm (không đến đc đích) hoặc độ dài quãng đường bé hơn 3 thì in ra "?" 
"""


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


def BellmanFord(s, q):
    dist[s] = 0
    # loop on vertice
    for i in range(nb_nodes):
        # loop on edges
        if dist[q] < 3:
            return True
        for j in range(nb_edges):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                path[v] = u
            if dist[q] < 3:
                return True
    for i in range(nb_edges):
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        if (dist[u] != INF) and (dist[u] + w < dist[v]):
            return True
    return False


INF = 10 ** 9
T = int(input())
for t in range(T):
    input()
    print("Case {}:".format(t + 1))
    nb_nodes = int(input())
    busyness_nodes = list(map(int, input().split()))
    nb_edges = int(input())
    MAX = nb_nodes
    dist = [INF for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]
    graph = []
    for e in range(nb_edges):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        w = (busyness_nodes[v] - busyness_nodes[u]) ** 3
        graph.append(Edge(u, v, w))
    s = 0
    nb_q = int(input())
    for i in range(nb_q):
        q = int(input())
        negative_cycle = BellmanFord(s, q - 1)
        if negative_cycle:
            print("?")
        else:
            print(dist[q - 1])
