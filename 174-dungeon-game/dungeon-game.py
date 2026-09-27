class Solution:
    def calculateMinimumHP(self, dungeon):
        m=len(dungeon)
        n=len(dungeon[0])
        dp=[float("inf")]*(n+1)
        dp[n-1]=1
        for i in range(m-1, -1, -1):
            dp[n]=float("inf")
            for j in range(n-1, -1, -1):
                need=min(dp[j], dp[j+1])-dungeon[i][j]
                dp[j]=max(1, need)
        return dp[0]