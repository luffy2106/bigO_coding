"""
Bài toán trở về việc chọn đoạn dãy con(các phần tử kề nhau) trong mảng đã cho sao cho tổng độ dài của nó không vượt quá T, và số phần tử của
dãy này phải là lớn nhất
=> mảng con này có thể kết thúc bằng A0 hoặc A1 hoặc A2, hoặc A3 ... hoặc An. 
=> output sẽ là mảng có số phần tử lớn nhất trong số các mảng có phần tử kết thúc như trên.

Ta sẽ sử dụng 2 pointer technique bằng cách duyệt tất cả phần tử trong mảng(i,j xuất phát với vị trí giống nhau).

1. tìm khoảng chặn trên của mảng cần tìm.
So sánh phần tử đang duyệt (A_i) với thời gian đọc sách còn lại
- Nếu lớn hơn, có nghĩa là để mảng con thỏa mãn độ dài T mà chứa A_i sẽ không chứa phần tử đầu dãy: [A1,A2 ...A_i] hoặc [A2,A2 ...A_i] ... => chuyển sang bước 2
- Nếu nhỏ hơn, ta tiếp tục thêm phần tử vào mảng chừng nào nó chưa vượt quá điều kiện T. 
2. Tìm khoảng chặn dưới của mảng cần tìm. 
Mảng cần tìm sẽ được tìm bằng cách loại lần lượt các phần tử đầu tiên cho đến khi nó thỏa mãn điều kiện T. 


mảng con chứa phần tử A_i thỏa mãn độ dài T sẽ bắt đầu từ đoạn j+1 => ta tìm tất cả các mảng con chứa phần tử A_i và 
bắt đầu bằng vị trí j+1 thỏa mãn độ dài T, sau đó chọn ra mảng con có số phần tử lớn nhất. Cụ thể :
[A_j+1, .... A_i], [A_j+1, .... A_i+1], [A_j+1, .... A_i+1, A_i+2] (tiếp tục tăng i chừng nào i+x < N và dãy vẫn thỏa mãn điều kiện T)
"""
N, T = map(int, input().split())
A = list(map(int, input().split()))
j = 0
read_books = max_books = 0


for i in range(N):
    while A[i] > T:
        T += A[j]
        j += 1
        read_books -= 1
    T -= A[i]
    read_books += 1
    max_books = max(max_books, read_books)


print(max_books)
