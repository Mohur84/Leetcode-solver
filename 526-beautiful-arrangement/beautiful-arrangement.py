class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def dp(pos, mask):
            if pos>n:
                return 1
            count=0
            for num in range(1, n+1):
                bit=1<<(num-1)
                if mask & bit:
                    continue
                if num%pos==0 or pos%num==0:
                    count+=dp(pos+1, mask|bit)
            return count
        return dp(1, 0)