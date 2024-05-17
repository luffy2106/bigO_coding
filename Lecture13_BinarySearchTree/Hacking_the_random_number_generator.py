"""
1. Question
You recently wrote a random number generator code for a web application and now you notice that some cracker has cracked it. It now gives numbers at a difference of some given value k more predominantly. You being a hacker decide to write a code that will take in n numbers as input and a value k and find the total number of pairs of numbers whose absolute difference is equal to k, in order to assist you in your random number generator testing.

NOTE: All values fit in the range of a signed integer, n, k>=1

Input
1st line contains n & k.
2nd line contains n numbers of the set. All the n numbers are assured to be distinct.

(Edited: n <= 10^5)

Output
One integer saying the number of pairs of numbers that have a diff k.

Ex :

Input:
5 2
1 5 3 4 2
Output:
3

Explain : We can see that there are 3 pairs which have diff k = 2: (1,3), (5,3), (4,2)


Source :

https://www.spoj.com/problems/HACKRNDM/

(this problem come from lecture binary search but you can also solve the problem by BST as well)
https://bigocoder.com/courses/138/lectures/1843/problems/1076?view=statement

2. Solution
- We can see that all integeres in the input has to be unique and we need to store the diff of unique value => we can use binary search tree
- We want to find all the pairs which the diff is k, it can be seen as for each element in array, find an element in BST that have the diff = k with this element

Implementation:
Step 1 : Set up binary tree with node, insert and search function
Step 2 : Create a binary search tree from the list
Step 3 : For each node:
- If the root - root.left < 2, move to the left(if it's equal to 2 => count). When top_left = Node, stop
- If the root.right - root < 2, move to the right(if it's equal to 2 => count). When top_right = Node, stop
"""


class Node:
    def __init__(self, val) -> None:
        self.val = val 
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    """Search value = key in binary tree root

    Args:
        root (Node): binary tree
        key (num): value which need to search

    Returns:
        num: return key if found and return None if not found 
    """
    if not root or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def count_pais_with_different_k(a, k):
    # Convert list to binary tree
    root = Node(a[0])
    count = 0
    for i in range(1, len(a)):
        insert(root, a[i])

    for num in a:
        target_bigger = num + k
        target_smaller = num - k
        if search(root, target_bigger):
            count+=1
        if search(root, target_smaller):
            count+=1

    # Because during the loop each pair will be count twice : (3,1) and (1,3) is the same, so we need to divide by 2
    count = count // 2

    return count
    
n, k = 5,2
a = [1,5,3,4,2]


print(count_pais_with_different_k(a,k))
    
