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
for j in range(len(list_L)-1, -1, -1): # For each loop j, we want to see how many people j can kill, if these people alreay be killed, we ignore them(based on the last people was killed in the previous loop)
    thresh = min(j, last_killed_index)
    for i in range(0, thresh, 1):
        if i + list_L[j] >= j: # if index j can kill index i
            if i < last_killed_index:
                nb_killed = thresh-i
                total_kill += nb_killed
                last_killed_index = i
                break
        

print(N-total_kill)

        