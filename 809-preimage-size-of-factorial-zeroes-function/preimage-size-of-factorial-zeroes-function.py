class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailing_zeros(x:int)->int:
            count=0
            while x>0:
                x//=5
                count+=x
            return count
        left, right=0, 5*(k+1)
        while left<right:
            mid=(left+right)//2
            if trailing_zeros(mid)<k:
                left=mid+1
            else:
                right=mid
        return 5 if trailing_zeros(left)==k else 0