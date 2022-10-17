class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        max_profit=0
        while right <len(prices):
            profit=prices[right]-prices[left]
            if prices[right] > prices[left]:
                max_profit=max(profit,max_profit)
            else:
                left=right
            right+=1
        return max_profit
        