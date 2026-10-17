class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD=10**9+7
        if k>n*(n-1)//2:
            return 0
        dp=[0]*(k+1)
        dp[0]=1
        for i in range(1, n+1):
            new_dp=[0]*(k+1)
            window=0
            for j in range(k+1):
                window+=dp[j]
                if j>=i:
                    window-=dp[j-i]
                new_dp[j]=window%MOD
            dp=new_dp
        return dp[k]