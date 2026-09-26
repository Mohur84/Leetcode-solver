class Solution:
    def minCut(self, s):
        n=len(s)
        isPal=[[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i]==s[j] and (j-i<=2 or isPal[i+1][j-1]):
                    isPal[i][j]=True
        dp=[0]*(n+1)
        dp[n]=-1
        for i in range(n-1, -1, -1):
            dp[i]=float("inf")
            for j in range(i, n):
                if isPal[i][j]:
                    dp[i]=min(dp[i], 1+dp[j+1])
        return dp[0]
