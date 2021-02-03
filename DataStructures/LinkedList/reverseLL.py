
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        return
    
    def display(self):
        cur = self.head
        while cur:
            print(cur.data) 
            cur = cur.next
    
    def reverse_iterate(self):
        cur = self.head
        prev = None

        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp
        self.head = prev
        return prev



mylist = linkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.display()
print("Reverse the Linked List>>>>>>>>")
mylist.reverse_iterate()
mylist.display()


