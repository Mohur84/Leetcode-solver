class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp=[0, float('-inf'), float('-inf')]
        for num in nums:
            prev=dp[:]
            for r in range(3):
                new_remainder=(r+num)%3
                dp[new_remainder]=max(
                    dp[new_remainder],
                    prev[r]+num
                )
        return dp[0]