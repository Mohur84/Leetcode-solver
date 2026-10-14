class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        sorted_nums=sorted(nums)
        n=len(nums)
        left=0
        while left<n and nums[left]==sorted_nums[left]:
            left+=1
        if left==n:
            return 0
        right=n-1
        while nums[right]==sorted_nums[right]:
            right-=1
        return right-left+1