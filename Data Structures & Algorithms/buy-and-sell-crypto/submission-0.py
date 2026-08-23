class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            currProfit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                profit = max(profit, currProfit)
            else:
                l = r
            r += 1

        return profit

