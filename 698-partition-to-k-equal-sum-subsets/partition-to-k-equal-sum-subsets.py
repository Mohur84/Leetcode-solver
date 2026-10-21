class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total=sum(nums)
        if total%k!=0:
            return False
        target=total//k
        nums.sort(reverse=True)
        if nums[0]>target:
            return False
        buckets=[0]*k
        def backtrack(index):
            if index==len(nums):
                return True
            num=nums[index]
            tried=set()
            for i in range(k):
                if buckets[i]+num<=target:
                    tried.add(buckets[i])
                    buckets[i]+=num
                    if backtrack(index+1):
                        return True
                    buckets[i]-=num
                if buckets[i]==0:
                    break
            return False
        return backtrack(0)