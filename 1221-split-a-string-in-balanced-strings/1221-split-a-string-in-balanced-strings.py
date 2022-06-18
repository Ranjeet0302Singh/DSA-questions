class Solution:
    def balancedStringSplit(self, s: str) -> int:
        w_count=0
        l_count=0
        r_count=0
        for Ch in s:
            if Ch=='L':
                l_count+=1
            else:
                r_count+=1
            if r_count==l_count:
                w_count+=1
        return w_count