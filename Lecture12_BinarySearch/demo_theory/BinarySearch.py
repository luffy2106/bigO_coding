"""
Question : Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return -1.
You must write an algorithm with O(log n) runtime complexity.

Input :
Ex :
a = [1,1,2,2,2,3,4,5,7]
target = 3

Expected output : 5
"""

def binary_search(a, target, left, right):
    """
    Binary search function using loop
    """
    while left <= right:
        mid = int((left + right) / 2)
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursion(a, target, left, right):
    """
    Binary search function using recursion
    """
    if left <= right:
        mid = (left + right)//2
        if a[mid] == target:
            return mid
        else: 
            if a[mid] < target:
                left = mid + 1
            else:
                right = mid - 1    
            return binary_search_recursion(a, target, left, right)
    return -1


if __name__ == '__main__':
    a = [1,1,2,2,2,3,4,5,7]
    target = 3
    left = 0
    right = len(a)
    print(binary_search(a, target, left, right))
    print(binary_search_recursion(a, target, left, right))

