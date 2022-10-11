class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        myDict={}
        for i in nums:
            if i in myDict:
                count+=myDict[i]
                myDict[i]+=1
            else:
                myDict[i]=1
        return count