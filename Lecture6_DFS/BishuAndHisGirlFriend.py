import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)


def DFS(s):
    stack = []
    stack.append(s)
    visited[s] = True
    while len(stack) > 0:
        u = stack.pop()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                path[v] = u
                stack.append(v)

def get_len_path(s, d, route):
    if s == d:
        return len(route)
    else:
        route.append(path[s])
        return get_len_path(path[s], d, route)




if __name__ == '__main__':
    N = int(input())
    graph = [[] for i in range(N+1)]
    visited = [False for i in range(N+1)]
    path = [-1 for i in range(N+1)]
    dist = [0 for i in range(N+1)]
    # build matrix
    MIN = N
    for i in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    DFS(1)
    Q = int(input())
    chosen = None
    for i in range(Q):
        q = int(input())
        dist[q] = get_len_path(q, 1, route=[])
        if dist[q] < MIN or (q < chosen and dist[q] == MIN):
            MIN = dist[q]
            chosen = q
    print(chosen)
        






