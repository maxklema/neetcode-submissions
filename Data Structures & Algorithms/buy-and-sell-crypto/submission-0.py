class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        max_profit = 0
        start = 0
        next = 1    

        while (next < len(prices)):
            if (prices[next] <= prices[start] and next > start):
                start += 1
            else:
                max_profit = max(max_profit, prices[next] - prices[start])
                next += 1

        return max_profit