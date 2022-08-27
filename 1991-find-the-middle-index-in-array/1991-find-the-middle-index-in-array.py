class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum,rightSum=0,sum(nums)
        for index,element in enumerate(nums):
            rightSum-=element
            if leftSum==rightSum:
                return index
            else:
                leftSum+=element
        return -1
        