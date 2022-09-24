class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        ans=0
        for i in range(0,n):
            for j in range(0,n):
                if i==j:
                    ans+=mat[i][j]
                elif(i+j)==n-1:
                    ans+=mat[i][j]
        return ans