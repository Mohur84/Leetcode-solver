class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows=len(matrix)
        cols=len(matrix[0])
        dp=[0]*(cols+1)
        max_side=0
        for i in range(1, rows+1):
            prev_diagonal=0
            for j in range(1, cols+1):
                top=dp[j]
                if matrix[i-1][j-1]=="1":
                    dp[j]=1+min(
                        dp[j],
                        dp[j-1],
                        prev_diagonal
                    )
                    max_side=max(max_side, dp[j])
                else:
                    dp[j]=0
                prev_diagonal=top
        return max_side*max_side