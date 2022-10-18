"""
https://bigocoder.com/courses/138/lectures/1779/problems/1056?view=statement
"""

"""
Trong bài toán này, ta cần quan tâm đến yếu tố:
- Người đằng sau không thể giết dc người đằng trước
- Số người còn sống bằng số người ban đầu trừ đi số người bị giết
"""


N = int(input())
list_L = [int(x) for x in input().split()]
total_kill = 0
last_killed_index = N-1
for i in range(len(list_L)-1, -1, -1): # For each loop j, we want to see how many people j can kill, if these people alreay be killed, we ignore them(based on the last people was killed in the previous loop)
    if i > i - list_L[i]: #The condition to make sure index i can kill at least one person 
        last_victim_of_i = max(0,i - list_L[i])
        if last_victim_of_i < last_killed_index:
            total_kill+= min(i, last_killed_index) - last_victim_of_i
            last_killed_index = last_victim_of_i
        
            
print(N-total_kill)

        