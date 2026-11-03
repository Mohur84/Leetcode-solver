class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[0]*n
        left=0
        right=n-1
        pos=n-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[pos]=nums[left]**2
                left+=1
            else:
                result[pos]=nums[right]**2
                right-=1
            pos-=1
        return result