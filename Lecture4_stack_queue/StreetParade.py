from cmath import pi
import queue
# N  = int(input())
# input = [int(x) for x in input().split(" ")]

input = [5, 1, 2, 4, 3]
input1 = input[::-1]
print(input1)



def convert_string_to_list(str):
    str_lst = str.split(" ")
    return [int(i) for i in str_lst]

list_input = []
while input() != "0":
    text_input = input()
    list_input.append[text_input]

N = int(list_input[0])
list_input_str = list_input[1:-1]
list_input_num = [convert_string_to_list(str) for str in list_input_str]


median = []
out = queue.Queue()
while out.qsize() <= len(input1):
    median.append(input1[-1])
    input1.pop()
    if median[-1] >= input1[-1]:
        out.put(input1[-1])
        input1.pop()
    else:
        out.put(median[-1])
        median.pop()
    if out.qsize() > 0:
        if len(median) == 0:
            if out.queue[0] > input1[-1]:
                print("no")
                exit()
        elif len(input1) == 0:
            if out.queue[0] > median[-1]:
                print("no")
                exit()
        elif out.queue[0] > max(input1[-1], median[-1]):
            print("no")
            exit()







def convert_string_to_list(str):
    str_lst = str.split(" ")
    str_lst.pop()
    return str_lst


list_input = []
while True:
    text = input()
    if text == "0":
        break
    else:
        list_input.append(text)
        print(text)
        
N = int(list_input[0])
list_input_str = list_input[1:]
list_input_num = [convert_string_to_list(str) for str in list_input_str]

print(list_input_num)


for input1 in list_input_num:
    median = []
    out = queue.Queue()
    while out.qsize() <= len(input1):
        median.append(input1[-1])
        input1.pop()
        if median[-1] >= input1[-1]:
            out.put(input1[-1])
            input1.pop()
        else:
            out.put(median[-1])
            median.pop()
        if out.qsize() > 0:
            if len(median) == 0:
                if out.queue[0] > input1[-1]:
                    print("no")
                    break
            elif len(input1) == 0:
                if out.queue[0] > median[-1]:
                    print("no")
                    break
            elif out.queue[0] > max(input1[-1], median[-1]):
                print("no")
                break
    print("yes")
    median = []
    out = queue.Queue()
