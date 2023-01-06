class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        count=0
        i=0
        while i<len(costs):
            if ans+costs[i]<=coins:
                ans+=costs[i]
                count+=1
            i+=1
        return count
            
        