class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        n=len(nums)
        original=0
        gain=0
        min_max=float('inf')
        max_min=float('-inf')
        for i in range(n-1):
            a=nums[i]
            b=nums[i+1]
            original+=abs(a-b)
            if i>0:
                gain=max(
                    gain,
                    abs(nums[0]-b)-abs(a-b)
                )
            if i<n-2:
                gain=max(
                    gain,
                    abs(nums[-1]-a)-abs(a-b)
                )
            min_max=min(min_max, max(a, b))
            max_min=max(max_min, min(a, b))
        gain=max(gain, 2*(max_min-min_max))
        return original+gain