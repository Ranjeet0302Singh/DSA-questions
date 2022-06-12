class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        a=set()
        i=0
        total=0
        res=0
        for j in range(len(nums)):
            x=nums[j]
            while i<j and x in a:
                a.remove(nums[i])
                total-=nums[i]
                i+=1
            a.add(nums[j])
            total+=nums[j]
            res=max(res,total)
        return res