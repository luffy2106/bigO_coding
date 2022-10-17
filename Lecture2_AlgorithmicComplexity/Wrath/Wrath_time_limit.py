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

nb_killed = 0
index_patient = 0
# for j in range(index_patient+1, len(list_L)):

while index_patient < len(list_L)-1:
    for j in range(index_patient+1, len(list_L)):
        if index_patient + list_L[j] >= j:
            nb_killed+=1
            break
    index_patient+=1


print(N-nb_killed)
