class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        result=nums[0]
        for num in nums[1:]:
            result=gcd(result, num)
            if result==1:
                return True
        return result==1