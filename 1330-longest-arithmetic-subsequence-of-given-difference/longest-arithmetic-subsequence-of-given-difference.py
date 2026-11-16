class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp={}
        for num in arr:
            prev=num-difference
            dp[num]=dp.get(prev, 0)+1
        return max(dp.values())