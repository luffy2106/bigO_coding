"""
Nhận xét:
Giải thích ví dụ: Ví dụ gồm 2 bộ test.

Bộ 1: chỉ một cặp có thể tạo được là {9, 3}.

Bộ 2: chỉ có một cặp tạo được là {-7, -2}.

Hướng dẫn giải: Ở đây đề bài yêu cầu ta chia N số nguyên sao cho được nhiều cặp nhất và mỗi cặp có tổng bằng MM. Vì mọi giá trị trong mảng đều phân biệt, n
ên hai cặp {a, b} và {c, d} với a + b = c + d = M thì ta chắc chắn thấy rằng 4 số này đều sẽ khác nhau. Như vậy, có thể sử dụng binary search. 
Với mỗi giá trị x, ta sẽ thử tìm y sao cho x + y = M. Vì vai trò của x và y là như nhau, nên ta giả sử x < y. 
Như vậy, bài toán sẽ trở thành với mỗi phần tử x ta chỉ cần kiểm tra xem phần tử M – y có nằm trong mảng hay không. 
Tức duyệt lần lượt qua mỗi phần tử, với mỗi a[i], xem M - a[i] 
có xuất hiện trong mảng con từ i + 1 đến N - 1 hay không (index tính từ 0).

Độ phức tạp: O(T * NlogN) với T là số lượng bộ dữ liệu, N là số lượng chiếc bánh pizza.


"""
import bisect


def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return False


T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    list_n = list(map(int, input().split()))
    list_n.sort()
    nb_pairs = 0
    for i in range(n):
        left_num = m - list_n[i]
        # index = bisect.bisect_left(list_n, left_num, i, len(list_n))
        index = bsFirst(list_n, i + 1, n - 1, left_num)
        if index:
            nb_pairs += 1
    print(nb_pairs)