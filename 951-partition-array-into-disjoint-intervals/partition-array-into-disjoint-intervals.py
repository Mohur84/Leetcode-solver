class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        n=len(nums)
        suffix_min=[0]*n
        suffix_min[n-1]=nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_min[i]=min(nums[i], suffix_min[i+1])
        left_max=nums[0]
        for i in range(n-1):
            left_max=max(left_max, nums[i])
            if left_max<=suffix_min[i+1]:
                return i+1
        return n