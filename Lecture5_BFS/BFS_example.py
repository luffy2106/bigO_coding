"""
Tim duong di ngan nhat tu 0 den 5 cua do thi sau:

9 11   #(V,E)

0 8    #Các cạnh
0 3
3 4
8 4
3 2
0 1
1 2
1 7
2 7
2 5
5 6

"""

from queue import Queue

MAX = 100
V = None  # verticle
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


def printPath(s, f):
    """
    Print shortest path from source to destination(no use recursive)
    """
    b = []
    if f == s:
        print(s)
        return
    if path[f] == -1:
        print("no path")
        return
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    for i in range(len(b) - 1, -1, -1):
        print(b[i], end=" ")


def printPathRecursion(s, f):
    if s == f:
        print(f, end=" ")
    else:
        if path[f] == -1:
            print("No path")
        else:
            printPathRecursion(s, path[f])
            print(f, end=" ")


if __name__ == "__main__":
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = 0  # source
    f = 5  # destination
    BFS(s)
    printPath(s, f)
