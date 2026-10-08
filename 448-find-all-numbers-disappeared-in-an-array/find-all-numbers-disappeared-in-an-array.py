class Solution:
    def findDisappearedNumbers(self, nums):
        for x in nums:
            index=abs(x)-1
            nums[index]=-abs(nums[index])
            result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        return result