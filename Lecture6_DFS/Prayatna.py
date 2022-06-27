"""
Nhận xét:
- Bài toán có thể đưa về việc tìm các thành phần liên thông trong đồ thị. Output của bài toán sẽ là số các thành phần 
liên thông trong đồ thị. 
=> Chạy DFS theo từng đỉnh để tìm các thành phần liên thông, mỗi lần chạy tăng biến đếm thêm 1, nếu đỉnh nào đã được duyệt, ta không chạy DFS để tìm các thành phần liên thông
của đỉnh đó nữa. output ra số thành phần liên thông. 
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
