class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        left, right=0, n-1
        while left<right:
            mid=(left+right)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                left=mid+1
            else:
                right=mid
        peak=left
        left, right=0, peak
        while left<=right:
            mid=(left+right)//2
            value=mountainArr.get(mid)
            if value==target:
                return mid
            elif value<target:
                left=mid+1
            else:
                right=mid-1
        left, right=peak+1, n-1
        while left<=right:
            mid=(left+right)//2
            value=mountainArr.get(mid)
            if value==target:
                return mid
            elif value>target:
                left=mid+1
            else:
                right=mid-1
        return -1