

def BinarySearch(a, q):
    left = 0
    right = len(a) - 1
    pos_last =  len(a)
    ans_upper_bound = 0
    # Tìm upper bound(phần tử nhỏ nhất lớn hơn nó), nếu vị trí của upper bound nằm ngoài dãy => xuất ra X
    while left<=right:
        mid = (left+right)//2
        if q < a[mid]:
            pos_last = min(pos_last,mid)     
            right = mid-1
        else:
            left = mid+1
    if pos_last == len(a):
        ans_upper_bound  = "X"
    else:
        ans_upper_bound = a[pos_last]
    
    left = 0
    right = len(a) - 1
    pos_front = -1
    ans_lower_bound = 0
    # Tìm lower bound(phần tử lớn nhất nhỏ hơn nó), nếu vị trí của lower bound nằm ngoài dãy => xuất ra X
    while left<=right:
        mid = (left+right)//2
        if q > a[mid]:
            pos_front = max(pos_front,mid)     
            left = mid+1
        else:
            right = mid-1
    if pos_front == -1:
        ans_lower_bound  = "X"
    else:
        ans_lower_bound = a[pos_front]
    
    print("{} {}".format(ans_lower_bound, ans_upper_bound))

            






N = int(input())
list_n = list(map(int, input().split()))
Q = int(input())
list_q = list(map(int, input().split()))
for q in list_q:
    BinarySearch(list_n, q)    