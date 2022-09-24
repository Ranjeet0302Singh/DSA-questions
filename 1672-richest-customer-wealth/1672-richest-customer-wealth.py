class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Max=0
        for i in range(len(accounts)):
            if sum(accounts[i])>Max:
                Max=sum(accounts[i])
        return Max