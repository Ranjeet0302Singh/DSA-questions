class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp=set(nums)
        if(len(nums)==len(temp)):
            return False
        else:
            return True