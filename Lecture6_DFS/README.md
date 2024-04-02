### DFS

#### Goal:

Thuật Toán DFS luôn tìm kiếm được đường đi từ một đỉnh bất kỳ cho tới các đỉnh khác(Nếu các đỉnh thuộc thành phần liên thông với nhau). Nhưng không chắc chắn đường đi tìm được sẽ là đường đi ngắn nhất.

Độ phức tập : O(V+E)
- V(Vertices): số lượng đỉnh của đồ thị
- E(Edges) : số lượng cạnh của đồ thị

DFS có thể cài đặt theo 2 cách :
- Đệ quy
- Không đệ quy

DFS có thể giúp bạn list ra toàn bộ đường đi từ điểm A bất kỳ đến điểm B bất kỳ. 

#### Solution

Ý tưởng chung của thuật toán :

Xuất phát từ 1 đỉnh bất kỳ, đi tới tất cả các đỉnh kề của đỉnh này và lưu đỉnh kề này lại. Vì vậy trong mọi bài toán, về cơ bản cần lưu thông tin sau trong quá trình thiết lập DFS :
- Thông tin các đỉnh và hàng xóm của chúng - graph
- Mảng lưu các đỉnh đã được duyệt - visited
- Stack lưu các đỉnh đang xét, sau mỗi lượt, đỉnh hiện tại sẽ được lấy ra, đồng thời các hàng xóm của nó sẽ dc thêm vào. - stack_current_visited
- Mảng lưu vết đường đi (bao gồm đỉnh đang xét hiện tại và đỉnh hàng xóm vừa đi qua trước đó) - path (*)

Điều kiện kết thúc của thuật toán:
- Thuật toán dừng khi stack rỗng, tức là tất cả các đỉnh đã được xét.

Kết quả sẽ cho ra đường đi từ đỉnh A bất kỳ đến đỉnh B bất kỳ dựa vào path (*)

#### Note

##### Input is a normal graph
Nếu đầu vào của bài toán là đồ thị với đỉnh và cạnh, ta có thể set up graph dùng list, trong đó index của list là vertice, giá trị của element tại index đó là list các vertice hàng xóm
```
MAX = 1000 + 5
visited = [False] * MAX
dist = [0] * MAX
graph = [[] for _ in range(MAX)]
```

##### Input is a matrix
Nếu đầu vào của bài toán là một matrix, ta có thể set up graph bằng các cách sau:
1. List of list 
```
rows, cols, k = map(int, input().split())  # rows, cols, k is rows, columns, nb_lakes
MAX = rows * cols
matrix_value = [["" for j in range(cols)] for i in range(rows)]
visited = [[False for j in range(cols)] for i in range(rows)]
graph = [[[] for j in range(cols)] for i in range(rows)]
```

2. Dictionary 



3. Python object


