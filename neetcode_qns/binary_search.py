class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pointer_1 = 0
        pointer_2 = len(nums) -1
        while pointer_2 >= pointer_1:
            average = (pointer_2 + pointer_1)//2
            print(nums[average], pointer_1, pointer_2)
            if nums[average] == target:
                return average
            if target > average:
                pointer_1 = average + 1
            elif average > target:
                pointer_2 = average - 1
        print(pointer_1, pointer_2)
        return -1
    


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        parameter = len(matrix[0]) #assume element exists [8, 13, 40]
        indexes = []
        matrix_pointer_1 = 0
        matrix_pointer_2 = len(matrix[0]) -1
        main = 0
      
        if target > matrix[-1][-1]:
             return -1
        elif target < matrix[0][0]:
            return -1
        else:
            while matrix_pointer_2>=matrix_pointer_1:

                average = matrix_pointer_1 + matrix_pointer_2

                if average[]

        print(parameters)