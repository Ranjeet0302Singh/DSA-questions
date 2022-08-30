class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i=len(nums)-1
        j=len(nums)-3
        while(j>=0):
            if nums[j]+nums[j+1]>nums[i]:
                return nums[j]+nums[j+1]+nums[i]
            j-=1
            i-=1
        return 0