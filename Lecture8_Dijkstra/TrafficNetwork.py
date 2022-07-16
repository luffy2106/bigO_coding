import heapq
import queue

"""
Nhận xét :
Với mỗi một two-way road proposed, tính chi phí đường đi từ S->T. Chi phí nào có đường đi ngắn nhất thì đó chính là kết quả.

Lưu ý: Để làm được việc này thì mỗi lần gắn đường đi hai chiều vào bạn phải chạy lại thuật toán Dijkstra. Việc này sẽ làm bài bạn bị quá thời gian (TLE). 
Bạn phải cải tiến thuật toán Dijkstra và cải tiến luôn việc không thể gọi Dijkstra mỗi lần gắn đường đi hai chiều mới vào bằng cách sau:

Tính Dijkstra từ S -> T và tính chiều ngược lại T->S (gọi Dijkstra hai lần).

Sau khi chạy Dijkstra ta có:

distS[u]: tìm đường đi từ đỉnh S đến đỉnh u (trong đồ thị demo tren platform la 1->5).
distT[v]: tìm đường đi từ đỉnh v đến đỉnh T (trong đồ thị demo tren platform la 3->4).
Gắn từng đường đi hai chiều vào, lúc này dùng công thức bên dưới, công thức này giống như việc gọi Dijkstra lại mỗi lần gắn đường đi hai chiều vào.

Sau khi gắn d vào, nếu tổng này nhỏ hơn đường đi hiện tại đang có thì nó chính là đường đi ngắn nhất.

"""


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def Dijkstra(s, dist, graph):
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


nb_dataset = int(input())
for i in range(nb_dataset):
    N, M, K, S, T = map(int, input().split())
    MAX = N + 1
    INF = M * 1001
    cost = INF
    path_S_T = []
    graph_S = [[] for i in range(MAX)]
    graph_T = [[] for i in range(MAX)]
    dist_ST = [INF for i in range(MAX)]
    dist_TS = [INF for i in range(MAX)]
    for m in range(M):
        u, v, w = map(int, input().split())
        graph_S[u].append(Node(v, w))
        graph_T[v].append(Node(u, w))

    dist_ST = Dijkstra(S, dist_ST, graph_S)
    dist_TS = Dijkstra(T, dist_TS, graph_T)

    for k in range(K):
        u, v, w = map(int, input().split())
        dist_S_U = dist_ST[u]  # shortest path from s to u, in the road from s to t
        dist_V_T = dist_TS[v]  # shortest path from t to v, in the road from t to s
        dist_S_V = dist_ST[v]  # shortest path from s to v, in the road from s to t
        dist_U_T = dist_TS[u]  # shortest path from t to u, in the road from t to s
        dist_S_U_V_T = dist_S_U + w + dist_V_T
        dist_S_V_U_T = dist_S_V + w + dist_U_T
        cost = min(cost, min(dist_S_U_V_T, dist_S_V_U_T))
    if cost == INF:
        print(-1)
    else:
        print(cost)
