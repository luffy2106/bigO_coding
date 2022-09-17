"""
This example sum up all the basic implementation to manipulate a Singly-Linked List.

Recall : 

Singly-Linked List consists of nodes, starting from head node to NULL, where each node contains a data field and a next pointer.
"""




"""
CREATE LINKED LIST
"""

# Node class
class Node:
    def __init__(self, data) -> None:
        """
        Function to initialize the node object. There are always 2 elements:
        - data
        - the pointer to the next node
        """
        self.data = data
        self.next = None
# Linked list class
    def __init__(self) -> None:
        """
        Function to initialize the Linked List object. There is alway a pointer to point to 
        the head of the link. If the linked list is empty, this pointer point to null
        """
        self.head = None



"""
INSERT A NODE TO THE FRONT OF LINKED LIST(3 STEPS)
- Time Complexity: O(1), We have a pointer to the head and we can directly attach a node and change the pointer. 
So the Time complexity of inserting a node at the head position is O(1) as it does a constant amount of work.
- Auxiliary Space: O(1).
"""
def push(self, data):
    # Allocate the new node with data
    new_node = Node(data)
    # Make the next node of the new node as head
    new_node.next = self.head
    # Make the head of the current linked list as new node
    self.head = new_node



"""
ADD A NODE AFTER A GIVEN NODE: (5 STEPS PROCESS) 
"""







