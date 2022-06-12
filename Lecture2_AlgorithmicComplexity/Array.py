from inspect import stack


N1 = 8 
K1 = 3
input1 = [1,1,2,2,3,3,4,5]

# N1 = 4 
# K1 = 2
# input1 = [1,2,2,3]

# N2 = 7
# K2 = 4
# input2 = [4,7,7,4,7,4,7]


def get_first_K(input, K):
    stack = []
    stack_index = []
    nb_distinc = 0
    for i in range(0, len(input)):
        if len(stack) == 0:
            nb_distinc+=1
        else:
            if input[i] not in stack:
                nb_distinc+=1
        stack.append(input[i])
        stack_index.append(i)
        if nb_distinc == K:
            break
    return stack, stack_index, nb_distinc

def get_min_first_k(first_k, first_k_index, K):
    stack = []
    stack_index = []
    nb_distinc = 0
    first_k_reverse = first_k[::-1]
    first_k_index_reverse = first_k_index[::-1]
    for i in range(0, len(first_k_reverse)):
        if nb_distinc == K:
            break
        if len(stack) == 0:
            stack.append(first_k_reverse[i])
            stack_index.append(first_k_index_reverse[i])
            nb_distinc+=1
        else:
            if first_k_reverse[i] not in stack:
                nb_distinc+=1
            stack.append(first_k_reverse[i])
            stack_index.append(first_k_index_reverse[i])

    
    stack  = stack[::-1]
    stack_index  = stack_index[::-1]
    stack_index = [i+1 for i in stack_index]
    return stack, stack_index


first_k, first_k_index, nb_distinc = get_first_K(input1, K1)

if nb_distinc == K1:
    # first_k_reverse = first_k[::-1]
    first_k_2, first_k_index_2 = get_min_first_k(first_k, first_k_index, K1)
    # out_put = first_k_index_2[::-1]
    # out_put = [i+1 for i in out_put]
    print(str(first_k_index_2[0])+" "+str(first_k_index_2[-1]))
else:
    print("-1 -1")
# first_k_index_min = get_min_first_k(first_k, first_k_index, K1)









# def get_list_distinc(input, K):
#     stack = []
#     stack_index = []
#     nb_distinc = 0
#     valid_distinc = True
#     for i in range(0, len(input)):
#         if len(stack) == 0:
#             stack.append(input[i])
#             stack_index.append(i)
#             nb_distinc +=1
#         else:
#             if input[i] in stack:
#                 if input[i] == stack[-1]:
#                     stack[-1] = input[i]
#                     stack_index[-1] = i
#                 else:
#                     stack.append(input[i])
#                     stack_index.append(i)
#             else:
#                 stack.append(input[i])
#                 stack_index.append(i)
#                 nb_distinc +=1
        
#         if nb_distinc == K:
#             break

#     if nb_distinc < K:
#         valid_distinc = False
#     stack = [e+1 for e in stack]
#     stack_index = [e+1 for e in stack_index]

#     return stack, stack_index, valid_distinc

# list_distinc, list_distinc_index, valid_distinc = get_list_distinc(input1, K1)
# print(valid_distinc)
# print(list_distinc)
# print(list_distinc_index)
# if nb_distinc == K1:
#     print(str(first_k_index_min[0])+" "+str(first_k_index_min[-1]))
#     # print(first_k)
#     # print(first_k_index)

# else:
#     print("-1 -1")

# 2 5 6 5 2 1 7 9 7 2 5 5 2 4 7 6 2 2 8 7 7 9 8 1 9 6 10 8 8 6 10 3 3 9 1 10 5 8 1 10 7 8 4 8 6 5 1 10 2 5

# 2 5 6 5 2 1 7 9 7 2 5 5 2 4 7 6 2 2 8 7 7 9 8 1 9 6 10 8 8 6 10 3 3 9 1 10 5 8 1 10 7 8 4 8 6 5 1 10 2