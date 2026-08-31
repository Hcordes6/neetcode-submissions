class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        mostProfit = 0

        while r < len(prices):
            currProfit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                mostProfit = max(mostProfit, currProfit)
            else:
                l = r
            r += 1
        return mostProfit