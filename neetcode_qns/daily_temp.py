class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = [] #[71, 72]
        counter = [0] * len(temperatures) 
        for x in range(len(temperatures)):
          
            while len(temp_stack) > 0 and temperatures[x] > temp_stack[-1][1]:
              
                val = temp_stack.pop()
                counter[val[0]] = x - val[0]
            
                
            temp_stack.append((x, temperatures[x])) #(index, value)
        #those not popped
        for x in temp_stack:
            counter[x[0]] = 0 
        return counter
    
    #Do not use accumulate because there will be missing data if you pop