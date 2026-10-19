class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        length=[1]*n
        count=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if length[j]+1>length[i]:
                        length[i]=length[j]+1
                        count[i]=count[j]
                    elif length[j]+1==length[i]:
                        count[i]+=count[j]
        longest=max(length)
        return sum(
            count[i] for i in range(n)
            if length[i]==longest
        )