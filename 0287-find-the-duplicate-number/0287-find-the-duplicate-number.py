class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setList=set()
        for i in nums:
            if i in setList:
                return i
            else:
                setList.add(i)
        
        
        