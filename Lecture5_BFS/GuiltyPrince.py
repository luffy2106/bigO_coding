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


def get_neighbors(position, queue_BFS):
    for [i, j] in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        move_i = position.row + i
        move_j = position.column + j
        if (
            valid_move(move_i, move_j)
            and matrix[move_i][move_j] == "."
            and visited[move_i][move_j] == False
        ):
            neighbor = Position(move_i, move_j)
            queue_BFS.put(neighbor)
    return queue_BFS


def BFS(source):
    nb_visited = 0
    q = queue.Queue()
    q.put(source)
    while not q.empty():
        u = q.get()
        if visited[u.row][u.column] == False:
            visited[u.row][u.column] = True
            nb_visited += 1
            q = get_neighbors(u, q)
    return nb_visited


T = int(input())
for t in range(T):
    columns, rows = map(int, input().split())
    matrix = [["" for j in range(columns)] for i in range(rows)]
    visited = [[False for j in range(columns)] for i in range(rows)]
    source = None
    # build matrix
    for i in range(rows):
        row_i = [c for c in input()]
        for j in range(len(row_i)):
            matrix[i][j] = row_i[j]
            if matrix[i][j] == "@":
                source = Position(i, j)
    # finish build matrix
    # BFS from source and count visited places
    print("Case {}: {}".format(t + 1, BFS(source)))
