"""
Trước tiên ta có nhận xét như sau:

1. Nếu có một ký tự nào trong t mà không có trong s thì chắc chắn ta không thể biến đổi chuỗi s thành chuỗi tt được -> “need tree”.
2. Nếu có một ký tự nào trong s mà không có ký tự trong t thì ta phải bỏ đi ký tự đó -> “automaton”.
3. Phép biến đổi “array” hoán đổi vị trí của hai ký tự chỉ cần thiết nếu thứ tự xuất hiện của các ký tự trong chuỗi t không trùng khớp với thứ tự của các ký tự đó trong chuỗi s.
Để giải quyết trường hợp 1 và 2, ta sử dụng một mảng đếm tần suất xuất hiện của từng ký tự trong chuỗi s và chuỗi t. Sau đó duyệt từng ký tự trong bảng chữ cái gồm 26 chữ:

- Nếu tần suất xuất hiện của ký tự đó trong chuỗi t lớn hơn chuỗi s, nghĩa là chuỗi s không đủ ký tự để ta biến đổi thành chuỗi t -> “need tree”.
- Nếu tần suất xuất hiện của ký tự đó trong chuỗi t nhỏ hơn chuỗi s, nghĩa là sẽ có một số ký tự thừa -> “automaton”.

Ta cần giải quyết trường hợp 3 để có thể đưa ra kết luận là “array” hay “both”.

Bằng cách duyệt qua từng ký tự trong chuỗi t, ta tìm vị trí của ký tự tương ứng trong chuỗi s. Nếu các vị trí này tăng dần nghĩa là các ký tự này đã đúng vị trí, ta không cần đổi chỗ. Ngược lại ta kết luận “array”.

Xem xét liệu “automaton” và “array” có cùng thỏa hay không để đưa ra kết luận là “both”.

Xem chi tiết hướng dẫn trong file PDF

"""


def getChar(x):
    return chr(x + ord("a"))


s = input()
t = input()

need_tree = suffix_automation = suffix_array = False


for i in range(0, 26):
    t_count = t.count(getChar(i))
    s_count = s.count(getChar(i))
    if t_count > s_count:
        need_tree = True
    elif t_count < s_count:
        suffix_automation = True


index_found, match = 0, -1

for i in range(len(t)):
    index_found = s.find(t[i], match + 1)
    if index_found > match:
        match = index_found
    else:
        suffix_array = True
        break


if need_tree:
    print("need tree")
elif suffix_automation and suffix_array:
    print("both")
elif suffix_automation:
    print("automaton")
else:
    print("array")
