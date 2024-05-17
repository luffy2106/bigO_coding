# Binary Search

#### 1. Application
Binary search is for finding an element in an SORTTED array.

#### 2. Complexity
The complexity is O(log(N))

#### 3. How it work
Xem mục ý tưởng của thuật toán trong link sau
```
https://drive.google.com/file/d/1J-DEapxn7gqJ4pFat_6DijO27YMzGMzH/view?fbclid=IwAR0qPvC3NA38iObQbsRe5sbcoAnPfkhU9WHyB83SOhdp2zXHa6HrQvXvakU
```
#### 4. Uses case
Các dạng bài thường gặp:
- Binary Search
- Binary Search First(tìm phần từ đầu tiên)
Ex : Cho mảng đã sắp xếp theo thứ tự tăng dần, tồn tại nhiều phần tử có giá trị giống nhau. Tìm phần tử đầu tiên có giá trị x = 33 trong mảng
- Binary Search Last(tìm phần tử cuối cùng)

#### 4. Use libary
Trong python không có hàm binary search nhưng có hàm tìm cận trên/dưới:
- Hàm tìm cận dưới(bisect_left)
Trả về vị trí đầu tiên lớn hơn hoặc bằng giá trị tìm kiếm trong đoạn [first, last](the index of the leftmost occurrence of that element)
Cú pháp : bisect_left(a, x, lo=0, hi=len(a))
```
if __name__ == '__main__':
    a = [1,1,2,2,2,3,4,5,7]
    n, x = 9,3
    pos = bisect.bisect_left(a, x, 0, n) #or bisect.bisect_left(a,x)
    print(pos) # the answer is index = 5
```

- Hàm tìm cận trên(bisect_right)
Trả về vị trí đầu tiên lớn hơn giá trị tìm kiếm trong đoạn [first, last](the index just after the rightmost occurrence of that element)
Cú pháp : bisect_right(a, x, lo=0, hi=len(a))
```
if __name__ == '__main__':
    a = [1,1,2,2,2,3,4,5,7]
    n, x = 9,3
    pos = bisect.bisect_right(a, x, 0, n) #or bisect.bisect_left(a,x)
    print(pos) # the answer is index = 6
```

#### 5. Demo
- Binary Search : Take a look at demo/BinarySearch.py
- 








