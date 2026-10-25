class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        xor_value=0
        for num in nums:
            xor_value^=num
        return xor_value==0 or len(nums)%2==0