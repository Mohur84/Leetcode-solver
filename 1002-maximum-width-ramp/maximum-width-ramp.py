class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack=[]
        for i, num in enumerate(nums):
            if not stack or num<nums[stack[-1]]:
                stack.append(i)
        ans=0
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j]>=nums[stack[-1]]:
                i=stack.pop()
                ans=max(ans, j-i)
        return ans