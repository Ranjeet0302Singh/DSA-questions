class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=s[0:len(s)//2]
        print(a)
        b=s[len(s)//2:]
        print(b)
        List=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        counta=0
        countb=0
        for i in range(len(s)//2):
            if a[i] in List:
                counta+=1
            if b[i] in List:
                countb+=1
        if counta==countb:
            return True
        else:
            return False
                
        