class Solution:
    def canMakeArithmeticProgression(self, nums: List[int]) -> bool:
        nums.sort()
        diff=nums[0]-nums[1]
        print(diff)
        for i in range(1,len(nums)):
            # print(nums[i-1]-nums[i])
            if diff!=nums[i-1]-nums[i]:
                return False
                
        return True