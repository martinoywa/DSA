# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        first = self.head # current
        
        while first and first.next:
            second = first.next

            # perform swap
            previous.next = second
            first.next = second.next
            second.next = first

            # move pointers
            previous = first
            first = first.next
            
        self.head = dummy.next
