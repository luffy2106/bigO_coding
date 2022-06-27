"""
Đề bài yêu cầu đổ đất vào các cells sao cho số lake giảm xuống còn k.
Bài toán trở thành:
1. Tìm số thành phần liên thông trong đồ thị sao cho các thành phần liên thông này ko có cell nào nằm ở viền
2. Chọn ra các thành phần liên thông có diện tích nhỏ nhất để lấp đầy cho đến khi số thành phần liên thông(số lake) bằng k.
=> chạy DFS để tìm ra thành phần liên thông và số lượng phần tử trong thành phần liên thông đó. 
"""
import heapq


def valid_move(move_i, move_j):
    if 0 <= move_i <= n - 1 and 0 <= move_j <= m - 1:
        return True
    else:
        return False


class PQEntry:
    """
    Use priority queue as min-heap
    """

    def __init__(self, position_connected_component):
        self.position_connected_component = position_connected_component

    def __lt__(self, other):
        return len(self.position_connected_component) < len(
            other.position_connected_component
        )


def check_point_in_border(point):
    if (
        point.row == 0
        or point.row == n - 1
        or point.column == 0
        or point.column == m - 1
    ):
        return True
    else:
        return False


def print_matrix(matrix):
    for row in range(len(matrix)):
        print("".join(matrix[row]))


def DFS(s):
    position_connected_component = []
    border = False
    connected_component_size = 0
    stack = []
    stack.append(s)
    position_connected_component.append(s)
    visited[s.row][s.column] = True
    connected_component_size += 1
    while len(stack) > 0:
        u = stack.pop()
        if check_point_in_border(u):
            border = True
        for [i, j] in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            move_i = u.row + i
            move_j = u.column + j
            if (
                valid_move(move_i, move_j)
                and map_berland[move_i][move_j] == "."
                and visited[move_i][move_j] == False
            ):
                visited[move_i][move_j] = True
                connected_component_size += 1
                # path[v] = u
                new_position = Point(move_i, move_j)
                stack.append(new_position)
                position_connected_component.append(new_position)

    if border == True:
        return None
    else:
        return position_connected_component


class Point:
    """
    Position of element in matrix 2D
    """

    def __init__(self, row, column):
        self.row = row
        self.column = column


n, m, k = map(int, input().split())  # n,m,k is rows, columns, nb_lakes
MAX = n * m
map_berland = [["" for j in range(m)] for i in range(n)]
visited = [[False for j in range(m)] for i in range(n)]
graph = [[[] for j in range(m)] for i in range(n)]


# build matrix
for row in range(n):
    map_berland[row] = [s for s in input()]

# build heap which store connected component, the top one will be the component with the smalles size
heap_min = []
for row in range(n):
    for col in range(m):
        if map_berland[row][col] == ".":
            if visited[row][col] == False:
                source = Point(row, col)
                position_connected_component = DFS(source)
                if position_connected_component:
                    heapq.heappush(heap_min, PQEntry(position_connected_component))


trans_form = 0
top_heap = None
while len(heap_min) > k:
    top_heap = heapq.heappop(heap_min)
    trans_form = trans_form + len(top_heap.position_connected_component)
    for e in top_heap.position_connected_component:
        map_berland[e.row][e.column] = "*"

print(trans_form)
print_matrix(map_berland)
