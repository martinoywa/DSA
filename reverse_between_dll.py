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
        
    def reverse_between(self, start_index, end_index):
        if self.head is None:
            return
        
        # create temp node
        temp = Node(0)
        temp.next = self.head
        before_start = temp
        
        # move start_index times
        for _ in range(start_index):
            before_start = before_start.next
            
        # create new start
        new_start = before_start.next
        current = new_start
        before = after = None
        
        # reverse_between
        for _ in range(end_index-start_index+1):
            after = current.next
            current.next = before
            current.prev = after
            before = current
            current = after
            
        # merge
        before_start.next, before.prev = before, before_start
        new_start.next = current
        if current is not None:
            current.prev = new_start
        self.head = temp.next
        self.head.prev = None
