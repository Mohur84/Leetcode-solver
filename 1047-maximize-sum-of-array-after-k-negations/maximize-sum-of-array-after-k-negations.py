class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i]=-nums[i]
                k-=1
        if k%2==1:
            nums.sort()
            nums[0]=-nums[0]
        return sum(nums)