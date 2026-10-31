class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even=0
        odd=1
        n=len(nums)
        while even<n and odd<n:
            if nums[even]%2==0:
                even+=2
            elif nums[odd]%2==1:
                odd+=2
            else:
                nums[even], nums[odd]=nums[odd], nums[even]
                even+=2
                odd+=2
        return nums