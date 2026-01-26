class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #rules of the game: an anagram contains the same amount, type of characters if s==t
        s_hashmap = {}
        if len(s) != len(t):
            return False
        for x in s:
            if x not in s_hashmap:
                s_hashmap[x] = 1
            else:
                s_hashmap[x] += 1
        for x in t:
            if x not in s_hashmap:
                return False    
            if x in s_hashmap:
                s_hashmap[x] -=1
            if s_hashmap[x] == 0:
                del s_hashmap[x]
        if len(s_hashmap) > 0: #if there are still remaining items 
            return False    
        return True
