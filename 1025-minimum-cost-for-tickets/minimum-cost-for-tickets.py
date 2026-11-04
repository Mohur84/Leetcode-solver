class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n=len(days)
        dp=[0]*(n+1)
        durations=[1, 7, 30]
        for i in range(n):
            dp[i+1]=float('inf')
            for duration, cost in zip(durations, costs):
                j=bisect_left(days, days[i]-duration+1)
                dp[i+1]=min(
                    dp[i+1],
                    dp[j]+cost
                )
        return dp[n]