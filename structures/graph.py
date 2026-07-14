from node import Node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        #add a new node to the graph if it doesn´t already exist
        if value not in self.nodes:
            self.nodes[value] = Node(value)


    def remove_node(self, value):
        #remove a node y all its connections if it exists
        if value not in self.nodes:
            return
        
        #remove the references to this node
        for current_node in self.nodes.values():
            current_node.remove_neighbor(value)

        #remove the node from the graph
        del self.nodes[value]

    def add_edge(self, origin, destination, cost=1):
        #add a edge diriged from origin to destination if both nodes exist
        if origin not in self.nodes:
            raise ValueError(f"Node {origin} does not exist in the graph.")
            return
        
        if destination not in self.nodes:
            raise ValueError(f"Node {destination} does not exist in the graph.")
            return
        
        self.nodes[origin].add_neighbor(destination, cost)

    def remove_edge(self, origin, destination):
        #remove a edge from origin to destination
        if origin not in self.nodes:
            raise ValueError(f"Node {origin} does not exist in the graph.")
        
        if destination not in self.nodes:
            raise ValueError(f"Node {destination} does not exist in the graph.")
        
        self.nodes[origin].remove_neighbor(destination)

    def get_node(self, value):
        #return the node if it exists, otherwise return None
        if value in self.nodes:
            return self.nodes[value]
        
        return None
    
    def contains(self, value):
        #check if a node exists in the graph
        return value in self.nodes
    
    def clear(self):
        #clear the graph
        self.nodes.clear()

    def __str__(self):
        result = ""

        for node in self.nodes.values():
            result += f"Node {node.value}: Neighbors -> {node.neighbors}\n"

        

        return result
    
    