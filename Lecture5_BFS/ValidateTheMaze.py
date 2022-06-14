"""
4 4
####
#...
#.##
#.##
"""
import numpy as np

M, N = map(int, input().split())  # rows and columns
a = [[0 for j in range(N)] for i in range(M)]

MAX = M * N
graph = [{} for i in range(MAX)]
visited = [{} for i in range(MAX)]
path = [{} for i in range(MAX)]


source_dest = []

# find available spot
for i in range(M):
    row_i = [e for e in input()]
    for j in range(len(row_i)):
        if row_i[j] == ".":
            a[i][j] = 1
            str_i_j = str(i) + str(j)
            graph[str_i_j] = []
            visited[str_i_j] = False
            path[str_i_j] = -1
            if i == 3 or j == 3:
                source_dest.append([i, j])


print("finish")


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
