class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        freq = [[] for x in range(len(nums))]
        final  = []
        for x in nums:
            numbers[x] = 1 + numbers.get(x, 0)
        for x,y in numbers.items():
            print(y, freq)
            freq[y-1].append(x)
        
        for x in range(1, len(freq) + 1):
            if(len(final) == k):
                break
            
            final.extend(freq[len(freq) - x])
        print(final)
        return final