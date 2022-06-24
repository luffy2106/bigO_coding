from ast import Return
import queue

"""
Ex input :
3 30
3
2 5 7

Nếu xem mỗi giá trị mà chìa khóa có thể nhận được là một đỉnh của đồ thị và mỗi phép nhân chìa khóa với một số bất kỳ 
trong N số được cho tạo nên một cạnh của đồ thị thì ta có thể sử dụng giải thuật BFS cho bài toán này như sau:
Bước 1: Xác định đỉnh xuất phát là giá trị ban đầu của chìa khóa.
Bước 2: Xác định đỉnh đích là giá trị khóa cần đạt được.
Bước 3: Duyệt BFS từ đỉnh xuất phát. Mỗi lần lấy ra một đỉnh u từ hàng đợi, ta thực hiện phép nhân giá trị của đỉnh đó với lần 
lượt từng số trong N số được cho. Kết quả thu được từ phép nhân trên được mod cho 100.000 chính là một đỉnh v mới trong đồ thị. 
Bước làm này chính là ta đang phát sinh các cạnh (u, v) có thể có của đồ thị.
"""



pri_key, lock_key = map(int, input().split())
N = int(input())
MAX = pow(10, 5) + 1
key_n = list(map(int, input().split()))
MOD = pow(10, 5)
dist = [-1] * MAX  #vị trí của mỗi phần tử trong mảng sẽ đại điện cho node trong đồ thị. Mỗi node đại diện cho giá trị khóa update sau phép nhân.

def BFS(s,f):
    q = queue.Queue()
    q.put(s)
    dist[s] = 0
    while not q.empty():
        u = q.get()
        for key in key_n:
            key_update = (u * key) % MOD
            if dist[key_update] == -1:
                dist[key_update] = dist[u] + 1
                q.put(key_update)

                if key_update == f:
                    return dist[key_update]
    return -1        


print(BFS(pri_key, lock_key))
