class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n=len(jobDifficulty)
        if n<d:
            return -1
        INF=float('inf')
        prev=[INF]*(n+1)
        prev[0]=0
        for day in range(1, d+1):
            curr=[INF]*(n+1)
            for i in range(day, n+1):
                max_difficulty=0
                for j in range(i-1, day-2, -1):
                    max_difficulty=max(
                        max_difficulty,
                        jobDifficulty[j]
                    )
                    curr[i]=min(
                        curr[i],
                        prev[j]+max_difficulty
                    )
            prev=curr
        return prev[n]