class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD=10**9+7
        dp=[[0]*(minProfit+1) for _ in range(n+1)]
        dp[0][0]=1
        for members, gain in zip(group, profit):
            for used in range(n, members-1, -1):
                for p in range(minProfit, -1, -1):
                    new_profit=min(minProfit, p+gain)
                    dp[used][new_profit]=(
                        dp[used][new_profit]+dp[used-members][p]
                    )%MOD
        return sum(dp[used][minProfit] for used in range(n+1))%MOD