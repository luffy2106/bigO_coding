class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


def addWord(root, s, priority):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        temp.countWord= max(temp.countWord, priority)

def findWord(root, s):
    temp = root
    for ch in s :
        if ch not in temp.child:
            return -1
        temp = temp.child[ch]
    return temp.countWord 

n, q = map(int, input().split())
root = Node()
for i in range(n):
    [word_i, priority_i] = input().split()
    priority_i = int(priority_i)
    addWord(root, word_i, priority_i)

for i in range(q):
    q_i = input()
    ans = findWord(root, q_i)
    print(ans)

