class Node:
    def _init_(self, value):
        self.value = value
        self.neighbors =[]

    def add_neighbor(self, node):
        #add a new neighboor if not already in the list
        if node not in self.neighbors:
            self.neighbors.append(node)

    def remove_nieghbor(self, node):
        #remove a neighbor if it is in the list
        if node in self.neighbors:
            self.neighbors.remove(node)

    def has_neighbor(self, node):
        #check if a node is a neigbor
        return node in self.neighbors
    
    def _str_(self):
        return str(self.value)
    
    def _repr_(self):
        return f"Node({self.value})"
    
    
