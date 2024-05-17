"""
Question : Given a sorted array of distinct integers and a target value, return the First index of the target if the target is found. If not, return -1.
You must write an algorithm with O(log n) runtime complexity.

Input :
Ex :
a = [1,1,2,2,2,3,4,5,7]
target = 2

Expected output : 4
"""

def binary_search_last(a, target, left, right):
    if left <= right:
        mid = (left + right)//2
        if a[mid] == target and (a[mid+1] != target or mid == right):
            return mid
        elif a[mid] < target:
            mid = left + 1
            return binary_search_last(a, target, left, right)
        else:
            mid = right -1
            return binary_search_last(a, target, left, right)
    return -1 
    




if __name__ == '__main__':
    a = [1,1,2,2,2,3,4,5,7]
    target = 2
    left = 0
    right = len(a)
    print(binary_search_last(a, target, left, right))
    