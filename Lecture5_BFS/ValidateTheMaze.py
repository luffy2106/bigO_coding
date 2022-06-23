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
Bạn sẽ chạy BFS trên mê cung đã cho mà không cần phải chuyển lại thành dạng ma trận kề hay danh sách kề. 
Cách này bạn phải thêm và chỉnh lại một số dòng code để chạy phù hợp.

- Tìm 2 điểm đầu vào và đầu ra. 
- Từ điểm đầu Từ điểm đầu ra bạn sẽ xác định 4 hướng đi (lên, xuống, trái, phải). 
Nếu có đường đi, nghĩa là gặp dấu “.” và nằm trong giới hạn của mê cung thì bạn sẽ dịch chuyển bước đi của mình xuống điểm mới. 
Lần lượt đi đến khi nào gặp đỉnh đầu ra thì dừng. Lúc này sẽ in ra là “valid”, ngược lại nếu đi mà không thấy đường ra sẽ in ra “invalid”.
"""

"""
Solution 2
"""


class Position:
    """
    Position of element in matrix 2D
    """

    def __init__(self, row, column):
        self.row = row
        self.column = column


def valid_move(move_i, move_j):
    if 0 <= move_i <= M - 1 and 0 <= move_j <= N - 1:
        return True
    else:
        return False


def move_to_neighbors(position, queue_BFS):
    for [i, j] in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        move_i = position.row + i
        move_j = position.column + j
        if (
            valid_move(move_i, move_j)
            and a[move_i][move_j] == "."
            and visited[move_i][move_j] == False
        ):
            neighbor = Position(move_i, move_j)
            queue_BFS.put(neighbor)
            visited[move_i][move_j] = True
    return


def BFS(source, dest):
    """
    Build graph BFS. s is the begin node
    """

    queue_BFS = Queue()
    visited[source.row][source.column] = True
    queue_BFS.put(source)
    # when the dest was visited => finish
    while not queue_BFS.empty():
        u = queue_BFS.get()
        if visited[dest.row][dest.column] == True:
            return "valid"
        move_to_neighbors(u, queue_BFS)
    return "invalid"


T = int(input())
for i in range(T):
    source_dest = []
    M, N = map(int, input().split())
    a = [["" for j in range(N)] for i in range(M)]
    visited = [[False for j in range(N)] for i in range(M)]
    count_sd = 0
    # Create matrix maze with input
    for i in range(M):
        row_i = [e for e in input()]
        for j in range(len(row_i)):
            a[i][j] = row_i[j]
            if (
                i == 0 or i == M - 1 or j == 0 or j == N - 1
            ):  # Position of source and dest
                if a[i][j] == ".":
                    count_sd += 1
                    source_dest.append(Position(i, j))
                    if count_sd > 2:
                        break
    if count_sd == 2:
        source = source_dest[0]
        dest = source_dest[1]
        print(BFS(source, dest))
    else:
        print("invalid")
