class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        #add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        #remove and return the item at the front of the queue
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        return self.items.pop(0)
    
    def peek(self):
        #return the item at the front of the dequeue without removing it
        if self.is_empty():
            raise IndexError("peek from empty queue")
        
        return self.items[0]
    
    def is_empty(self):
        #check if the queue is empty
        return len(self.items) == 0
    
    def size(self):
        #return the number of the items in the dequeue
        return len(self.items)
    

    def clear(self):
        #remove all items from the queue
        self.items.clear()

    def __str__(self):
        return str(self.items)
    
    