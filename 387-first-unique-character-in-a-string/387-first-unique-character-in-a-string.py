class Solution:
    def firstUniqChar(self, s: str) -> int:
        abc = "abcdefghijklmnopqrstuvwxyz"
        ans = 10**5     # since 1 <= s.length <= 105, the answer must be smaller than 10^5
        print(s.find('e'))
        for c in abc:
            idx = s.find(c)     # check if this word is in s
            if (idx != -1 and idx == s.rfind(c)):   # check if first index == last index
                ans = min(ans, idx)     # store the smallest 
                
        return ans if ans < 10**5 else -1