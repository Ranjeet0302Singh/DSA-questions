class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit=0
        MinCost=prices[0]
        for i in range(len(prices)):
            MinCost=min(MinCost,prices[i])
            profit=prices[i]-MinCost
            MaxProfit=max(MaxProfit,profit)
        return MaxProfit