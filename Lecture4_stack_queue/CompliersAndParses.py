"""
Theo tutor
- Duyệt từng phẩn tử của mảng, nếu gặp "<", bỏ vào stack
- Nếu gặp ">", kiểm tra stack có rỗng không, nếu stack rỗng => ">" xuất hiện mà không có "<" đứng trước đó => không hợp lệ => dừng thuật toán và in ra 0
- Nếu gặp ">" mà stack không rỗng, pop stack ra (kiểu gì cũng là phần tử "<"), rồi kiểm tra xem tách rỗng không, nếu stack rỗng, cập nhật độ dài = i + 1 
"""


T = int(input())
count = 0
for i in range(T):
    count = 0
    stack = []
    expression = [e for e in input()]
    for i in range(len(expression)):
        if expression[i] == "<":
            stack.append(expression[i])
        else:
            if len(stack) == 0:
                break
            else:
                stack.pop()
                count = i + 1 if len(stack) == 0 else count
    print(count)
