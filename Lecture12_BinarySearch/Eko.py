"""
Giải thích ví dụ: Bạn chọn HH = 15 vì : • Chặt cây đầu tiên có độ dài là 20 thì lượng gỗ bị chặt là 5 • Chặt cây thứ hai có độ dài là 15 thì lượng gỗ bị chặt là 0 • Chặt cây thứ ba, vì cây thứ ba độ dài đã nhỏ hơn 15 rồi nên không cần chặt nên lượng gỗ chặt là 0 • Chặt cây thứ tư có độ dài là 17 thì lượng gỗ bị chặt là 2. Tổng lượng gỗ bị chặt: 5 + 0 + 0 + 2 = 7 ≥ 7 thỏa mãn. Ta không thể nào tìm được một độ cao HH tốt hơn 15 nữa.

Hướng dẫn giải:

Ta dựa vào một nhận xét như sau: Khi HH càng tăng, rõ ràng tổng lượng gỗ bị chặt sẽ càng giảm và ngược lại. Do đó, nếu giả sử như ta có thể quy định midmid là độ dài của các khúc gỗ mà sau khi chặt không được phép vượt quá midmid. Nếu như tổng lượng gỗ bị chặt mà ≥ M, điều này có nghĩa rằng đáp án của ta có thể là mid, hoặc đáp án của ta sẽ nằm trong đoạn từ mid + 1mid+1 trở về sau. Còn nếu tổng lượng gỗ bị chặt mà < M<M thì rõ ràng ta không thể nào nhận mid làm đáp án được mà phải tìm từ mid - 1mid−1 trở về trước. Từ ý tưởng này, ta hình thành nên thuật toán chặt nhị phân như sau:

Gọi getSum(x)getSum(x) là tổng lượng gỗ bị chặt khi ta quy định độ dài của các cây sau khi chặt không được vượt quá xx.
Ta đặt l = 0l=0, r = 10^9 + 10r=10
​9
​​ +10, đại diện cho trường hợp xấu nhất là chặt hết gỗ vẫn không đủ và trường hợp tốt nhất là không cần chặt cây nào.
Trong lúc l ≤ r, ta đặt mid = (l + r) / 2mid=(l+r)/2, nếu getSum(mid) >= MgetSum(mid)>=M thì ta tiến hành cập nhật res = midres=mid, đồng thời tìm kết quả tiếp trên đoạn [mid + 1, r][mid+1,r], tức gán l = mid + 1l=mid+1. Ngược lại, nếu getSum(mid) < MgetSum(mid)<M thì ta tìm kết quả trên đoạn [l...mid - 1][l...mid−1], tức gán r = mid - 1r=mid−1.
Độ phức tạp: O(Nlog(max(hi))O(Nlog(max(hi)) với NN là số lượng cây và max(hi)max(hi) là chiều cao lớn nhất của cây.


"""

def check(a, setting):
    sum = 0
    for element in a:
        sum+=max(0, element-setting)
    return sum




def binarySearch(a, left, right, x):
    value = 0    
    while left<= right:
        mid = (left+right)//2
        setting = mid
        if check(a, setting) >= x:  # cần phải thu gọn tập tìm kiếm về phía phải, nếu không tìm được chiều cao chặt có độ chính xác mong muốn, có thể nâng lên dư ra cũng dc, nên không nhất thiết phép so sánh phải là phép so sánh bằng
            value = setting
            left = mid + 1 
        else: # cần phải thu gọn tập tìm kiếm về phía trái
            right = mid - 1
    return value



N, M = map(int, input().split())
height_trees = list(map(int, input().split()))

vmin = 0
vmax = 10 ** 9

value = binarySearch(height_trees, 0, vmax, M)
print(value)
