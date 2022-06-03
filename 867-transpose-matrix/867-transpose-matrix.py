class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a=[]
        for i in range(len(matrix[0])):
            b=[]
            for j in range(len(matrix)):
                b.append(matrix[j][i])
            a.append(b)
        return a
            