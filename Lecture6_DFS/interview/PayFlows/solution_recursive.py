from typing import List


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

2.1 Using recursive
- For each node of the matrix, if that node is zero, we try to find all zero connected to that zero recursively.
- We need a set to store all the location that we already travel

Reason:
- I use a lot for for, so it will be confused when debug, let's say it's not an optimal approach
- We can not have set of a list, we can only have set of tuple(in this case you still can track the order of the elements)

"""




def get_neighbor(matrix, i, j):
    """Get neigbor of a node at the location (i,j)

    Args:
        matrix (_type_): _description_
        i (_type_): _description_
        j (_type_): _description_
        set_connected_zero (_type_): _description_
    """
    neighbors = []
    rows = len(matrix)
    cols = len(matrix[0])
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if  0<=x<rows and 0<=y<cols and (x,y) != (i,j):
                neighbors.append((x,y))
    
    return neighbors               


def recursive_find_connected_neighbors(location_node, matrix, traveled_nodes, list_connected_neighbor):
    neighbors = get_neighbor(matrix, location_node[0], location_node[1])
    for neighbor in neighbors:
        if neighbor not in traveled_nodes: 
            if matrix[neighbor[0]][neighbor[1]]==0:
                traveled_nodes.add(neighbor)
                list_connected_neighbor.append(neighbor)
                recursive_find_connected_neighbors(neighbor, matrix, traveled_nodes, list_connected_neighbor)

    return list_connected_neighbor, traveled_nodes

def find_connected_zero(matrix, traveled_nodes):
    list_connected_zero = []

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            location_node = (i,j)
            if location_node not in traveled_nodes:
                traveled_nodes.add(location_node)
                if matrix[i][j] == 0 :
                    list_connected_neighbor = []
                    list_connected_neighbor.append(location_node)
                    list_connected_neighbor, traveled_nodes = recursive_find_connected_neighbors(location_node, matrix, traveled_nodes, list_connected_neighbor)
                    list_connected_zero.append(list_connected_neighbor)
    return list_connected_zero
     
    
def main():

   matrix = [[0, 2, 1, 0],
             [0, 1, 0, 1],
             [1, 1, 0, 1],
             [0, 1, 0, 1]]
   traveled_nodes = set()
   list_connected_zero = find_connected_zero(matrix, traveled_nodes)
   output = [len(connected_zero) for connected_zero in list_connected_zero]
   print(output)

if __name__ == "__main__":
    main()