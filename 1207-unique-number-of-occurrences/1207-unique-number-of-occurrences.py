class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        myDict={}
        for i in arr:
            if i not in myDict:
                myDict[i]=1
            else:
                myDict[i]+=1
        print(myDict)
        ans=set()
        arr=sorted(list(set(arr)))
        for i in range(len(myDict)):
            print(myDict[arr[i]])
            if myDict[arr[i]] not in ans:
                ans.add(myDict[arr[i]])
            else:
                return False
        return True
        