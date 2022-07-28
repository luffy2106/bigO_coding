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
Nếu nhìn vào đường đi của thời gian tại mỗi circle, ta thấy mọi thời gian đều nằm giữa 2 số chính phương liên tiếp :  
x^2 + 1 <= temp <= (x+1)^2. Dựa vào (1) và (2) ta thấy nếu x là 1 số chẵn thì x^2 + 1 sẽ có vị trí (x+1, 1), còn nếu x là 
1 số lẻ thì x^2 + 1 sẽ có vị trí (1, x+1). Để tìm x, ta chỉ cần lấy temp - 1, lấy căn bậc 2 rồi 
lấy phần nguyên.

Gọi số đầu vào là m

Ta thấy mọi số sẽ nằm trên đoạn (1, a)....(a, a).....(a, 1). Sẽ có 2 trường hợp.
- Số tại vị trí (1, a) là min, Số tại vị trí (a, 1) là max. Ta so sánh số đã cho với giá trị tại (a, a). 
   * Nếu bằng thì giá trị trả về là (a,a)
   * Nếu lớn hơn thì giá trị trả về là (1+max-m, a)
   * Nếu nhỏ hơn thì giá trị trả về là (a, 1+m-min)
- Số tại vị trí (1, a) là max, Số tại vị trí (a, 1) là min. Ta so sánh số đã cho với giá trị tại (a, a). 
   * Nếu bằng thì giá trị trả về là (a,a)
   * Nếu lớn hơn thì giá trị trả về là (1+m-min, a)
   * Nếu nhỏ hơn thì giá trị trả về là (a, 1+max-m) 
"""


import math
def find_row_or_column(a):
    """
    Flag = True nghĩa là phần tử bé nhất sẽ có dạng (a,1), phần tử lớn nhất path sẽ có dạng(1,a). Flag = False thì ngược lại
    """

    min_position = None
    max_position = None
    flag = False
    x = int(math.sqrt(a - 1))
    if x % 2 == 0:
        min_position = (x+1, 1)
        max_position = (1, x+1)
        flag = True
        # return (x+1, 1), "left"
    else:
        min_position = (1, x+1)
        max_position = (x+1, 1)
        # return (1, x+1), "right"
    return min_position, max_position, flag

def begin_path(a):
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
    min_position, max_position, flag = find_row_or_column(a)
    ans = None
    max_row_col = max(min_position)
    if flag == True:
        min_value = temp_x_1(min_position[0])
        max_value = temp_1_x(max_position[1])
        mid_value = min_value + max(min_position)-1
        if a == mid_value:
            ans = (max_row_col, max_row_col)
            # print(ans)
            # print(mid_value)
        elif a > mid_value:
            ans = (1+max_value-a, max_row_col)
        else:
            ans = (max_row_col, 1+a-min_value)
    else:
        min_value = temp_1_x(min_position[1])
        max_value = temp_x_1(max_position[0])
        mid_value = min_value + max(min_position)-1
        if a == mid_value:
            ans = (max_row_col, max_row_col)
            # print(ans)
            # print(mid_value)
        elif a > mid_value:
            ans = (max_row_col, 1+max_value-a)
        else:
            ans = (1+a-min_value, max_row_col)
    print("Case {}: {} {}".format(case, ans[0], ans[1]))
    
        


