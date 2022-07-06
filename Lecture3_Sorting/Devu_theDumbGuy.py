"""
Nhận xét:
- Để số giờ là tối ưu, chương học nào ít chapter nhất nên đặt lên đầu, như thế học các chủ đề tiếp theo gồm nhiều chương hơn sẽ hiệu quả hơn về mặt thời gian
"""


n, x = map(int, input().split())
list_c = list(map(int, input().split()))

list_c.sort()

cost = x
total_cost = 0
for c in list_c:
    total_cost += cost * c
    if cost > 1:
        cost -= 1


print(total_cost)
