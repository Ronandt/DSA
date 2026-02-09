class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for x in s:
            if x in "[({":
                stack.append(x)
            else:
                if len(stack) == 0 or hashmap[x] != stack.pop():
                    return False
        return len(stack) ==0

            
