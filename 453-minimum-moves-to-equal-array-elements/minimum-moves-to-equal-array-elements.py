class Solution:
    def minMoves(self, nums):
        minimum=min(nums)
        return sum(nums)-len(nums)*minimum