class Node:
    def __init__(self,val):
        self.val=val
        self.leftChild=None
        self.rightChild=None
        self.parent=None
    

    def insert(self, val):
        # If value to be inserted is less than current value ---> insert value in left sub tree
        # Else insert in right sub Tree
        if val < self.val:
            if self.leftChild:
                return self.leftChild.insert(val)
            else:
                self.leftChild = Node(val)
        elif val > self.val:
            if self.rightChild:
                return self.rightChild.insert(val)
            else:
                self.rightChild = Node(val)

    def search(self, val):
        if val > self.val:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return False
        elif val < self.val:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return False
        else:
            return True 
        return False

    
    def delete(self,val):

        if val < self.val:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
            else:
                print(str(val)+" not found in the tree")
                return None
        
        elif val > self.val:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
            else:
                print(str(val)+" not found in the tree")
                return None
        
        else:  
            # val Node found at leaf node
            if (self.rightChild is None) and (self.leftChild is None):
                self = None
                return None
            
            # val Node found with left child
            elif (self.leftChild is None):
                temp = self.rightChild
                self = None
                return temp
            # val Node found with right child
            elif (self.rightChild is None):
                temp = self.leftChild
                self = None
                return temp
            
            # val node found with two children
            
            else:
                # first get the inorder successor
                current = self.rightChild
                # loop down to find the leftmost leaf
                while(current.leftChild):
                    current = current.leftChild
                self.val = current.val
                self.rightChild = self.rightChild.delete(current.val)

        return self 

            
            

                    

