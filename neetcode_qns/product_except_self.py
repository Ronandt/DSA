class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
    
        output = []

        # Build prefix (product BEFORE index)
        prefix.append(1)
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])

        # Build postfix (product AFTER index)
        postfix = [0] * len(nums)
        postfix[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        # Build output
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])

        return output