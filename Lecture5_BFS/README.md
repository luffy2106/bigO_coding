## Breadth-First Search (BFS):

Complexity O(V+E)
- V(Vertices) : # of vertices
- E(Edges) : # of edges


#### Solution

BFS seach horizontially, the basic set up is the same as DFS, except one thing. BFS use queue as data structure to iterate neigbors of each node in the graph. The following is the basic setup of BFS
- Visted : list to store all nodes visited
- graph : A list to store the neigbor of each node in the graph
- path : list to store the pervious state of each visted node(*)
- queue : A queue to store all the considered node

Điều kiện kết thúc của thuật toán:
- Thuật toán dừng khi queue rỗng, tức là tất cả các đỉnh đã được xét.

Kết quả sẽ cho ra đường đi từ đỉnh A bất kỳ đến đỉnh B bất kỳ dựa vào path (*), đó sẽ là đường đi ngắn nhất.


##### If the input is the normal graph
```
from queue import Queue
MAX = 100
visited = [False for i in range(rows)]
path = [-1 for i in range MAX]
graph = [[] for i in range MAX]
queue = Queue()
```

##### If the input is the normam graph
```
MAX = rows * cols
visited = [[False for j in range(cols)] for i in range(rows)]
path = [-1 for i in range MAX]
matrix_value = [["" for j in range(cols)] for i in range(rows)]
graph = [[[] for j in range(cols)] for i in range(rows)]
```

#### Application

Use BFS when:
- Need to find the shortest path from the source to a destination vertex.
- The main focus is to explore all neighbors of a node before moving on to the next level.
- Memory usage is not a concern, as BFS might require more memory due to the nature of exploring all neighbors.

Applications:
- Shortest path problems.
- Minimum spanning trees.
- Level-order traversal of a tree.

Decision Factors:
- Memory Usage: If memory is a limiting factor, consider using DFS.
- Finding Shortest Path: If finding the shortest path is crucial, BFS is usually the better choice.
- Exploration Strategy: DFS explores deeply before moving horizontally, while BFS explores neighbor nodes before deeper levels.

