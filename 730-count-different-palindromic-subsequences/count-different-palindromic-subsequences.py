class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD=10**9+7
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=1
        for length in range(2, n+1):
            for i in range(n-length+1):
                j=i+length-1
                if s[i]!=s[j]:
                    dp[i][j]=(
                        dp[i+1][j]
                        +dp[i][j-1]
                        -(dp[i+1][j-1] if length>2 else 0)
                    )%MOD
                else:
                    low=i+1
                    high=j-1
                    while low<=high and s[low]!=s[i]:
                        low+=1
                    while low<=high and s[high]!=s[i]:
                        high-=1
                    inner=dp[i+1][j-1] if length>2 else 0
                    if low>high:
                        dp[i][j]=(2*inner+2)%MOD
                    elif low==high:
                        dp[i][j]=(2*inner+1)%MOD
                    else:
                        between=dp[low+1][high-1] if low+1 <= high-1 else 0
                        dp[i][j]=(2*inner-between)%MOD
        return dp[0][n-1]