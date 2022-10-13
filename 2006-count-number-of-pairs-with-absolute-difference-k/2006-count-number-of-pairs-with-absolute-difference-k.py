class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        myDict={}
        count=0
        for i in nums:
            if i in myDict:
                myDict[i]+=1
            else:
                myDict[i]=1
        for i in nums:
            if i+k in myDict:
                count+=myDict[i+k]
        return count
                
        