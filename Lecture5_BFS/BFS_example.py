"""
Tim duong di ngan nhat tu 0 den 5 cua do thi sau:
#(V,E)
#Các cạnh 

9 11
0 8 
0 3
3 4
8 4
3 2
0 1
1 2
1 7
2 7
2 5
5 6

The expected result is [0]

"""


from queue import Queue

V, E = map(int, input().split())
MAX = V * E
visited = [False] * MAX
path = [-1] * MAX
graph = [[] for i in range(MAX)]
queue_current_visited = Queue()


def create_graph(graph, E):
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph


def BFS(source, path):
    visited[source] = True
    queue_current_visited.put(source)
    while not queue_current_visited.empty():
        current_node = queue_current_visited.get()
        list_neighbor = graph[current_node]
        for neighbor in list_neighbor:
            if visited[neighbor] == False:
                visited[neighbor] =  True
                queue_current_visited.put(neighbor)
                path[neighbor] = current_node
    return path


def path_bfs_non_recursive(source, dest, path):
    path_source_dest = [dest]
    if source == dest:
        return [source]
    elif path[dest] == -1: # Dest is a seperated node
        return []
    while path[dest] != -1:
        dest = path[dest]
        path_source_dest.append(dest)
        if source == dest:
            path_source_dest = path_source_dest[::-1]
            return path_source_dest
        
    return []
    

def path_bfs_recursive(source,dest, path, path_source_dest):
    if source == dest:
        return path_source_dest
    else:
        dest = path[dest]
        if dest == -1:
            return []
        else:
            path_source_dest.append(dest)
            path_bfs_recursive(source, dest, path, path_source_dest)
    path_source_dest = path_source_dest[::-1]
    return path_source_dest



def main():
    source = 0
    dest = 5
    create_graph(graph, E)
    BFS(source, path)
    # print(path_bfs_non_recursive(source, dest, path))
    print(path_bfs_recursive(source, dest, path, path_source_dest=[dest]))



if __name__ == "__main__":
    main()




































