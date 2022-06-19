

from ast import While
from inspect import stack
import queue

class PQEntry_max:
    """
    Use priority queue as max-heap
    """

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

def get_check_stack(stack_test, list_operation):
    for operation in list_operation:
        type = int(operation[0])
        number = int(operation[1])
        if type == 1:
            stack_test.append(number)
        elif type == 2:
            if stack_test[-1] == number:
                stack_test.pop()
            else:
                return False
    return True

def get_check_queue(queue_test, list_operation):
    for operation in list_operation:
        type = int(operation[0])
        number = int(operation[1])
        if type == 1:
            queue_test.put(number)
        elif type == 2:
            if queue_test.queue[0] == number:
                queue_test.get()
            else:
                return False
    return True

def get_check_priority_queue(pq_test, list_operation):
    for operation in list_operation:
        type = int(operation[0])
        number = int(operation[1])
        if type == 1:
            pq_test.put(PQEntry_max(number))
        else:
            if pq_test.queue[0].value == number:
                pq_test.get()
            else:
                return False
    return True

str_N = ''

while True:
    try:
        str_N = input()
    except:
        break
    #print(str_N)
    # if not str_N:
    #     break
    N = int(str_N)
    stack_test = []
    queue_test = queue.Queue()
    pq_test = queue.PriorityQueue()
    list_operation = []
    for i in range(N):
        operation = input().split(" ")
        list_operation.append(operation)
    check_stack = get_check_stack(stack_test, list_operation)
    check_queue = get_check_queue(queue_test, list_operation)
    check_priority_queue = get_check_priority_queue(pq_test, list_operation)
    if (check_queue and check_stack) or (check_queue and check_priority_queue) or (check_stack and check_priority_queue):
        print("not sure")
    elif check_stack:
        print("stack")
    elif check_queue:
        print("queue")
    elif check_priority_queue:
        print("priority queue")
    else:
        print("impossible")





