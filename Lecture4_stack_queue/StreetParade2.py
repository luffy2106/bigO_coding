import queue
N = 5
input = [5, 1, 2, 4, 3]
text_input = "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1"
input1 = [int(x) for x in text_input.split(" ")]

# input1 = input[::-1]
# print(input1)


def get_minimum_top_stack(stack1, stack2):
    if len(stack1) == 0 and len(stack2) > 0:
        delete = stack2[-1]
        stack2.pop()
        return delete
    if len(stack1) > 0 and len(stack2) == 0:
        delete = stack1[-1]
        stack1.pop()
        return delete
    if len(stack1) > 0 and len(stack2) > 0:
        if stack1[-1] > stack2[-1]:
            delete = stack2[-1]
            stack2.pop()
            return delete
        else:
            delete = stack1[-1]
            stack1.pop()
            return delete
        

# N = ""
# list_input = []
# while True:
#     N = input()
#     if N == "0":
#         break
#     input_test = []
#     text = input()
#     input_test.append(N)
#     input_test.append(text)
#     list_input.append(input_test)



# print(list_input)

# for input_test in list_input:
#     N = input_test[0]
#     input1 = [int(x) for x in input_test[1].split(" ")[0:-1]]
N = 20
medium = []
out = queue.Queue()
possible = True        
for i in range(N, 0, -1):
    list_queue = list(out.queue)
    if len(medium)>=2:
        if medium[-1] > medium[-2]:
            # print("no")
            possible = False
            break
    if out.qsize()>=2:
        if out.queue[0] > out.queue[1]:
            # print("no") 
            possible = False
            break
    if len(input1) > 1:
        if input1[-1] > input1[-2]:
            medium.append(input1[-1])
        else:
            out.put(get_minimum_top_stack(input1, medium))
    else:
        while len(input)>0 and len(medium) > 0:
            out.put(get_minimum_top_stack(input1, medium))

if possible:
    print("yes")
else:
    print("no")






for input_test in list_input:
    N = int(input_test[0])
    input1 = [int(x) for x in input_test[1].split(" ")[0:-1]]
    medium = []
    out = queue.Queue()        
    possible = True 
    for i in range(N, 0, -1):
        if len(medium)>=2:
            if medium[-1] > medium[-2]:
                possible = False
                break
        if out.qsize()>=2:
            if out.queue[0] > out.queue[1]:
                possible =  False 
                break
        if len(input1) > 1:
            if input1[-1] > input1[-2]:
                medium.append(input1[-1])
            else:
                out.put(get_minimum_top_stack(input1, medium))
        else:
            while len(input)>0 and len(medium) > 0:
                out.put(get_minimum_top_stack(input1, medium))
    
    if possible:
        print("yes")
    else:
        print("no")