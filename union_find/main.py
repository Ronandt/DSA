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
            self.array[current_val] = self.array[self.array[current_val]] #path compression
            current_val = self.array[current_val] 
        return current_val
    def find(self, q, p):
        return self.find_value_root(q) == self.find_value_root(p)
    def union(self, q, p):
        val1 = self.find_value_root(q)
        val2 = self.find_value_root(p)
        if(val1 ==val2):
            return 
        if(self.tree_count[val1] > self.tree_count[val2]):

            self.tree_count[val1] +=self.tree_count[val2]
            self.array[val2] = val1
        else:
            self.tree_count[val2] +=self.tree_count[val1]
            self.array[val1] =self.array[val2]

            
#[1,2,3,4,5]
#[0,0,0,0,0]



                
    






