"""
Tự làm nhưng cần đọc hướng dẫn để hiểu yêu cầu của đề bài. 
Nhận xét:
- Nếu một bài toán có độ phức tạp Ai, nó cần ít nhất 1 dạng bài có độ phức tạp Bj>=Ai. Ta nên chọn giá trị
Bj bé nhất có thể, để dành các dạng bài có độ phức tạp cao hơn cho các bài toán khó hơn.
- Lưu ý là các bài toán và các dạng toán đều có độ phức tạp tăng dần

"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

j=0
count = 0
for i in range(N):
    #find Bj such as Bj>=Ai, stop when found
    while j < M:
        if B[j] >= A[i]:
            count+=1
            j+=1
            break
        j+=1

print(N-count)


