class Solution:
    def totalHammingDistance(self, nums):
        n=len(nums)
        total=0
        for bit in range(32):
            ones=sum((num>>bit)&1 for num in nums)
            total+=ones*(n-ones)
        return total