class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum,rightSum=0,sum(nums)
        
        for index,element in enumerate(nums):
            rightSum-=element
            if rightSum==leftSum:
                return index
            else:
                leftSum+=element
        return -1