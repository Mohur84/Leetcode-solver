class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_value=max(nums)
        max_index=nums.index(max_value)
        for i, num in enumerate(nums):
            if i !=max_index and max_value<2*num:
                return -1
        return max_index