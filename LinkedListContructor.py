class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # initialize the head and tail pointers
        self.head = self.tail = Node(value)
        # self.length = 1

    def print_list(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next

    def append(self, value):
        # create a new node then append
        new_node = Node(value)
        
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        # create new node then prepend
        new_node = Node(value)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, index, value):
        # TODO edge case for out of bounds index i.e index < 0 or index >= self.length
        # find index then insert new node
        # if index == 0, prepend, if index == -1 or last index, append
        # otherwise insert middle.
        new_node = Node(value)
        current_index = 0 # TODO add a length attribute
        current = self.head

        if index == current_index:
            self.prepend(value)
            return
        else:
            while current.next != None:
                current = current.next
                current_index += 1
                if current_index == index:
                    # TODO may need to keep track of previous node or increment index first
                    """
                    current_index += 1 # TODO this means we're always checking the next node before reaching it
                    if current_index == index:
                        temp = current.next
                        current.next = new_node
                        new_node = temp # TODO fix: current.next.next = temp
                        return
                    current = current.next
                    """
                    pass # TODO remove
                break # TODO remove
            # if current.next == None, i.e index == -1, append
            if current.next == None:
                self.append(value)
                return

    def pop(self):
        # Remove last node
        # edge cases, empty and single node
        current = self.head
        if self.head == None:
            return None
        elif self.head.next == None:
            self.head = self.tail = None
        else:
            # current = self.head
            previous = None
            while current.next != None: # get to the end
                previous = current
                current = current.next
            self.tail = previous
            self.tail.next = None
        # self.length -= 1
        return current

    def pop_first(self):
        # edge cases, empty, single nodes
        current = self.head
        if self.head == None:
            return None
        elif self.head.next == None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        current.next = None # detatch the removed node
        return current

LL = LinkedList(1)
LL.pop()
LL.pop()
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(5)
LL.pop()
LL.prepend(10)
LL.prepend(300)
LL.pop_first()
LL.print_list()
