class NormalUnionFind:
    def __init__(self):
        self.array = list(range(0,10))
    def find(self, q, p):
        return self.array[q] == self.array[p]
    def union(self, q, p): 
        for x in range(len(self.array)):
            if(self.array[x] == self.array[q]):
                self.array[x] = self.array[p]
normal = NormalUnionFind()
normal.union(1, 2)
normal.union(2, 3)
normal.union(3, 4)

print(normal.array)

class GraphUnionFind:
    def __init__(self):
        self.array = list(range(0,10))
    def find_value_root(self,a):
        current_val = a
        while(self.array[current_val] != current_val):
            current_val = self.array[current_val] 
        return current_val
    def find(self, q, p):
        return self.find_value_root(q) == self.find_value_root(p)
    def union(self, q, p):
        self.array[q] = p

class OptimisedGraphUnionFind:
    def __init__(self):
        self.array = list(range(0,10))
        self.tree_count =[0 for _ in self.array]

    def find_value_root(self,a):
        current_val = a
        while(self.array[current_val] != current_val):
            current_val = self.array[current_val] 
        return current_val
    def find(self, q, p):
        return self.find_value_root(q) == self.find_value_root(p)
    def union(self, q, p):
        if(q ==p):
            return 
        
        if(self.tree_count[q] > self.tree_count[p]):

            self.tree_count[p] +=1
            self.array[p] = q
        else:
            self.tree_count[q] +=1
            self.array[q] =p

            
#[1,2,3,4,5]
#[0,0,0,0,0]



                
    






