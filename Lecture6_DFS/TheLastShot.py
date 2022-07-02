"""
Độ phức tạp: O(V * (V + E)) với V là số lượng đỉnh, và E là số lượng cạnh của đồ thị.

Lưu ý : trong python, phép gán mảng luôn nhanh hơn thao tác thêm bớt 
Ví dụ :
- (stack = [s]) faster than (stack.append(s))
- visited = [False] * (N + 1) faster than (visited = [False for _ in range(N+1)])

"""

def DFS(s):
    visited = [False] * (N + 1)
    count=0
    stack = [s]
    visited[s] = True
    while len(stack) > 0:
        u = stack.pop()
        count+=1
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                stack.append(v)
    return count




N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for edge in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
max_impact = 0
for n in range(1, N+1):
    impact_n = DFS(n) 
    if impact_n > max_impact:
        max_impact = impact_n
print(max_impact)




