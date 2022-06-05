class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        List=[]
        ans=0
        nums.sort()
        for i in range(1,len(nums)):
            if(nums[i]^nums[i-1]==0):
                List.append(nums[i])
        List.sort()
        return List
            