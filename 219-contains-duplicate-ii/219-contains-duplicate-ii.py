class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict={}
        for idx in range(len(nums)):
            if nums[idx] in myDict and abs(idx-myDict[nums[idx]])<=k:
                return True
            myDict[nums[idx]]=idx
        return False
        print(myDict)