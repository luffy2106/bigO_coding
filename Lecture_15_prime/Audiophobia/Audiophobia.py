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
    """
    Lưu ý : trong python, tất cả các tham số(immutable) trong hàm đều mặc định là local, nên nếu ta muốn thao tác
    với các tham số global trong hàm, ta cần khai báo global để cấp quyền truy cập vào các biến này.
    Tuy nhiên với các biến dạng mutable(list,set,dict), ta ko cần thực hiện điều này vì python sẽ tự hiểu đây là biến
    global nếu được sử dụng trong function.
    """
    # global DFS_graph
    # global visited
    # global graph
    # global dist
    # global path
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
    # print("done add DFS")


def DFS_recursion(s,f,max_const):
    """
    Gọi max_cost là độ dài cạnh lớn nhất trên đường đi từ node đầu đến node hiện tại
    Lưu ý: để tìm được cạnh dài nhất trong đường đi từ s đến f, ta cần đảm bảo biến truyền vào max_const là 
    một hằng số chứ không phải 1 biến. Dieu nay se dam bao duoc tai moi node truoc khi goi recursive, max_cost sẽ được lưu và không thay đổi trong quá trình recursive
    """
    # global DFS_graph
    # global visited_DFS
    if s == f:
        return max_const   
    visited_DFS[s] = True
    for node in DFS_graph[s]:
        v = node.id
        w = node.dist
        # max_const = max(w, max_const)
        if not visited_DFS[v]:
            tmp_max_const =  DFS_recursion(v,f,max(w, max_const)) #tim max_cost at node neighbor. Tai moi node, max_cost se la canh co do dai lon nhat tu node goc den not hien tai
            if tmp_max_const != INF:
                return tmp_max_const
    return INF




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
    path = [-1] * MAX
    DFS_graph = [[] for i in range(MAX)]
    for s in range(S):
        c1, c2, d = map(int, input().split())
        graph[c1].append(Node(c2,d))
        graph[c2].append(Node(c1,d))
    for i in range(1, len(visited)):
        if visited[i] == False:
            prim(i)
    for q in range(Q):
        s,f = map(int, input().split())
        visited_DFS = [False] * MAX
        # max_const = 0
        # found = False
        max_const = DFS_recursion(s,f,0)
        print(max_const if max_const < INF else 'no path')
    print()

    