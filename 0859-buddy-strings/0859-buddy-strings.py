class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        idx=[]
        count=0
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            if s[i]!=goal[i]:
                count+=1
                idx.append(i)
        if count>2:
            return False
        elif count==2 and s[idx[0]] == goal[idx[1]] and s[idx[1]] == goal[idx[0]]:
            return True
        elif count == 0 and len(set(s))<len(s):
            return True
                
        