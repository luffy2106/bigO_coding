"""
Nhận xét :

Trong cây nhị phân tìm kiếm, xét một node bất kỳ, giá trị của mọi node trên cây con trái luôn nhỏ hơn node đang xét
và giá trị của mọi node trên cây con phải luôn lớn hơn node đang xét => tất cả các phần tử trong cây nhị phân tìm kiếm 
đều riêng biệt.

=> ta chỉ cần thêm tất cả các phần tử của mảng vào cây nhị phân tìm kiếm rồi so sánh số phần tử của cây này với X 

"""




T = int(input())

for t in range(0, T):
    N, X = map(int, input().split())
    a = list(map(int, input().split()))
    set_a = set(a)
    if len(set_a) > X:
        print("Average")
    elif len(set_a) < X:
        print("Bad")
    else:
        print("Good")



