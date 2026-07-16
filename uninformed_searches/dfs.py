from structures.stack import Stack

def depth_first_search(graph, start_node):
    stack = Stack()
    visited = set()
    traversal = []
    
    stack.push(start_node)
    visited.add(start_node)
    
    while not stack.is_empty():
        current = stack.pop()
        current_node = graph.get_node(current)
        traversal.append(current_node.value)

        for neighbor in reversed(list(current_node.neighbors)):
            if neighbor not in visited:
                stack.push(neighbor)
                visited.add(neighbor)

    return traversal
