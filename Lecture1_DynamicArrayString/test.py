"""
Generate tat cac cac chuoi nam trong khoang tu aa...aa den zz...zz voi n bat ky 
"""

"""
Solution tutor
"""
def permute(a, lst, l, n):
	if l > n: return 
	for i in range(97,122):
		a += chr(i)
		permute(a, lst, len(a), n)
		if len(a) == n: lst.append(a)
		a = a[:-1]
lst = []
n = int(input())
permute('', lst, 0, n)
print(len(lst))
print(lst)



"""
My solution(not finished)
"""
n = 2
N = pow(26, n)
output_list = set()
str = ""
start = [97] * n
slice = [0] * n 
step = 0
step_slice = 1
for i in range(0,N):
    step += 1
    slice[-step_slice] = step
    print(slice)
    zipped_lists = zip(start, slice)
    listBetween_num = [x + y for (x, y) in zipped_lists]
    listBetween = "".join([chr(num) for num in listBetween_num])
    output_list.add(listBetween)
    if step == 25:
        step = 0
        slice = [0] * n
        step_slice += 1
    if step_slice == n:
        break

print(N)
print(output_list)
print(len(output_list))        


if 'aa' in output_list:
    print('aa')
if 'cc' in output_list:
    print('cc')
