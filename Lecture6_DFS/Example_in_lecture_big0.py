"""
1. Question
Take a look at the example in page 40, lecture 6 - DFS.

Find the way from the Vertice 0 to Vertices 5.

You need to provide the solution in 2 ways:
- Using stack
- Using recursion

The input will be:
- First line will be the number of Vertices(V) and Edges(E), seperate by white space. Ex : 6, 8 
- The next E line is pair of edge, seperate by white space. Ex :
0 3
0 1
3 4
3 1
3 5
1 5
1 2
2 5

2. Solution
MAX : let's suppose the number of nodes in our graph is MAX

From the source node, find the path from its all neighbor until it reach the target. In this case, we don't need to visit all vertices, only need to visit vertices which is connected
to source(*). Therefore, at the beginning we put the source vertice into the stack then iterate visit all their neighbors and the algorithm will end when the stack is empty.

The expected solution will be any path from 0 to 5. Ex 
- 0 -> 1 -> 5
- 0 -> 3 -> 5
"""

MAX = 100 # Maximum number of vertices in the graph
V = None
E = None
visited = [False for i in range(MAX)]  # list to store the visited vertices
path = [-1 for i in range(MAX)] # Mang luu vet duong di, moi dinh se co 1 dinh ke voi no, dinh nay la vertice da duoc duyet truoc do, gia su ban dau moi dinh deu co thang thai truoc do la 0
graph = [[] for i in range(MAX)] # Mang luu hang xom cua cac dinh sau moi luot duyet.
stack_current_visited =  []




def create_graph():
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split()) #edge connect u, v will be stored
        graph[u].append(v)
        graph[v].append(u)
    return graph


def DFS_non_recursive(src):
    """Find all the path connected to source

    Args:
        src (_type_): source vertice

    Returns:
        path:  connected path of all node in the graph
    """
    visited[src] = True
    stack_current_visited.append(src)
    while len(stack_current_visited) > 0:
        current_node = stack_current_visited.pop()
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path[neighbor] = current_node # update path
                stack_current_visited.append(neighbor) # update stack    
    return path
            
def DFS_recursive(current_node):
    """For each node, recurisve find all neighbor of that node.

    When the recursive end ?
    When all the neighbor of the current node is visited

    Args:
        src (_type_): _description_
    """
    visited[current_node] = True
    for neighbor in graph[current_node]:
        if visited[neighbor] == False:
            path[neighbor] = current_node
            DFS_recursive(neighbor)
    return path
    
        

def get_path(source, dest):
    route = []
    temp = dest
    while True:
        route.append(temp)
        if path[temp] == -1:
            break   
        temp = path[temp]
    if source not in route:
        return []
    else:
        return route
    

if __name__ == '__main__':
    graph = create_graph()
    source = 0
    dest = 5
    # path = DFS_non_recursive(source)
    path = DFS_recursive(source)
    route  = get_path(source,dest)
    route_from_begin = route[::-1]
    print(route_from_begin)











