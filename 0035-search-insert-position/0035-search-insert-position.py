class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if(i==len(nums)-1 and nums[i]!=target):
                break
            elif(nums[i]==target):
                return i
        for j in range(len(nums)):
            if(j==len(nums)-1 and nums[j]<target):
                return len(nums)
            elif(nums[j]>target):
                return j
                