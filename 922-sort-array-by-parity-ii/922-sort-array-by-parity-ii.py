class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans=[]
        even=[]
        odd=[]
        e_count=0
        o_count=0
        for i in nums:
            if(i%2==0):
                even.append(i)
            else:
                odd.append(i)
        for j in range(len(nums)):
            if(j%2==0):
                ans.append(even[e_count])
                e_count+=1
            else:
                ans.append(odd[o_count])
                o_count+=1
        return ans