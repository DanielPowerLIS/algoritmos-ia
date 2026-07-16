from structures.queue import Queue

def breadth_first_search(graph, start_node):
    queue = Queue()
    visited = set()
    traversal= []

    queue.enqueue(start_node)
    visited.add(start_node)
    while not queue.is_empty():
        current = queue.dequeue()
        current_node = graph.get_node(current)    
        traversal.append(current_node.value)

        for neighbor in current_node.neighbors:
            if neighbor not in visited:
                queue.enqueue(neighbor)
                visited.add(neighbor)   

    return traversal
