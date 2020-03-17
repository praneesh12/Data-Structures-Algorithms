
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head

        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def length(self):
        curr = self.head
        total = 0
        while curr.next:
            total += 1
            curr = curr.next
        return total

    def display(self):
        elements = []
        curr = self.head
        while curr.next:
            curr = curr.next
            elements.append(curr.data) 
        print(elements)
    
    def get(self, index):
        if index >= self.length():
            print("Search index not in linked list")
            return None

        cur_idx = 0
        curr = self.head
        while curr.next:
            curr = curr.next
            if cur_idx == index:
                return curr.data
            else:
                cur_idx += 1

    def Delete(self, index):
        if index >= self.length():
            print("Delete element out of range")
            return None
        curr_idx = 0
        curr = self.head
        while curr.next:
            last_node = curr
            curr = curr.next
            if index == curr_idx:
                last_node.next = curr.next
                return 
            curr_idx += 1

    
    def prepend(self, data):
        new_node = node(data)
        curr = self.head
        new_node.next = curr.next
        curr.next = new_node
        return 

    def insert(self, data, index):

        if index >= self.length():
            print("Insert index out of range")
            return 
        curr = self.head
        new_node = node(data)

        curr_idx = 0
        while curr.next:
    
            if curr_idx == index:
                last_node = curr
                new_node.next = curr.next
                last_node.next = new_node
            curr = curr.next
            curr_idx += 1
        return 

    def del_element(self, index):
        if index > self.length():
            print("Index out of range")

        curr = self.head
        curr_idx = 0
        while curr.next:
            last_node = curr
            curr = curr.next
            if curr_idx == index:
                last_node.next = curr.next
                curr = None
                return

            curr_idx += 1
    
    def reverse_iterative(self):
        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

        
    def rev_iterate(self):
        cur = self.head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        print(prev.data)
        self.head = prev
        return prev



 
my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
# print(my_list.length())
# my_list.Delete(3)
# my_list.display()
# my_list.prepend(10)
# my_list.display()

# my_list.insert(20,4)
# my_list.display()

# my_list.del_element(7)
my_list.display()
my_list.rev_iterate()
# my_list.reverse_iterative()
# my_list.reverse_recursive()
my_list.display()