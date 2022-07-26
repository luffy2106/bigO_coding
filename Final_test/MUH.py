"""
Ta can luu 2 list:
- list_str_index : chua list cac index co value giong nhau, va dc sap xep dua tren viec value cua index tuong ung dc sap xep theo thu tu tang dan
- list_swap_index : luu tru cac list index tương ứng của list_str_index trên

Dau tien kiem tra so permutation tối đa là bao nhiêu dựa vào list_swap_index:
- Nếu số lượng permutation tối đa nhỏ hơn 3 => in ra No
- Ngược lại in ra Yes, lưu ý là đề bài chỉ bắt ta in ra 2 permutations nữa thôi nên ta sẽ duyệt list_swap_index như sau:
    * Nếu một phần tử trong list_index_swap có độ dài lớn hơn 3 => có 3 vị trí có thể hoán vị cho nhau => in ra 2 hoán vị dựa vào index tương ứng. Kết thúc vòng lặp
    * Nếu một phần tử trong list_index_swap có độ dài lớn hơn 2 => có 2 vị trí có thể hoán vị cho nhau => đổi vị trí 2 phần tử có vị trí tương ứng với index và in ra permutation. Tiếp
    tục làm như thế cho đến khi tìm được 2 permutation

"""


import queue
import copy


class PQEntry:
    def __init__(self, index, value) -> None:
        self.index = index
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


def swapPositions(list, pos1, pos2):
    li2 = copy.deepcopy(list)
    li2[pos1], li2[pos2] = li2[pos2], li2[pos1]
    return li2


def get_number_permutation(list_swap_index):
    nb = 1
    for swap_index in list_swap_index:
        nb = nb * len(swap_index)
    return nb


N = int(input())
line_n = list(map(int, input().split()))
pq = queue.PriorityQueue()
for i in range(len(line_n)):
    pq.put(PQEntry(i + 1, line_n[i]))

list_swap_index = []
list_str_index = []
temp_top = PQEntry(0, 0)
i = 0
while not pq.empty():
    top_heap = pq.get()
    if top_heap.value != temp_top.value:
        list_str_index.append([top_heap.index])
        list_swap_index.append([i])
    else:
        list_str_index[-1].append(top_heap.index)
        list_swap_index[-1].append(i)
    i += 1
    temp_top = top_heap


nb_permutation = get_number_permutation(list_swap_index)


original_ans = []
for list_num in list_str_index:
    for num in list_num:
        original_ans.append(num)


if nb_permutation < 3:
    print("NO")
else:
    print("YES")
    print(" ".join([str(e) for e in original_ans]))
    count = 0
    for swap_index in list_swap_index:
        if len(swap_index) >= 3:
            permutation_1 = swapPositions(original_ans, swap_index[0], swap_index[1])
            print(" ".join([str(e) for e in permutation_1]))
            permutation_2 = swapPositions(original_ans, swap_index[1], swap_index[2])
            print(" ".join([str(e) for e in permutation_2]))
            break
        elif len(swap_index) == 2:
            permutation = swapPositions(original_ans, swap_index[0], swap_index[1])
            print(" ".join([str(e) for e in permutation]))
            count += 1
        if count == 2:
            break