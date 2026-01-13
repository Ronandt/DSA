class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def is_empty(self):
        return self.first == None
    def enqueue(self, item):
        oldlast = self.last
        self.last = Node(item=item)
    
        if(self.is_empty()):
            self.first = self.last
        else:
            oldlast.next = self.last #first -> last (Who is the next person in line not the next person aftere)
    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if(self.is_empty()):
            self.last = None
        return item
        
        
