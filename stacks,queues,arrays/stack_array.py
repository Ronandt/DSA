
        

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
    

