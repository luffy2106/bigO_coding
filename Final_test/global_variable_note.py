"""
Cách sử dụng biến global
"""


"""
Đoạn code dưới đây sẽ gây lỗi do ta cố truy cập biến global x bằng phép gán mà không khai báo biến global bên trong hàm
"""
# x = 2
# def foo():
#     x = x * 2
#     return x 
    
# x = foo()
# print(x)





"""
Đoạn code dưới đây vẫn thực hiện được dù ta ko khai báo biến global  bên trong hàm. Đó là vì mặc dù ta truy cập vào biến 
global nhưng ta không cố gắng thay đổi nó, ta chỉ tham chiếu đến nó để thực hiện phép toán trả về
"""
x = 2
def foo():
    return x * 2 
    
x = foo()
print(x)

