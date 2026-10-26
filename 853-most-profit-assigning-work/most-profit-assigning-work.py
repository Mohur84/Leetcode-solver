class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) ->int:
        jobs=sorted(zip(difficulty, profit))
        max_profit=0
        best_profit=[]
        best=0
        for diff, prof in jobs:
            best=max(best, prof)
            max_profit=max(max_profit, best)
            best_profit.append((diff, best))
        total=0
        j=0
        best=0
        for ability in sorted(worker):
            while j<len(jobs) and jobs[j][0]<=ability:
                best=max(best, jobs[j][1])
                j+=1
            total+=best
        return total