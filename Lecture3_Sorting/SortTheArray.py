"""
Nhận xét :
- Sau khi sắp xếp mảng segment, mảng ban đầu sẽ chuyển thành mảng đã được sắp xếp. Vậy ta so sánh mảng ban đầu và mảng đã sắp xếp
và tìm xem những đoạn con nào chung từ trái sang phải và từ phải sang trái, phần khác nhau chính là segment



"""

n = int(input())
list_a = list(map(int, input().split()))
index_a = list(range(0, len(list_a)))
sort_a = sorted(list_a)

while len(list_a) > 0:
    if list_a[0] == sort_a[0]:
        list_a.pop(0)
        sort_a.pop(0)
        index_a.pop(0)
    else:
        break


while len(list_a) > 0:
    if list_a[-1] == sort_a[-1]:
        list_a.pop()
        sort_a.pop()
        index_a.pop()
    else:
        break

# print(list_a)
# print(sort_a)

if len(list_a) == 0:
    print("yes")
    print("1 1")
else:
    for i in range(0, int(len(list_a) / 2)):
        list_a[i], list_a[-i - 1] = list_a[-i - 1], list_a[i]
    if list_a == sort_a:
        print("yes")
        print(str(index_a[0] + 1) + " " + str(index_a[-1] + 1))
    else:
        print("no")
