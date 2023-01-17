class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count=0
        ans=0
        for i in s:
            if i=='1':
                count+=1
            elif count>0:
                count-=1
                ans+=1
        return ans