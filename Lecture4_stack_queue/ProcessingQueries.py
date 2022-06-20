from http import server
import queue


"""
Bai giai dua theo tutor
Nhận xét:
- Nếu hàng đợi chưa đầy thì kiểu gì cũng bỏ thêm query vào được và kiểu gì query bỏ thêm vào cũng được xử lý
- Lưu mốc thời gian sau khi xử lý các query vào một hàng đợi (*).
- Nếu một query đến vào lúc hàng đợi đang đầy => in ra -1
- Nếu query đến có mốc thời gian lớn hơn thời gian xử lý bất kỳ query nào trước đó, pop thời gian xử lý query trước đó ra khỏi hàng đợi (*)
"""


n, b = map(int, input().split())
queue_test = queue.Queue()
server_time = 0  # Thời gian xử lý query hiện tại

for i in range(n):
    ti, di = map(int, input().split())
    while queue_test.qsize() != 0 and ti >= queue_test.queue[0]:
        queue_test.get()
    if queue_test.qsize() <= b:
        server_time = max(server_time, ti) + di
        queue_test.put(server_time)
        print(server_time, end=" ")
    else:
        print("-1", end=" ")
