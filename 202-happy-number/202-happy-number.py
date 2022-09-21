class Solution:
    def isHappy(self, n: int) -> bool:
        ans=set()
        while n!=1:
            n= sum([int(i)**2 for i in str(n)])
            if n in ans:
                return False
            else:
                ans.add(n)
        return True
        