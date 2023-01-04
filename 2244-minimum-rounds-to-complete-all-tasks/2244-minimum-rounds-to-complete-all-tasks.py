class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count=0
        myDict={}
        for i in tasks:
            if i in myDict:
                myDict[i]+=1
            else:
                myDict[i]=1
        # print(myDict)
        
        for j in list(myDict.values()):
            if j == 1:
                return -1
            else:
                count+= j//3 + bool(j%3)
        return count
                
            
        