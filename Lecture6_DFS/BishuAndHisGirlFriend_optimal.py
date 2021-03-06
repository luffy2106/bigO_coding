"""
Chạy thuật toán DFS, sau đó lấy lần lượt từng vùng đất của các cô gái rồi tìm đường đi tới vùng đất số 1. 
Lấy vùng đất có lượng đường đi qua các đỉnh là ít nhất. Để chọn ID nhỏ thì chỉ khi vùng đất nào thật sự 
lớn hơn vùng đất hiện tại bạn mới cập nhật lại. Nếu bằng thì cũng không cập nhật.

Bạn cũng có thể cải tiến một chút bằng cách chạy thuật toán từ vùng đất số 1 mà Bishu đang đứng để lấy kết quả 
đường đi đến các vùng đất mà các cô gái đang đứng. Cách này sẽ đỡ phải mất thời gian chạy đi chạy lại DFS nhiều lần.

Độ phức tạp: O(V + E + Q) với V là số lượng đỉnh của cây, E = V - 1 là số lượng cạnh của cây và 
Q là số lượng vùng đất cô gái đang ở.
"""




MAX = 1000 + 5
visited = [False] * MAX
dist = [0] * MAX
graph = [[] for _ in range(MAX)]

def DFS(scr):
    s = [scr]
    visited[scr] = True
    
    while len(s):
        u = s.pop()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                s.append(v)

V = int(input())
E = V - 1

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(1)
ans = 0
min_dist = MAX

Q = int(input())

for _ in range(Q):
    u = int(input())
    if dist[u] < min_dist or (dist[u] == min_dist and u < ans):
        min_dist = dist[u]
        ans = u

print(ans)