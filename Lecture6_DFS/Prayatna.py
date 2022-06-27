"""
Nhận xét:
- Bài toán có thể đưa về việc tìm các thành phần liên thông trong đồ thị. Output của bài toán sẽ là số các thành phần 
liên thông trong đồ thị. 
=> Chạy DFS theo từng đỉnh để tìm các thành phần liên thông, nếu đỉnh nào đã nằm trong thành phần liên thông, ta không xét nữa. (thêm các đỉnh vào 
đã nằm trong thành phần liên thông vào 1 set)
"""


def DFS(s):
    stack = []
    stack.append(s)
    visited[s] = True
    while len(stack) > 0:
        u = stack.pop()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                # path[v] = u
                stack.append(v)


T = int(input())
for t in range(T):
    N = int(input())
    E = int(input())
    graph = [[] for g in range(N)]
    visited = [False for v in range(N)]
    set_node = set()
    for e in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    nb_connected_components = 0
    n = 0
    while n < N:
        if visited[n] == True:
            n += 1
            continue
        # do sth
        DFS(n)
        nb_connected_components += 1
        n += 1
    print(nb_connected_components)
