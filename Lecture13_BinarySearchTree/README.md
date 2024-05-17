# Binary Tree(BST)

Remmeber that all functions of BST apply recursion, so make sure you understand how recursion work

#### Theory
- Each node has max 2 children
- Bậc của binary tree là 2(do mỗi node có tối đa 2 node con)
- left_node < mid_node < right_node
- In binary tree, each node must contain a unique value to maintain the order and search properties of the BST structure.

#### Application

Binary tree is a strong data structure to solve searching problem. 

#### Key function of BST
Ký hiệu h là chiều cao của cây
Ký hiệu n là số nốt trong cây

- Create struture of node
```
class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None
```
- Initiate new node : O(1)
```
def createNode(x):
    newNode = Node()
    newNode.key = x
    return newNode
```
- Insert new value to BST : O(h)
```
def insertNode(root, x):
    if root == None:
        return createNode(x)
    if x < root.key: 
        # If the key is less than the value of the current root, the function recursively calls insert on the left child of the current root.
        root.left = insertNode(root.left, x)
    elif x > root.key:
        # If the key is greater than or equal to the value of the current root, the function recursively calls insert on the right child of the current root.
        root.right = insertNode(root.right, x)
    return root
```
- Create a BST : O(h*n)
```
def createTree(a,n):
    root = None
    for i in range(n):
        root = insertNode(root, a[i])
    return root
```
- Search a value in BST : O(h) với h là chiều cao của cây, worst case O(n)
```
def searchNode(root,x):
    if root == None or root.key == x:
        return root
    if root.key < x:
        return searchNode(root.right,x)
    return searchNode(root.left, x)
```
- Delete a value in BST : O(h) với h là chiều cao của cây, worst case O(n)
Check slide for the code example(too long)
```
https://drive.google.com/file/d/16Aeyjzhil5RInO6r8InAEN8w4kcnhHAi/view?fbclid=IwAR0k8B93OpclfL9LT4sfnkMTxKUXVYr2Yw8c2J2Aj1wzhny7YZJz0x8od5w
```
- Tree traversal all nodes of BST(duyệt Binary Search Tree) : O(n)
```
def traversalTree(root):
    if root != None:
        traversalTree(root.left)
        print(root.key, end='')
        traversalTree(root.right)
```
- Count the number of nodes in BST : O(n)
```
def size(root):
    if root == None:
        return 0
    return size(root.left) + 1 + size(root.right)
```
- Delete BST : O(n)
```
def deleteTree(root):
    if root == None:
        return
    deleteTree(root.left)
    deleteTree(root.right)
    del root
```





