class Solution:
    def splitArray(self, nums, k):
        left=max(nums)
        right=sum(nums)
        while left<right:
            mid=left+(right-left)//2
            parts=1
            current=0
            for num in nums:
                if current+num>mid:
                    parts+=1
                    current=num
                else:
                    current+=num
            if parts>k:
                left=mid+1
            else:
                right=mid
        return left