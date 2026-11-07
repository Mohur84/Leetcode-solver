class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n=len(customers)
        satisfied=0
        for i in range(n):
            if grumpy[i]==0:
                satisfied+=customers[i]
        window=0
        for i in range(minutes):
            if grumpy[i]==1:
                window+=customers[i]
        max_window=window
        for i in range(minutes, n):
            if grumpy[i]==1:
                window+=customers[i]
            if grumpy[i-minutes]==1:
                window-=customers[i-minutes]
            max_window=max(max_window, window)
        return satisfied+max_window