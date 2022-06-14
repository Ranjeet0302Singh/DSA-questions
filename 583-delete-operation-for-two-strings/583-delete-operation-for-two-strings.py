class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        c = [[0]*(len(word1)+1) for row in range(len(word2)+1)] #row_index+1 for word2_index
        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word1[j-1] == word2[i-1]:
                    c[i][j] = c[i-1][j-1] + 1
                else:
                    c[i][j] = max(c[i-1][j], c[i][j-1])

        return len(word1) + len(word2) - 2*c[-1][-1]