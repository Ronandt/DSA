class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_start = 0
        pointer_end = len(numbers)-1
        while True:
            if numbers[pointer_start] + numbers[pointer_end] == target:
                return [pointer_start +1, pointer_end + 1]
            if (numbers[pointer_start] + numbers[pointer_end]) > target:
                pointer_end -=1
            if (numbers[pointer_start] + numbers[pointer_end]) < target:
                pointer_start +=1
        