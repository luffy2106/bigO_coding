"""
Ta có thể dùng thuật toán DSU để giải quyết bài toán này. Nếu coi mỗi lần hỏi 1 cặp mà họ trả lời là cùng chung tôn giáo, 
tương đương với việc hợp 2 nốt để tạo thành 1 component lớn hơn. Với mỗi lẫn hợp nhất mà thành công, tức là 2 phần tử không
cùng 1 thành phần liên thông thì số lượng thành phần liên thông tối đa giảm đi 1 (ban đầu khi chưa tiến hành hợp nhất, số thành
phần liên thông sẽ bằng số node)
"""

def makeSet():
    global parent, ranks
    parent = [i for i in range(MAX+5)]
    ranks = [0 for i in range(MAX+5)]

def findSet(u):
    if parent[u] !=u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSetByRank(u,v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return max_nb_connected_component
    if ranks[up] > ranks[vp]:
        parent[vp] = up
        return max_nb_connected_component -1 
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        return max_nb_connected_component -1
    else:
        parent[up] = vp
        ranks[vp] += 1
        return max_nb_connected_component -1

def unionSet(u,v):
    up = findSet(u)
    vp = findSet(v)
    if up!=vp:
        parent[up] = vp
        return True
    return False


MAX = 50000
parent = []
ranks = []
case = 0
while True:
    case+=1
    n, m = map(int, input().split())
    if [n,m] == [0,0]:
        break
    makeSet()
    max_nb_connected_component = n
    for i in range(m):
        u, v = map(int, input().split())
        max_nb_connected_component = unionSetByRank(u,v)
    print("Case {}: {}".format(case, max_nb_connected_component))