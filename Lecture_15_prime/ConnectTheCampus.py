"""
Nhận xét:
Giả sử ta đã kết nối được tất cả các buildings, thì đường đi giữa các building phải là một minimum 
spanning tree(MST)prime để đảm bảo đi qua tất cả các building với chi phí nhỏ nhất, và cây này phải 
chứa cạnh đã kết nối. 

Ta để tìm MST prime mà đảm bảo cây bao gồm các cạnh đã được connect network thì ta cần đảm bảo đường đi 
giữa 2 node là bé nhất(=0), khi đó trong quá trình MST được build, MST sẽ lấy các cạnh này. 
Vậy ta set up 1 complete graph từ các đỉnh đã cho rồi gán độ dài các cạnh đã được connect network = 0.
Chi phí xây cạnh mới sẽ bằng chi phí cây MST.
"""

import math
import queue

def get_distance(u , v, dict_node):
    return math.sqrt((dict_node[u][0] - dict_node[v][0]) ** 2 + (dict_node[u][1] - dict_node[v][1]) ** 2)

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def weightMST():
    ans = 0
    for i in range(1, N+1):
        if path[i] == -1:
            continue
        ans+= dist[i]
    return ans



def prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        if dist[u] != w:  # optimize like dijkstra
            continue
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u
                    




while True:
    dict_node = dict()
    N = 0
    try:
        N = int(input())
    except:
        break
    INF = 10000
    graph = [[] for i in range(N+1)]
    visited = [False for i in range(N + 1)]
    dist = [INF for i in range(N + 1)]
    path = [-1 for i in range(N + 1)]
    list_node = set(range(1,N+1))
    for t in range(1, N+1):
        x, y = map(int, input().split())
        dict_node[t] = [x,y]


    M = int(input())
    set_edge = set()
    cost_existing_cabble = 0
    for m in range(M):
        u, v = map(int, input().split())
        cost_existing_cabble+= get_distance(u,v,dict_node)
        set_edge.add((u,v))
        set_edge.add((v,u))


    # Create completed graph for unvisted 
    for node in range(1,N+1):
        remain_node = [rn for rn in list_node if rn!=node]
        for rn in remain_node:
            w = get_distance(node,rn,dict_node)
            if (rn,node) in set_edge:
                w = 0
            graph[node].append(Node(rn, w))
    
    prim(1)
    cost = weightMST()
    print("%.2f" % round(cost, 2))
