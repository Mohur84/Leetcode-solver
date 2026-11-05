class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        result=[]
        remainder=0
        for bit in nums:
            remainder=(remainder*2+bit)%5
            result.append(remainder==0)
        return result