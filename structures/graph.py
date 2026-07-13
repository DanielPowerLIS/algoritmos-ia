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
        node_to_remove = self.nodes[value]
        
        #remove the references to this node
        for current_node in self.nodes.values():
            current_node.remove_neighbor(node_to_remove)

        #remove the node from the graph
        del self.nodes[value]

    def add_edge(self, origin, destination):
        #add a edge diriged from origin to destination if both nodes exist
        if origin not in self.nodes:
            raise ValueError(f"Node {origin} does not exist in the graph.")
            return
        
        if destination not in self.nodes:
            raise ValueError(f"Node {destination} does not exist in the graph.")
            return
        
        self.nodes[origin].add_neighbor(self.nodes[destination])

    def remove_edge(self, origin, destination):
        #remove a edge from origin to destination
        if origin not in self.nodes:
            raise ValueError(f"Node {origin} does not exist in the graph.")
            return
        
        if destination not in self.nodes:
            raise ValueError(f"Node {destination} does not exist in the graph.")
            return
        
        self.nodes[origin].remove_neighbor(self.nodes[destination])

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

    def _str_(self):
        result = ""

        for node in self.nodes.values():
            neighbors = [
                neighbor.value for neighbor in node.neighbors
            ]

        result += f"Node {node.value}: Neighbors -> {neighbors}\n"

        return result
    
    