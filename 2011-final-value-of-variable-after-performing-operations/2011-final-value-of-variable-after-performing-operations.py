class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for i in (operations):
            if i == '--X':
                ans= ans-1
            elif i == 'X--':
                ans= ans-1
            elif i == '++X':
                ans= 1+ans
            else:
                ans= ans+1
        return ans
                
        