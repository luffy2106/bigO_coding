"""
1. Question
You have an integer matrix representing a plot of land, where the value at
the location represents the height above the sea level. A value of zero 
indicates water. A pond is a region of water connected vertically, 
horizontally, or diagonally. The size of the pond is the total number of 
connected water cells. Write a function to compute the size of all ponds 
in the matrix.
Example :
Input :
   [[0, 2, 1, 0],
   [0, 1, 0, 1],
   [1, 1, 0, 1],
   [0, 1, 0, 1]]
Output : [2, 4, 1] (in any order)



2. Solution 
We can use DFS to solve this problem
- Visit each vertice in the graph, if the vertice is zero, find all the connected vertices recursively. continiuosly Add the list of connected vertices to a list
- Need a list to store all the vertices which is already visited
- Need a function to check if a vertice is a neighbor or another vertices
- Need to convert matrix to the graph
"""



rows = 4
cols = 4
visited = [[False for j in range(cols)] for i in range(rows)]
value_matrix =  [[-1 for j in range(cols)] for i in range(rows)]
graph = [[[] for j in range(cols)] for i in range(rows)]
list_connected_vertices = []


def get_location_neighbors(matrix, i, j):
    rows = len(matrix)
    cols = len(matrix[0])
    list_location_neighbors = [[i-1, j], [i-1, j], [i-1, j+1],[i, j-1], [i, j+1], [i+1,j-1],[i+1, j], [i+1, j+1]]
    list_location_neighbors = [neighbor for neighbor in list_location_neighbors if 0<=neighbor[0]< rows and 0<=neighbor[1]<cols]
    return list_location_neighbors



# def create_graph(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     for i in range(rows):
#         for j in range(cols):
#             graph[i][j] = get_location_neighbors(matrix, i, j)
#     return graph



def DFS(matrix,i, j, connected_vertices = []):
    """Recursively find all connected vertices of i,j

    Args:
        matrix (_type_): _description_
    """
    visited[i][j] = True
    connected_vertices.append([i,j])
    list_location_neighbors = get_location_neighbors(matrix, i, j)
    for neighbor_location in list_location_neighbors:
        if matrix[neighbor_location[0]][neighbor_location[1]] == 0 and visited[neighbor_location[0]][neighbor_location[1]] == False:
            # connected_vertices.append(neighbor_location)
            DFS(matrix, neighbor_location[0], neighbor_location[1], connected_vertices)
    return connected_vertices


def main():
    matrix =    [[0, 2, 1, 0],
                 [0, 1, 0, 1],
                 [1, 1, 0, 1],
                 [0, 1, 0, 1]]
    # graph = create_graph(matrix)
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == False and matrix[i][j] == 0:
                connected_vertices = DFS(matrix, i, j, connected_vertices = [])
                list_connected_vertices.append(connected_vertices)
    
    count_list = [len(connected_vertices) for connected_vertices in list_connected_vertices]
    print(count_list)


    




if __name__ == '__main__':
    main()

            


