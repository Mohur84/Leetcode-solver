class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD=10**9+7
        n=len(s)
        dp=[1]*(n+1)
        for i in range(n):
            new_dp=[0]*(n-i)
            if s[i]=='I':
                running_sum=0
                for j in range(n-i):
                    running_sum=(running_sum+dp[j])%MOD
                    new_dp[j]=running_sum
            else:
                running_sum=0
                for j in range(n-i-1, -1, -1):
                    running_sum=(running_sum+dp[j+1])%MOD
                    new_dp[j]=running_sum
            dp=new_dp
        return dp[0]