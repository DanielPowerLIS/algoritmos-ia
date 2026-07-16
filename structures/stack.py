class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        #add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        #remove and return the item at the top of the stack
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        #return the item at the top of the stack without removing it
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        #check if the stack is empty
        return len(self.items) == 0
    
    def size(self):
        #return the number of the items in the stack
        return len(self.items)
    
    def clear(self):
        #remove all items from the stack
        self.items.clear()

    def __str__(self):
        return str(self.items)  