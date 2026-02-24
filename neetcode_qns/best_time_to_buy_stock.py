class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 1
        minimum = 0
        max_price = 0
        while maximum < len(prices):
            max_price = max(max_price, prices[maximum] - prices[minimum])
            if prices[maximum] < prices[minimum]:
                minimum = maximum
            maximum+=1
        
            
        return max_price
