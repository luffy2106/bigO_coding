"""
Nhận xét :

Nếu coi mỗi cầu thủ là 1 đỉnh của đồ thị thì nhiệm vụ cần làm là tìm đường đi ngắn nhất từ node của 1 cầu thủ đến
node IvanKov => có thể sử dụng thuật toán Dijkstra

"""
import queue


class Node:
    def __init__(self, name, dist):
        self.name = name
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist


def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.name
        w = top.dist
        if graph.get(u):
            for neighbor in graph.get(u):
                if w + neighbor.dist < dist[neighbor.name]:
                    dist[neighbor.name] = w + neighbor.dist
                    pq.put(Node(neighbor.name, dist[neighbor.name]))
                    path[neighbor.name] = u



N = int(input())
INF = int(1e9)
graph = {}
dist = {}
path = {} 
set_team = set()
for n in range(0, N):
    set_member = set(input().split())
    set_team.update(set_member)
    for member in set_member:
        not_member = set([Node(m, 1) for m in set_member if m != member])
        if member not in graph.keys():
            graph[member] = not_member
        else:
            graph[member].update(not_member)

list_team = list(set_team)
list_team.sort()

for name in list_team:
    dist[name] = INF

Dijkstra("Isenbaev")
for name in list_team:
    if dist[name] != INF:
        print(name+" "+str(dist[name]))
    else:
        print(name+" "+"undefined")

    


