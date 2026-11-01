class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count=defaultdict(int)
        count[0]=1
        prefix_sum=0
        result=0
        for num in nums:
            prefix_sum+=num
            result+=count[prefix_sum-goal]
            count[prefix_sum]+=1
        return result