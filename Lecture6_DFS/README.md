### DFS

#### Goal:

Thuật Toán DFS luôn tìm kiếm được đường đi từ một đỉnh bất kỳ cho tới các đỉnh khác(Nếu các đỉnh thuộc thành phần liên thông với nhau). Nhưng không chắc chắn đường đi tìm được sẽ là đường đi ngắn nhất.

Độ phức tập : O(V+E)
- V(Vertices): số lượng đỉnh của đồ thị
- E(Edges) : số lượng cạnh của đồ thị

DFS có thể cài đặt theo 2 cách :
- Đệ quy
- Không đệ quy

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



