class SelectionSort:
    def __init__(self, array):
        self.array = array
    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]
    def sort(self):
        for x in range(len(self.array)): #minus ne ? 
            min_item = x
            for y in range(x + 1, len(self.array)):
                if(self.array[min_item] > self.array[y]):
                    min_item = y 
            self.swap(x, y)
            
                
    def compare(self, a, b):
        return a > b
