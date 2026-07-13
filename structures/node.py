class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, node, cost=1):
        #add a new neighboor if not already in the list
        if node not in self.neighbors:
            self.neighbors[node] = cost

    def remove_neighbor(self, node):
        #remove a neighbor if it is in the list
        if node in self.neighbors:
            del self.neighbors[node]

    def has_neighbor(self, node):
        #check if a node is a neigbor
        return node in self.neighbors
    
    def _str_(self):
        return str(self.value)
    
    def _repr_(self):
        return f"Node({self.value})"
    

