class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        parameter = len(matrix[0]) #assume element exists [8, 13, 40]
        indexes = []
        matrix_pointer_1 = 0
        matrix_pointer_2 = len(matrix) -1

        main = 0
      
        if target > matrix[-1][-1]:
             return False
        elif target < matrix[0][0]:
            return False
        else:
            while matrix_pointer_2>=matrix_pointer_1:

                average = (matrix_pointer_1 + matrix_pointer_2)//2
                print(average)
                if matrix[average][-1] >= target and matrix[average][0] <= target:
                    main = average
                    break
                elif matrix[average][-1] < target:
                    matrix_pointer_1 = average + 1
                elif matrix[average][0] > target:
                    matrix_pointer_2 = average-1
        selected_array = matrix[main]
        array_pointer_1 = 0
        array_pointer_2 = len(selected_array) -1
        while array_pointer_2 >= array_pointer_1:
            average = (array_pointer_1 + array_pointer_2)//2
            if selected_array[average] == target:
                print(selected_array[average])
                return True
            elif selected_array[average] > target:
                array_pointer_2 = average-1
            elif selected_array[average] < target:
                array_pointer_1 = average + 1
        
        return False
        


        