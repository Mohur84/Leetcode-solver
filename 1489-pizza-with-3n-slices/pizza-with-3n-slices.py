class Solution:
    def maxSizeSlices(self, slices: list[int]) -> int:
        n=len(slices)//3
        def solve(arr, k):
            m=len(arr)
            dp=[[0]*(k+1) for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, min(k,(i+1)//2)+1):
                    take=arr[i-1]
                    if i>=2:
                        take+=dp[i-2][j-1]
                    skip=dp[i-1][j]
                    dp[i][j]=max(take, skip)
            return dp[m][k]
        return max(
            solve(slices[:-1], n),
            solve(slices[1:], n)
        )