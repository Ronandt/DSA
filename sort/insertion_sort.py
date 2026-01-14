
class InsertionSort:
    def __init__(self, array):
        self.array = array
    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]
    def sort(self):
        n = len(self.array)
        for i in range(1,n):
            insert_index = i
            current_value = self.array[i]
            for j in range(i-1, -1, -1): #[0,2,3,1] -> [0,2,3,3] (insert index is 2) -> [0, 2,2,3] (insert index is 1) ->
                if self.array[j] > current_value:
                    self.array[j+1] = self.array[j] #shift one up for the special thing and thn donw
                    insert_index = j #do it until you find the furthest insert index then swap with the current vaue 
                else:
                    break
            self.array[insert_index] = current_value
            
                
    def compare(self, a, b):
        return a > b   