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


def BellmanFord(s):
    dist[s] = 0
    # loop on vertice
    for i in range(nb_nodes - 1):
        for edge in graph:
            u = edge.source
            v = edge.target
            w = edge.weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                path[v] = u
    for i in range(
        nb_nodes
    ):  # phải loop n lần vì khi gán 1 node nằm ở trong chu trình âm thì nó có thể kéo theo các node khác cũng nằm trong chu trình âm=> duyệt thêm n-1 lần nữa
        for edge in graph:
            u = edge.source
            v = edge.target
            w = edge.weight
            # Nếu như tồn tại chu trình âm thì hủy kết nối các cạnh này(gán tất cả các cạnh có độ dài bằng âm vô cùng, không dán bằng dương vô cùng vì có thể trùng với các đỉnh chưa duyệt),
            # để đảm bảo rằng các đỉnh đích cần xét nếu có nằm trong chu trình âm thì không thể đến dc.
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = -INF


INF = 10 ** 9
T = int(input())
for t in range(T):
    input()
    print("Case {}:".format(t + 1))
    nb_nodes = int(input())
    busyness_nodes = [0] + list(map(int, input().split()))
    nb_edges = int(input())
    MAX = nb_nodes + 1
    dist = [INF for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]
    graph = []
    for e in range(nb_edges):
        u, v = map(int, input().split())
        w = (busyness_nodes[v] - busyness_nodes[u]) ** 3
        graph.append(Edge(u, v, w))
    s = 1
    BellmanFord(s)
    nb_q = int(input())
    for i in range(nb_q):
        f = int(input())
        print(dist[f] if dist[f] != INF and dist[f] >= 3 else "?")
