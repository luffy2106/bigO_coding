import math

def hash(x,y):
    result = math.sqrt(x**2 + y**2)
    return round(result, 7)


dict_location = {}
n, s = map(int, input().split())
for i in range(n):
    x_i, y_i, k_i = map(int, input().split())
    hash_x_y = hash(x_i, y_i)
    if hash_x_y in dict_location.keys():
        dict_location[hash_x_y]+=k_i
    else:
        dict_location[hash_x_y]=k_i

#print(dict_location)

list_dict_key = sorted(list(dict_location.keys()))

i = 0
sum_population = 0
addtional_population = 10 ** 6 - s

max_key = None
while i < len(list_dict_key):
    sum_population+=dict_location[list_dict_key[i]]
    if sum_population >= addtional_population:
        max_key = list_dict_key[i]
        break
    i+=1

if sum_population < addtional_population:
    print(-1)
else:
    print(max_key)

    

