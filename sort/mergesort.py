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