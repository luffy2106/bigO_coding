"""
Gọi địa điểm tốt nhất để 2 người gặp nhau là X, ta cần tìm X sao cho tổng đường (A->X) + (B->X) is minimum(1). Vậy ta xây dựng bảng đường đi ngắn nhất 
bằng "FLoyd-Warshall" từ 1 node đến tất cả các node, sau đó xét lần lượt X trong phương trình (1) với X là các node trong đồ thị. Do độ dài của mỗi cạnh
là 1 số dương nên đồ thị sẽ không tồn tại chu trình âm.
"""


def FloydWarShall(dist, path, N):
    for k in range(N):
        for i in range(N):
            if dist[i][k] == INF:
                continue
            for j in range(N):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]


while True:
    N = int(input())
    if N == 0:
        break
    MAX = 26
    nb_edges_max = N * (N - 1)
    INF = 10 ** 9
    dist_y_d = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]
    path_y_d = [[-1 for i in range(MAX)] for j in range(MAX)]

    # path_p_d = [[None for i in range(MAX)] for j in range(MAX)]
    dist_p_d = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]
    path_p_d = [[-1 for i in range(MAX)] for j in range(MAX)]

    for n in range(N):
        age, direct, x, y, c = input().split()
        x = ord(x) - ord("A")
        y = ord(y) - ord("A")
        if age == "Y":
            dist_y_d[x][y] = min(dist_y_d[x][y], int(c))
            path_y_d[x][y] = x
            if direct == "B":
                # bidirectional
                dist_y_d[y][x] = min(dist_y_d[y][x], int(c))
                path_y_d[y][x] = y
        else:
            dist_p_d[x][y] = min(dist_p_d[x][y], int(c))
            path_p_d[x][y] = x
            if direct == "B":
                # bidirectional
                dist_p_d[y][x] = min(dist_p_d[y][x], int(c))
                path_p_d[y][x] = y

    y, p = input().split()
    y = ord(y) - ord("A")
    p = ord(p) - ord("A")
    FloydWarShall(dist_y_d, path_y_d, MAX)
    FloydWarShall(dist_p_d, path_p_d, MAX)

    minDist = INF
    res = []
    for n in range(MAX):
        if (
            dist_p_d[p][n] != INF
            and dist_y_d[y][n] != INF
            and dist_p_d[p][n] + dist_y_d[y][n] <= minDist
        ):
            res.append((dist_y_d[y][n] + dist_p_d[p][n], n))
            minDist = dist_y_d[y][n] + dist_p_d[p][n]

    if not res:
        print("You will never meet.")
    else:
        res.sort()
        print(minDist, end="")

        for place in res:
            if place[0] != minDist:
                break
            print(" " + chr(place[1] + ord("A")), end="")
        print()
