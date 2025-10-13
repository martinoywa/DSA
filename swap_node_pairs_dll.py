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
        
    def swap_pairs(self):
        temp = Node(0)
        temp.next = self.head
        before = temp
        first = self.head # current
        
        while first is not None and first.next is not None:
            second = first.next

            # perform swap
            before.next = second
            first.next = second.next
            second.next = first
            first.prev = second
            second.prev = before
            
            # check if there's a node after current pair
            if first.next is not None:
                first.next.prev = first

            # move pointers
            before = first
            first = first.next
            
        self.head = temp.next
        
        if self.head:
            self.head.prev = None
