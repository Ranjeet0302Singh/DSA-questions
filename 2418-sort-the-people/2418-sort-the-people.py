class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        myDict={}
        ans=[]
        for i in range(len(names)):
            myDict[heights[i]]=names[i]
        print(myDict)
        for j in reversed(sorted(myDict.keys())):
            ans.append(myDict[j])
        print(ans)
        return ans
            