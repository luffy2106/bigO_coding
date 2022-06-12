N1 = 50 
K1 = 7

input = "2 5 6 5 2 1 7 9 7 2 5 5 2 4 7 6 2 2 8 7 7 9 8 1 9 6 10 8 8 6 10 3 3 9 1 10 5 8 1 10 7 8 4 8 6 5 1 10 2 5"
input1 = input.split(" ")
#input1 = [1,1,2,2,3,3,4,5]
index_input1 = list(range(1,len(input1)+1))


dict_fre = {}
for e in input1:
    if e not in dict_fre.keys():
        dict_fre[e] = 1
    else:
        dict_fre[e]+=1

print(dict_fre)

def sum_value_dict(dict_free):
    return sum(dict_fre[key] for key in dict_fre.keys())

def update_dict(e, dict_fre):
    dict_fre_test = dict_fre.copy()
    if e in dict_fre_test.keys():
        if dict_fre_test[e] > 1:
            dict_fre_test[e]-= 1
        else:
            del dict_fre_test[e]
    return dict_fre_test
def move(list_test, dict_fre, gap):
    # sum_before_move = sum_value_dict(dict_fre)
    move_index = 0
    dict_fre_move_left = update_dict(list_test[0],dict_fre)
    dict_fre_move_right = update_dict(list_test[-1], dict_fre)
    if dict_fre[input1[0]] > 1:
        move_index = 0
        gap[0]+=1
        del list_test[move_index]
        return dict_fre_move_left
    if dict_fre[input1[-1]] > 1:
        move_index = -1
        gap[1]-=1
        del list_test[move_index]
        return dict_fre_move_right

    
    if sum_value_dict(dict_fre_move_left) <= sum_value_dict(dict_fre_move_right):
        move_index = 0
        gap[0]+=1
        del list_test[move_index]
        return dict_fre_move_left
    else:
        move_index = -1
        gap[1]-=1
        del list_test[move_index]
        return dict_fre_move_right

    # sum_after_move = sum_value_dict(dict_fre)
    

    # return dict_fre


index = 1
gap = [1, N1]
for i in range(0, len(input1)):
    if len(dict_fre.keys()) == K1:
        if (dict_fre[input1[0]] > 1 or dict_fre[input1[-1]] > 1):
            dict_fre = move(input1, dict_fre, gap)
        else:
        # print(str(index)+" "+str(N1))
            print(dict_fre)
            print(str(gap[0])+" "+str(gap[1]))
            exit()
    else:
        dict_fre = move(input1, dict_fre, gap)
        index+=1

print("-1 -1")




# index_input_test = list(range(1,len(input_test)+1))
# def get_first_K(input, index_input, K,nb_recursive=0):
#     if nb_recursive > 1:
#         return str(index_input[-1])+" "+str(index_input[0]) 
#     else:
#         stack = []
#         nb_distinc=0
#         for i in range(0, len(input)):
#             if len(stack) == 0:
#                 nb_distinc+=1
#             else:
#                 if input[i] not in stack:
#                     nb_distinc+=1
#             stack.append(input[i])
#             if nb_distinc == K:
#                 break
#         index_input = index_input[0:len(stack)]
#         if nb_recursive==0:
#             stack = stack[::-1]
#             index_input = index_input[::-1]
#         if nb_distinc < K:
#             return("-1 -1")
#         nb_recursive+=1
#         return get_first_K(stack, index_input, K,nb_recursive)


# print(get_first_K(input_test, index_input_test ,K, 0))