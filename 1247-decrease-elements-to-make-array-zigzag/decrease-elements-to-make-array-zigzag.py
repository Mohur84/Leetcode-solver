class Solution:
    def movesToMakeZigzag(self, nums: list[int]) -> int:
        n=len(nums)
        def calculate(parity):
            operations=0
            for i in range(parity, n, 2):
                left=nums[i-1] if i>0 else float('inf')
                right=nums[i+1] if i<n-1 else float('inf')
                minimum_neighbor=min(left, right)
                if nums[i]>=minimum_neighbor:
                    operations+=nums[i]-minimum_neighbor+1
            return operations
        return min(calculate(0), calculate(1))