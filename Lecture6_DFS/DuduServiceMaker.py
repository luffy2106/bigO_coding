"""
Bài toán trở về thành, trong tất cả các đỉnh, có tồn tại đường đi nào từ đỉnh đến chính nó hay không.
=> sử dụng DFS để tìm đường đi đến tất cả các đỉnh, trong quá trình tìm, nếu tồn tại cycle thì trả về YES,
còn không thì là No.
"""
import sys
sys.setrecursionlimit(10005)


def cycle_DFS(s):
    stack = []
    stack.append(s)
    visited[s] = True
    visited_node_DFS = [0 for i in range(N+1)]
    while len(stack) > 0:
        u = stack.pop()
        visited_node_DFS[u] +=1
        for v in graph[u]:
            # if visited[v] == False:
            visited[v] = True
            path[v] = u
            stack.append(v)
        if visited_node_DFS[u] > 1:
            return True    
    return False


T = int(input())
for t in range(T):
    N,M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    path = [-1 for i in range(N+1)]
    # nodes = [n for n in range(1, N+1)]
    nodes = set()
    for m in range(M):
        a,b = map(int, input().split())
        nodes.add(a)
        nodes.add(b)
        graph[a].append(b)
    ans = "NO"
    for node in nodes:
        if cycle_DFS(node):
            ans = "YES"
            break
    print(ans)


    


