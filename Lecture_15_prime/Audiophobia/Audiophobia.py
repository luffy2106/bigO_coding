"""
Đường đi có mức âm tối thiểu sẽ nằm trên cây khung nhỏ nhất bởi vì trong quá trình tạo ra cây khung nhỏ
nhất, các cạnh với đường đi ngắn nhất sẽ được thêm vào.
- Ta sẽ duyệt tất cả các đỉnh bằng cách xây dựng các cây khung nhỏ nhất
- Sau khi đã có cây khung nhỏ nhất, ta áp dụng BFS/DFS để tìm đường đi từ c1->c2
- Kết quả sẽ là cạnh có trọng số lớn nhất trên path c1->c2
"""

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist




import queue
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
    # Đẩy các cạnh của cây khung vào 1 đồ thị mới để sử dụng DFS:
    for u in range(1,MAX):
        v = path[u]
        w = dist[u]
        if path[u] != -1:
            DFS_graph[u].append(Node(v,w))
            DFS_graph[v].append(Node(u,w))
    print("done add DFS")


def DFS_recursion(s,f,max_const, found):
    """
    Đang bị lỗi, tìm cách khử đệ quy
    """
    visited_DFS[s] = True
    if s == f:
        return True
    else:
        for node in DFS_graph[s]:
            v = node.id
            w = node.dist
            max_const = max(w, max_const)
            if not visited_DFS[v]:
                DFS_recursion(v,f, max_const, found)
        return found

case = 0
while True:
    C, S, Q = map(int, input().split())
    if [C, S, Q] == [0,0,0]:
        break
    case+=1
    print("Case #{}".format(case))
    MAX = C + 1
    INF = 1200
    visited = [False] * MAX
    graph = [[] for i in range(MAX)]
    dist = [INF] * MAX
    # path = [-1] * MAX
    DFS_graph = [[] for i in range(MAX)]
    for s in range(S):
        c1, c2, d = map(int, input().split())
        graph[c1].append(Node(c2,d))
        graph[c2].append(Node(c1,d))
    for i in range(1, len(visited)):
        path = [-1] * MAX
        if visited[i] == False:
            prim(i)
    for q in range(Q):
        s,f = map(int, input().split())
        visited_DFS = [False] * MAX
        max_const = 0
        found = False
        DFS_recursion(s,f,max_const, found)
        if found:
            print(max_const)
        else:
            print("no path")

    