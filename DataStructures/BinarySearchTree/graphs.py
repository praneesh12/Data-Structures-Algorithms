from LinkedList import LinkedList

class Graph():
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # Adjacency list : Array of n linked lists 
        # n: no. of vertices
        self.array = []
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)
    
    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        
        if (source < self.vertices and destination < self.vertices):    
            self.array[source].insert_at_head(destination)
#             self.array[destination].insert_at_head(source)
    
    # Print graph
    def print_graph(self):
        print(">>Adjacency list of directed graphs<<")
        
        for idx in range(len(self.array)):
            print("|", idx, end=" | =>")
            temp = self.array[idx].get_head()
            while temp:
                print("[", temp.data, end=" ] ->")
                temp = temp.next_element
            print("None")
            
            
