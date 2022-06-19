class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_f="qwertyuiop"
        # temp=''.join(sorted(row_f))
        # print(temp)
        # ....eiopqrtuwy
        row_s="asdfghjkl"
        row_t="zxcvbnm"
        ans=[]
        for i in words:
            j=0
            count=0
            temp_s=str(i)            
            if temp_s[0].lower() in row_f:
                S=row_f
            elif temp_s[0].lower() in row_s:
                S=row_s
            elif temp_s[0].lower() in row_t:
                S=row_t
            while(j<len(temp_s)):
                if temp_s[j].lower() in S:
                    count+=1
                    # print(count)
                j+=1
            if(count==len(temp_s)):
                ans.append(temp_s)
        return ans
                    
        