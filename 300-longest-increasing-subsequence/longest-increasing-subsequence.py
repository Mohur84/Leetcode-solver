class Solution:
    def lengthOfLIS(self, nums):
        tails=[]
        for num in nums:
            left=0
            right=len(tails)
            while left<right:
                mid=(left+right)//2
                if tails[mid]<num:
                    left=mid+1
                else:
                    right=mid
            if left==len(tails):
                tails.append(num)
            else:
                tails[left]=num
        return len(tails)