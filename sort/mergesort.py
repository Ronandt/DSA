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
        while left and right: #until one of them empty
            min_num = left.pop(0) if left[0] <= right[0] else right.pop(0)
            output.append(min_num)
        output.extend(left)
        output.extend(right)
        return output
    

"""
Why this works:

The while left and right: loop stops when one list is empty

The remaining list is already sorted

extend efficiently appends all remaining values

Example:

output = [1, 3, 5]
left = []
right = [6, 7, 8]

output.extend(left)   # does nothing
output.extend(right)  # adds 6,7,8


Result:

[1, 3, 5, 6, 7, 8]
"""