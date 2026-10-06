class Solution:
    def maxRotateFunction(self, nums):
        n=len(nums)
        total=sum(nums)
        current=sum(i*nums[i] for i in range(n))
        answer=current
        for i in range(n-1, 0, -1):
            current=current+total-n*nums[i]
            answer=max(answer, current)
        return answer