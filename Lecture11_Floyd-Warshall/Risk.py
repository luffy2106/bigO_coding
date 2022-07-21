"""
Nhận xét:
Do đường đi giữa các cạnh có chiều dài là một, nên ta có thể coi số thành chiếm được khi đi từ điểm đầu đến điểm đích sẽ bằng số cạnh, và nếu muốn
phải chiếm ít thành nhất, ta chỉ cần tìm đường đi ngắn nhất từ điểm đầu đến điểm đích với mỗi cặp source dest => sử dụng thuật toán Floyd Warshall thông thường
"""


def FloydWarShall(dist, N):
    for k in range(N):
        for i in range(N):
            if dist[i][k] == INF:
                continue
            for j in range(N):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


INF = 10 ** 9
MAX = 20
case = 0
while True:
    try:
        case += 1
        dist = [[0 if i == j else INF for j in range(MAX + 1)] for i in range(MAX + 1)]
        for i in range(1, MAX):
            line_i = list(map(int, input().split()))
            nb_neighbor = line_i[0]
            if nb_neighbor == 0:
                continue
            else:
                neighbors = line_i[1:]
                for n in neighbors:
                    dist[i][n] = 1
                    dist[n][i] = 1
        FloydWarShall(dist, MAX + 1)
        N = int(input())
        print("Test Set #{}".format(case))
        for n in range(N):
            n1, n2 = map(int, input().split())
            print("{:2d} to {:2d}: {}".format(n1, n2, dist[n1][n2]))
        print()
    except EOFError:
        break