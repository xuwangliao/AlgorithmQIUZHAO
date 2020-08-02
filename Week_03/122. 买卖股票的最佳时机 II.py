class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_rev = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_rev += prices[i]-prices[i-1]
        return max_rev