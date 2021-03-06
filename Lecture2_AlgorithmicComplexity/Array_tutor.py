"""
Tutorial
Ý tưởng giải dựa trên kỹ thuật Two Pointers với hai biến chạy i và j:

Bước 1: Sử dụng biến chạy i để chạy tìm đoạn đầu tiên chứa đủ K số phân biệt.

Bước 2: Sử dụng biến chạy j chạy từ dưới lên nhằm rút ngắn đoạn tìm được, đảm bảo trong [j, i] không còn bất cứ đoạn con nào cũng thỏa yêu cầu.

Bước 3: In ra kết quả bài toán nằm trong hai biến j và i.

Trong đó, để kiểm soát số phần tử phân biệt đã tìm được, ta dùng thêm một mảng đếm phân phối fre[] với fre[X] là số lần X xuất hiện trong khoảng [j, i]. 
Với mỗi lần fre[X] thay đổi từ 0 lên 1, tức là ta vừa nhận được thêm một số mới không trùng với những số trước đó, 
ta tăng biến đếm số lượng phần tử phân biệt lên 1.

Độ phức tạp: O(N) với N là số lượng phần tử trong dãy.
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
fre = [0] * (10 ** 5 + 1)
unique = 0
j = 0

for i in range(n):
    if fre[a[i]] == 0:
        unique += 1
    fre[a[i]] += 1
    while unique == k:
        fre[a[j]] -= 1
        if fre[a[j]] == 0:
            print(j + 1, i + 1)
            exit()
        j += 1

print("-1 -1")
