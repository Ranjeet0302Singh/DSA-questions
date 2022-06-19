class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)):
            # if(i<len(nums)-1):
                
            ans^=nums[i]
        return ans
        