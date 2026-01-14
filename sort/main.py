class SelectionSort:
    def __init__(self, array):
        self.array = array
    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]
    def sort(self):
        for x in range(len(self.array)):
            min_item = x
            for y in range(x + 1, len(self.array)):
                if(self.array[min_item] > self.array[y]):
                    min_item = y 
            self.swap(x, y)
            
                
    def compare(self, a, b):
        return a > b

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
    

class MergeSort:
    def merge_sort(self, arr: list) -> list:
        n = len(arr)
        if n <= 1: #base case 
            return arr
        mid = n // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)
    def merge(self, left: list, right: list) -> list:
        output = []
        while left and right:
            min_num = left.pop(0) if left[0] <= right[0] else right.pop(0)
            output.append(min_num)
        output.extend(left)
        output.extend(right)
        return output