"""
while 



"""



import queue
N = 5
# input = [5, 1, 2, 4, 3]
text_input = "19 3 5 4 20 14 10 2 12 15 11 6 8 13 1"
input = [int(x) for x in text_input.split(" ")]
input = input[::-1]


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

def check_condition_medium(stack):
    # in stack, the top element have to be smaller than the below element
    if len(stack) <= 1:
        return True
    else:
        if stack[-1] > stack[-2]:
            return False
        else:
            return True

def check_condition_output(stack):
    # in the stack output, the top element have to be bigger than the below element
    if len(stack) <= 1:
        return True
    else:
        if stack[-1] < stack[-2]:
            return False
        else:
            return True 





N = 20
medium = []
out = []
possible = True
while len(out) < len(input):
    if len(medium) == 0:
        if len(input) > 1:
            if input[-1] >= input[-2]: # put to medium
                medium.append(input[-1])
            else:
                out.append(input[-1])
            input.pop()
        elif len(input) == 1:
            out.append(input[-1])
            input.pop()
    else:
        if len(input) > 1:
            if input[-1] >= input[-2]: # put to medium
                if input[-1] >= medium[-1]:
                    out.append(medium[-1])
                    medium.pop()
                medium.append(input[-1])
                input.pop()
            else:
                out.append(get_minimum_top_stack(input, medium))
        elif len(input) == 1:
            out.append(get_minimum_top_stack(input, medium))
        else: #input is empty, put all elements in stack medium to output
            while len(medium) > 0:
                out.append(medium[-1])
                medium.pop()
    if not check_condition_medium(medium):
        possible = False
        break 
    if not check_condition_output(out):
        possible = False
        break
        

if possible:
    print("yes")
else:
    print("no")    



# for input_test in list_input:
#     N = int(input_test[0])
#     input = [int(x) for x in input_test[1].split(" ")[0:-1]]
#     input = input[::-1]
#     medium = []
#     out = []
#     possible = True
#     while len(out) < len(input):
#         if len(medium) == 0:
#             if len(input) > 1:
#                 if input[-1] >= input[-2]: # put to medium
#                     medium.append(input[-1])
#                 else:
#                     out.append(input[-1])
#             else:
#                 out.append(input[-1])
#             input.pop()
#         else:
#             if len(input) > 1:
#                 if input[-1] >= input[-2]: # put to medium
#                     if input[-1] >= medium[-1]:
#                         out.append(medium[-1])
#                         medium.pop()
#                     medium.append(input[-1])
#                 else:
#                     out.append(get_minimum_top_stack(input, medium))
#             elif len(input) == 1:
#                 out.append(get_minimum_top_stack(input, medium))
#             else: #input is empty
#                 while len(medium) > 0:
#                     out.append(medium[-1])
#                     medium.pop()
#         if not check_condition_medium(medium):
#             possible = False
#             break 
#         if not check_condition_output(out):
#             possible = False
#             break
            

#     if possible:
#         print("yes")
#     else:
#         print("no") 
