"""
Bài toán này có thể được tối ưu bằng cách kiểm tra xem path đang xét có nằm trong path
của path đã duyệt trước đó không, nếu có thì không cần duyệt lại Dijkstra. Lúc này chi phí 
của path(source, dest) = dist[dest] - dist[source]

"""
import heapq
class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def Dijkstra(s):
    pq = []
    heapq.heappush(pq, Node(s,0))
    dist[s] = 0
    while len(pq) > 0:
        top = heapq.heappop(pq)
        u = top.id
        w = top.dist
        if (dist[u] != w):
            continue
        for neighbor in graph[u]:
            if neighbor.dist + w < dist[neighbor.id]:
                dist[neighbor.id] = neighbor.dist + w
                heapq.heappush(pq, Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u
    return


def get_path(source, dest, path_s_d):
    if source == dest:
        path_s_d.append(source)
        return path_s_d
    else:
        path_s_d.append(dest)
        dest = path[dest]
        return get_path(source, dest, path_s_d)






s = int(input())
for s_i in range(s):
    dict_city = dict()
    n = int(input())
    MAX = n+1
    max_cost = 2 * (10**5)
    graph = [[] for i in range(MAX)]
    for n_i in range(1, n+1):
        name_n_i = input()
        dict_city[name_n_i] = n_i
        nb_neighbors = int(input())
        for i in range(nb_neighbors):
            neighbor_i, w_i = map(int, input().split())
            graph[n_i].append(Node(neighbor_i, w_i))
            # graph[neighbor_i].append(Node(n_i, w_i))


    r = int(input())
    path_source_dest = []
    for i in range(r):
        source_name_i, dest_name_i = input().split()
        source_i = dict_city[source_name_i]
        dest_i = dict_city[dest_name_i]
        dist = [max_cost for i in range(MAX)]
        path = [-1 for i in range(MAX)]
        path_source_dest = []
        Dijkstra(source_i)
        # print(get_path(source_i, dest_i, path_source_dest))
        print(dist[dest_i])
    space = input()

 


