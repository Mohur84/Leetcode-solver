class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD=10**9+7
        max_pos=min(steps, arrLen-1)
        dp=[0]*(max_pos+1)
        dp[0]=1
        for _ in range(steps):
            new_dp=[0]*(max_pos+1)
            for i in range(max_pos+1):
                new_dp[i]+=dp[i]
                if i>0:
                    new_dp[i]+=dp[i-1]
                if i<max_pos:
                    new_dp[i]+=dp[i+1]
                new_dp[i]%=MOD
            dp=new_dp
        return dp[0]