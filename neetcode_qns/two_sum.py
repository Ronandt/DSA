class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap_pair = {}
        for x in range(len(nums)):
            if(nums[x] in hashmap_pair):
               
                return list(sorted([hashmap_pair[nums[x]],x]))
               
            hashmap_pair[target - nums[x]] = x #Or should i do this cuz ultimately the index is the goal 
        return -1
          
