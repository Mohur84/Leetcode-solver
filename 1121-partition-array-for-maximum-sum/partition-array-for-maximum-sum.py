class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)
        for i in range(1, n+1):
            max_val=0
            for length in range(1, min(k, i)+1):
                max_val=max(max_val, arr[i-length])
                current_sum=dp[i-length]+max_val*length
                dp[i]=max(dp[i], current_sum)
        return dp[n]