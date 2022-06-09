class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        while start<end:
            sum=numbers[start]+numbers[end]
            if sum==target:
                return [start+1 ,end+1]
            if sum>target:
                end-=1
            else:
                start+=1