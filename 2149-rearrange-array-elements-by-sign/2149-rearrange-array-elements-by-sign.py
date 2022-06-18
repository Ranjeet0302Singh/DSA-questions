class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[]
        pos=[]
        neg=[]
        p_count=n_count=0
        for i in nums:
            if(i>=0):
                pos.append(i)

            else:
                neg.append(i)
        for k in range(len(nums)):
            if(k%2==0):
                ans.append(pos[p_count])
                p_count+=1
            else:
                ans.append(neg[n_count])
                n_count+=1
        return ans
                