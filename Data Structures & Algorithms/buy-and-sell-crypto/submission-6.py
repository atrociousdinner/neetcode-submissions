class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        j = 1
        while j < len(prices):
            if prices[i] >= prices[j]:
                i = j
            else:
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
                
                
            j += 1
            

        return max_profit



        