class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        moves=0
        for i in range(1, len(nums)):
            if nums[i]<=nums[i-1]:
                new_value=nums[i-1]+1
                moves+=new_value-nums[i]
                nums[i]=new_value
        return moves