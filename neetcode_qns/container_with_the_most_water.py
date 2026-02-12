class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #so how do you know which one is the largest?
        #largest distance (number of bars between + 1 or len -x)* height
        #assume the greater the length teh better, how do we adjust for height?
        #can't sort because it's tied to the config rn
        pointer_1 = 0
        pointer_2 = len(heights) -1 
        max_calc = 0 #assume nothing
        for x in range(len(heights)):
            calc =(len(heights) - (x+1)) * min(heights[pointer_1], heights[pointer_2])
            if calc > max_calc:
                max_calc = calc
            if heights[pointer_1] > heights[pointer_2]:
                pointer_2 -= 1
            else:
                pointer_1 += 1
        return max_calc
            