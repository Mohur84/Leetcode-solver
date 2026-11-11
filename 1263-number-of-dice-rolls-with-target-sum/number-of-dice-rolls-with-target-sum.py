class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD=10**9+7
        dp=[0]*(target+1)
        dp[0]=1
        for _ in range(n):
            new_dp=[0]*(target+1)
            for total in range(1, target+1):
                for face in range(1, min(k, total)+1):
                    new_dp[total]+=dp[total-face]
                new_dp[total]%=MOD
            dp=new_dp
        return dp[target]