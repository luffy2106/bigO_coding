"""

Sắp xếp độ phức tạp của công việc theo thứ tự tăng dần, chọn a phần tử đầu tiên rồi chọn ra phần tử cuối cùng của dãy a, tạm gọi là thresh
lúc này :
a = nb of element <= thresh (1)
b = nb of element > thresh (2)

Ta tăng dần thresh lên rồi check xem có thỏa mãn điều kiện (1) và (2) không, nếu có thì tăng số cách chọn lên 1, nếu không thì break.

Để tối ưu thuật toán, có thể check xem thresh có lớn hơn hoặc bằng phần tử cuối của dãy a và nhỏ hơn phần tử đầu tiên của dãy b không 
 """

n, a, b = map(int, input().split())
list_h = list(map(int, input().split()))
list_h.sort()

count = 0
list_b = list_h[:b]
list_a = list_h[b:]
thresh = list_b[-1]

if len(list_a) == a and len(list_b) == b:
    while True:
        valid_b = True if thresh >= list_b[-1] else False
        valid_a = True if thresh < list_a[0] else False
        if valid_a and valid_b:
            count += 1
        else:
            break
        thresh += 1
    print(count)
else:
    print(count)
