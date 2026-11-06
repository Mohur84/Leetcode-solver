class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[{} for _ in range(n)]
        result=2
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]=dp[j].get(diff, 1)+1
                result=max(result, dp[i][diff])
        return result