"""
Nhận xét : 
- Nếu ô đích là X(cracked ice) thì ta chỉ cần tìm đường đến ô đó.
- Nếu ô đích là .(intact ice) thì sau khi đến được nơi đó xong. Xung quanh ô đó phải có ít nhất 1 ô là intact để ta có thể
đi đến ô đích(để biến ô đích thành cracked ice) sau đó đi sang ô xung quanh, rồi quay trở về chỗ cracked ice đích để rơi xuống. 
Bài toán chuyển thành tìm đường đi từ điểm đầu đến điểm đích với BFS, trong đó mỗi ô được visit tối đa 2 lần.
"""
import queue
class Position:
    """
    Position of element in matrix 2D
    """

    def __init__(self, row, column):
        self.row = row
        self.column = column


def valid_move(move_i, move_j):
    if 0 <= move_i <= rows - 1 and 0 <= move_j <= columns - 1:
        return True
    else:
        return False




def get_neighbors(q, ur, uc, dr, dc):
    for [i, j] in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        move_i = ur + i
        move_j = uc + j
        if (
            valid_move(move_i, move_j)
            and visited[move_i][move_j] == 0
        ) or (move_i == dr and move_j == dc):
            #visited[move_i][move_j] = 1
            neighbor = (move_i, move_j)
            q.put(neighbor)
    return q

rows, columns = map(int, input().split())
matrix = [["" for j in range(columns)] for i in range(rows)]
visited = [[False for j in range(columns)] for i in range(rows)]

# Build matrix
for i in range(rows):
    row_i = [c for c in input()]
    for j in range(columns):
        matrix[i][j] = row_i[j]
        if matrix[i][j] == ".": 
            visited[i][j] = False
        else:
            visited[i][j] = True
    


def BFS(sr, sc, dr, dc):
    q = queue.Queue()
    q.put((sr,sc))
    visited[sr][sc] = True
    while not q.empty():
        ur, uc  = q.get()
        for [i, j] in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            move_i = ur + i
            move_j = uc + j
            if move_i == dr and move_j == dc and visited[move_i][move_j] == True:
                return True
            if (
                valid_move(move_i, move_j)
                and visited[move_i][move_j] == False
            ):
                visited[move_i][move_j] = True
                neighbor = (move_i, move_j)
                q.put(neighbor)
    return False

s_r, s_c =  [int(x)-1 for x in input().split()]
d_r, d_c = [int(x)-1 for x in input().split()]
print("YES" if BFS(s_r, s_c, d_r, d_c) else "NO")
    



    



