class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abcb
        if len(s) == 0:
            return 0
        pointer_1 = 0
        dictionary = {}
        maximum = 0
        for x in s:
            if(x not in dictionary):
                dictionary[x] = 0
                maximum = max(maximum, len(dictionary))
            else:
                while x in dictionary:
                    del dictionary[s[pointer_1]]
                    pointer_1+=1
                dictionary[x] = 0
        return maximum

