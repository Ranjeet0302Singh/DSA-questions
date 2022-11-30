class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum=0
        maxi=nums[0]
        for i in nums:
            Sum=Sum+i
            maxi=max(maxi,Sum)
            if Sum<0:
                Sum=0
        return maxi
        