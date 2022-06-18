class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        Sum=0
        for i in nums:
            Sum=Sum+i
            ans.append(Sum)
        return ans