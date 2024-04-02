"""
Question:


Anh ESP thường nói "ALL IZZ WELL" bất cứ khi nào anh ấy gặp rắc rối. Vì vậy, bạn bè của anh ấy và những người xung quanh anh ấy đã từng cười nhạo anh ấy. Nhưng anh ESP rất tin tưởng vào niềm tin của mình. Anh ấy tin rằng thuật ngữ “ALL IZZ WELL” sẽ khiến mọi thứ trở nên tốt đẹp. Bây giờ nhiệm vụ của bạn là bỏ qua câu chuyện ở trên và tìm xem liệu có một đường đi nào trong ma trận đã cho tạo nên câu "ALL IZZ WELL"

Có đường đi từ một ô bất kỳ đến tất cả các ô lân cận của nó. Ô lân cận có thể chung cạnh hoặc chung góc.

Dữ liệu nhập
- Dòng đầu tiên bao gồm một số nguyên t đại diện cho số lượng trường hợp thử nghiệm.
- Dòng đầu tiên của mỗi trường hợp bao gồm hai số nguyên R và C đại diện cho số hàng và số cột trong ma trận. Sau đó là mô tả của ma trận.

Có một dòng mới sau mỗi trường hợp thử nghiệm trong đầu vào.

t ≤ 1000
R ≤ 100
C ≤ 100

Dữ liệu xuất
Đối với mỗi trường hợp kiểm tra, hãy in “YES” nếu có một đường đi tạo thành câu “ALLIZZWELL”. Ngược lại in “NO”.

Ví dụ:
Input:

5
3 6
AWE.QX
LLL.EO
IZZWLL

1 10
ALLIZZWELL

2 9
A.L.Z.E..
.L.I.W.L.

3 3
AEL
LWZ
LIZ

1 10
LLEWZZILLA

Ouput:

YES
YES
NO
NO
YES


Solution:
- Create list which store all the path of one vertice which has the value A 
- For each path start with "A", recursively check if neighbor == ALLIZZWELL queue remove first element:
    - if equal, store standard string to temp string then continue check
    - the algorithm will end if the string "ALLIZZWELL" has nothing left


Step 1:
- Build a matrix with the value of a cordinator in matrix is the list of it's neighbor. We can use list of list in this step. 
Step 2:
- Use DFS to store all path of each vertice to all other vertice 


Sucess but there is error on this input:

6 5
.AWW.
.ALL.
.ZZI.
.WE..
.LL..
AAALL

"""
T = int(input())
# R, C = map(int, input().split())
# rows, cols = R, C
# matrix_value = [["" for j in range(cols)] for i in range(rows)]
# visited = [[False for j in range(cols)] for i in range(rows)]
# graph = [[[] for j in range(cols)] for i in range(rows)]
# path = [[[-1,-1] for j in range(cols)] for i in range(rows)]
standard_str = "ALLIZZWELL"

def get_list_neighbor_matrix(i,j, rows, cols):
    list_neighbor = []
    list_neighbor.append([i-1,j-1])
    list_neighbor.append([i-1,j])
    list_neighbor.append([i-1,j+1])
    list_neighbor.append([i,j-1])
    list_neighbor.append([i,j+1])
    list_neighbor.append([i+1,j-1])
    list_neighbor.append([i+1,j])
    list_neighbor.append([i+1,j+1])
    list_neighbor = [neighbor for neighbor in list_neighbor if 0<=neighbor[0]<rows and 0<=neighbor[1]<cols]
    return list_neighbor




def create_graph(rows, cols):
    for i in range(rows):
        row_value = list(input())
        for j in range(cols):
            matrix_value[i][j] = row_value[j]
            list_neigbor = get_list_neighbor_matrix(i,j, rows, cols)
            graph[i][j] = list_neigbor
    
    return matrix_value, graph
    
def DFS(current_location, standard_str, list_validation):
    if len(standard_str) == 0:
        list_validation.append(True)    
    else:
        if visited[current_location[0]][current_location[1]]== False:
            visited[current_location[0]][current_location[1]]= True
            current_value = matrix_value[current_location[0]][current_location[1]]
            if current_value == standard_str[0]:
                remain_standard_str = standard_str[1:]
                list_neighbor_location = graph[current_location[0]][current_location[1]]
                for neighbor_location in list_neighbor_location:
                    DFS(neighbor_location, remain_standard_str, list_validation)
    return list_validation
                
    

def find_list_path(source_value, standard_str, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if matrix_value[i][j] == source_value:
                source_location = [i,j]
                list_validation = []
                list_validation = DFS(source_location, standard_str, list_validation) 
                if True in list_validation:
                    return True
    return False



if __name__ == '__main__':
    # matrix_value, graph = create_graph(rows, cols)
    # print(matrix_value)
    source_value = "A"
    for i in range(T):
        R, C = map(int, input().split())
        rows, cols = R, C
        matrix_value = [["" for j in range(cols)] for i in range(rows)]
        visited = [[False for j in range(cols)] for i in range(rows)]
        graph = [[[] for j in range(cols)] for i in range(rows)]
        path = [[[-1,-1] for j in range(cols)] for i in range(rows)]
        matrix_value, graph = create_graph(rows, cols)
        if find_list_path(source_value, standard_str, rows, cols):
            print("YES")
        else:
            print("NO")
        break_line = input()









