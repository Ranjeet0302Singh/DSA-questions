class Solution:
    def mySqrt(self, x: int) -> int:
        start=0
        end=x
        mid=start+(end-start)//2
        ans=-1
        while(start<=end):
            if(mid*mid==x):
                return mid
            if(mid*mid>x):
                end=mid-1
            else:
                start=mid+1
                ans=mid
            mid=start+(end-start)//2
        return ans

        