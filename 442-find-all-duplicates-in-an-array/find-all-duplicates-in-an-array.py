class Solution:
    def findDuplicates(self, nums):
        result=[]
        for x in nums:
            index=abs(x)-1
            if nums[index]<0:
                result.append(abs(x))
            else:
                nums[index]=-nums[index]
        return result