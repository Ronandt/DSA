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
    