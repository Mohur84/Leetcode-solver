class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows=len(matrix)
        cols=len(matrix[0])
        memo=[[0]*cols for _ in range(rows)]
        directions=[
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        def dfs(r, c):
            if memo[r][c]!=0:
                return memo[r][c]
            best=1
            for dr, dc in directions:
                nr=r+dr
                nc=c+dc
                if (
                    0<=nr<rows
                    and 0<=nc<cols
                    and matrix[nr][nc]>matrix[r][c]
                ):
                    best=max(best, 1+dfs(nr, nc))
            memo[r][c]=best
            return best
        answer=0
        for r in range(rows):
            for c in range(cols):
                answer=max(answer, dfs(r, c))
        return answer