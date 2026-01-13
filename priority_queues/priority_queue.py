class UnorderedPQ:
    def __init__(self, capacity):
        self.pq = [None for _ in range(capacity)]
        self.length =0

    def is_empty(self):
        return self.length == 0 
    
    def insert(self,key):
        pass

print(UnorderedPQ(6).pq)