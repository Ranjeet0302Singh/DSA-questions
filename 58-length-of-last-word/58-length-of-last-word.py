class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        List=list(map(str,s.split()))
        # print(List)
        ans=len(List[-1])
        return ans