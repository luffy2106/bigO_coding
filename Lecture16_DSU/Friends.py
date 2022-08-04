"""
Để tìm largest of friend, ta cần hợp các cặp bạn bè với nhau thành 1 tập hợp lớn. Số phần từ của tập hợp này sẽ là đáp án.
Ta cần một biến num[i] để lưu số lượng phẩn tử trong tập có đỉnh i là cha. Kết quả cuối cùng là num[i] có giá trị lớn nhất
"""


# def makeSet():
#     global parent, rank, num
#     parent = [i for i in range(MAX+1)]
#     rank  = [0] * (MAX+1)
#     num = [1] * (MAX+1)


def findSet(u):
    """
    Path compression
    """
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    """
    union by rank
    """
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return
    if rank[up] > rank[vp]:  # rank nào lớn hơn thì nối (con->cha)
        parent[vp] = up
        num[up] += num[
            vp
        ]  # sau khi nối, tập hợp các phần tử có nút gốc la vp sẽ dc cộng thêm tập hợp các phần tử có nút gốc là up
        # rank[up]+=1
    elif rank[up] < rank[vp]:
        parent[up] = vp
        num[vp] += num[up]
        # rank[vp]+=1
    else:
        parent[up] = vp
        rank[vp] += 1
        num[vp] += num[up]


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    MAX = N
    parent = [i for i in range(MAX + 1)]
    rank = [0] * (MAX + 1)
    num = [1] * (MAX + 1)
    for m in range(M):
        a, b = map(int, input().split())
        unionSet(a, b)
    print(max(num))
