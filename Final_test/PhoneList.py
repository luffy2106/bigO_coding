"""
Sau moi phep toan, de kiem tra xem từ có từ nào bao gồm 1 từ khác trong cây Trie hay không cần xét 2 trường hợp:
- Nếu từ thêm vào ngắn hơn nhánh dài hơn bao gồm nó thì sau khi duyệt tất cả các từ, root vẫn còn con.
- Nếu từ thêm vào dài hơn tiền tố mà nó bao gồm. Tổng countWord trên path đó sẽ lớn hơn 1

"""


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
    temp.countWord += 1


def addWord(root, s):
    count = 0
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.countWord >= 1:
            count += 1
    temp.countWord += 1
    count += 1
    if temp.child:
        return True
    return count > 1


T = int(input())
for t in range(T):
    N = int(input())
    ans = True
    root = Node()
    for n in range(N):
        line_numb = input()
        if addWord(root, line_numb):
            ans = False
    if ans:
        print("YES")
    else:
        print("NO")