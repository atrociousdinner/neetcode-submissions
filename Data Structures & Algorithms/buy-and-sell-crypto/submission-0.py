class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(len(prices)):
            print(f"L: ${prices[l]} R: ${prices[r]}")
            while (prices[r] - prices[l]) < 0:
                l += 1
            res = max(prices[r]-prices[l], res)

        return res