class Solution:
    def numberOfArithmeticSlices(self, nums):
        n=len(nums)
        dp=[defaultdict(int) for _ in range(n)]
        result=0
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                result+=dp[j][diff]
                dp[i][diff]+=dp[j][diff]+1
        return result