# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def partition_list(self, x):
        if self.head is None:
            return
        
        less_nodes, greater_nodes = Node(0), Node(0)
        current, current_less, current_greater = self.head, less_nodes, greater_nodes
        
        while current is not None:
            if current.value < x:
                current_less.next = current
                current_less.next.prev = current_less
                current_less = current_less.next
            else:
                current_greater.next = current
                current_greater.next.prev = current_greater
                current_greater = current_greater.next
            current = current.next
            
        # make sure greater_nodes.next if not None
        current_less.next = greater_nodes.next
        if greater_nodes.next is not None:
            greater_nodes.next.prev = current_less
        current_greater.next = None
        
        self.head = less_nodes.next
        self.head.prev = None # detach dummy node
