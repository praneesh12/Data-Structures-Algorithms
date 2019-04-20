class node:
    ''' Wrapper class for LinkedList'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    ''' Main LinkedList class'''
    def __init__(self):
        self.head = node()

    # Define append function
    def append(self, data):
        new_node = node(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def display_as_list(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)

        print(elements)


    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next != None:
            total += 1
            cur_node = cur_node.next
        return total

    def get(self, index):
        if index >= self.length():
            print("Error : Get index out of range!")
            return None

        cur_idx = 0
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            if cur_idx==index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("Error : erase index is out of range")
            return None

        cur_idx = 0
        cur_node = self.head
        while cur_node.next!=None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx==index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def insert(self, index, data):
        if index >= self.length():
            print("Error : insert index out of range")
            return None

        cur_idx = 0
        cur_node = self.head
        insert_node = node(data)
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            if index==cur_idx:
                insert_node.next = last_node.next
                last_node.next = insert_node.next
                return None
            cur_idx += 1





my_list = linked_list()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)


my_list.display_as_list()
print("element at 2nd index {}".format(my_list.get(2)))

# print("erase 2nd element of the list {}".format(my_list.erase(2)))
my_list.display_as_list()
print("insert 7 as 2nd element of the list\n".format(my_list.insert(2, data=7)))
my_list.display_as_list()



















