class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lenght=len(nums)
        for i in range(lenght):
            nums.append(nums[i])
        return nums
        