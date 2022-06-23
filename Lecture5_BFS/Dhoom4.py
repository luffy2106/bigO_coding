from queue import Queue

from sklearn import neighbors

"""
Ex input :
3 30
3
2 5 7

Bài toán có thể chuyển về thành: trong số tất cả các đường đi từ primary key đến tất các các node còn lại, nếu tìm dc đường đi nào có giá trị tính toán
bằng lock thì dừng. 
"""


pri_key, lock_key = map(int, input().split())
N = int(input())
MAX = pow(10, 5) + 1
# visited = [False for i in range(MAX)]
# path = [-1 for i in range(MAX)]

visited_value = [Visited_value(False, -1) for i in range(MAX)]
path_value = [Path_value(-1, -1) for i in range(MAX)]

key_n = list(map(int, input().split()))

class Path_value:
    """
    Position of element in matrix 2D
    """
    def __init__(self, path, value):
        self.visited = path
        self.value = value

class Visited_value:
    """
    Position of element in matrix 2D
    """
    def __init__(self, visit, value):
        self.visit = visit
        self.value = value




def BFS(s, key_n):
    visited[s] = True
    q = Queue()
    for key in key_n:
        q.put(key)
    while not q.empty():
        u = q.get()
        for neighbor in key_n:
            if u == neighbor:
                continue
            else:
                if visited_value[neighbor].visited == False:
                    visited_value[neighbor].visited == True
                    visited_value[neighbor].value == (s*neighbor)%100000
                    path_value[neighbor].path == u


        if visited[neighbor] == False:
            visited[neighbor] = True

        for neighbor in q.queue:






    q.put(s)
    while not q.empty():
        u = q.get()
        for neighbor in key_n:
            if neighbor == u:
                continue
            if visited[neighbor] == False:
                visited[neighbor] = True
                s = (neighbor * s) % 100000
                if s == lock_key:
                    path[neighbor] = u
                    print(getPathRecursion(s, neighbor, []))
                    break
                q.put(neighbor)


def getPathRecursion(s, f, path_recursion):
    if s == f:
        path_recursion.append(s)
        return len(path_recursion)
    else:
        if path[f] == -1:
            return -1
        else:
            path_recursion.append(path[f])
            return getPathRecursion(s, path[f], path_recursion)


BFS(pri_key, key_n)
