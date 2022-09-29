class Solution:
    

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict={}
        for i in range(len(nums)):
            new=target-nums[i]
            if new not in myDict:
                myDict[nums[i]]=i
            else:
                return[myDict[new],i]