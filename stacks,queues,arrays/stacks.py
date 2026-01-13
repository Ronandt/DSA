class Node:
    #Where next is node, null means it terminates
    def __init__(self, item, next = None ):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.first = None
    def is_empty(self):
        return self.first == None
    def push(self,item): #Change self.first to the new one and reference to the old first
        oldfirst = self.first
        self.first = Node(item)
        self.first.next = oldfirst
    def pop(self): #change the reference to self.first.nexet
        item = self.first.item
        self.first = self.first.next
        return item
    
        

class ArrayStack:
    def __init__(self, length):
        self.fixed_arr = list(range(0, length))
        self.length = 0
    def is_empty(self):
        return self.length == 0
    def push(self, item):
        self.fixed_arr[self.length] = item
        self.length += 1
    def pop(self):
        current_value = self.fixed_arr[self.length -1]
        self.fixed_arr[self.length -1] = None
        self.length -= 1
        return current_value
    
class ArrayStackGrowth:
    def __init__(self):
        self.fixed_arr = [None]
        self.length = 0
    def is_empty(self):
        return self.length == 0
    def push(self, item):
        if(len(self.fixed_arr)== self.length):
            self.resize(self.length * 2)
        self.fixed_arr[self.length] = item
        self.length += 1
    def pop(self):
        
        current_value = self.fixed_arr[self.length -1]
        self.fixed_arr[self.length -1] = None
        self.length -= 1
        if self.length > 0 and self.length == len(self.fixed_arr)/4:
            self.resize(self.length/2)
        return current_value
    def resize(self, value):
        new_arr = [None for _ in range(value)]
        for x in range(0, self.length):
            new_arr[x] = self.fixed_arr[x]
        self.fixed_arr = new_arr
    

