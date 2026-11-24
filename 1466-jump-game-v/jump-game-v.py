class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n=len(arr)
        dp=[0]*n
        def dfs(i):
            if dp[i]!=0:
                return dp[i]
            dp[i]=1
            for j in range(i-1, max(-1, i-d-1), -1):
                if arr[j]>=arr[i]:
                    break
                dp[i]=max(dp[i], 1+dfs(j))
            for j in range(i+1, min(n, i+d+1)):
                if arr[j]>=arr[i]:
                    break
                dp[i]=max(dp[i], 1+dfs(j))
            return dp[i]
        answer=0
        for i in range(n):
            answer=max(answer, dfs(i))
        return answer