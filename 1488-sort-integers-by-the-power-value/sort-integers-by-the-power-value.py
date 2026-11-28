class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def power(x):
            if x==1:
                return 0
            if x%2==0:
                return 1+power(x//2)
            else:
                return 1+power(3*x+1)
        nums=list(range(lo, hi+1))
        nums.sort(key=lambda x:(power(x), x))
        return nums[k-1]