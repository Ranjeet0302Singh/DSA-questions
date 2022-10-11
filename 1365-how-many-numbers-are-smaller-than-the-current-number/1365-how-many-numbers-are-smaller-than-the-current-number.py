class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j] and j!=i:
                    count+=1
            ans.append(count)
        return ans
    
        