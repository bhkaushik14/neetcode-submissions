class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        total = 0
        best = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                best = max(best, prices[r] - prices[l])
            
            r += 1
        total += best
        return total