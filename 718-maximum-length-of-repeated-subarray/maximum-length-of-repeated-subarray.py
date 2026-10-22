class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        m, n=len(nums1), len(nums2)
        dp=[0]*(n+1)
        longest=0
        for i in range(1, m+1):
            for j in range(n, 0, -1):
                if nums1[i-1]==nums2[j-1]:
                    dp[j]=dp[j-1]+1
                    longest=max(longest, dp[j])
                else:
                    dp[j]=0
        return longest