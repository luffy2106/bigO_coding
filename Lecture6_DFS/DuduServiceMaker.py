"""
Đồ thị chỉ có thể tồn tại chu trình chỉ khi nào có một cạnh nối từ u đến một đỉnh v nào đó được thăm trước đó, đồng thời từ v phải đến được uu.
Do đó ta cần thêm một mảng để truy vết đường đi và kiểm tra điều kiện trên, tạm gọi là mảng path.
Như vậy, ý tưởng giải cơ bản sẽ là sử dụng DFS để duyệt qua từng đỉnh, với mỗi đỉnh uu đang xét, ta duyệt qua từng đỉnh v kề với u:

- Nếu v chưa thăm thì ta duyệt DFS(v).
- Nếu v thăm rồi, lúc này cần kiểm tra trong mảng path xem từ v có đến được uu hay không, nếu đến được thì chứng tỏ có chu trình.
Độ phức tạp: O(N) với mỗi đỉnh -> O(N^2) cho toàn đồ thị.

Ta có thể tối ưu theo như hướng dẫn giải, bài này khá trừu tượng, cần xem lại.

"""
import sys

sys.setrecursionlimit(10005)


# def get_path(s, d, route):
#     if s == d:
#         return route
#     else:
#         route.append(path[s])
#         return get_path(path[s], d, route)


def check_current_path_cycle(s, d, route):
    # Kiem tra xem co duong di nao den chinh no hay khong
    if s == d:
        return route
    else:
        route.append(path[s])
        return check_current_path_cycle(path[s], d, route)


def cycle_DFS(u):
    visited[u] = 1
    for v in graph[u]:
        if visited[v] == 1:  # u đã được duyệt và v là hàng xóm của u. v đã được duyệt.
            return True
        elif (
            visited[v] == 0
        ):  # u đã được duyệt và v là hàng xóm của u. v chưa được duyệt.
            if cycle_DFS(
                v
            ):  # v chưa được duyệt, kiểm tra xem nó có tồn tại đường đi từ v đến đỉnh u gốc không, nếu có tức là tồn tại chu trình
                return True
    # v đã được duyệt và v không nẵm trong path DFS duyệt từ đỉnh u, tuy nhiên Khi mình duyệt xong DFS(u),
    # thì lúc trở về đỉnh cha của u, chắc chắn u không nằm trên đường đi từ gốc đến cha của u, vì vậy cần gán giá trị u là chưa được duyệt trước
    # khi thoát khỏi dfs(u)
    visited[u] = 2
    return False


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    path = [-1 for i in range(N + 1)]
    inPath = [
        False for _ in range(N + 1)
    ]  # inPath[i] = True nếu i nằm trong đường đi từ gốc DFS đến đỉnh u đang xét
    nodes = [n for n in range(1, N + 1)]
    nodes = set()
    for m in range(M):
        a, b = map(int, input().split())
        nodes.add(a)
        nodes.add(b)
        graph[a].append(b)
    ans = "NO"
    for node in nodes:
        if visited[node] == 0:
            if cycle_DFS(node):
                ans = "YES"
                break
    print(ans)
