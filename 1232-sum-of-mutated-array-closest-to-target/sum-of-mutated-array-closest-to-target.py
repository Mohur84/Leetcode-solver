class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        left, right=0, max(arr)
        while left<right:
            mid=(left+right)//2
            total=sum(min(num, mid) for num in arr)
            if total<target:
                left=mid+1
            else:
                right=mid
        sum1=sum(min(num, left) for num in arr)
        sum2=sum(min(num, left-1) for num in arr)
        if abs(sum1-target)<abs(sum2-target):
            return left
        else:
            return left-1