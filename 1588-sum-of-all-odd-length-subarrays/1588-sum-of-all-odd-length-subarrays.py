class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result=sum(arr)
        lenght=len(arr)
        for i in range(3,lenght+1,2):
            for j in range(lenght):
                if i+j>lenght:
                    break
                result+=sum(arr[j:i+j])
        return result