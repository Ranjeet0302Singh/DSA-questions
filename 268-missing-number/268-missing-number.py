class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)):
            if(i!=nums[i]):
                return i
            elif(nums[len(nums)-1]==i):
                return len(nums)
            