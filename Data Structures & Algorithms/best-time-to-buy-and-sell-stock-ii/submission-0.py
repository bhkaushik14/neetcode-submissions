class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        
        while i < len(prices) - 1:
            if prices[i] < prices[i + 1]:
                index = self.increase(prices[i:], i)
                print(index)
                profit += prices[index] - prices[i]
                i = index
            i += 1

        return profit

    def increase(self, prices: List[int], currentIndex) -> int:
        count = currentIndex
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                count += 1
            else:
                break
        
        return count
