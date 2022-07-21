"""
Nhận xét:
Bài toán có thể đưa về thành tìm đường đi ngắn nhất giữa các đỉnh với nhau. Đường đi ngắn nhất này cần đảm bảo được rằng chi phí 
tổ chức tiệc tại một thành phố trong số các thành phố đã đi qua là lớn nhất. Ta tạo một mảng maxCost để lưu chi phí thành phố host
đắt nhất giữa hai điểm bất kỳ

Tutorial
Lưu ý: Bài tập này có thể được giải bằng cả ba thuật toán tìm đường đã học: Dijkstra, Bellman Ford và Floyd Warshall. Tuy nhiên với mỗi bộ test, ta lại có nhiều truy vấn. Do đó sẽ rất bất tiện nếu sử dụng Dijkstra hay Bellman Ford vì với mỗi truy vấn, ta phải chạy lại thuật toán. Floyd Warshall chính là lựa chọn rất tốt để giải quyết vấn đề trên.

Về việc áp dụng Floyd Warshall trong bài tập này, ta cần lưu ý:

Chi phí đi từ u đến v lúc này không chỉ bằng tổng trọng số các cạnh trên đường đi đã chọn mà còn phụ thuộc vào chi phí của đỉnh lớn nhất trong đường đi.
⇒ Dùng thêm ma trận maxCost với maxCost[i][j] là chi phí của đỉnh lớn nhất trên đường đi nhỏ nhất từ i đến j.
Khi này, đường đi từ i đến đỉnh trung gian k, rồi từ đỉnh trung gian k đến j có thể tính bằng công thức: dist[i][k] + dist[k][j] + max(maxCost[i][k], maxCost[k][j]).

Ta đem so sánh đường qua đỉnh trung gian k với đường đi hiện tại từ i đến j là dist[i][j] + maxCost[i][j]. Nếu tốt hơn thì cập nhật lại cả độ dài đường đi ngắn nhất và giá trị trong maxCost.

Lưu ý: Với bài này, hai đại lượng là distdist và maxCostmaxCost có thể ảnh hưởng qua lại lẫn nhau (dist tính theo maxCost, còn maxCost thì chỉ được cập nhật khi dist thay đổi) nên để đảm bảo rằng cả hai đại lượng đều tối ưu, ta phải duyệt Floyd 2 lần.

Độ phức tạp: O(T * C^3) với T là số lượng bộ test, C là số thành phố trong mỗi test case.

"""

def FloydWarShall(dist, N, maxCost):
    for _ in range(2):
        for k in range(N):
            for i in range(N):
                if dist[i][k] == INF:
                    continue
                for j in range(N):
                    maxFeast = max(maxCost[i][k], maxCost[k][j])
                    if dist[k][j] != INF and dist[i][j] + maxCost[i][j]> dist[i][k] + dist[k][j] + maxFeast:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        maxCost[i][j] = maxFeast


INF = 10 ** 9
case = 1
while True:
    C, R, Q = map(int, input().split())
    if [C, R, Q] == [0,0,0]:
        break
    cost = [0] + list(map(int,input().split()))
    maxCost = [[max(cost[i], cost[j]) for j in range(C + 1)] for i in range(C + 1)]
    dist = [[0 if i == j else INF for j in range(C + 1)] for i in range(C + 1)]
    for r in range(R):
        c1, c2, d = map(int, input().split())
        dist[c1][c2] = d
        dist[c2][c1] = d
    FloydWarShall(dist, C+1, maxCost)
    if case > 1:
        print()
    print("Case #{}".format(case))
    case+=1
    for q in range(Q):
        q1, q2 = map(int, input().split())
        print(-1 if dist[q1][q2] == INF else dist[q1][q2] + maxCost[q1][q2])

    



    


