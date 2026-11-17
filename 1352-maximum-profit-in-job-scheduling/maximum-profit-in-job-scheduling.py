class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs=sorted(zip(startTime, endTime, profit))
        starts=[job[0] for job in jobs]
        n=len(jobs)
        dp=[0]*(n+1)
        for i in range(n-1, -1, -1):
            start, end, p=jobs[i]
            next_job=bisect_right(starts, end-1)
            skip=dp[i+1]
            take=p+dp[next_job]
            dp[i]=max(take, skip)
        return dp[0]