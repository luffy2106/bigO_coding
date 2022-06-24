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
            and matrix[move_i][move_j] == 1
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


while True:
    rows, columns = map(int, input().split())
    if [rows, columns] == [0, 0]:
        break
    visited = [[False for j in range(columns)] for i in range(rows)]
    matrix = [[0 for j in range(columns)] for i in range(rows)]
    dict_lick = {}  # key is the size, value is the number of slicks has the same size
    # build matrix
    for i in range(rows):
        matrix[i] = list(map(int, input().split()))
    # build dictionary of licks
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 1 and visited[i][j] == False:
                # Start search licks
                start_point_slick = Position(i, j)
                area_slick = BFS(start_point_slick)
                if area_slick in dict_lick.keys():
                    dict_lick[area_slick] += 1
                else:
                    dict_lick[area_slick] = 1
    key_list = list(dict_lick.keys())
    key_list.sort()
    nb_licks = sum([dict_lick[key] for key in key_list])
    print(nb_licks)
    for key in key_list:
        print(str(key) + " " + str(dict_lick[key]))
