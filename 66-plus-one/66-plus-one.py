class Solution:
    def plusOne(self, a: List[int]) -> List[int]:
        num=""
        for i in range(len(a)):
            num+=str(a[i])
        num=int(num)+1
        num=str(num)
        a=[]
        for i in range(len(num)):
            a.append(int(num[i]))
        return a
            