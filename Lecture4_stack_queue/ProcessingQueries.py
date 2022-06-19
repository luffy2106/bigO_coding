from http import server
import queue




def check_server_busy(current_time, ti):
    if current_time > ti:
        return True
    else:
        return False

def check_queue_full(queue_test, n):
    if queue_test.qsize() < n:
        return False
    else:
        return True

n = int(input())
b = int(input())
queue_test = queue.Queue()
current_time = 0
server_busy = False
process_qr = []
for i in range(n):
    [ti, di] = map(int, input().split())
    if i == 0:
        current_time = ti
    if check_queue_full(queue_test, n):
        if check_server_busy(current_time, ti):
            process_qr.append[-1]
        else:
            front = queue_test.queue[0]
            queue_test.get()
            queue_test.put([ti,di])
            current_time = current_time + front[1]
            process_qr.append(current_time)
    else:
        queue_test.put([ti,di])
        if check_server_busy(current_time, ti):
            continue
        else:
            queue_test.get()
            current_time = current_time + di
            process_qr.append(current_time)
