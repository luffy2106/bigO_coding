"""
Nhận xét:
Giả sử mỗi loại tiền tệ là đỉnh của một đồ thị, trader sẽ có lợi nhuận nếu như quãng đường lớn nhất từ nó đến chính nó có tích độ dài lớn hơn 1. Vậy ta sẽ sử dụng
FoydWarShall để xây dựng bảng lưu trữ đường đi dài nhất có thể từ các node đến nhau, trong quá trình đó, xác dịnh xem có tồn tại chu trình dương không, nếu tồn tại chu trình 
dương và tích độ dài của chu trình dương này lớn hơn 1 thì trader có thể kiếm được lợi nhuận
"""


def FloydWarShall(dist, N):
    for k in range(N):
        for i in range(N):
            if dist[i][k] == 0:
                continue
            for j in range(N):
                if dist[k][j] != 0 and dist[i][j] < dist[i][k] * dist[k][j]:
                    dist[i][j] = dist[i][k] * dist[k][j]
                    # path[i][j] = path[k][j]
        for i in range(N):
            if dist[i][i] > 1:
                return True
    return False


case = 0
while True:
    case += 1
    N = int(input())
    if N == 0:
        break
    # graph = [[None for i in range(n)] for j in range(n)]
    dist = [[0 for i in range(N)] for j in range(N)]
    dict_currency = dict()
    for i in range(N):
        ci = input()
        dict_currency[ci] = i
    nb_edges = int(input())
    for e in range(nb_edges):
        c1, rate, c2 = input().split()
        nb_c1, nb_c2 = dict_currency[c1], dict_currency[c2]
        dist[nb_c1][nb_c2] = float(rate)
    if FloydWarShall(dist, N):
        print("Case {}: Yes".format(case))
    else:
        print("Case {}: No".format(case))
    input()
