class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start=0
        end=num
        mid=start+(end-start)//2
        while(start<=end):
            if(mid**2==num):
                return True
            if(mid**2<num):
                start=mid+1
            else:
                end=mid-1
            mid=start+(end-start)//2
        return False