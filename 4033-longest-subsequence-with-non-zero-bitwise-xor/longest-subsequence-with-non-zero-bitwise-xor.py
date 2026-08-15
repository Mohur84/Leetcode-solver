class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        total_xor = 0
        has_nonzero = False
        for v in nums:
            total_xor ^= v
            if v != 0:
                has_nonzero = True

        if total_xor != 0:
            return n
        if has_nonzero:
            return n - 1
        return 0