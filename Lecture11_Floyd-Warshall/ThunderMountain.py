"""
Bài toán trở thành tìm đường đi ngắn nhất từ điểm 1 đến điểm n, với một điều kiện là khoảng cách giữa 2 điểm bất kỳ không
được vượt quá 10km => ta duyệt tất cả các cặp đỉnh, cặp đỉnh nào có độ dài bé hơn 10km thì nối vào. Ta muốn biết chi phí vận chuyển
từ town này sang town khác trong TH xấu nhất, vậy ta cần tìm quãng đường dài nhất trong số các đoạn đường ngắn nhất từ đỉnh này đến 
đỉnh kia mà ta vừa tìm dc, trong TH tồn tại 1 cặp không có đường đi => "Send Kurdy"

"""
import math

def get_distance(node1, node2, dict_coord):
    return math.sqrt( (dict_coord[node1][0] - dict_coord[node2][0])  ** 2 + (dict_coord[node1][1] - dict_coord[node2][1])  ** 2)

def FloydWarShall(dist, N):
    for k in range(N):
        for i in range(N):
            if dist[i][k] == INF:
                continue
            for j in range(N):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    

INF = 10 ** 9
cases = int(input())
for c in range(cases):
    N = int(input())
    dist = [[0 if i==j else INF for j in range(N)] for i in range(N)]
    dict_coord = dict()
    for n in range(N):
        x_n, y_n = map(int, input().split())
        dict_coord[n] = [x_n, y_n]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            test_distance = get_distance(i,j, dict_coord)
            if test_distance <= 10:
                dist[i][j] = test_distance

    FloydWarShall(dist, N)
    max_cost = 0
    possible = False
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            max_cost = max(dist[i][j], max_cost)
    print("Case #{}:".format(c+1))
    print(max_cost if max_cost != INF else 'Send Kurdy')
    print()