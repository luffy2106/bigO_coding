


# def binarySearchRecursive(a, left, right, x):
#     if left <= right:
#         mid = (left + right) // 2
#         if a[mid] == x:
#             return mid
#         elif x < a[mid]:
#             return binarySearchRecursive(a, left, mid - 1, x)
#         else:
#             return binarySearchRecursive(a, mid + 1, right, x)
#     return -1


def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return -1


case_nb = 0
while True:
    N, Q = map(int, input().split())
    case_nb += 1
    if [N, Q] == [0, 0]:
        break
    list_n = []
    list_q = []
    for n in range(N):
        nb_n = int(input())
        list_n.append(nb_n)
    list_n.sort()
    for q in range(Q):
        nb_q = int(input())
        list_q.append(nb_q)

    left = 0
    right = len(list_n) - 1
    print("CASE# " + str(case_nb) + ":")
    for q in list_q:
        # ans = bisect.bisect_left(list_n, q, left, right)
        # ans = binarySearchRecursive(list_n, left, right, q)
        ans = bsFirst(list_n, left, right, q)
        if ans == -1:
            print(str(q) + " not found")
        else:
            print(str(q) + " found at " + str(ans + 1))
