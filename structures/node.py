class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost=1):
        #add a new neighboor if not already in the list
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = cost

    def remove_neighbor(self, neighbor):
        #remove a neighbor if it is in the list
        if neighbor in self.neighbors:
            del self.neighbors[neighbor]

    def has_neighbor(self, neighbor):
        #check if a neighbor is in the list
        return neighbor in self.neighbors

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node({self.value})"
    

