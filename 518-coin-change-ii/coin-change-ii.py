class Solution:
    def change(self, amount, coins):
        n = len(coins)
        prev = [0] * (amount + 1)
        for target in range(amount + 1):
            if target % coins[0] == 0:
                prev[target] = 1
        for ind in range(1, n):
            cur = [0] * (amount + 1)
            for target in range(amount + 1):
                notTaken = prev[target]
                taken = 0
                if coins[ind] <= target:
                    taken = cur[target - coins[ind]]
                cur[target] = notTaken + taken
            prev = cur
        return prev[amount]