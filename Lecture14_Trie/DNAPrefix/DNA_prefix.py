


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()

def addWord(root, s):
    global ans
    temp = root
    for i in range(len(s)):
        if s[i] not in temp.child:
            temp.child[s[i]] =  Node()
        temp.child[s[i]].countWord+=1
        temp = temp.child[s[i]]
        ans =  max(ans, temp.countWord * (i+1))



T = int(input())
case  = 0
for t in range(T):
    case+=1
    N = int(input())
    root = Node()
    ans = 1
    for n in range(N):
        word = input()
        addWord(root, word)
    print("Case {}: {}".format(case, ans))