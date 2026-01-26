class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, value):
        
        if(self.head == None):
            self.head = Node(value)
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = Node(value)
    def reverse(self):
        if(self.head == None):
            return -1
        prev = None
        current = self.head 
        while current:
            next = current.next #the actual next one (second last)
            current.next = prev
            prev = current
            current = next
        
    
"""
rev = None, current = A
Iteration 1 (Focusing on A):
next = B (save the rest of the list)
current.next = None (A now points to nothing)
prev = A
current = B
List looks like: None ← [A] ...and... [B] → [C]
Iteration 2 (Focusing on B):
next = C
current.next = A (B now points back to A)
prev = B
current = C
List looks like: None ← [A] ← [B] ...and... [C]
Iteration 3 (Focusing on C):
next = None
current.next = B (C now points back to B)
prev = C
current = None
List looks like: None ← [A] ← [B] ← [C]

"""