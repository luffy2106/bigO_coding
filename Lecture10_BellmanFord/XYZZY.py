"""
Bài toán trở về thành :
- Xác định có hay ko đường đi ngắn nhất từ đỉnh đầu đến đỉnh cuối sao cho tổng chi phí >= 0. Nếu có thì in ra winnable, không thì in ra hopeless.
- Giá trị dist ban đầu tất cả các node trong đồ thị là -INF(chứ không phải là INF như thường lệ) 
- Ngoài ra cần xét thêm 1 trường hợp đặc biệt, đó là nếu tồn tại chu trình dương thì về bản chất vẫn có thể tìm được đường đi từ nguồn đến đích nếu như
tồn tại đường đi từ 1 trong các cạnh của chu trình dương đó đến đích. 
"""
import queue


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


# def DFS(s, f):
#     visited = [False] * (MAX)
#     stack = []
#     stack.append(s)
#     visited[s] = True
#     while len(stack) > 0:
#         u = stack.pop()
#         for v in graph[u]:
#             if visited[v] == False:
#                 visited[v] = True
#                 path[v] = u
#                 stack.append(v)
#             if v == f:
#                 return True
#     return False


def hasPathBFS(s, f):
    visited = [False] * (MAX)
    q = queue.Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)

            if v == f:
                return True

    return False


def BellmanFord(s, q):
    dist = [-INF] * (MAX)
    dist[s] = 100
    # loop on vertice
    for u in range(1, MAX - 1):
        neighbor_u = graph[u]
        for v in neighbor_u:
            if dist[u] > 0:  # dist[u] > 0 dai dien cho viec dinh do chua dc xet
                dist[v] = max(dist[v], dist[u] + energy_node[v])
                path[v] = u

    # Kiểm tra xem có tồn tại chu trình dương không, nếu có, kiểm tra xem có tồn tại đường đi từ 1 đỉnh
    # trong chu trình dương đến điểm đích ko
    for u2 in range(1, MAX - 1):
        neighbor_u = graph[u2]
        for v in neighbor_u:
            if (
                (dist[u2] > 0)
                and (dist[u2] + energy_node[v] > dist[v])
                and hasPathBFS(u2, q)
            ):
                return True

    return dist[q] > 0


INF = 10 ** 9
while True:
    nb_nodes = int(input())
    if nb_nodes == -1:
        break
    start_node = 1
    end_node = nb_nodes
    MAX = nb_nodes + 1
    dist = [-INF for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]
    graph = [[] for _ in range(MAX)]
    energy_node = [0 for _ in range(MAX)]

    for r in range(1, MAX):
        line = list(map(int, input().split()))
        energy_node[r] = line.pop(0)

        if not line:  # input could be ill-formated
            line.extend(list(map(int, input().split())))

        m = line.pop(0)

        while len(line) != m:
            line.extend(list(map(int, input().split())))

        for v in line:
            graph[r].append(v)
        # line_r = list(map(int, input().split()))
        # energy_r = line_r[0]
        # nb_doors = line_r[1]
        # energy_node[r] = energy_r
        # for i in range(2, len(line_r)):
        #     # edge_i = Edge(r, line_r[i], energy_r)
        #     graph[r].append(line_r[i])
    canGo = BellmanFord(start_node, end_node)
    print("winnable" if canGo else "hopeless")
