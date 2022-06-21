from requests import patch


import queue

R, C = map(int, input().split())
nb_rows_bomb = int(input())
MAX = max(R, C)
visited = [[False] * MAX for _ in range(MAX)]
path = [None] * MAX

matrix_road = [[True] * C for _ in range(R)]


class Cell:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c


# def BFS(s, f):
#     q = queue.Queue()
#     visited

for i in range(R):
    for j in range(C):
        visited[i][j] = False


for i in range(nb_rows_bomb):
    line_row = list(map(int, input().split()))
    row = line_row[0]
    bom_row = line_row[1]
    if bom_row > 0:
        for i in range(2, len(line_row)):
            column = line_row[i]
            matrix_road[row, column] = False
