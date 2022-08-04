"""
Nhận xét :
Ban đầu, số lượng connected component sẽ bằng số đỉnh, sau mỗi mần thực hiện union thành công, số lượng connected component sẽ giảm đi 1
"""


def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return False
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1
    return True


T = int(input())
input()
for t in range(T):
    char_node = input()
    nb_node = nb_connnected_components = int(ord(char_node)) - int(ord("A")) + 1
    MAX = nb_node
    parent = [i for i in range(MAX)]
    ranks = [0] * (MAX)
    uv = ""
    while True:
        try:
            uv = input()
        except:
            break
        if uv == "":
            break
        [u, v] = [char for char in uv]
        u = ord(u) - ord("A")
        v = ord(v) - ord("A")
        union_success = unionSet(u, v)
        if union_success:
            nb_connnected_components -= 1
    print(nb_connnected_components)
    print()
