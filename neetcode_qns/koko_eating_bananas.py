import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #index is the number of bananas
        #number of hours to eat banans 
        #banas per hour of k
        #if pile has less than k banas you can finish but cannot eat another pile 
        #return minimum k such that you can eat all the bnas iwthin h 
        #Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.
        #Remember that h will alWAYS BE greater or equal to the number of piles
        pointer_2 = max(piles) - 1
        pointer_1 = 1
        minimum = max(piles)
        while pointer_2 >= pointer_1:
            average = (pointer_2 + pointer_1)//2
            total = 0 
            for x in piles:
                total += math.ceil(x/(average))
            print(pointer_2, pointer_1, average, minimum)
            #total
            if total > h:
                pointer_1 = average+1
            elif total <= h:
                pointer_2 = average-1
                minimum = min(average, minimum)
        return minimum
            

        