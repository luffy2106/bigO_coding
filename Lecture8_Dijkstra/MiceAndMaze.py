"""
Nhận xét :
Mỗi con chuột được đặt trên 1 cell để tìm đường ra => số chuột sẽ bằng số cell.

Bài toán trở về :
Tìm đường đi ngắn nhất từ exit cell đến các cell còn lại(lưu ý chỗ này lúc add node vào graph sẽ add ngược chiều mũi tên vì mình xuất phát từ điểm exit). Nếu đường đi ngắn nhất nhỏ hơn hoặc bằng T (count-down timer) thì con chuột
đó sẽ tìm được lối thoát trong thời gian cho phép. 
"""
from operator import ne
import queue

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist

N = int(input())
E = int(input())
T = int(input())
M = int(input()) 
MAX = N
graph = [[] for i in range(MAX+1)]
dist = [T+1 for i in range(MAX+1)]

def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id 
        w = top.dist
        if dist[u] != w:
            continue
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                

for m in range(M):
    a,b,w = map(int, input().split())
    node_a = Node(a, w)
    graph[b].append(node_a)
Dijkstra(E)
count = 0
for i in range(len(dist)):
    if dist[i] <= T:
        count+=1

print(count)


