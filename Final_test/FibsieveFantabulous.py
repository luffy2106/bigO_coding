"""
Nhận xét :
1>
(1,1) = 1^2
(1,2) = 1^2 + 1
(1,3) = 3^2 
(1,4) = 3^2 + 1
(1,5) = 5^2 
(1,6) = 5^2 + 1
=> vị trí có dạng (1, x) => thời gian tương ứng được xác định như sau : 
- Nếu x là số lẻ, thời gian tương ứng là bình phương của x
- Nếu x là số chẵm thời gian tương tứng là bình phương của x-1 sau đó cộng thêm 1 

2>
(1,1) = 0^2+1
(2,1) = 2^2
(3,1) = 2^2+1
(4,1) = 4^2
(5,1) = 4^2+1
=> vị trí có dạng (x,1) => thời gian tương ứng được xác định như sau:
- Nếu x là số lẻ, thời gian tương ứng là bình phương của x-1 sau đó cộng thêm 1
- Nếu x là số chẵn, thời gian tương ứng là bình phương của x

3>
Mọi thời gian đều nằm giữa 2 số chính phương liên tiếp :  x^2 + 1 <= temp <= (x+1)^2
Dựa vào (1) và (2) ta thấy nếu x là 1 số chẵn thì x^2 + 1 sẽ có vị trí (x+1, 1), còn nếu x là 
1 số lẻ thì x^2 + 1 sẽ có vị trí (1, x+1). Để tìm x, ta chỉ cần lấy căn bậc 2 của temp




- Nếu phần nguyên bên trái của căn bậc 2 của 1 số là 1 số lẻ và bằng x => số đó sẽ nằm trên hàng x + 1
- Nếu phần nguyên bến trái của căn bậc 2 của 1 số là 1 số chẵn và bằng x => số đó sẽ nằm trên cột x + 1

Vậy ta có thể tiếp cận bài toán như sau:
Đầu tiên tìm xem số đó nằm trên hàng(cột) nào, sau đó tìm tiếp cột(hàng) dựa vào tính chất (1) và (2). Ví dụ
- Theo tính chất 3, ta biết được rằng thời gian 20 sẽ nằm trên hàng 5, vị trí có cột nhỏ nhất và cũng có hàng là 5
là (5,1) tương ứng với giá trị 17, 20 hơn 17 là 3 đơn vị mà lại buộc phải cùng hàng, vậy vị trí cần tìm phải là (5,1+3) = (5,4) 

"""


import math
def find_row_or_column(a):
    x = int(math.sqrt(a))
    if x % 2 == 0:
        return (x+1, 1), "left"
    else:
        return (1, x+1), "right"

def temp_1_x(x):
    if x % 2 == 1:
        return x ** 2
    return (x-1)**2 + 1


def temp_x_1(x):
    if x % 2 == 1:
        return (x-1)**2 + 1
    return x ** 2





T = int(input())
case = 0
for t in range(T):
    case+=1
    a  = int(input())
    value, bol = find_row_or_column(a)
    if bol == "left":
        min_col = value
        min_temp = temp_x_1(value[0])
        distance = a - min_temp
        print("Case {}: {} {}".format(case, value[0], 1 + distance))
    else:
        min_row = value
        min_temp = temp_1_x(value[1])
        distance = a - min_temp
        print("Case {}: {} {}".format(case, 1 +  distance, value[1]))
        


