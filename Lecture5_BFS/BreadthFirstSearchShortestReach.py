from queue import Queue

MAX = 100
V = None  # vertex
E = None  # edge
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [
    [] for i in range(MAX)
]  # i se tuong duong voi dinh, [i] se tuong duong voi dinh dc noi den chinh no


def BFS(s):
    """
    Build graph BFS. s is the begin node
    """
    for i in range(V):
        visited[i] = False
        path[i] = -1
    q = Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:  # loop in all neighbor of vetex u
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u


def getPathRecursion(s, f, cost):
    cost_path = 0
    if s == f:
        # print(cost, end=" ")
        cost_path = cost
        return cost_path
    else:
        if path[f] == -1:
            # print("-1")
            # cost = -1
            return -1
        else:
            cost = cost + 6
            getPathRecursion(s, path[f], cost)
            # print(f, end=" ")


Q = int(input())
out_total = []
for i in range(Q):
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = int(input())
    list_dest = [x for x in range(1, V + 1) if x != s]
    BFS(s)
    out = ""
    for dest in list_dest:
        getPathRecursion(s, dest, 0)
        out = out + " " + str(getPathRecursion(s, dest, 0))
    out_total.append(out.strip())

for out in out_total:
    print(out)
