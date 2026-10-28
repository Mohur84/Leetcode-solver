class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n=len(arr)
        index={value: i for i, value in enumerate(arr)}
        dp=[[2]*n for _ in range(n)]
        longest=0
        for k in range(n):
            for j in range(k):
                prev=arr[k]-arr[j]
                if prev<arr[j] and prev in index:
                    i=index[prev]
                    dp[j][k]=dp[i][j]+1
                    longest=max(longest, dp[j][k])
        return longest if longest>=3 else 0