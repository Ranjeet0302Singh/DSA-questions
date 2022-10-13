class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1={}
        dict2={}
        for i in word1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
                
        for j in word2:
            if j in dict2:
                dict2[j]+=1
            else:
                dict2[j]=1
        # print(dict1)
        a=list(dict1.values())
        b=list(dict2.values())
        c=list(dict1.keys())
        d=list(dict2.keys())
        print(c)
        print(d)
        print(sorted(c))
        print(sorted(d))
        if sorted(a)==sorted(b) and sorted(c)==sorted(d):
            return True
        else:
            return False