import imp
from queue import Queue

"""
4 4
####
#...
#.##
#.##
"""


"""
Nhận xét :
- Đề bài yêu cầu Maze có đúng 1 đường vào và 1 đường ra.
- Các điểm vào và điểm ra đều nằm trên mép của hình chữ nhật => điều kiện là có đúng 2 điểm vào ra nằm trên mép của đồ thị, nếu không là invalid
- Bài toán trở thành xác định có hay không đường đi từ điểm mép này với điểm mép kia.


Cách 1:
- Build 1 đồ thị gồm tất cả các node trong ma trận 
- Nếu tồn tại đường đi giữa 2 node kề nhau => nối chúng lại
- Tìm 2 node source và dest nằm trong đồ thị
- Xác định có hay ko đường đi từ source đến dest
=> Cách này khiến chúng ta phải tốn thời gian xây dụng đồ thị dựa theo ma trận đầu vào 


Cách 2:

"""
import numpy as np

M, N = map(int, input().split())  # rows and columns
a = [[0 for j in range(N)] for i in range(M)]

MAX = (M + 1) * (N + 1)
V = MAX
graph = [[] for i in range(MAX)]
visited = [False] * MAX
path = [0 for i in range(MAX)]


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
