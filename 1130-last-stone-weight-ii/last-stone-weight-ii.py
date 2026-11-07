class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total=sum(stones)
        target=total//2
        dp=[0]*(target+1)
        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j]=max(dp[j], dp[j-stone]+stone)
        return total-2*dp[target]