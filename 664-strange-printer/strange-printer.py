class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        t=[]
        for ch in s:
            if not t or t[-1]!=ch:
                t.append(ch)
        s="".join(t)
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i]=1
            for j in range(i+1, n):
                dp[i][j]=1+dp[i+1][j]
                for k in range(i+1, j+1):
                    if s[k]==s[i]:
                        middle=dp[i+1][k-1] if k>i+1 else 0
                        dp[i][j]=min(
                            dp[i][j],
                            middle+dp[k][j]
                        )
        return dp[0][n-1]