class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):

            var = matrix[i][:]
            if(target in var):
                return True
        return False
