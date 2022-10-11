class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping={' ':' '}
        i=0
        ans = ''
        letter='abcdefghijklmnopqrstuvwxyz'
        
        for char in key:
            if char not in mapping:
                mapping[char]=letter[i]
                i+=1
        for char in message:
            ans+=mapping[char]
        return ans
        