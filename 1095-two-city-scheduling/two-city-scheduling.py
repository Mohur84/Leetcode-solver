class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        n=len(costs)
        total=0
        for i in range(n//2):
            total+=costs[i][0]
        for i in range(n//2, n):
            total+=costs[i][1]
        return total