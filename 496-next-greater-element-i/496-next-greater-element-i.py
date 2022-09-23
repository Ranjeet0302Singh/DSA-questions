class Solution:
    def nextGreaterElement(self, num1: List[int], num2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(num1)):
            if num1[i] in num2:
                index=num2.index(num1[i])
                for j in range(index,len(num2)):
                    if num2[j]>num1[i]:
                        ans.append(num2[j])
                        break
                else:
                    ans.append(-1)
        return ans
        