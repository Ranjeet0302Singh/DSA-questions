class Solution:
    def frequencySort(self, s: str) -> str:
        myDict={}
        ans=""
        for i in range(len(s)):
            if s[i] in myDict:
                myDict[s[i]]+=1
            else:
                myDict[s[i]]=1
        # print(myDict)
        sortDict=dict(reversed(sorted(myDict.items(),key=lambda x:x[1])))
        print(sortDict)
        value=list(sortDict.values())
        key=list(sortDict.keys())
        # print(value)
        # print(key)
        temp=len(value)*[None]
        for j in range(len(value)):
            temp[j]=key[j]*value[j]
        print(temp)
        return ''.join((temp))
            
            