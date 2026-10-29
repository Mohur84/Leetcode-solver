class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp=[0]*(k+1)
        moves=0
        while dp[k]<n:
            moves+=1
            for eggs in range(k, 0, -1):
                dp[eggs]=dp[eggs]+dp[eggs-1]+1
        return moves