class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit=0
        MinCost=prices[0]
        for i in prices:
            MinCost=min(MinCost,i)
            profit=i-MinCost
            MaxProfit=max(MaxProfit,profit)
        return MaxProfit