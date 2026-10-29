class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        MOD=10**9+7
        nums.sort()
        n=len(nums)
        result=0
        power=1
        for i in range(n):
            result=(result+nums[i]*(power-pow(2, n-1-i, MOD)))%MOD
            power=(power*2)%MOD
        return result