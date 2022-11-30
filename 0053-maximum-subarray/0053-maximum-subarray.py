class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum=maxi=nums[0]
        for i in nums[1:]:
            Sum= max(i,Sum+i)
            maxi=max(maxi,Sum)
        return maxi
        