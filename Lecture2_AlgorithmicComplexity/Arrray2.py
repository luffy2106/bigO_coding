N1 = 8 
K1 = 3
input1 = [1,1,2,2,3,3,4,5]
index_input1 = list(range(1,len(input1)+1))


def get_first_K(input, index_input, K,nb_recursive=0):
    if nb_recursive > 1:
        return str(index_input[-1])+" "+str(index_input[0]) 
    else:
        stack = []
        nb_distinc=0
        for i in range(0, len(input)):
            if len(stack) == 0:
                nb_distinc+=1
            else:
                if input[i] not in stack:
                    nb_distinc+=1
            stack.append(input[i])
            if nb_distinc == K:
                break
        index_input = index_input[0:len(stack)]
        if nb_recursive==0:
            stack = stack[::-1]
            index_input = index_input[::-1]
        if nb_distinc < K:
            return("-1 -1")
        nb_recursive+=1
        return get_first_K(stack, index_input, K,nb_recursive)

    

    # return stack, index_input, nb_distinc




print(get_first_K(input1, index_input1 ,K1, 0))

# if nb_distinc == K1:
#     # first_k_reverse = first_k[::-1]
#     first_k_2, first_k_index_2 = get_min_first_k(first_k, first_k_index, K1)
#     # out_put = first_k_index_2[::-1]
#     # out_put = [i+1 for i in out_put]
#     print(str(first_k_index_2[0])+" "+str(first_k_index_2[-1]))
# else:
#     print("-1 -1")
# # first_k_index_min = get_min_first_k(first_k, first_k_index, K1)