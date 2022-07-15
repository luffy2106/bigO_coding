from dis import dis
import queue

"""
Trong bài toán này chúng ta cần giải quyết 2 vấn đề:
- Tất cả các building đều phải được commandos đi qua ít nhất 1 lần
- Tất cả các commandos phải hội tụ tại headquarter trong thời gian sớm nhất
=> bài toán trở trành:
Để một commandos tìm đường đi ngắn nhất từ điểm xuất phát đến head quarter. Ta kiểm tra xem có những đỉnh nào đã được đi qua rồi. Những đỉnh nào chưa đi qua,
ta tìm đường đi ngắn nhất từ điểm xuất phát đến đỉnh đó và sau đó tìm đường đi ngắn nhất từ đỉnh này đến head quarter. 

Đáp án sẽ là thời gian lớn nhất từ điểm xuất phát đến 1 điểm bất kỳ, và từ điểm này đến đích(trong quá trình duyệt tất cả các đỉnh)

Cách này phải Dijkstra nhiều lần, nên xem lời giải trong tutorial
"""


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def Dijkstra(s, dist):
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
                path[neighbor.id] = u
    return dist


def validate_path_visited(source, dest, visited_path, path):
    if source == dest:
        visited_path[source] = True
        return visited_path
    else:
        visited_path[dest] = True
        dest = path[dest]
        return validate_path_visited(source, dest, visited_path, path)


def check_all_node_visited(visited):
    if all(node == True for node in visited):
        return True
    else:
        return False


T = int(input())
for t in range(T):
    N = int(input())
    R = int(input())
    MAX = N
    INF = R + 1
    graph = [[] for i in range(MAX)]
    dist_s = [INF for i in range(MAX)]
    visited = [False for i in range(MAX)]
    path = [-1 for i in range(MAX)]
    for r in range(R):
        u, v = map(int, input().split())
        graph[u].append(Node(v, 1))
        graph[v].append(Node(u, 1))
    s, d = map(int, input().split())
    Dijkstra(s, dist_s)
    validate_path_visited(s, d, visited, path)
    dist_source_dest = dist_s[d]
    cost = dist_source_dest
    # max_cost_remain = 0
    while not check_all_node_visited(visited):
        not_visited_node = [index for index in range(MAX) if visited[index] == False]
        for node in not_visited_node:
            dist_source_node = dist_s[node]
            dist_node = [INF for i in range(MAX)]
            path = [-1 for i in range(MAX)]
            Dijkstra(node, dist_node)
            validate_path_visited(node, d, visited, path)
            dist_node_dest = dist_node[d]
            additional_time = dist_source_node + dist_node_dest
            if additional_time > cost:
                cost = additional_time

    print("Case {}: {}".format(t + 1, cost))
