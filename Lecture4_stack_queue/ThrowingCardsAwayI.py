import queue
list_queue = []
while True:
    N = int(input())
    if N == 0:
        break
    queue_i = queue.Queue()
    for i in range(1, N+1):
        queue_i.put(str(i))
        # print(i)
    list_queue.append(queue_i)

#print(list_queue)

for queue_i in list_queue:
    stack_drop = []
    while queue_i.qsize() > 1:
        stack_drop.append(queue_i.get())
        queue_i.put(queue_i.get())
    if len(stack_drop) > 0:
        str_drop = ', '.join(stack_drop)
        print("Discarded cards: {}".format(str_drop))
    else:
        print("Discarded cards:")
    print("Remaining card: {}".format(queue_i.queue[0]))
