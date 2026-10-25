from typing import List
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num
        dp = [0.0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = prefix[i] / i
        for groups in range(2, k + 1):
            for i in range(n, groups - 1, -1):
                best = 0.0
                for j in range(groups - 1, i):
                    avg = (prefix[i] - prefix[j]) / (i - j)
                    best = max(best, dp[j] + avg)
                dp[i] = best
        return dp[n]