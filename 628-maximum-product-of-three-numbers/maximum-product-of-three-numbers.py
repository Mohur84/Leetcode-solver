class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        return max(
            nums[n-1]*nums[n-2]*nums[n-3],
            nums[0]*nums[1]*nums[n-1]
        )