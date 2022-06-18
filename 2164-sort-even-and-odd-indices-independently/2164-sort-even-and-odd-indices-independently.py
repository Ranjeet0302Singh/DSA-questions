class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        ans=[]
        e_count=0
        o_count=0
        for i in range(len(nums)):
            if(i%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        # print(even)
        
        odd.sort()
        
        odd.reverse()
        # print(odd)
        for j in range(len(nums)):
            if(j%2==0):
                ans.append(even[e_count])
                e_count+=1
            else:
                ans.append(odd[o_count])
                o_count+=1
        return ans
        