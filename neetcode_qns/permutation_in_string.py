class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pointer_1 = 0
        original_freq_map = {}
        for x in s1:
            if x in original_freq_map:
                original_freq_map[x] +=1
            else:
                original_freq_map[x] = 1

        window_freq_map = original_freq_map.copy()
        #If it exists check if it's more than we need, if it is, backtrack until there's no duplicates
        #If it doesn't exists backtrack until we find the thing because the rest doesn't matter then 
        for ind,x in enumerate(s2):
            local_output = True
            local_total = 0
       
            if x in window_freq_map:
                window_freq_map[x] -= 1
                while window_freq_map[x] < 0:
                    if(s2[pointer_1] in window_freq_map):
                        window_freq_map[s2[pointer_1]] += 1
                    pointer_1+=1

                for d,y in window_freq_map.items():
                    if y!= 0:
                        local_output = False
                if(local_output):
                    return local_output
            
            else:
                while pointer_1 != ind:

                    if(s2[pointer_1] in window_freq_map):
                        window_freq_map[s2[pointer_1]] += 1
                    pointer_1+=1

        return False

