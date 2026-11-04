class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n=len(nums)
        flipped=[0]*n
        active_flips=0
        result=0
        for i in range(n):
            if i>=k:
                active_flips^=flipped[i-k]
            if nums[i]^active_flips==0:
                if i+k>n:
                    return -1
                active_flips^=1
                flipped[i]=1
                result+=1
        return result