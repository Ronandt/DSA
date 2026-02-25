class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pointer = 0
        dictionary = {}
        
        #Minimum allowable is the 
        #{A: 3, B:2} number :2
        #{A: 1, B:1, C:1} 
        #Transform the ones that have lower numbs
        maximum = 0
    
        for x in s:

            if(x in dictionary):
                dictionary[x] += 1
            else:
                dictionary[x] = 1
            highest = 0
            total_window = 0 
            for values, index in dictionary.items():
                highest = max(highest, index)
                total_window += index
            
   
            while total_window -highest > k:
                total_window -=1
                dictionary[s[pointer]] -=1 
                pointer +=1
            maximum  = max(total_window, maximum)

        return maximum

